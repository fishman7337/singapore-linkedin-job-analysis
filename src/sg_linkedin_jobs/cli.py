"""Command-line entrypoint for the data preparation pipeline."""

from __future__ import annotations

import argparse
from pathlib import Path

from sg_linkedin_jobs.config import DEFAULT_PROCESSED_FILE, DEFAULT_RAW_DIR
from sg_linkedin_jobs.pipeline import build_analysis_dataset, write_processed_dataset


def build_parser() -> argparse.ArgumentParser:
    """Build the job-dataset preparation argument parser."""
    parser = argparse.ArgumentParser(
        description="Build the cleaned Singapore LinkedIn job analysis dataset."
    )
    parser.add_argument(
        "--raw-dir",
        type=Path,
        default=DEFAULT_RAW_DIR,
        help="Directory with raw files.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_PROCESSED_FILE,
        help="CSV path for the processed dataset.",
    )
    parser.add_argument(
        "--keep-outliers",
        action="store_true",
        help="Keep salary outliers instead of applying the IQR filter.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    """Build and write the configured LinkedIn job analysis dataset.

    Args:
        argv: Command-line arguments without the executable name. Uses
            ``sys.argv`` when omitted.

    Returns:
        A process exit code.
    """
    args = build_parser().parse_args(argv)
    dataset = build_analysis_dataset(args.raw_dir, remove_outliers=not args.keep_outliers)
    output_path = write_processed_dataset(dataset, args.output)
    print(f"Wrote {len(dataset):,} rows to {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
