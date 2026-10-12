from pydantic import BaseModel, Field


class PredictRequest(BaseModel):
    text: str = Field(..., min_length=1, description="Text")


class PredictResponse(BaseModel):
    prediction: str
