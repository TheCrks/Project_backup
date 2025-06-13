import torch
from transformers import BertTokenizerFast, BertConfig
from torch.nn.functional import mse_loss
from transformers import BertPreTrainedModel, BertModel
import torch.nn as nn

#Load the trained model
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
            loss = mse_loss(logits, labels)

        return {"loss": loss, "logits": logits}

def loadModel():
    model_path = "bert_relevance_model"
    tokenizer = BertTokenizerFast.from_pretrained(model_path)
    config = BertConfig.from_pretrained(model_path)
    model = BertForRelevanceRegression.from_pretrained(model_path, config=config)
    return model, tokenizer

def evaluate(sample,model,tokenizer):

    inputs = tokenizer(
        sample['features']['title'] + " " + sample['features']['abstract'],
        ' '.join(sample['features']['keywords']),
        max_length=512,
        truncation=True,
        padding='max_length',
        return_tensors='pt'
    )

    with torch.no_grad():
        outputs = model(**inputs)
        score = outputs["logits"].item()

    return score