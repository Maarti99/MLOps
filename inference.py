import joblib
from sentence_transformers import SentenceTransformer


def load_models():
    transformer = SentenceTransformer("model/sentence_transformer.model")
    classifier = joblib.load("model/classifier.joblib")
    return (transformer, classifier)


def predict(text: str, transformer: SentenceTransformer, classifier) -> str:
    embedding = transformer.encode([text])
    prediction_idx = classifier.predict(embedding)[0]
    classes = {0: "negative", 1: "neutral", 2: "positive"}
    return classes.get(prediction_idx, "unknown")
