.PHONY: install run test docker sample clean

install:
	pip install -r requirements.txt

run:
	uvicorn synthetic_credit_data_api.main:app --host 0.0.0.0 --port 8000 --reload

test:
	pytest -q

docker:
	docker compose up --build

sample:
	python scripts/make_samples.py

clean:
	find . -name '__pycache__' -type d -prune -exec rm -rf {} + ; rm -rf .pytest_cache
