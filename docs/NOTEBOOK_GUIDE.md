# Notebook Guide

The notebook folder contains three forms of the CA1 analysis:

| Path | Purpose |
| --- | --- |
| `notebooks/original/CA1 (1).ipynb` | Exact original submitted notebook |
| `notebooks/ca1_linkedin_job_analysis.ipynb` | Cleaned full notebook aligned to the repository structure |
| `notebooks/sections/` | Section-level notebooks generated from the original notebook |

The section notebooks preserve every original cell in order. The test suite checks that concatenating the section notebooks reconstructs the original notebook cells exactly.

## Before Running

Place source data in `data/raw/` and install the project dependencies:

```powershell
python -m pip install -e ".[dev]"
```

## Path Convention

Because the cleaned full notebook lives under `notebooks/`, raw-data paths should use:

```python
../data/raw/postings1.csv
../data/raw/postings2.csv
../data/raw/postings3.csv
../data/raw/postings4.csv
../data/raw/postings5.xlsx
```

## Recommended Workflow

1. Run the reusable CLI to validate data loading and cleaning.
2. Open the cleaned full notebook for an end-to-end run.
3. Restart the kernel and run all cells.
4. Compare the notebook outputs with the written conclusions.
5. Keep any generated data or figures out of Git unless approved.

Use the original notebook for submission traceability and the section notebooks for focused review.
