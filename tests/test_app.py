from fastapi.testclient import TestClient
from app import app
from inference import load_models

client = TestClient(app)


def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome"}


def test_models_loading():
    transformer, classifier = load_models()
    assert transformer is not None
    assert classifier is not None


def test_valid_inference():
    samples = [
        "What a nice nice meal, I am very satisfied",
        "This is absolutely terrible.",
        "Just a normal day.",
    ]
    for text in samples:
        response = client.post("/predict", json={"text": text})
        assert response.status_code == 200

        data = response.json()
        assert "prediction" in data
        assert data["prediction"] in ["negative", "neutral", "positive"]


def test_input_empty_string():
    response = client.post("/predict", json={"text": ""})
    assert response.status_code == 422


def test_input_wrong_format():
    response = client.post("/predict", json={"wrong_key": "some text"})
    assert response.status_code == 422
