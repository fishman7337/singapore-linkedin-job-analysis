# Architecture

The repository separates exploratory analysis from reusable data-preparation code.

## Layers

| Layer | Path | Responsibility |
| --- | --- | --- |
| Raw data | `data/raw/` | Local-only source files |
| Processed data | `data/processed/` | Local-only generated outputs |
| Notebooks | `notebooks/` | Original, cleaned full, and section-level EDA notebooks |
| Package | `src/sg_linkedin_jobs/` | Reusable loading, cleaning, feature, validation, and CLI code |
| Tests | `tests/` | Synthetic-data validation for reusable logic |
| CI | `.github/workflows/ci.yml` | Automated linting and tests |

## Package Modules

| Module | Purpose |
| --- | --- |
| `config.py` | Shared filenames and default paths |
| `data.py` | Raw CSV and Excel loading |
| `validation.py` | Raw and processed schema checks |
| `cleaning.py` | Merge, column selection, missing-value handling, type conversion |
| `features.py` | Salary normalisation, posting duration, apply-to-view ratio, outlier filters |
| `pipeline.py` | End-to-end build and write functions |
| `cli.py` | Command-line interface |

## Design Notes

- Notebook code remains available for assessment traceability.
- Reusable transformation logic is testable outside Jupyter.
- CI does not need raw data because tests use synthetic fixtures.
- Raw and processed data folders are tracked only with placeholders and documentation.
