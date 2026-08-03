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
"""

import ast
import re
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
TB_EXAMPLES = REPO_ROOT / "common" / "docs" / "tb-examples.md"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _extract_python_blocks(text: str) -> list:
    """Return list of Python code block contents from a markdown string.

    Finds all fenced code blocks marked with ```python ... ``` and returns
    the text between the fences (excluding the fence lines themselves).
    """
    return re.findall(r"```python\n(.*?)```", text, re.DOTALL)


def _validate_python_syntax(blocks: list) -> list:
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
# DOC-01: README.md tests
# ---------------------------------------------------------------------------


def test_readme_exists():
    """README.md exists at the repository root."""
    readme = REPO_ROOT / "README.md"
    assert readme.is_file(), f"README.md does not exist at {readme}"


def test_readme_has_quickstart():
    """README.md contains quickstart section with install, client, and error handling."""
    readme = REPO_ROOT / "README.md"
    assert readme.is_file(), "README.md does not exist"
    content = readme.read_text(encoding="utf-8")

    assert "## Quickstart" in content, "README.md missing '## Quickstart' section heading"
    assert "pip install" in content, "README.md missing 'pip install' instruction"
    assert "ThingsboardClient" in content, "README.md missing 'ThingsboardClient' class name"
    assert "ApiException" in content, "README.md missing 'ApiException' error handling"


def test_readme_code_blocks_valid_python():
    """All Python code blocks in README.md are syntactically valid."""
    readme = REPO_ROOT / "README.md"
    assert readme.is_file(), "README.md does not exist"
    content = readme.read_text(encoding="utf-8")

    blocks = _extract_python_blocks(content)
    assert blocks, "README.md has no Python code blocks"

    errors = _validate_python_syntax(blocks)
    assert not errors, "README.md has Python code blocks with syntax errors:\n" + "\n".join(
        f"  Block {i}: {msg}" for i, msg in errors
    )


def test_readme_uses_keyword_constructor():
    """README.md Python code blocks use keyword argument form (username=...)."""
    readme = REPO_ROOT / "README.md"
    assert readme.is_file(), "README.md does not exist"
    content = readme.read_text(encoding="utf-8")

    blocks = _extract_python_blocks(content)
    assert blocks, "README.md has no Python code blocks"

    has_keyword_form = any("username=" in block for block in blocks)
    assert has_keyword_form, (
        "README.md has no Python code block containing 'username=' "
        "(must use keyword argument form, not positional)"
    )


# ---------------------------------------------------------------------------
# DOC-04: common/docs/tb-examples.md tests
# ---------------------------------------------------------------------------


def test_tb_examples_exists():
    """common/docs/tb-examples.md exists."""
    examples = TB_EXAMPLES
    assert examples.is_file(), f"common/docs/tb-examples.md does not exist at {examples}"


def test_tb_examples_required_sections():
    """common/docs/tb-examples.md contains all required operation sections."""
    examples = TB_EXAMPLES
    assert examples.is_file(), "common/docs/tb-examples.md does not exist"
    content = examples.read_text(encoding="utf-8")
    lower = content.lower()

    # The JWT section is the one that needs both terms, so it stays its own assertion.
    assert "jwt" in lower and "login" in lower, (
        "tb-examples.md missing JWT login section (must contain 'jwt' and 'login')"
    )

    # Each row is one required section and the alternatives that satisfy it — any one
    # is enough. Add a required section by adding a row. The two auth-mode sections are
    # matched on their headings, since prose mentioning them in passing is not the point.
    required_sections = (
        ("api key login", ("api key", "api_key")),
        ("pre-existing token", ("## pre-existing token",)),
        ("no authentication", ("## no authentication",)),
        ("device", ("device",)),
        ("telemetry", ("telemetry",)),
        ("alarm", ("alarm",)),
        ("with-statement", ("with ", "context manager")),
    )
    for name, alternatives in required_sections:
        assert any(alt in lower for alt in alternatives), (
            f"tb-examples.md missing {name} section "
            f"(must contain one of {', '.join(repr(a) for a in alternatives)})"
        )


def test_tb_examples_code_blocks_valid_python():
    """All Python code blocks in common/docs/tb-examples.md are syntactically valid."""
    examples = TB_EXAMPLES
    assert examples.is_file(), "common/docs/tb-examples.md does not exist"
    content = examples.read_text(encoding="utf-8")

    blocks = _extract_python_blocks(content)
    assert blocks, "common/docs/tb-examples.md has no Python code blocks"

    errors = _validate_python_syntax(blocks)
    assert not errors, (
        "common/docs/tb-examples.md has Python code blocks with syntax errors:\n"
        + "\n".join(f"  Block {i}: {msg}" for i, msg in errors)
    )


def test_tb_examples_uses_keyword_constructor():
    """common/docs/tb-examples.md Python code blocks use keyword argument form (username=...)."""
    examples = TB_EXAMPLES
    assert examples.is_file(), "common/docs/tb-examples.md does not exist"
    content = examples.read_text(encoding="utf-8")

    blocks = _extract_python_blocks(content)
    assert blocks, "common/docs/tb-examples.md has no Python code blocks"

    has_keyword_form = any("username=" in block for block in blocks)
    assert has_keyword_form, (
        "common/docs/tb-examples.md has no Python code block containing 'username=' "
        "(must use keyword argument form, not positional)"
    )
