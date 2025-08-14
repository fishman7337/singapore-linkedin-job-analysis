# Singapore Job Market Analysis

An exploratory data analysis project on structured job listing data to uncover hiring trends, in-demand roles, and skill gaps within Singapore’s labour market. This analysis uses real-world job postings to generate actionable insights for workforce planning and job-seeking strategies.

---

## Overview
The project investigates:
- What factors make job postings more visible and increase application rates
- How job seekers can leverage these insights to improve their job search

---

## Tech Stack
- **Python**
- **pandas** – Data wrangling and preprocessing
- **NumPy** – Numerical computations
- **matplotlib** – Data visualisation

---

## Features
- Merging multiple datasets of job listings by **Job ID**
- Data cleaning, including:
  - Imputing missing values (median, interpolation, etc.)
  - Removing duplicates
  - Correcting data types
  - Standardising formats
- Outlier removal using **IQR** and **Z-score** methods
- Feature engineering to summarise and transform key variables
- Detailed visualisations, including:
  - Job posting duration trends
  - Job type distribution
  - Viewer-to-applicant ratios
  - Apply-to-view ratios across salary ranges
  - Salary insights by experience level
  - Work type (remote/on-site) breakdowns
  - Posting duration vs. apply-to-view ratios

---

## Key Insights
- Job postings typically last for around **1 month**
- Not all viewers become applicants; conversion rates vary
- Remote work is rare, especially for internships and senior roles, despite high demand
- Both lower and higher salary ranges have higher apply-to-view ratios than mid-range salaries
- Higher-experience roles pay more but have lower apply-to-view ratios compared to junior roles
- Job postings see the highest apply-to-view ratio at **120 days** duration
