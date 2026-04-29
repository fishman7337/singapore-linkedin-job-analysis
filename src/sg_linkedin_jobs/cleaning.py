"""Data cleaning operations adapted from the CA1 notebook."""

from __future__ import annotations

from collections.abc import Mapping

import pandas as pd

from sg_linkedin_jobs.validation import validate_raw_tables

IRRELEVANT_COLUMNS = [
    "job_posting_url",
    "sponsored",
    "posting_domain",
    "application_url",
    "description",
    "original_listed_time",
    "skills_desc",
    "closed_time",
    "company_id",
    "currency",
    "compensation_type",
    "work_type",
    "med_salary",
    "Easter Egg",
    "Unimportant Column",
    "title_y",
    "company_name_y",
]

PAY_PERIOD_LABELS = {
    "YEARLY": "Yearly",
    "MONTHLY": "Monthly",
    "BIWEEKLY": "Biweekly",
    "WEEKLY": "Weekly",
    "HOURLY": "Hourly",
}


def clean_job_postings(raw_tables: Mapping[str, pd.DataFrame]) -> pd.DataFrame:
    """Return a cleaned analysis table from the five raw assignment tables."""

    merged = merge_posting_tables(raw_tables)
    selected = select_analysis_columns(merged)
    imputed = impute_missing_values(selected)
    deduplicated = imputed.drop_duplicates()
    typed = coerce_analysis_types(deduplicated)
    return standardise_pay_period(typed)


def merge_posting_tables(raw_tables: Mapping[str, pd.DataFrame]) -> pd.DataFrame:
    """Merge the five raw posting tables on ``job_id`` using inner joins."""

    validate_raw_tables(raw_tables)
    merged = (
        raw_tables["postings_core"]
        .merge(raw_tables["postings_description"], on="job_id", how="inner")
        .merge(raw_tables["postings_salary"], on="job_id", how="inner")
        .merge(raw_tables["postings_metadata"], on="job_id", how="inner")
        .merge(raw_tables["postings_extra"], on="job_id", how="inner")
    )
    return merged.set_index("job_id", drop=True)


def select_analysis_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Remove columns that do not support the research question."""

    selected = df.drop(columns=IRRELEVANT_COLUMNS, errors="ignore").copy()
    return selected.rename(columns={"company_name_x": "company_name", "title_x": "title"})


def impute_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """Fill missing values using the rules from the original notebook."""

    imputed = df.copy()

    if "company_name" in imputed:
        imputed["company_name"] = imputed["company_name"].fillna("Unknown")

    for column in ["views", "applies", "remote_allowed"]:
        if column in imputed:
            imputed[column] = pd.to_numeric(imputed[column], errors="coerce").fillna(0)

    for column in ["pay_period", "formatted_experience_level"]:
        if column in imputed:
            imputed[column] = imputed[column].fillna(_mode_or_default(imputed[column], "Unknown"))

    for column in ["max_salary", "min_salary"]:
        if column in imputed:
            imputed[column] = pd.to_numeric(imputed[column], errors="coerce")
            imputed = interpolate_salary_by_group(imputed, column)
            imputed[column] = imputed[column].fillna(imputed[column].median()).fillna(0)

    return imputed


def interpolate_salary_by_group(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """Interpolate salary values within pay-period and seniority groups."""

    group_columns = ["pay_period", "formatted_experience_level"]
    if column not in df or any(group_column not in df for group_column in group_columns):
        return df

    sort_columns = [column for column in [*group_columns, "listed_time"] if column in df]
    interpolated = df.sort_values(sort_columns).copy() if sort_columns else df.copy()
    interpolated[column] = interpolated.groupby(group_columns, dropna=False)[column].transform(
        lambda series: series.interpolate(method="linear", limit_direction="both")
    )
    return interpolated.sort_index()


def coerce_analysis_types(df: pd.DataFrame) -> pd.DataFrame:
    """Convert known analysis columns to stable numeric and datetime dtypes."""

    typed = df.copy()
    integer_columns = ["max_salary", "views", "min_salary", "applies", "remote_allowed"]

    for column in integer_columns:
        if column in typed:
            typed[column] = (
                pd.to_numeric(typed[column], errors="coerce")
                .fillna(0)
                .round()
                .astype("int64")
            )

    for column in ["expiry", "listed_time"]:
        if column in typed:
            typed[column] = pd.to_datetime(typed[column], unit="ms", errors="coerce")

    return typed


def standardise_pay_period(df: pd.DataFrame) -> pd.DataFrame:
    """Use title-case pay-period labels for readable reporting."""

    standardised = df.copy()
    if "pay_period" in standardised:
        standardised["pay_period"] = standardised["pay_period"].replace(PAY_PERIOD_LABELS)
    return standardised


def _mode_or_default(series: pd.Series, default: str) -> object:
    mode = series.dropna().mode()
    return mode.iloc[0] if not mode.empty else default
