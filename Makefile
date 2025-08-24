.PHONY: install test run train

install:
	python -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt

train:
	python training/train.py

test:
	pytest -q

run:
	uvicorn app.main:app --reload
