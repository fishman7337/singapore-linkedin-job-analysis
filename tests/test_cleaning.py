from __future__ import annotations

import pandas as pd

from sg_linkedin_jobs.cleaning import (
    clean_job_postings,
    merge_posting_tables,
    select_analysis_columns,
)


def test_merge_posting_tables_uses_job_id_index(raw_tables):
    merged = merge_posting_tables(raw_tables)

    assert merged.index.name == "job_id"
    assert len(merged) == 2
    assert "company_name_x" in merged.columns
    assert "company_name_y" in merged.columns


def test_select_analysis_columns_removes_irrelevant_fields(raw_tables):
    selected = select_analysis_columns(merge_posting_tables(raw_tables))

    assert "company_name" in selected.columns
    assert "title" in selected.columns
    assert "description" not in selected.columns
    assert "Easter Egg" not in selected.columns
    assert "job_posting_url" not in selected.columns


def test_clean_job_postings_imputes_and_coerces_values(raw_tables):
    cleaned = clean_job_postings(raw_tables)

    assert cleaned.loc[2, "company_name"] == "Unknown"
    assert cleaned.loc[2, "pay_period"] == "Monthly"
    assert cleaned.loc[2, "formatted_experience_level"] == "Entry level"
    assert cleaned.loc[2, "views"] == 0
    assert cleaned.loc[2, "remote_allowed"] == 0
    assert cleaned.loc[2, "max_salary"] == 6000
    assert cleaned.loc[2, "min_salary"] == 4000
    assert pd.api.types.is_datetime64_any_dtype(cleaned["listed_time"])
    assert pd.api.types.is_integer_dtype(cleaned["applies"])
