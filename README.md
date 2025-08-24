# FraudWatch (Python, FastAPI + scikit-learn)
Mini piattaforma MLOps: training di un modello di classificazione *fraud/no-fraud*, servizio di prediction via API, test, Docker e CI.

> **Disclaimer**
> This repository is an educational **demo** for end-to-end ML (training + serving).
> The model is trained on **synthetic data** and **must not** be used to make real financial decisions.
> No real personal data is included.

## Avvio rapido (local)
```bash
python -m venv .venv && source .venv/bin/activate  # (Windows: .venv\Scripts\activate)
pip install -r requirements.txt
python training/train.py         # genera models/model.pkl
uvicorn app.main:app --reload    # http://localhost:8000/docs
```

## Endpoints
- `GET /health` → stato
- `POST /predict` → body: `{ "features": [0.1, 0.2, 0.3, ...] }`

## Test
```bash
pytest -q
```

## Docker
```bash
docker build -t fraudwatch-api .
docker run -p 8000:8000 fraudwatch-api
# oppure
docker compose up --build
```

## Struttura
```
fraudwatch-python/
  app/
    main.py
    routers/predict.py
    schemas.py
  training/train.py
  models/ (generata)
  tests/test_api.py
  requirements.txt
  Dockerfile
  docker-compose.yml
  .github/workflows/python-ci.yml
  Makefile
```

## Limitations & Responsible Use
- Synthetic dataset; results are illustrative only.
- No calibration/monitoring/drift checks included yet.
- No PII is processed; do not submit real customer data to the demo API.
- Before any production use, add: data governance, monitoring, bias audits, rate limiting, auth, logging, model registry (e.g., MLflow).


---
© drfb02
