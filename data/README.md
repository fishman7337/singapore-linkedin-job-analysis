# Data Directory

Raw and processed datasets are intentionally not committed to Git.

## Expected Raw Files

Place the original assignment files in `data/raw/`:

| File | Purpose |
| --- | --- |
| `postings1.csv` | Core posting identity fields such as `job_id`, company, and title |
| `postings2.csv` | Description and maximum salary fields |
| `postings3.csv` | Salary, company, location, pay period, and view fields |
| `postings4.csv` | Application, work arrangement, seniority, timestamp, and metadata fields |
| `postings5.xlsx` | Supplemental assignment table with duplicate identity and irrelevant exercise columns |

## Generated Files

Processed outputs should be written to `data/processed/`, for example:

```powershell
python -m sg_linkedin_jobs.cli --raw-dir data/raw --output data/processed/linkedin_jobs_cleaned.csv
```

## Governance

- Do not commit raw data.
- Do not commit large generated files unless explicitly approved.
- Keep source filenames stable so the notebook and CLI remain reproducible.
- Document schema changes in `docs/DATA_DICTIONARY.md`.
