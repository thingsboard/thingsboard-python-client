"""
Guards the common/ -> edition overlay performed by generate-client.sh.

generate-client.sh copies common/ verbatim into every tb_<edition>_client/ package,
and those copies are committed. Nothing else in CI compares them, so a fix landed in
common/ but overlaid into only some editions would ship stale code to the rest.

Both the module list and the edition list are derived from the repo rather than
hardcoded, so adding either a file to common/ or a new edition directory extends the
check automatically.
"""

from pathlib import Path

import pytest

_REPO_ROOT = Path(__file__).parent.parent

# Entries in common/ that are deliberately NOT byte-identical in the editions:
#   docs        — generate-client.sh overlays it into <edition>/docs, not the package
#   __init__.py — post_process.py merges it with the generated package __init__
#   __pycache__ — build output, never committed
_NOT_OVERLAID = {"docs", "__init__.py", "__pycache__"}


def _overlaid_files() -> list[str]:
    """Names in common/ that must appear verbatim in every edition package."""
    return sorted(p.name for p in (_REPO_ROOT / "common").iterdir() if p.name not in _NOT_OVERLAID)


def _editions() -> list[str]:
    """Edition directory names, discovered from the committed <edition>/tb_*_client/ dirs."""
    return sorted(p.parent.name for p in _REPO_ROOT.glob("*/tb_*_client") if p.is_dir())


def test_discovery_finds_files_and_editions():
    """Both derived lists are non-empty.

    Without this, a glob that silently matched nothing would collect zero
    parametrized cases and the sync check would vacuously pass.
    """
    assert _overlaid_files(), "no overlaid modules discovered in common/"
    assert _editions(), "no <edition>/tb_*_client/ directories discovered"


@pytest.mark.parametrize("edition", _editions())
@pytest.mark.parametrize("name", _overlaid_files())
def test_edition_copy_matches_common(edition, name):
    """Each committed edition copy is byte-identical to its common/ source."""
    source = _REPO_ROOT / "common" / name
    copy = _REPO_ROOT / edition / f"tb_{edition}_client" / name

    assert copy.exists(), f"{copy} is missing — run generate-client.sh"
    assert copy.read_bytes() == source.read_bytes(), (
        f"{copy.relative_to(_REPO_ROOT)} is out of sync with common/{name}. "
        f"Edit common/{name} and re-run generate-client.sh (or copy it into "
        f"every tb_*_client/ package)."
    )
