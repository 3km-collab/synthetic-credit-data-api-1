#!/usr/bin/env python3
"""Regenerate sample_data/ (CSV + JSON + SQL) locally."""
import json
from pathlib import Path

from synthetic_credit_data_api.generator import generate_records

OUT = Path(__file__).resolve().parent.parent / "sample_data"
OUT.mkdir(exist_ok=True)


def main(rows: int = 500) -> None:
    data = generate_records(rows)
    (OUT / "records.json").write_text(json.dumps(data, indent=2))
    print(f"wrote {len(data)} records to {OUT}")


if __name__ == "__main__":
    main()
