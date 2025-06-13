from typing import List, Dict
import requests
from bs4 import BeautifulSoup

from schemas import SorterSchema
from schemas.SorterSchema import SortData, SorterItemSchema, Metadata
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re
from sentence_transformers import SentenceTransformer, util
from serviceReferences.FirebaseServiceReference import FirebaseServiceReference
from services.Trainer.EvaluaterService import evaluate, loadModel


def normalize(scores):
    if not scores:
        return {}
    min_score, max_score = min(scores.values()), max(scores.values())
    if max_score == min_score:
        return {k: 0.0 for k in scores}  # avoid divide-by-zero
    return {k: (v - min_score) / (max_score - min_score) for k, v in scores.items()}

def sort(data: SortData, weights: Dict[str, float] = None):
    try:
        if weights is None:
            weights = {
                "simple": 0.05,
                "tfidf": 0.3,
                "embedding": 0.25,
                "popularity": 0.4
            }

        items = data.results
        item_map = {id(item): item for item in items}

        # Get individual score maps
        scores_simple = simpleScore(items, data.keywords) if weights["simple"] else {}
        scores_tfidf = tfidfScore(items, data.keywords) if weights["tfidf"] else {}
        scores_embed = sentenceEmbeddingScore(items, data.keywords) if weights["embedding"] else {}
        scores_popularity = calculatePopularityScores(items) if weights.get("popularity") else {}

        scores_simple = normalize(scores_simple)
        scores_tfidf = normalize(scores_tfidf)
        scores_embed = normalize(scores_embed)
        scores_popularity = normalize(scores_popularity)

        # Combine all normalized scores
        final_scores = {}
        for item_id in item_map:
            final_scores[item_id] = (
                weights["simple"] * scores_simple.get(item_id, 0.0) +
                weights["tfidf"] * scores_tfidf.get(item_id, 0.0) +
                weights["embedding"] * scores_embed.get(item_id, 0.0)+
                weights["popularity"] * scores_popularity.get(item_id, 0.0)
            )


        # Sort by combined score
        sorted_items = sorted(item_map.items(), key=lambda x: final_scores.get(x[0], 0.0), reverse=True)
        data.results = [item for _, item in sorted_items]
        """print("\n--- Score Breakdown After Sorting ---")
        for item in data.results:
            item_id = id(item)
            title = getattr(item, "title", "(no title)")
            print(f"Title: {title}")
            print(f"  Simple Score     : {scores_simple.get(item_id, 0.0):.4f}")
            print(f"  TF-IDF Score     : {scores_tfidf.get(item_id, 0.0):.4f}")
            print(f"  Embedding Score  : {scores_embed.get(item_id, 0.0):.4f}")
            print(f"  Popularity Score : {scores_popularity.get(item_id, 0.0):.4f}")
            print(f"  FINAL Score      : {final_scores.get(item_id, 0.0):.4f}")
            print("-" * 50)
    
        """
        return data
    except Exception as e:
        print("Error Sorting: ", e)
        return data


def sortWithModel(data: SortData, weights: Dict[str, float] = None):
    try:
        if weights is None:
            weights = {
                "model": 0.7,
                "popularity": 0.3
            }

        items = data.results
        item_map = {id(item): item for item in items}

        scores_model = modelRelevance(items, data.keywords)
        scores_popularity = calculatePopularityScores(items)
        scores_popularity = normalize(scores_popularity)

        final_scores = {}
        for item_id in item_map:
            final_scores[item_id] = (
                    weights["model"] * scores_model.get(item_id, 0.0) +
                    weights["popularity"] * scores_popularity.get(item_id, 0.0)
            )

        sorted_items = sorted(item_map.items(), key=lambda x: final_scores.get(x[0], 0.0), reverse=True)
        data.results = [item for _, item in sorted_items]
        return data
    except Exception as e:
        print("Error Sorting: ", e)
        return data




def simpleScore(items: List[SorterItemSchema], keywords: List[str]) -> Dict[int, float]:
    keyword_phrases = [kw.lower() for kw in keywords]
    total = sum(range(1, len(keyword_phrases) + 1))
    keyword_weights = {
        k.lower(): (len(keyword_phrases) - i) / total
        for i, k in enumerate(keyword_phrases)
    }

    scores = {}
    for item in items:
        text = item.data or ""
        if not text:
            scores[id(item)] = 0.0
            continue
        total_score = sum(weight * wordCount(keyword, text) for keyword, weight in keyword_weights.items())
        scores[id(item)] = total_score
    return scores

def wordCount(keyword, data):
    pattern = r'\b' + re.escape(keyword.lower()) + r'\b'
    return len(re.findall(pattern, data.lower()))


def tfidfScore(items: List[SorterItemSchema], keywords: List[str]) -> Dict[int, float]:
    texts = [item.data or "" for item in items]
    vectorizer = TfidfVectorizer(ngram_range=(1, 2))
    tfidf_matrix = vectorizer.fit_transform(texts)
    query_vector = vectorizer.transform([" ".join(keywords)])
    similarities = cosine_similarity(query_vector, tfidf_matrix).flatten()
    return {id(item): score for item, score in zip(items, similarities)}


def sentenceEmbeddingScore(items: List[SorterItemSchema], keywords: List[str]) -> Dict[int, float]:
    model = SentenceTransformer("all-MiniLM-L6-v2")
    doc_embeddings = model.encode([item.data for item in items], convert_to_tensor=True)
    query_embedding = model.encode(" ".join(keywords), convert_to_tensor=True)
    cos_scores = util.cos_sim(query_embedding, doc_embeddings)[0].cpu().tolist()
    return {id(item): score for item, score in zip(items, cos_scores)}

def parse_access_value(value: str) -> int:
    match = re.match(r"([\d.,]+)([kK]?)", value)
    if not match:
        return 0
    number, suffix = match.groups()
    try:
        number = float(number.replace(",", ""))
        if suffix.lower() == 'k':
            number *= 1000
        return int(number)
    except ValueError:
        return 0

def calculatePopularityScores(items: List[SorterItemSchema]) -> Dict[int, float]:
    accesses_list = []
    citations_list = []

    raw_scores = {}
    for item in items:
        meta = item.metadata or {}
        raw_access = meta.get("accesses", "0").replace("Accesses", "").strip()
        raw_citations = meta.get("citations", "0").strip()

        accesses = parse_access_value(raw_access)
        citations = int(re.sub(r"[^\d]", "", raw_citations)) if raw_citations.isdigit() or raw_citations else 0

        accesses_list.append(accesses)
        citations_list.append(citations)
        raw_scores[id(item)] = {"accesses": accesses, "citations": citations}

    def normalize(values):
        if not values:
            return []
        min_val, max_val = min(values), max(values)
        if max_val == min_val:
            return [0.0] * len(values)
        return [(v - min_val) / (max_val - min_val) for v in values]

    norm_accesses = normalize(accesses_list)
    norm_citations = normalize(citations_list)

    alpha = 0.3  # accesses weight
    beta = 0.8   # citations weight

    popularity_scores = {}
    for item, acc_score, cit_score in zip(items, norm_accesses, norm_citations):
        score = alpha * acc_score + beta * cit_score
        popularity_scores[id(item)] = score

    return popularity_scores

def modelRelevance(items: List[SorterItemSchema], keywords: List[str]) -> Dict[int, float]:
    model, tokenizer = loadModel()
    scores = []
    for item in items:
        sample = {
            "features": {
                "title": item.title,
                "abstract": item.data,
                "keywords": keywords,
            }
        }
        score = evaluate(sample, model, tokenizer)
        scores.append(score)
    return {id(item): score for item, score in zip(items, scores)}