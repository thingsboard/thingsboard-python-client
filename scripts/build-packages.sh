#!/bin/bash
#
# Copyright © 2026 ThingsBoard, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

#
# Builds Python wheel and sdist packages for every ThingsBoard client edition listed in
# editions.txt, including version stamping, generation, and smoke testing.
#
# Usage:
#   ./scripts/build-packages.sh
#
# What it does:
#   1. Reads version from root pyproject.toml
#   2. Cleans dist/
#   3. Generates all 3 editions via generate-client.sh all
#   4. For each edition: stamps version, builds wheel + sdist, smoke-tests in clean venv
#   5. Asserts all 3 wheels have the same version in their filenames
#   6. Prints summary of built artifacts
#
# Prerequisites:
#   - poetry installed (pipx install poetry)
#   - python3 available in PATH
#   - generate-client.sh accessible from repo root
#

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$SCRIPT_DIR/.."
DIST_DIR="$ROOT_DIR/dist"
# Editions come from generate-client.sh's own parse of editions.txt, so this script
# never reimplements that format — see the comment on the EDITIONS block there.
# Captured into a variable first: process substitution discards the child's exit status,
# so `set -e` would not see --list-editions fail and we would build nothing, silently.
editions_output="$("$ROOT_DIR/generate-client.sh" --list-editions)"
EDITIONS=()
while read -r line; do
  [ -n "$line" ] && EDITIONS+=("$line")
done <<< "$editions_output"
if [ -z "${EDITIONS[*]:-}" ]; then
  echo "Error: generate-client.sh --list-editions returned no editions" >&2
  exit 1
fi
EDITION_COUNT=${#EDITIONS[@]}

# Add project venv to PATH so that tools installed via pip install (e.g. poetry)
# are accessible without requiring a manual `source .venv/bin/activate`.
if [ -d "$ROOT_DIR/.venv/bin" ]; then
    export PATH="$ROOT_DIR/.venv/bin:$PATH"
fi

# ANSI color codes (disabled when not a terminal)
if [ -t 1 ]; then
    GREEN='\033[0;32m'
    RED='\033[0;31m'
    YELLOW='\033[1;33m'
    BOLD='\033[1m'
    RESET='\033[0m'
else
    GREEN=''
    RED=''
    YELLOW=''
    BOLD=''
    RESET=''
fi

ok()   { echo -e "${GREEN}[OK]${RESET} $*"; }
fail() { echo -e "${RED}[FAIL]${RESET} $*" >&2; exit 1; }
info() { echo -e "${BOLD}=== $* ===${RESET}"; }

# ---------------------------------------------------------------------------
# 1. Read version from root pyproject.toml
# ---------------------------------------------------------------------------
info "Reading version"

VERSION=$(python3 -c "
import re, pathlib, sys
content = pathlib.Path('${ROOT_DIR}/pyproject.toml').read_text()
m = re.search(r'^version\s*=\s*[\"\'](.*?)[\"\']\s*$', content, re.MULTILINE)
if not m:
    sys.exit('ERROR: version not found in root pyproject.toml')
print(m.group(1))
")

if [ -z "$VERSION" ]; then
    fail "Could not read version from root pyproject.toml"
fi

ok "Version: ${VERSION}"

# ---------------------------------------------------------------------------
# 2. Clean dist/
# ---------------------------------------------------------------------------
info "Cleaning dist/"
rm -rf "$DIST_DIR"
mkdir -p "$DIST_DIR"
ok "dist/ cleaned"

# ---------------------------------------------------------------------------
# 3. Generate all editions
# ---------------------------------------------------------------------------
info "Generating all editions"
# generate-client.sh uses `exec > >(tee logfile)` which can trigger SIGPIPE (exit 141)
# when used with 'all'. Run each edition separately to avoid this issue.
for edition in "${EDITIONS[@]}"; do
    gen_exit=0
    (cd "$ROOT_DIR" && ./generate-client.sh "$edition") || gen_exit=$?
    # Exit 141 = 128+SIGPIPE: tee process substitution teardown — generation completed.
    if [ "$gen_exit" -ne 0 ] && [ "$gen_exit" -ne 141 ]; then
        fail "generate-client.sh $edition failed with exit code $gen_exit"
    fi
    ok "Generated $edition"
done
ok "All editions generated"

# ---------------------------------------------------------------------------
# 4. Smoke test function
# ---------------------------------------------------------------------------
smoke_test() {
    local edition="$1"
    local pkg_name="tb_${edition}_client"
    local pypi_name="tb-${edition}-client"

    echo ""
    echo -e "${YELLOW}--- Smoke test: ${edition} ---${RESET}"

    # Find the wheel — wheel filename uses underscores
    local wheel
    wheel=$(ls "${DIST_DIR}/${pkg_name}-"*.whl 2>/dev/null | head -1 || true)
    if [ -z "$wheel" ]; then
        fail "No wheel found for $edition in $DIST_DIR"
    fi
    echo "  Wheel: $(basename "$wheel")"

    # Create temp venv
    local tmpdir
    tmpdir=$(mktemp -d)
    trap "rm -rf '$tmpdir'" EXIT

    python3 -m venv "$tmpdir/venv"
    "$tmpdir/venv/bin/pip" install --quiet "$wheel"

    # Verify import and metadata
    "$tmpdir/venv/bin/python" -c "
import importlib.metadata, sys

meta = importlib.metadata.metadata('${pypi_name}')
pkg_name = meta['Name']
pkg_ver  = meta['Version']
print(f'  Installed: {pkg_name} {pkg_ver}')

if pkg_ver != '${VERSION}':
    sys.exit(f'  ERROR: version mismatch — expected ${VERSION}, got {pkg_ver}')

from ${pkg_name} import ThingsboardClient
if ThingsboardClient is None:
    sys.exit('  ERROR: ThingsboardClient is None')
print(f'  Import OK: ThingsboardClient importable')
"

    # Clean up
    rm -rf "$tmpdir"
    trap - EXIT

    ok "Smoke test PASSED for ${edition}"
}

# ---------------------------------------------------------------------------
# 5. Per-edition: stamp version, build, smoke test
# ---------------------------------------------------------------------------
for edition in "${EDITIONS[@]}"; do
    info "Building ${edition}"

    # 5a. Stamp version into edition's pyproject.toml
    echo "  Stamping version ${VERSION} into ${edition}/pyproject.toml"
    sed -i.bak "s/^version = .*/version = \"${VERSION}\"/" "${ROOT_DIR}/${edition}/pyproject.toml"
    rm -f "${ROOT_DIR}/${edition}/pyproject.toml.bak"
    ok "Version stamped"

    # 5b. Build wheel + sdist
    echo "  Running poetry build ..."
    (cd "${ROOT_DIR}/${edition}" && poetry build --output "${DIST_DIR}" --quiet)
    ok "Build complete"

    # 5c. Smoke test
    smoke_test "$edition"
done

# ---------------------------------------------------------------------------
# 6. Final verification: assert all 3 wheels have the same version
# ---------------------------------------------------------------------------
info "Final verification"

WHEEL_COUNT=0
for edition in "${EDITIONS[@]}"; do
    pkg_name="tb_${edition}_client"
    wheel=$(ls "${DIST_DIR}/${pkg_name}-${VERSION}-"*.whl 2>/dev/null | head -1 || true)
    if [ -z "$wheel" ]; then
        fail "Expected wheel tb_${edition}_client-${VERSION}-*.whl not found in dist/"
    fi
    WHEEL_COUNT=$((WHEEL_COUNT + 1))
    ok "  ${edition}: $(basename "$wheel")"
done

if [ "$WHEEL_COUNT" -ne "$EDITION_COUNT" ]; then
    fail "Expected $EDITION_COUNT wheels, found $WHEEL_COUNT"
fi

ok "All $EDITION_COUNT editions built with version ${VERSION}"

# ---------------------------------------------------------------------------
# 7. Print summary
# ---------------------------------------------------------------------------
info "Build artifacts"
ls -lh "${DIST_DIR}"/*.whl "${DIST_DIR}"/*.tar.gz 2>/dev/null

echo ""
echo -e "${GREEN}${BOLD}All packages built and smoke-tested successfully.${RESET}"
echo "Version: ${VERSION}"
echo "Output:  ${DIST_DIR}/"
