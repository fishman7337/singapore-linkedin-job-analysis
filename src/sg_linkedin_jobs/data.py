"""Raw data loading helpers."""

from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

import pandas as pd

from sg_linkedin_jobs.config import DEFAULT_RAW_DIR, RAW_TABLE_FILES

RawTables = dict[str, pd.DataFrame]


def load_raw_tables(
    raw_dir: str | Path = DEFAULT_RAW_DIR,
    table_files: Mapping[str, str] | None = None,
) -> RawTables:
    """Load all raw tables required by the analysis.

    Parameters
    ----------
    raw_dir:
        Directory containing the assignment source files.
    table_files:
        Optional mapping of logical table names to filenames. Defaults to the
        coursework filenames documented in ``data/README.md``.
    """
    raw_path = Path(raw_dir)
    files = dict(table_files or RAW_TABLE_FILES)
    missing = [
        raw_path / filename for filename in files.values() if not (raw_path / filename).exists()
    ]

    if missing:
        formatted = "\n".join(f"- {path}" for path in missing)
        raise FileNotFoundError(
            "Missing raw dataset files. Place the assignment data under "
            f"{raw_path.resolve()}:\n{formatted}"
        )

    return {name: read_table(raw_path / filename) for name, filename in files.items()}


def read_table(path: str | Path) -> pd.DataFrame:
    """Read a CSV or Excel table from disk."""
    table_path = Path(path)
    suffix = table_path.suffix.lower()

    if suffix == ".csv":
        return pd.read_csv(table_path)
    if suffix in {".xlsx", ".xls"}:
        return pd.read_excel(table_path)

    raise ValueError(f"Unsupported table format for {table_path}. Expected CSV or Excel.")
