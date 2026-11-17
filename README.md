<!-- ABN-BADGES -->
# Synthetic Credit Data API

<p align="center">
  <a href="https://3km-collab.github.io/synthetic-credit-data-api-1/"><img alt="Live Demo" src="https://img.shields.io/badge/Live%20Demo-View%20Site-6366f1?style=for-the-badge"></a>
  <a href="https://autonomousstudio.gumroad.com/l/icmdfe"><img alt="Download Package" src="https://img.shields.io/badge/Download%20Package-Get%20Now-22d3ee?style=for-the-badge"></a>
  <img alt="Made by CredSynth" src="https://img.shields.io/badge/by-CredSynth-10b981?style=for-the-badge">
</p>

[**Live Demo**](https://3km-collab.github.io/synthetic-credit-data-api-1/) · [**Download the package**](https://autonomousstudio.gumroad.com/l/icmdfe)

---

# Synthetic Credit Data API

A production-ready Python package by **CredSynth** (datasets). Ships with a
FastAPI service, a deterministic synthetic-data generator, a pytest suite,
Docker, Postman, automation presets, and 2,500+ sample records.

## Features
- Modular FastAPI service (app/) with logging and error handling
- Deterministic generator (seedable) — privacy-safe synthetic data
- pytest suite that actually runs
- Docker + docker-compose, Makefile, .env.example
- Ready sample data: CSV, JSON, SQL schema (2,500+ records)
- Postman collection for instant API testing
- Importable presets/ for automation

## Structure
```
synthetic_credit_data_api/
  main.py  models.py  generator.py  config.py  logging_conf.py
tests/test_main.py
presets/  sample_data/  scripts/
Dockerfile  docker-compose.yml  Makefile  requirements.txt  QUICKSTART.md
```

## Install
```bash
pip install -r requirements.txt
make run
```

See `QUICKSTART.md` for the 3-step setup.
