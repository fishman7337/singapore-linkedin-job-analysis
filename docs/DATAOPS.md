# DataOps Workflow

This project uses lightweight DataOps practices appropriate for an academic analytics repository.

## Principles

- Keep raw data local and immutable.
- Make transformations repeatable through code.
- Validate schemas before and after processing.
- Test reusable logic with synthetic data.
- Run CI on every push and pull request.
- Document assumptions, limitations, and ethical considerations.

## Data Lifecycle

1. Acquire the assignment datasets through the approved module channel.
2. Store raw files in `data/raw/` with the documented filenames.
3. Run the processing CLI:

   ```powershell
   python -m sg_linkedin_jobs.cli --raw-dir data/raw --output data/processed/linkedin_jobs_cleaned.csv
   ```

4. Review generated outputs in `data/processed/`.
5. Use the notebook for exploratory charts and interpretation.
6. Keep raw and processed data out of Git unless explicit approval is given.

## Validation Gates

| Gate | Tool | Purpose |
| --- | --- | --- |
| Static lint | `ruff check src tests` | Detect import, style, and common Python issues |
| Unit tests | `pytest` | Validate cleaning, feature engineering, and output writing |
| Schema validation | `sg_linkedin_jobs.validation` | Check required raw and processed columns |
| Data policy | `.gitignore` | Prevent accidental raw-data commits |

## Reproducibility Contract

The pipeline expects these files:

- `postings1.csv`
- `postings2.csv`
- `postings3.csv`
- `postings4.csv`
- `postings5.xlsx`

The reusable code intentionally avoids live external data access. Reproducibility depends on preserving the approved source files and keeping transformation code versioned.

## Quality Controls

- Missing numeric counts are filled with zero where absence means no recorded activity.
- Missing company names are filled as `Unknown`.
- Missing pay period and experience level values use the mode of the available data.
- Missing salary values are interpolated within pay-period and experience-level groups, then filled with the median if needed.
- Salary is annualised before comparing across pay periods.
- Division by zero in apply-to-view ratio returns `0`.
- IQR outlier removal is used by default because it is robust for skewed salary data.

## Limitations

- CI uses synthetic test data because raw coursework data is not committed.
- The analysis is exploratory and does not prove causation.
- LinkedIn posting data may reflect platform, collection, and employer-selection biases.
- Salary normalisation assumes 40 work hours per week and 52 weeks per year for hourly roles.

## Future Improvements

- Add Great Expectations or Pandera checks if the data contract becomes larger.
- Add notebook execution checks once raw data is available in a secure CI environment.
- Add data versioning with DVC or lakeFS if approved by the module or project owner.
- Export final charts to `reports/figures/` for easier review.
