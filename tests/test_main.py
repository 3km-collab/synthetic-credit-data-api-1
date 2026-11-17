"""pytest suite for the synthetic_credit_data_api package."""
from fastapi.testclient import TestClient

from synthetic_credit_data_api.generator import generate_records
from synthetic_credit_data_api.main import app

client = TestClient(app)


def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"


def test_meta():
    r = client.get("/v1/meta")
    assert r.status_code == 200
    assert "product" in r.json()


def test_generate_basic():
    r = client.post("/v1/generate", json={"rows": 5, "schema_name": "default"})
    assert r.status_code == 200
    body = r.json()
    assert body["rows"] == 5
    assert len(body["data"]) == 5


def test_generate_invalid_rows():
    r = client.post("/v1/generate", json={"rows": 0})
    assert r.status_code in (400, 422)


def test_generator_deterministic_with_seed():
    a = generate_records(3, seed=1)
    b = generate_records(3, seed=1)
    assert a == b


def test_generator_rejects_bad_schema():
    try:
        generate_records(2, schema_name="nope")
    except ValueError:
        return
    raise AssertionError("expected ValueError")
