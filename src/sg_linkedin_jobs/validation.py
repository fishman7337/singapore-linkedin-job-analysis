"""Schema validation helpers for raw and processed data."""

from __future__ import annotations

from collections.abc import Mapping

import pandas as pd

RAW_REQUIRED_COLUMNS: dict[str, set[str]] = {
    "postings_core": {"job_id", "company_name", "title"},
    "postings_description": {"job_id", "description", "max_salary"},
    "postings_salary": {
        "job_id",
        "company_id",
        "pay_period",
        "location",
        "views",
        "med_salary",
        "min_salary",
    },
    "postings_metadata": {
        "job_id",
        "applies",
        "remote_allowed",
        "formatted_experience_level",
        "listed_time",
        "expiry",
    },
    "postings_extra": {"job_id", "company_name", "title"},
}

PROCESSED_REQUIRED_COLUMNS = {
    "company_name",
    "title",
    "max_salary",
    "pay_period",
    "location",
    "views",
    "min_salary",
    "applies",
    "remote_allowed",
    "formatted_experience_level",
    "expiry",
    "listed_time",
    "max_salary_normalised",
    "min_salary_normalised",
    "postingDuration",
    "salary_range",
    "apply_view_ratio",
}


def require_columns(df: pd.DataFrame, required_columns: set[str], table_name: str) -> None:
    """Raise a clear error when expected columns are missing."""
    missing = sorted(required_columns.difference(df.columns))
    if missing:
        raise ValueError(f"{table_name} is missing required columns: {', '.join(missing)}")


def validate_raw_tables(tables: Mapping[str, pd.DataFrame]) -> None:
    """Validate that all required raw tables and minimum columns are present."""
    missing_tables = sorted(set(RAW_REQUIRED_COLUMNS).difference(tables))
    if missing_tables:
        raise ValueError(f"Missing raw tables: {', '.join(missing_tables)}")

    for table_name, required_columns in RAW_REQUIRED_COLUMNS.items():
        require_columns(tables[table_name], required_columns, table_name)


def validate_processed_schema(df: pd.DataFrame) -> None:
    """Validate the processed dataset used for analysis and visualisation."""
    require_columns(df, PROCESSED_REQUIRED_COLUMNS, "processed dataset")

    non_negative_columns = [
        "max_salary_normalised",
        "min_salary_normalised",
        "salary_range",
        "views",
        "applies",
        "apply_view_ratio",
    ]
    negative_counts = df[non_negative_columns].lt(0).sum()
    failing = negative_counts[negative_counts > 0]
    if not failing.empty:
        details = ", ".join(f"{column}={count}" for column, count in failing.items())
        raise ValueError(f"Processed dataset contains negative values: {details}")
