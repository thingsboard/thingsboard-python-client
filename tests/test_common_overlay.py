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

# The directory generate-client.sh overlays into <edition>/docs rather than into the
# package. Named once for the two source-side uses — the package check excludes it and
# the docs check reads from it. The destination happens to share the name, but the
# script hardcodes that separately (`cp "$common_docs_dir/"* "$module_dir/docs/"`), so
# renaming this constant would not rename the edition directories.
_DOCS_DIRNAME = "docs"

# Excluded only where they sit at the top level of common/ — a nested file of the
# same name would still be overlaid verbatim and must stay checked:
#   docs        — generate-client.sh overlays it into <edition>/docs, not the package
#   __init__.py — post_process.py merges it with the generated package __init__
_EXCLUDED_TOP_LEVEL = {_DOCS_DIRNAME, "__init__.py"}

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


def _overlaid_doc_filenames(root: Path = _COMMON_DIR / _DOCS_DIRNAME) -> list[str]:
    """Names directly under root that must appear verbatim in every <edition>/docs/.

    Flat rather than recursive: the script overlays these with `cp common/docs/* ...`,
    which copies top-level entries only — and would abort on a subdirectory, since it
    passes no -r.

    A missing directory yields an empty list rather than raising, matching what rglob
    does for _overlaid_filenames. Both then shrink to zero parametrized cases, and
    test_discovery_finds_filenames_and_editions is the single place that reports it —
    as a plain test failure, rather than a collection-time error that would take the
    unrelated package-sync cases down with it.
    """
    if not root.is_dir():
        return []
    return sorted(p.name for p in root.iterdir() if p.is_file())


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


def _assert_identical(source: Path, copy: Path, destinations: str) -> None:
    """Assert copy exists and is byte-identical to source, or explain how to fix it.

    destinations names where the source has to be copied to, e.g. "every tb_*_client/
    package" — the rest of the remediation is the same for both callers.
    """
    source_rel = source.relative_to(_REPO_ROOT).as_posix()
    copy_rel = copy.relative_to(_REPO_ROOT).as_posix()
    # Action-first and with no trailing "after editing it": on the missing-copy branch
    # the source is fine and re-running the script is the only step needed.
    remediation = f"Run generate-client.sh (or copy {source_rel} into {destinations})."

    assert copy.is_file(), f"{copy_rel} is missing. {remediation}"
    assert copy.read_bytes() == source.read_bytes(), (
        f"{copy_rel} is out of sync with {source_rel}. {remediation}"
    )


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


def test_doc_walk_is_flat(tmp_path):
    """The docs helper takes top-level files only, matching `cp common/docs/*`.

    Kept deliberately flat because the script passes no -r; a subdirectory would abort
    it, so silently skipping one here is the right behaviour rather than an oversight.
    """
    (tmp_path / "tb-examples.md").write_text("x")
    (tmp_path / "sub").mkdir()
    (tmp_path / "sub" / "nested.md").write_text("x")  # skipped: not a top-level file

    assert _overlaid_doc_filenames(tmp_path) == ["tb-examples.md"]


@pytest.mark.parametrize("walk", (_overlaid_filenames, _overlaid_doc_filenames))
def test_missing_directory_yields_empty_list(walk, tmp_path):
    """Both helpers degrade to [] rather than raising when their root is absent.

    Parametrized over both so the parity _overlaid_doc_filenames claims in its
    docstring is enforced rather than asserted.
    """
    assert walk(tmp_path / "missing") == []


@pytest.mark.parametrize("edition", _editions())
@pytest.mark.parametrize("filename", _overlaid_filenames())
def test_edition_copy_matches_common(edition, filename):
    """Each committed edition copy is byte-identical to its common/ source."""
    _assert_identical(
        _COMMON_DIR / filename,
        _REPO_ROOT / edition / f"tb_{edition}_client" / filename,
        "every tb_*_client/ package",
    )


@pytest.mark.parametrize("edition", _editions())
@pytest.mark.parametrize("filename", _overlaid_doc_filenames())
def test_edition_doc_copy_matches_common(edition, filename):
    """Each committed <edition>/docs/ copy is byte-identical to its common/docs/ source.

    The package overlay above skips common/docs because the script sends it to
    <edition>/docs instead; without this, a hand-edit to one edition's copy of the
    shared documentation would pass CI unnoticed.
    """
    _assert_identical(
        _COMMON_DIR / _DOCS_DIRNAME / filename,
        _REPO_ROOT / edition / _DOCS_DIRNAME / filename,
        f"every <edition>/{_DOCS_DIRNAME}/ directory",
    )
