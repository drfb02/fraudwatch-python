# FraudWatch (Python, FastAPI + scikit-learn)

Mini piattaforma MLOps: training di un modello di classificazione *fraud/no-fraud*, servizio di prediction via API, test, Docker e CI.

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

## Prossimi passi
- Aggiungere pipeline (Prefect/Airflow), tracking (MLflow), e feature store.
- Aggiungere autenticazione API key e rate limiting.
- Integrare un piccolo dataset reale e notebook EDA.

---
© drfb02
