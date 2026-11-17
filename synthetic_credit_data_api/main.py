"""FastAPI application entrypoint for Synthetic Credit Data API."""
from __future__ import annotations

import logging

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

from .config import settings
from .generator import generate_records
from .logging_conf import setup_logging
from .models import GenerateRequest, GenerateResponse

setup_logging()
log = logging.getLogger(__name__)

app = FastAPI(title="Synthetic Credit Data API", version="1.0.0")


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "version": "1.0.0"}


@app.get("/v1/meta")
def meta() -> dict:
    return {
        "product": "Synthetic Credit Data API",
        "feature": "Privacy-safe synthetic datasets via a clean REST API",
        "max_rows": settings.max_rows,
    }


@app.post("/v1/generate", response_model=GenerateResponse)
def generate(req: GenerateRequest) -> GenerateResponse:
    """Generate synthetic records. Privacy-safe synthetic datasets via a clean REST API"""
    if req.rows < 1 or req.rows > settings.max_rows:
        raise HTTPException(status_code=400, detail=f"rows must be 1..{settings.max_rows}")
    log.info("generate requested rows=%s schema=%s", req.rows, req.schema_name)
    try:
        rows = generate_records(req.rows, req.schema_name, seed=req.seed)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    return GenerateResponse(rows=req.rows, schema_name=req.schema_name, data=rows)


@app.exception_handler(Exception)
async def unhandled(_request, exc: Exception):  # pragma: no cover
    log.exception("unhandled error: %s", exc)
    return JSONResponse(status_code=500, content={"detail": "internal error"})
