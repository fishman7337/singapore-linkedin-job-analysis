"""Feature engineering and outlier handling for job-posting analysis."""

from __future__ import annotations

from collections.abc import Iterable

import numpy as np
import pandas as pd

PAY_PERIOD_MULTIPLIERS = {
    "Hourly": 40 * 52,
    "Weekly": 52,
    "Biweekly": 26,
    "Monthly": 12,
    "Yearly": 1,
}

OUTLIER_COLUMNS = ["min_salary_normalised", "max_salary_normalised", "salary_range"]


def add_analysis_features(df: pd.DataFrame) -> pd.DataFrame:
    """Add derived salary, duration, and engagement metrics."""
    featured = add_salary_features(df)
    featured = add_temporal_features(featured)
    return add_engagement_features(featured)


def add_salary_features(df: pd.DataFrame) -> pd.DataFrame:
    """Annualise salary fields and calculate salary range."""
    featured = df.copy()
    multiplier = featured["pay_period"].map(PAY_PERIOD_MULTIPLIERS).fillna(1)
    featured["max_salary_normalised"] = (
        pd.to_numeric(featured["max_salary"], errors="coerce").fillna(0) * multiplier
    )
    featured["min_salary_normalised"] = (
        pd.to_numeric(featured["min_salary"], errors="coerce").fillna(0) * multiplier
    )
    featured["salary_range"] = (
        featured["max_salary_normalised"] - featured["min_salary_normalised"]
    ).clip(lower=0)
    return featured


def add_temporal_features(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate posting duration in days."""
    featured = df.copy()
    featured["postingDuration"] = (featured["expiry"] - featured["listed_time"]).dt.days
    featured["postingDuration"] = featured["postingDuration"].fillna(0).astype("int64")
    return featured


def add_engagement_features(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate application conversion while avoiding division by zero."""
    featured = df.copy()
    views = pd.to_numeric(featured["views"], errors="coerce").replace(0, np.nan)
    applies = pd.to_numeric(featured["applies"], errors="coerce").fillna(0)
    featured["apply_view_ratio"] = (applies / views).replace([np.inf, -np.inf], np.nan).fillna(0)
    return featured


def remove_outliers_iqr(
    df: pd.DataFrame,
    columns: Iterable[str] = OUTLIER_COLUMNS,
    multiplier: float = 1.5,
) -> pd.DataFrame:
    """Remove outliers column-by-column using the interquartile range method."""
    filtered = df.copy()

    for column in columns:
        if column not in filtered or filtered[column].empty:
            continue

        q1 = filtered[column].quantile(0.25)
        q3 = filtered[column].quantile(0.75)
        iqr = q3 - q1

        if pd.isna(iqr) or iqr == 0:
            continue

        lower_fence = q1 - multiplier * iqr
        upper_fence = q3 + multiplier * iqr
        filtered = filtered[filtered[column].between(lower_fence, upper_fence)]

    return filtered


def remove_outliers_zscore(
    df: pd.DataFrame,
    columns: Iterable[str] = OUTLIER_COLUMNS,
    threshold: float = 3.0,
) -> pd.DataFrame:
    """Remove outliers column-by-column using z-scores."""
    filtered = df.copy()

    for column in columns:
        if column not in filtered or filtered[column].empty:
            continue

        standard_deviation = filtered[column].std()
        if pd.isna(standard_deviation) or standard_deviation == 0:
            continue

        z_score = (filtered[column] - filtered[column].mean()) / standard_deviation
        filtered = filtered[z_score.abs() <= threshold]

    return filtered
