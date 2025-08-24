from fastapi import FastAPI
from app.routers.predict import router as predict_router

app = FastAPI(title="FraudWatch API", version="0.1.0")

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(predict_router, prefix="")
