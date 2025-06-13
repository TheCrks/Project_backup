import torch
from torch.utils.data import Dataset, DataLoader
from transformers import BertTokenizer, BertModel, BertPreTrainedModel, BertConfig
from transformers import Trainer, TrainingArguments
from transformers import BertTokenizerFast, BertForSequenceClassification
import torch.nn as nn
import numpy as np
from sklearn.model_selection import train_test_split
import os
import shutil
import tempfile
import torch
from transformers import BertTokenizerFast, TrainingArguments, Trainer
from filelock import FileLock

# Custom Dataset
class RelevanceDataset(Dataset):
    def __init__(self, samples, tokenizer, max_length=512):
        self.samples = samples
        self.tokenizer = tokenizer
        self.max_length = max_length

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, idx):
        sample = self.samples[idx]
        inputs = self.tokenizer(
            sample['features']['title'] + " " + sample['features']['abstract'],
            ' '.join(sample['features']['keywords']),
            max_length=self.max_length,
            truncation=True,
            padding='max_length',
            return_tensors='pt'
        )

        inputs = {k: v.squeeze() for k, v in inputs.items()}
        inputs['labels'] = torch.tensor(sample['label'], dtype=torch.float)
        return inputs

def trainModel():
    from serviceReferences.FirebaseServiceReference.FirebaseServiceReference import fetch_and_format_logs
    dataset = fetch_and_format_logs()

    tokenizer = BertTokenizerFast.from_pretrained("bert-base-uncased")

    train_data, val_data = train_test_split(dataset, test_size=0.1, random_state=42)
    train_dataset = RelevanceDataset(train_data, tokenizer)
    val_dataset = RelevanceDataset(val_data, tokenizer)

    # Model (Regression head)
    class BertForRelevanceRegression(BertPreTrainedModel):
        def __init__(self, config):
            super().__init__(config)
            self.bert = BertModel(config)
            self.regressor = nn.Linear(config.hidden_size, 1)
            self.init_weights()

        def forward(self, input_ids=None, attention_mask=None, token_type_ids=None, labels=None):
            outputs = self.bert(
                input_ids=input_ids,
                attention_mask=attention_mask,
                token_type_ids=token_type_ids,
            )
            pooled_output = outputs.pooler_output
            logits = self.regressor(pooled_output).squeeze(-1)

            loss = None
            if labels is not None:
                loss_fn = nn.MSELoss()
                loss = loss_fn(logits, labels)

            return {"loss": loss, "logits": logits}

    model = BertForRelevanceRegression.from_pretrained("bert-base-uncased")

    training_args = TrainingArguments(
        output_dir="./bert-relevance-model",
        num_train_epochs=4,
        per_device_train_batch_size=8,
        per_device_eval_batch_size=8,
        learning_rate=2e-5,
        eval_strategy="epoch",
        save_strategy="epoch",
        logging_dir="./logs",
        load_best_model_at_end=True,
        metric_for_best_model="eval_loss",
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=val_dataset,
    )

    trainer.train()
    trainer.save_model("bert_relevance_model")