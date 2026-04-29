"""Project configuration and path conventions."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_RAW_DIR = PROJECT_ROOT / "data" / "raw"
DEFAULT_PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"
DEFAULT_PROCESSED_FILE = DEFAULT_PROCESSED_DIR / "linkedin_jobs_cleaned.csv"

RAW_TABLE_FILES = {
    "postings_core": "postings1.csv",
    "postings_description": "postings2.csv",
    "postings_salary": "postings3.csv",
    "postings_metadata": "postings4.csv",
    "postings_extra": "postings5.xlsx",
}


@dataclass(frozen=True)
class PipelineConfig:
    """Runtime configuration for the data preparation pipeline."""

    raw_dir: Path = DEFAULT_RAW_DIR
    output_path: Path = DEFAULT_PROCESSED_FILE
    remove_outliers: bool = True
