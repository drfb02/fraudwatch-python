from pydantic import BaseModel, field_validator
from typing import List

class PredictRequest(BaseModel):
    features: List[float]

    @field_validator("features")
    @classmethod
    def check_len(cls, v):
        if len(v) < 3:
            raise ValueError("Provide at least 3 features for the demo model.")
        return v

class PredictResponse(BaseModel):
    fraud_probability: float
    predicted_class: int
