"""Split the original CA1 notebook into section notebooks.

The generated notebooks are reading-friendly excerpts. They intentionally keep
the original cells unchanged so the full submitted notebook can be reconstructed
by concatenating the section notebook cells in manifest order.
"""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SOURCE_NOTEBOOK = PROJECT_ROOT / "notebooks" / "original" / "CA1 (1).ipynb"
OUTPUT_DIR = PROJECT_ROOT / "notebooks" / "sections"
MANIFEST_PATH = OUTPUT_DIR / "notebook_manifest.json"


@dataclass(frozen=True)
class NotebookSection:
    filename: str
    title: str
    first_cell: int
    last_cell: int


SECTIONS = [
    NotebookSection(
        filename="00_cover_and_table_of_contents.ipynb",
        title="Cover and Table of Contents",
        first_cell=1,
        last_cell=2,
    ),
    NotebookSection(
        filename="01_introduction_and_research_context.ipynb",
        title="1. Introduction and Research Context",
        first_cell=3,
        last_cell=10,
    ),
    NotebookSection(
        filename="02_data_preparation_and_cleaning.ipynb",
        title="2. Data Preparation and Cleaning",
        first_cell=11,
        last_cell=192,
    ),
    NotebookSection(
        filename="03_data_analysis_and_visualisation.ipynb",
        title="3. Data Analysis and Visualisation",
        first_cell=193,
        last_cell=230,
    ),
    NotebookSection(
        filename="04_answering_research_question.ipynb",
        title="4. Answering of Research Question",
        first_cell=231,
        last_cell=232,
    ),
    NotebookSection(
        filename="05_references.ipynb",
        title="5. References",
        first_cell=233,
        last_cell=234,
    ),
]


def main() -> int:
    source = read_notebook(SOURCE_NOTEBOOK)
    cells = source["cells"]
    validate_sections(SECTIONS, len(cells))

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    manifest_sections = []

    for section in SECTIONS:
        section_cells = cells[section.first_cell - 1 : section.last_cell]
        section_notebook = {
            "cells": section_cells,
            "metadata": source.get("metadata", {}),
            "nbformat": source.get("nbformat", 4),
            "nbformat_minor": source.get("nbformat_minor", 5),
        }
        output_path = OUTPUT_DIR / section.filename
        write_notebook(output_path, section_notebook)

        manifest_sections.append(
            {
                "file": section.filename,
                "title": section.title,
                "first_cell": section.first_cell,
                "last_cell": section.last_cell,
                "cell_count": len(section_cells),
                "cells_sha256": checksum_json(section_cells),
            }
        )

    manifest = {
        "source_notebook": str(SOURCE_NOTEBOOK.relative_to(PROJECT_ROOT)).replace("\\", "/"),
        "generated_by": "scripts/split_notebook.py",
        "original_cell_count": len(cells),
        "original_cells_sha256": checksum_json(cells),
        "sections": manifest_sections,
    }
    MANIFEST_PATH.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {len(SECTIONS)} section notebooks to {OUTPUT_DIR.relative_to(PROJECT_ROOT)}")
    return 0


def read_notebook(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_notebook(path: Path, notebook: dict[str, Any]) -> None:
    path.write_text(json.dumps(notebook, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def validate_sections(sections: list[NotebookSection], cell_count: int) -> None:
    expected_first_cell = 1

    for section in sections:
        if section.first_cell != expected_first_cell:
            raise ValueError(
                f"{section.filename} starts at cell {section.first_cell}; "
                f"expected {expected_first_cell}."
            )
        if section.last_cell < section.first_cell:
            raise ValueError(f"{section.filename} has an invalid cell range.")
        expected_first_cell = section.last_cell + 1

    if expected_first_cell - 1 != cell_count:
        raise ValueError(
            f"Section ranges cover {expected_first_cell - 1} cells; source has {cell_count}."
        )


def checksum_json(value: Any) -> str:
    encoded = json.dumps(value, ensure_ascii=False, sort_keys=True).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


if __name__ == "__main__":
    raise SystemExit(main())
