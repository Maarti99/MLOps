from fastapi import FastAPI
from schemas import PredictRequest, PredictResponse
from inference import load_models, predict as make_prediction

app = FastAPI()
transformer_model, classifier_model = load_models()


@app.get("/")
def welcome_root():
    return {"message": "Welcome"}


@app.post("/predict")
def predict(request: PredictRequest) -> PredictResponse:
    result = make_prediction(request.text, transformer_model, classifier_model)
    return PredictResponse(prediction=result)
