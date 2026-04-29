# Data Dictionary

This dictionary documents the main fields used by the notebook and reusable pipeline. Raw files should be placed in `data/raw/`.

## Raw Tables

### `postings1.csv`

| Column | Meaning |
| --- | --- |
| `job_id` | Unique job-posting identifier used for joins |
| `company_name` | Name of the hiring company |
| `title` | Job title |

### `postings2.csv`

| Column | Meaning |
| --- | --- |
| `job_id` | Unique job-posting identifier |
| `description` | Text description of the role |
| `max_salary` | Maximum advertised salary before pay-period normalisation |

### `postings3.csv`

| Column | Meaning |
| --- | --- |
| `job_id` | Unique job-posting identifier |
| `company_id` | Company identifier from source data |
| `pay_period` | Salary period such as yearly, monthly, weekly, biweekly, or hourly |
| `location` | Job location |
| `views` | Number of recorded posting views |
| `med_salary` | Median advertised salary, not used in the final analysis |
| `min_salary` | Minimum advertised salary before pay-period normalisation |

### `postings4.csv`

| Column | Meaning |
| --- | --- |
| `job_id` | Unique job-posting identifier |
| `applies` | Number of recorded applications |
| `remote_allowed` | Binary remote-work indicator, where `1` means remote allowed |
| `formatted_experience_level` | Experience level label |
| `listed_time` | Posting listed timestamp in milliseconds |
| `expiry` | Posting expiry timestamp in milliseconds |
| `formatted_work_type` | Human-readable work-type label |
| `application_type` | Application flow category |
| `skills_desc` | Skill description text |

### `postings5.xlsx`

| Column | Meaning |
| --- | --- |
| `job_id` | Unique job-posting identifier |
| `company_name` | Duplicate company field |
| `title` | Duplicate title field |
| `Easter Egg` | Assignment exercise field, removed from analysis |
| `Unimportant Column` | Assignment exercise field, removed from analysis |

## Processed Fields

| Column | Meaning |
| --- | --- |
| `company_name` | Cleaned company name, filled with `Unknown` when missing |
| `title` | Job title |
| `max_salary` | Cleaned maximum salary in original pay-period units |
| `min_salary` | Cleaned minimum salary in original pay-period units |
| `pay_period` | Standardised pay-period label |
| `location` | Job location |
| `views` | Cleaned number of views |
| `applies` | Cleaned number of applications |
| `remote_allowed` | Cleaned binary remote-work indicator |
| `formatted_experience_level` | Cleaned experience-level label |
| `listed_time` | Converted listing datetime |
| `expiry` | Converted expiry datetime |
| `max_salary_normalised` | Maximum salary annualised to yearly equivalent |
| `min_salary_normalised` | Minimum salary annualised to yearly equivalent |
| `salary_range` | Difference between annualised max and min salary |
| `postingDuration` | Number of days between listing and expiry |
| `apply_view_ratio` | Applications divided by views, with zero views handled safely |
