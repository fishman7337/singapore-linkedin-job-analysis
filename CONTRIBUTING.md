# Contributing

Thank you for improving this project. Contributions should keep the original CA1 analysis understandable while making the repository easier to reproduce, review, and maintain.

## Development Setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## Local Checks

Run these before opening a pull request:

```powershell
ruff check src tests
pytest
```

## Contribution Guidelines

- Keep raw datasets out of Git.
- Add or update tests when changing pipeline behaviour.
- Update `docs/DATA_DICTIONARY.md` when columns or derived features change.
- Update `docs/DATAOPS.md` when workflow, validation, or CI practices change.
- Preserve the academic attribution in `README.md`.
- Use clear commit messages that describe the user-facing change.

## Pull Request Checklist

- The change is scoped and described clearly.
- Tests pass locally.
- Documentation has been updated where needed.
- No raw data, credentials, or private files are included.
- Notebook changes are intentional and reproducible.
