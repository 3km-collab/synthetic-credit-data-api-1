# Quickstart — Synthetic Credit Data API

Get the API running in **3 steps**.

## 1. Install
```bash
pip install -r requirements.txt
```

## 2. Run
```bash
make run
# or: uvicorn synthetic_credit_data_api.main:app --reload
```

## 3. Call it
```bash
curl -X POST http://localhost:8000/v1/generate \
  -H "Content-Type: application/json" \
  -d '{"rows": 100}'
```

Open interactive docs: http://localhost:8000/docs

## Docker (one command)
```bash
docker compose up --build
```

## Tests
```bash
make test
```

## Sample data included
`sample_data/` ships with **2,500+** ready records (CSV + JSON + SQL):
- `sample_data/records.csv`
- `sample_data/records.json`
- `sample_data/schema.sql`

## Postman
Import `postman_collection.json` to test every endpoint instantly.
