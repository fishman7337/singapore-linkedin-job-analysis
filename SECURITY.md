# Security Policy

## Supported Versions

This is an academic analytics project. The latest `main` branch is the supported version.

## Reporting a Vulnerability

Report security concerns privately to the repository maintainer or the relevant academic supervisor. Include:

- affected file or workflow
- steps to reproduce
- potential impact
- suggested mitigation, if known

## Data Handling

- Do not commit raw LinkedIn datasets, credentials, API tokens, or local exports.
- Store raw files in `data/raw/` only on trusted machines.
- Keep processed outputs in `data/processed/` local unless the output has been approved for sharing.
- Remove personally identifiable information before publishing derived artifacts.
