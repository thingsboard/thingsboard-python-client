"""
Tests validating README.md and common/docs/tb-examples.md content.

Validates:
- README.md existence, quickstart section, code block syntax (DOC-01)
- README.md uses keyword constructor form: username=... (DOC-01)
- common/docs/tb-examples.md existence, required sections, code block syntax (DOC-04)
- common/docs/tb-examples.md uses keyword constructor form: username=... (DOC-04)

The examples are checked at their source in common/docs/ rather than in one edition's
copy: that is the file people edit, and test_common_overlay.py already proves every
<edition>/docs/ copy is byte-identical to it, so all three editions are covered here.

Checks that apply to both documents are parametrized over DOCUMENTS rather than written
twice, so a rule added for one cannot silently miss the other.
"""

import ast
import re
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).parent.parent
README = REPO_ROOT / "README.md"
TB_EXAMPLES = REPO_ROOT / "common" / "docs" / "tb-examples.md"

DOCUMENTS = (README, TB_EXAMPLES)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _label(path: Path) -> str:
    """Repo-relative name for a document, used for both test ids and messages.

    Falls back to the full path for the tmp_path fixtures the helper tests use.
    """
    if path.is_relative_to(REPO_ROOT):
        return path.relative_to(REPO_ROOT).as_posix()
    return str(path)


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _has_heading(content: str, heading: str) -> bool:
    """Whether content contains heading as a whole line of its own.

    Anchored and case-sensitive, so the match means what the caller spells: a
    demotion to '### ...', a change of capitalization, or the heading appearing
    mid-line all count as absent. A bare substring would survive deleting the very
    section it is meant to guard, since these terms recur in prose and code samples.
    """
    return re.search(rf"^{re.escape(heading)}[ \t]*$", content, re.MULTILINE) is not None


def _assert_heading(path: Path, heading: str) -> None:
    """Assert the document contains heading as a whole line."""
    assert _has_heading(_read(path), heading), f"{_label(path)} missing '{heading}' section"


def _require_python_blocks(path: Path) -> list[str]:
    """Return the document's ```python blocks, failing if it has none.

    The non-empty guard keeps a document that lost all its code samples from
    vacuously satisfying the rules applied to those samples.
    """
    blocks = re.findall(r"```python\n(.*?)```", _read(path), re.DOTALL)
    assert blocks, f"{_label(path)} has no Python code blocks"
    return blocks


def _validate_python_syntax(blocks: list[str]) -> list:
    """Validate Python syntax for each block using ast.parse.

    Returns a list of (block_index, error_message) tuples for any blocks
    that fail to parse. Returns an empty list if all blocks are valid.
    """
    errors = []
    for i, block in enumerate(blocks):
        try:
            ast.parse(block)
        except SyntaxError as e:
            errors.append((i, str(e)))
    return errors


# ---------------------------------------------------------------------------
# The heading matcher both documents' section checks rely on
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "line, expected",
    (
        ("## JWT Login", True),
        ("### JWT Login", False),  # demoted
        ("## jwt login", False),  # recased
        ("x ## JWT Login", False),  # not at the start of a line
        ("## JWT Login extra", False),  # not the whole line
    ),
)
def test_has_heading_is_anchored_and_case_sensitive(line, expected):
    """Pin the matcher's strictness, which the section checks assert nothing about."""
    assert _has_heading(f"intro\n{line}\nbody\n", "## JWT Login") is expected


def test_require_python_blocks_fails_without_any(tmp_path):
    """A document that lost all its ```python fences fails instead of passing vacuously."""
    doc = tmp_path / "no-blocks.md"
    doc.write_text("# Title\n\nProse only.\n", encoding="utf-8")
    with pytest.raises(AssertionError, match="no Python code blocks"):
        _require_python_blocks(doc)


# ---------------------------------------------------------------------------
# DOC-01 / DOC-04: checks that apply to both documents
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("path", DOCUMENTS, ids=_label)
def test_document_exists(path):
    """The document exists where the other tests expect to find it."""
    assert path.is_file(), f"{_label(path)} does not exist at {path}"


@pytest.mark.parametrize("path", DOCUMENTS, ids=_label)
def test_document_code_blocks_valid_python(path):
    """All Python code blocks in the document are syntactically valid."""
    errors = _validate_python_syntax(_require_python_blocks(path))
    assert not errors, f"{_label(path)} has Python code blocks with syntax errors:\n" + "\n".join(
        f"  Block {i}: {msg}" for i, msg in errors
    )


@pytest.mark.parametrize("path", DOCUMENTS, ids=_label)
def test_document_uses_keyword_constructor(path):
    """The document's Python code blocks use keyword argument form (username=...)."""
    has_keyword_form = any("username=" in block for block in _require_python_blocks(path))
    assert has_keyword_form, (
        f"{_label(path)} has no Python code block containing 'username=' "
        "(must use keyword argument form, not positional)"
    )


# ---------------------------------------------------------------------------
# DOC-01: README.md only
# ---------------------------------------------------------------------------


def test_readme_has_quickstart():
    """README.md contains quickstart section with install, client, and error handling."""
    _assert_heading(README, "## Quickstart")

    content = _read(README)
    assert "pip install" in content, "README.md missing 'pip install' instruction"
    assert "ThingsboardClient" in content, "README.md missing 'ThingsboardClient' class name"
    assert "ApiException" in content, "README.md missing 'ApiException' error handling"


# ---------------------------------------------------------------------------
# DOC-04: common/docs/tb-examples.md only
# ---------------------------------------------------------------------------

_REQUIRED_HEADINGS = (
    "## JWT Login",
    "## API Key Login",
    "## Pre-existing Token",
    "## No Authentication",
    "## Context Manager",
    "## List Devices",
    "## Push Telemetry",
    "## List Alarms",
)


@pytest.mark.parametrize("heading", _REQUIRED_HEADINGS)
def test_tb_examples_required_sections(heading):
    """common/docs/tb-examples.md contains each required section heading."""
    _assert_heading(TB_EXAMPLES, heading)
