"""
Guards the common/ -> edition overlay performed by generate-client.sh.

generate-client.sh copies common/*.py verbatim into every tb_<edition>_client/
package, and those copies are committed. Nothing else in CI compares them, so a
fix landed in common/ but overlaid into only some editions would ship stale code
to the rest. These tests fail on exactly that.
"""

from pathlib import Path

import pytest

_REPO_ROOT = Path(__file__).parent.parent

# Hand-written modules overlaid verbatim. __init__.py is excluded: post_process.py
# merges it with the generated package __init__, so the copies legitimately differ.
_OVERLAID_MODULES = ["client.py", "_auth.py", "_retry.py"]

_EDITIONS = ["ce", "pe", "paas"]


@pytest.mark.parametrize("edition", _EDITIONS)
@pytest.mark.parametrize("module", _OVERLAID_MODULES)
def test_edition_copy_matches_common(edition, module):
    """Each committed edition copy is byte-identical to its common/ source."""
    source = _REPO_ROOT / "common" / module
    copy = _REPO_ROOT / edition / f"tb_{edition}_client" / module

    assert copy.exists(), f"{copy} is missing — run generate-client.sh"
    assert copy.read_bytes() == source.read_bytes(), (
        f"{copy.relative_to(_REPO_ROOT)} is out of sync with common/{module}. "
        f"Edit common/{module} and re-run generate-client.sh (or copy it into "
        f"every tb_*_client/ package)."
    )


def test_all_common_modules_are_covered():
    """_OVERLAID_MODULES lists every hand-written module in common/.

    Without this, adding a new file to common/ would silently escape the sync check.
    """
    present = {
        path.name for path in (_REPO_ROOT / "common").glob("*.py") if path.name != "__init__.py"
    }
    assert present == set(_OVERLAID_MODULES)
