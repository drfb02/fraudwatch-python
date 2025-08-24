from fastapi import APIRouter, HTTPException
from app.schemas import PredictRequest, PredictResponse
import joblib
import os

router = APIRouter()

MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "models", "model.pkl")

def load_model():
    if not os.path.exists(MODEL_PATH):
        return None
    return joblib.load(MODEL_PATH)

@router.post("/predict", response_model=PredictResponse)
def predict(req: PredictRequest):
    model = load_model()
    if model is None:
        raise HTTPException(status_code=500, detail="Model not found. Run training/train.py first.")
    proba = model.predict_proba([req.features])[0][1]
    pred = int(proba >= 0.5)
    return PredictResponse(fraud_probability=float(proba), predicted_class=pred)
