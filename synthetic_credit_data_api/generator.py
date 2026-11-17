"""Synthetic record generator for Synthetic Credit Data API (privacy-safe, deterministic with seed)."""
from __future__ import annotations

SUPPORTED_SCHEMAS = ("default", 'credit')


def generate_records(rows: int, schema_name: str = "default", seed: int | None = None) -> list[dict]:
    if rows < 1:
        raise ValueError("rows must be >= 1")
    if schema_name not in SUPPORTED_SCHEMAS:
        raise ValueError(f"unsupported schema: {schema_name}")
    import random
    from datetime import datetime, timedelta

    rng = random.Random(seed) if seed is not None else random.Random()
    occupations = ["engineer", "teacher", "nurse", "analyst", "designer", "driver", "chef", "developer"]
    purposes = ["home", "auto", "personal", "business", "education"]
    out = []
    for i in range(rows):
        income = rng.randint(18000, 180000)
        debt = int(income * rng.uniform(0.05, 1.4))
        dti = round(debt / max(income, 1), 3)
        util = round(rng.uniform(0.0, 0.98), 3)
        late = rng.choices([0, 1, 2, 3], weights=[80, 12, 5, 3])[0]
        score = int(max(300, min(850, 650 + income / 1800 - dti * 120 - util * 90 - late * 25 + rng.randint(-30, 30))))
        pd = round(1 / (1 + 2.71828 ** ((score - 620) / 40)), 4)
        out.append({
            "customer_id": f"C{100000 + i}",
            "age": rng.randint(18, 75),
            "occupation": rng.choice(occupations),
            "annual_income": income,
            "total_debt": debt,
            "debt_to_income": dti,
            "credit_utilization": util,
            "num_late_payments": late,
            "loan_purpose": rng.choice(purposes),
            "credit_score": score,
            "default_probability": pd,
            "defaulted": 1 if pd > 0.5 else 0,
        })
    return out
