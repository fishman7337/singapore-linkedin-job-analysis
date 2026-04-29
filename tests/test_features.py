from __future__ import annotations

import pandas as pd

from sg_linkedin_jobs.features import (
    add_analysis_features,
    remove_outliers_iqr,
    remove_outliers_zscore,
)


def test_add_analysis_features_annualises_salary_and_engagement():
    day_ms = 24 * 60 * 60 * 1000
    df = pd.DataFrame(
        {
            "pay_period": ["Hourly", "Monthly", "Biweekly", "Weekly", "Yearly"],
            "max_salary": [10, 1000, 2000, 500, 60000],
            "min_salary": [8, 800, 1500, 400, 50000],
            "views": [0, 20, 50, 100, 200],
            "applies": [5, 2, 10, 20, 40],
            "listed_time": pd.to_datetime([0, 0, 0, 0, 0], unit="ms"),
            "expiry": pd.to_datetime(
                [day_ms, 2 * day_ms, 3 * day_ms, 4 * day_ms, 5 * day_ms],
                unit="ms",
            ),
        }
    )

    featured = add_analysis_features(df)

    assert featured.loc[0, "max_salary_normalised"] == 20_800
    assert featured.loc[1, "max_salary_normalised"] == 12_000
    assert featured.loc[2, "max_salary_normalised"] == 52_000
    assert featured.loc[3, "max_salary_normalised"] == 26_000
    assert featured.loc[4, "max_salary_normalised"] == 60_000
    assert featured.loc[0, "apply_view_ratio"] == 0
    assert featured.loc[1, "apply_view_ratio"] == 0.1
    assert featured.loc[4, "postingDuration"] == 5


def test_remove_outliers_iqr_removes_extreme_salary_values():
    df = pd.DataFrame(
        {
            "min_salary_normalised": [10, 11, 12, 13, 14, 500],
            "max_salary_normalised": [20, 21, 22, 23, 24, 900],
            "salary_range": [10, 10, 10, 10, 10, 400],
        }
    )

    filtered = remove_outliers_iqr(df)

    assert len(filtered) == 5
    assert 500 not in filtered["min_salary_normalised"].to_list()


def test_remove_outliers_zscore_keeps_stable_values_when_std_is_zero():
    df = pd.DataFrame(
        {
            "min_salary_normalised": [100, 100, 100],
            "max_salary_normalised": [200, 200, 200],
            "salary_range": [100, 100, 100],
        }
    )

    filtered = remove_outliers_zscore(df)

    assert len(filtered) == 3
