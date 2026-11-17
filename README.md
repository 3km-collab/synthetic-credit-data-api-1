# CredSynth - Synthetic Credit Data API

## Overview
CredSynth is a lightweight, zero‑cost API that generates realistic synthetic credit‑risk data on‑the‑fly. It is useful for fintech developers, data scientists, and academic researchers who need quick access to dummy credit datasets for testing, prototyping, or teaching credit‑risk models without dealing with privacy constraints.

## Features
- Generate any number of records (default 1000) via a simple HTTP GET request.
- Fully reproducible random seed for consistent results.
- JSON output compatible with pandas, scikit‑learn, etc.
- No external database – data is generated in memory.
- Docker‑ready for one‑click deployment.

## Quick Start

```bash
# Clone the repo
git clone https://github.com/yourname/credsynth.git
cd credsynth

# Install dependencies
pip install -r requirements.txt

# Run the API
python app.py
```

The service will be available at `http://127.0.0.1:5000`.

### Example request

```bash
curl "http://127.0.0.1:5000/data?rows=5"
```

Response (pretty‑printed):

```json
[
  {
    "id": 1,
    "age": 34,
    "income": 54000,
    "employment_length": 5,
    "credit_score": 712,
    "loan_amount": 15000,
    "purpose": "car",
    "default": 0
  },
  ...
]
```

## API Endpoints

| Method | Path | Query Parameters | Description |
|--------|------|------------------|-------------|
| GET | `/data` | `rows` (int, optional, default = 1000) | Returns a JSON array with the requested number of synthetic credit records. |
| GET | `/health` | – | Simple health‑check returning `{"status":"ok"}`. |

## Docker

```bash
docker build -t credsynth .
docker run -p 5000:5000 credsynth
```

## Customization
The data generation logic lives in `generate_data.py`. You can modify distributions, add new fields, or plug in your own faker providers.

## License
This project is released under the MIT License – feel free to use, modify, and share.
