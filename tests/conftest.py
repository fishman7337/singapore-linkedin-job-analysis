from __future__ import annotations

import numpy as np
import pandas as pd
import pytest


@pytest.fixture
def raw_tables() -> dict[str, pd.DataFrame]:
    day_ms = 24 * 60 * 60 * 1000

    return {
        "postings_core": pd.DataFrame(
            {
                "job_id": [1, 2],
                "company_name": ["Acme Analytics", np.nan],
                "title": ["Data Analyst", "AI Engineer"],
            }
        ),
        "postings_description": pd.DataFrame(
            {
                "job_id": [1, 2],
                "description": ["Analyse dashboards", "Build models"],
                "max_salary": [6000, np.nan],
            }
        ),
        "postings_salary": pd.DataFrame(
            {
                "job_id": [1, 2],
                "company_id": [101, 102],
                "pay_period": ["MONTHLY", np.nan],
                "location": ["Singapore", "Singapore"],
                "views": [100, np.nan],
                "med_salary": [5000, np.nan],
                "min_salary": [4000, np.nan],
            }
        ),
        "postings_metadata": pd.DataFrame(
            {
                "job_id": [1, 2],
                "job_posting_url": ["https://example.com/1", "https://example.com/2"],
                "application_url": ["https://apply.example.com/1", np.nan],
                "formatted_work_type": ["Full-time", "Full-time"],
                "remote_allowed": [1, np.nan],
                "application_type": ["OffsiteApply", "SimpleOnsiteApply"],
                "formatted_experience_level": ["Entry level", np.nan],
                "skills_desc": ["Python", "ML"],
                "posting_domain": ["example.com", "example.com"],
                "sponsored": [0, 0],
                "work_type": ["FULL_TIME", "FULL_TIME"],
                "currency": ["SGD", "SGD"],
                "compensation_type": ["BASE_SALARY", "BASE_SALARY"],
                "applies": [10, np.nan],
                "original_listed_time": [0, day_ms],
                "listed_time": [0, day_ms],
                "expiry": [30 * day_ms, 31 * day_ms],
                "closed_time": [np.nan, np.nan],
            }
        ),
        "postings_extra": pd.DataFrame(
            {
                "job_id": [1, 2],
                "company_name": ["Acme Analytics", "Backup Company"],
                "title": ["Data Analyst", "AI Engineer"],
                "Easter Egg": ["ignore", "ignore"],
                "Unimportant Column": ["ignore", "ignore"],
            }
        ),
    }
