"""
Guards the common/ -> edition overlays performed by generate-client.sh.

generate-client.sh copies common/ verbatim into every tb_<edition>_client/ package and
common/docs/ into every <edition>/docs/, and those copies are committed. Nothing else in
CI compares them, so a fix landed in common/ but overlaid into only some editions would
ship stale code — or stale documentation — to the rest.

Every list is taken from the thing that defines it rather than hardcoded here:
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

# Excluded only where they sit at the top level of common/ — a nested file of the
# same name would still be overlaid verbatim and must stay checked:
#   docs        — generate-client.sh overlays it into <edition>/docs, not the package
#   __init__.py — post_process.py merges it with the generated package __init__
_EXCLUDED_TOP_LEVEL = {"docs", "__init__.py"}

# Excluded at any depth, because they are build output that is never committed:
_EXCLUDED_DIRS_ANY_DEPTH = {"__pycache__"}


def _overlaid_filenames(root: Path = _COMMON_DIR) -> list[str]:
    """Paths under root that must appear verbatim in every edition package.

    Walks recursively and returns forward-slash paths relative to root, because
    generate-client.sh `cp -r`s every entry — subdirectories included.
    """
    names = []
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(root)
        if rel.parts[0] in _EXCLUDED_TOP_LEVEL:
            continue
        if _EXCLUDED_DIRS_ANY_DEPTH.intersection(rel.parts):
            continue
        names.append(rel.as_posix())
    return sorted(names)


def _overlaid_doc_filenames() -> list[str]:
    """Names in common/docs/ that must appear verbatim in every <edition>/docs/.

    Flat rather than recursive: the script overlays these with `cp common/docs/* ...`,
    which copies top-level entries only.
    """
    docs_dir = _COMMON_DIR / "docs"
    if not docs_dir.is_dir():
        return []
    return sorted(p.name for p in docs_dir.iterdir() if p.is_file())


def _editions() -> list[str]:
    """Edition names parsed from the EDITIONS array in generate-client.sh."""
    script = (_REPO_ROOT / "generate-client.sh").read_text(encoding="utf-8")
    match = re.search(r"^EDITIONS=\(([^)]*)\)", script, re.MULTILINE)
    assert match, "could not find the EDITIONS=(...) array in generate-client.sh"
    return sorted(re.findall(r'"([^"]+)"', match.group(1)))


def test_discovery_finds_filenames_and_editions():
    """Every derived list is non-empty.

    Without this, a glob or regex that silently matched nothing would collect zero
    parametrized cases and the sync check would vacuously pass.
    """
    assert _overlaid_filenames(), "no overlaid files discovered in common/"
    assert _overlaid_doc_filenames(), "no overlaid docs discovered in common/docs/"
    assert _editions(), "no editions parsed from generate-client.sh"


def test_walk_exclusion_semantics(tmp_path):
    """The two exclusion sets are anchored differently — pin that against a fixture.

    common/ is flat today apart from docs/, so nothing real exercises the recursion
    or the any-depth filter; this checks them now rather than the first time someone
    adds a subdirectory.
    """
    (tmp_path / "client.py").write_text("x")
    (tmp_path / "__init__.py").write_text("x")  # excluded: top level
    (tmp_path / "docs").mkdir()
    (tmp_path / "docs" / "guide.md").write_text("x")  # excluded: under top-level docs
    (tmp_path / "sub").mkdir()
    (tmp_path / "sub" / "mod.py").write_text("x")  # kept: nested file
    (tmp_path / "sub" / "__init__.py").write_text("x")  # kept: not at the top level
    (tmp_path / "sub" / "docs").mkdir()
    (tmp_path / "sub" / "docs" / "guide.md").write_text("x")  # kept: not at the top level
    (tmp_path / "sub" / "__pycache__").mkdir()
    (tmp_path / "sub" / "__pycache__" / "mod.pyc").write_bytes(b"x")  # excluded: any depth

    assert _overlaid_filenames(tmp_path) == [
        "client.py",
        "sub/__init__.py",
        "sub/docs/guide.md",
        "sub/mod.py",
    ]


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


@pytest.mark.parametrize("edition", _editions())
@pytest.mark.parametrize("filename", _overlaid_doc_filenames())
def test_edition_doc_copy_matches_common(edition, filename):
    """Each committed <edition>/docs/ copy is byte-identical to its common/docs/ source.

    The package overlay above skips common/docs because the script sends it to
    <edition>/docs instead; without this, a hand-edit to one edition's copy of the
    shared documentation would pass CI unnoticed.
    """
    source = _COMMON_DIR / "docs" / filename
    copy = _REPO_ROOT / edition / "docs" / filename

    assert copy.is_file(), f"{copy} is missing — run generate-client.sh"
    assert copy.read_bytes() == source.read_bytes(), (
        f"{copy.relative_to(_REPO_ROOT)} is out of sync with common/docs/{filename}. "
        f"Edit common/docs/{filename} and re-run generate-client.sh (or copy it into "
        f"every <edition>/docs/ directory)."
    )
