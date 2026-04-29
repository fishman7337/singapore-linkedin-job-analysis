# Notebook Guide

The original CA1 notebook is stored at `notebooks/ca1_linkedin_job_analysis.ipynb`.

## Before Running

Place source data in `data/raw/` and install the project dependencies:

```powershell
python -m pip install -e ".[dev]"
```

## Path Convention

Because the notebook now lives under `notebooks/`, raw-data paths should use:

```python
../data/raw/postings1.csv
../data/raw/postings2.csv
../data/raw/postings3.csv
../data/raw/postings4.csv
../data/raw/postings5.xlsx
```

## Recommended Workflow

1. Run the reusable CLI to validate data loading and cleaning.
2. Open the notebook.
3. Restart the kernel and run all cells.
4. Compare the notebook outputs with the written conclusions.
5. Keep any generated data or figures out of Git unless approved.
