"""Application settings from environment (with safe defaults)."""
from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    max_rows: int = int(os.getenv("MAX_ROWS", "100000"))
    log_level: str = os.getenv("LOG_LEVEL", "INFO")
    env: str = os.getenv("ENV", "production")


settings = Settings()
