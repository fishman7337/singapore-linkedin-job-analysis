# Singapore LinkedIn Job Market Analytics

Singapore LinkedIn Job Market Analytics is a DataOps-ready exploratory data analysis project on Singapore job listings. It studies how salary, work arrangement, seniority, posting duration, views, and applications relate to job-post visibility and applicant conversion.

This repository preserves the original ST1510 CA1 notebook and presentation while adding a maintainable Python package, tests, documentation, and CI for future reuse.

## Academic Context

| Field | Details |
| --- | --- |
| Institution | Singapore Polytechnic, School of Computing |
| Diploma | Diploma in Applied AI & Analytics |
| Module | ST1510 Programming for Data Analytics |
| Assessment | CA1 |
| Academic year | AY24/25, Year 1 Semester 2 |
| Student | Goh Kun Ming, DAAA Student |
| Lecturer | Senior Lecturer Goh Chia Ming |

## Research Question

What factors make job postings more visible and increase application rates, and how can job seekers use these insights to improve their job search?

## Project Structure

```text
.
├── .github/                  # CI workflow, issue templates, PR template
├── data/
│   ├── raw/                  # Local-only source files, see data/README.md
│   └── processed/            # Local-only generated datasets
├── docs/                     # DataOps, data dictionary, ethics, runbook, charter
├── notebooks/                # Original CA1 analysis notebook
├── reports/slides/           # Original CA1 presentation deck
├── src/sg_linkedin_jobs/     # Reusable data loading, cleaning, feature code
└── tests/                    # Pytest coverage for reusable logic
```

## Quick Start

Use Python 3.10 or newer.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
pytest
```

For macOS or Linux:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
pytest
```

## Data Setup

The raw LinkedIn job-listing files are not committed to the repository. Place the assignment data in `data/raw/` using these exact names:

```text
postings1.csv
postings2.csv
postings3.csv
postings4.csv
postings5.xlsx
```

Then build the processed analysis dataset:

```powershell
python -m sg_linkedin_jobs.cli --raw-dir data/raw --output data/processed/linkedin_jobs_cleaned.csv
```

The notebook in `notebooks/ca1_linkedin_job_analysis.ipynb` expects the same raw files under `data/raw/`.

## Reproducibility

The reusable pipeline performs the main preparation steps from the notebook:

- load five raw posting tables
- merge on `job_id`
- remove analysis-irrelevant columns
- fill missing company, salary, views, applications, remote-work, pay-period, and seniority values
- standardise pay-period labels
- convert timestamp fields
- engineer annualised salary, salary range, posting duration, and apply-to-view ratio
- optionally remove salary outliers with the IQR method

## Validation

Run the local quality gate before committing:

```powershell
ruff check src tests
pytest
```

GitHub Actions runs the same checks on push and pull request events.

## Documentation

- [Data setup](data/README.md)
- [Data dictionary](docs/DATA_DICTIONARY.md)
- [DataOps workflow](docs/DATAOPS.md)
- [Ethics and privacy](docs/ETHICS.md)
- [Operational runbook](docs/RUNBOOK.md)
- [Project charter](docs/PROJECT_CHARTER.md)
- [Contributing guide](CONTRIBUTING.md)

## License

Released under the MIT License. See [LICENSE](LICENSE).
