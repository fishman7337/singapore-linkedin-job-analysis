from __future__ import annotations

import pandas as pd

from sg_linkedin_jobs.cleaning import clean_job_postings
from sg_linkedin_jobs.features import add_analysis_features
from sg_linkedin_jobs.pipeline import write_processed_dataset
from sg_linkedin_jobs.validation import validate_processed_schema


def test_processed_schema_accepts_featured_dataset(raw_tables):
    processed = add_analysis_features(clean_job_postings(raw_tables))

    validate_processed_schema(processed)


def test_write_processed_dataset_creates_parent_directory(tmp_path, raw_tables):
    processed = add_analysis_features(clean_job_postings(raw_tables))
    output_path = tmp_path / "nested" / "linkedin_jobs_cleaned.csv"

    written = write_processed_dataset(processed, output_path)

    assert written == output_path
    assert output_path.exists()
    round_tripped = pd.read_csv(output_path)
    assert len(round_tripped) == len(processed)
