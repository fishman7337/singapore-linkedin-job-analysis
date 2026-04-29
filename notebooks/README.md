# Notebooks

This folder contains the CA1 exploratory analysis notebooks:

| Path | Purpose |
| --- | --- |
| `ca1_linkedin_job_analysis.ipynb` | Cleaned full notebook aligned to the reorganised repository paths |
| `original/CA1 (1).ipynb` | Exact original submitted notebook retained for traceability |
| `sections/` | Section-level notebooks generated from the original notebook |

The cleaned full notebook expects raw files in `../data/raw/` because it sits one level below the repository root. The original and generated section notebooks preserve the submitted notebook cells.

Run the reusable Python pipeline first when possible. It provides faster feedback on data availability, schemas, and transformation logic before rerunning the full exploratory notebook.
