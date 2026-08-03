"""
Guards the common/ -> edition overlay performed by generate-client.sh.

generate-client.sh copies common/ verbatim into every tb_<edition>_client/ package,
and those copies are committed. Nothing else in CI compares them, so a fix landed in
common/ but overlaid into only some editions would ship stale code to the rest.

Both lists are taken from the things that define them rather than hardcoded here:
filenames from common/ itself, editions from generate-client.sh. Adding either a file
or an edition extends the check with no test edit — and, because the editions come
from the script rather than from whichever directories happen to exist, an edition
whose package directory is missing fails instead of quietly dropping out.
"""

import re
from pathlib import Path

import pytest

_REPO_ROOT = Path(__file__).parent.parent
_COMMON_DIR = _REPO_ROOT / "common"

# Entries in common/ that are deliberately NOT byte-identical in the editions:
#   docs        — generate-client.sh overlays it into <edition>/docs, not the package
#   __init__.py — post_process.py merges it with the generated package __init__
#   __pycache__ — build output, never committed
_EXCLUDED_TOP_LEVEL = {"docs", "__init__.py"}
_EXCLUDED_DIRS = {"__pycache__"}


def _overlaid_filenames() -> list[str]:
    """Paths under common/ that must appear verbatim in every edition package.

    Walks recursively and returns paths relative to common/, because
    generate-client.sh `cp -r`s every entry — subdirectories included.
    """
    names = []
    for path in _COMMON_DIR.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(_COMMON_DIR)
        if rel.parts[0] in _EXCLUDED_TOP_LEVEL or _EXCLUDED_DIRS.intersection(rel.parts):
            continue
        names.append(str(rel))
    return sorted(names)


def _editions() -> list[str]:
    """Edition names parsed from the EDITIONS array in generate-client.sh."""
    script = (_REPO_ROOT / "generate-client.sh").read_text(encoding="utf-8")
    match = re.search(r"^EDITIONS=\(([^)]*)\)", script, re.MULTILINE)
    assert match, "could not find the EDITIONS=(...) array in generate-client.sh"
    return sorted(re.findall(r'"([^"]+)"', match.group(1)))


def test_discovery_finds_filenames_and_editions():
    """Both derived lists are non-empty.

    Without this, a glob or regex that silently matched nothing would collect zero
    parametrized cases and the sync check would vacuously pass.
    """
    assert _overlaid_filenames(), "no overlaid files discovered in common/"
    assert _editions(), "no editions parsed from generate-client.sh"


@pytest.mark.parametrize("edition", _editions())
@pytest.mark.parametrize("filename", _overlaid_filenames())
def test_edition_copy_matches_common(edition, filename):
    """Each committed edition copy is byte-identical to its common/ source."""
    source = _COMMON_DIR / filename
    copy = _REPO_ROOT / edition / f"tb_{edition}_client" / filename

    assert copy.is_file(), f"{copy} is missing — run generate-client.sh"
    assert copy.read_bytes() == source.read_bytes(), (
        f"{copy.relative_to(_REPO_ROOT)} is out of sync with common/{filename}. "
        f"Edit common/{filename} and re-run generate-client.sh (or copy it into "
        f"every tb_*_client/ package)."
    )
