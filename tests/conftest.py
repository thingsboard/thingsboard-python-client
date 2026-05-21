"""
Test configuration and fixtures for thingsboard-python-client tests.

Inserts the ce/ and pe/ edition directories into sys.path so that the
generated tb_ce_client and tb_pe_client packages can be imported in tests.
"""

import os
import sys

# Make tb_ce_client / tb_pe_client importable from their edition directories
_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
for _edition in ("ce", "pe"):
    _edition_dir = os.path.join(_ROOT, _edition)
    if _edition_dir not in sys.path:
        sys.path.insert(0, _edition_dir)
