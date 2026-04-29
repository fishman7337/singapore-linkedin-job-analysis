.PHONY: install lint test checks pipeline

install:
	python -m pip install -e ".[dev]"

lint:
	ruff check src tests scripts

test:
	pytest

checks: lint test

pipeline:
	python -m sg_linkedin_jobs.cli --raw-dir data/raw --output data/processed/linkedin_jobs_cleaned.csv
