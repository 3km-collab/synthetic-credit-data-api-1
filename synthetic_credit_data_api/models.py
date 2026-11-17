"""Pydantic models for request/response validation."""
from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


class GenerateRequest(BaseModel):
    rows: int = Field(default=100, ge=1, le=100000)
    schema_name: str = Field(default="default")
    seed: int | None = None


class GenerateResponse(BaseModel):
    rows: int
    schema_name: str
    data: list[dict[str, Any]]
