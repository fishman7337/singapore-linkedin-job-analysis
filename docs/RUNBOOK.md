# Runbook

## Install

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## Prepare Data

Place the raw files in `data/raw/`:

```text
postings1.csv
postings2.csv
postings3.csv
postings4.csv
postings5.xlsx
```

## Build Processed Dataset

```powershell
python -m sg_linkedin_jobs.cli --raw-dir data/raw --output data/processed/linkedin_jobs_cleaned.csv
```

To keep outliers:

```powershell
python -m sg_linkedin_jobs.cli --raw-dir data/raw --output data/processed/linkedin_jobs_cleaned.csv --keep-outliers
```

## Run Checks

```powershell
ruff check src tests
pytest
```

## Open the Notebook

```powershell
jupyter notebook notebooks/ca1_linkedin_job_analysis.ipynb
```

## Common Issues

### Missing raw files

If the CLI reports missing files, confirm the names and location under `data/raw/`. The filenames must match exactly.

### Excel dependency error

Install dependencies again:

```powershell
python -m pip install -e ".[dev]"
```

### Unexpected schema error

Check whether the source files have changed. Update `docs/DATA_DICTIONARY.md`, tests, and validation code if the schema change is intentional.
