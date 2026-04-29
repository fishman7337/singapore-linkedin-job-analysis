import json
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
ORIGINAL_NOTEBOOK = PROJECT_ROOT / "notebooks" / "original" / "CA1 (1).ipynb"
SECTIONS_DIR = PROJECT_ROOT / "notebooks" / "sections"
MANIFEST_PATH = SECTIONS_DIR / "notebook_manifest.json"


def test_section_notebooks_reconstruct_original_cells():
    original = json.loads(ORIGINAL_NOTEBOOK.read_text(encoding="utf-8"))
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))

    reconstructed_cells = []
    for section in manifest["sections"]:
        notebook = json.loads((SECTIONS_DIR / section["file"]).read_text(encoding="utf-8"))
        reconstructed_cells.extend(notebook["cells"])

    assert manifest["original_cell_count"] == len(original["cells"])
    assert reconstructed_cells == original["cells"]
