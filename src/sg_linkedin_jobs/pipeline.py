"""End-to-end data preparation pipeline."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from sg_linkedin_jobs.cleaning import clean_job_postings
from sg_linkedin_jobs.config import DEFAULT_PROCESSED_FILE, DEFAULT_RAW_DIR
from sg_linkedin_jobs.data import load_raw_tables
from sg_linkedin_jobs.features import OUTLIER_COLUMNS, add_analysis_features, remove_outliers_iqr
from sg_linkedin_jobs.validation import validate_processed_schema


def build_analysis_dataset(
    raw_dir: str | Path = DEFAULT_RAW_DIR,
    remove_outliers: bool = True,
) -> pd.DataFrame:
    """Load raw tables and return the processed analysis dataset."""
    raw_tables = load_raw_tables(raw_dir)
    cleaned = clean_job_postings(raw_tables)
    featured = add_analysis_features(cleaned)
    processed = remove_outliers_iqr(featured, OUTLIER_COLUMNS) if remove_outliers else featured
    validate_processed_schema(processed)
    return processed


def write_processed_dataset(
    df: pd.DataFrame,
    output_path: str | Path = DEFAULT_PROCESSED_FILE,
) -> Path:
    """Write the processed dataset to CSV and return the output path."""
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=True)
    return path
