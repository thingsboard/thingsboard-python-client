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
# Generates Python REST clients from OpenAPI specs using openapi-generator-cli.
#
# Usage:
#   ./generate-client.sh [options] <edition> [base-url]
#
# Arguments:
#   edition    one of the names in editions.txt, or "all"
#   base-url   Optional. Fetches spec from <base-url>/v3/api-docs/thingsboard
#              and updates the local spec file before generation.
#              Not supported with "all".
#
# Options:
#   --verbose  Show full generator output (per-file writes, operations, etc.)
#   --dry-run  Generate into target/generated/ only. Skip copying to package dir,
#              common module overlay, and post-processing.
#
# Examples:
#   ./generate-client.sh ce                           # Generate CE from local spec
#   ./generate-client.sh all                          # Generate all editions from local specs
#   ./generate-client.sh ce http://localhost:8080      # Fetch spec from local TB, then generate
#   ./generate-client.sh --dry-run ce                  # Generate to target/ only, don't touch package dir
#   ./generate-client.sh --verbose ce                  # Full output, no log filtering
#
# What it does:
#   1. Optionally fetches OpenAPI spec from a running ThingsBoard instance
#   2. Validates the spec (warns on duplicate operationIds)
#   3. Runs openapi-generator-cli with Python target (per-tag output, one class per controller)
#   4. Copies generated tb_{edition}_client/ into the edition's package directory
#   5. Overlays common/ contents into the package directory
#   6. Runs scripts/post_process.py (license headers, lazy imports, JsonNode fixes, cleanup)
#   7. Runs openapi-generator docs pass with custom templates to produce {edition}/docs/
#
# Preserved on regeneration:
#   - <edition>/spec/openapi.json  (only updated when base-url is provided)
#
# Replaced on regeneration:
#   - <edition>/tb_{edition}_client/  (fully replaced from generated output)
#
#
# Prerequisites: Java (for openapi-generator-cli JAR), Python 3
#

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
# Which editions exist. editions.txt is the shared source for this script,
# scripts/build-packages.sh and tests/test_common_overlay.py, so none of them has to
# parse another's formatting. It governs that list only — the per-edition controller
# thresholds below, and the spec/ directories, still need their own edits.
#
# Format: one name per line; blank lines and # comments ignored, surrounding whitespace
# trimmed. `read -r line` with the default IFS does that trimming, which is exactly
# str.strip() in the Python mirror — do not add `tr -d [:space:]`, which would also
# delete whitespace *inside* a line and silently disagree with it.
EDITIONS=()
# `|| [ -n "$line" ]` so a final line with no trailing newline is not dropped.
while read -r line || [ -n "$line" ]; do
  case "$line" in ''|'#'*) continue ;; esac
  EDITIONS+=("$line")
done < "$SCRIPT_DIR/editions.txt"
# `${EDITIONS[*]:-}` rather than ${#EDITIONS[@]}: the latter is unbound under set -u on
# bash < 4.4 when the array is empty, which is exactly the case being tested for.
if [ -z "${EDITIONS[*]:-}" ]; then
  echo "Error: no editions listed in $SCRIPT_DIR/editions.txt"; exit 1
fi

VERBOSE=false
DRY_RUN=false
while [ $# -gt 0 ]; do
  case "$1" in
    --verbose) VERBOSE=true; shift ;;
    --dry-run) DRY_RUN=true; shift ;;
    # Lets tests assert against this script's own parse of editions.txt rather than a
    # reimplementation of it. Must stay ahead of the JAR download below.
    --list-editions) printf '%s\n' "${EDITIONS[@]}"; exit 0 ;;
    -*) echo "Unknown option: $1"; exit 1 ;;
    *) break ;;
  esac
done

if [ $# -eq 0 ]; then
  echo "Usage: $0 [--verbose] [--dry-run] [--list-editions] <edition> [base-url]"
  echo "  edition: ${EDITIONS[*]} | all"
  echo "  base-url: optional, fetches spec from <base-url>/v3/api-docs/thingsboard"
  exit 1
fi

EDITION="$1"
BASE_URL="${2:-}"

# -------------------------------------------------------------------
# JAR management (version-locked to match Java client)
# -------------------------------------------------------------------
OPENAPI_GENERATOR_VERSION="7.20.0"
GENERATOR_CACHE_DIR="${OPENAPI_GENERATOR_CACHE_DIR:-${HOME}/.cache/openapi-generator}"
GENERATOR_JAR="$GENERATOR_CACHE_DIR/openapi-generator-cli-${OPENAPI_GENERATOR_VERSION}.jar"

if [ ! -f "$GENERATOR_JAR" ]; then
  echo "Downloading openapi-generator-cli ${OPENAPI_GENERATOR_VERSION}..."
  mkdir -p "$GENERATOR_CACHE_DIR"
  curl -fSL -o "$GENERATOR_JAR" \
    "https://repo1.maven.org/maven2/org/openapitools/openapi-generator-cli/${OPENAPI_GENERATOR_VERSION}/openapi-generator-cli-${OPENAPI_GENERATOR_VERSION}.jar"
fi

# Wrapper function so call sites look identical to the npx-based CLI
openapi-generator-cli() { java -jar "$GENERATOR_JAR" "$@"; }

# -------------------------------------------------------------------
# generate() — process a single edition
# -------------------------------------------------------------------
generate() {
  local edition="$1"
  local spec_file="$SCRIPT_DIR/$edition/spec/openapi.json"
  local output_dir="$SCRIPT_DIR/$edition/target/generated"
  local module_dir="$SCRIPT_DIR/$edition"

  # --- Optional spec fetch ---
  if [ -n "$BASE_URL" ]; then
    local api_url="$BASE_URL/v3/api-docs/thingsboard"
    echo "Fetching spec for $edition from $api_url"
    mkdir -p "$(dirname "$spec_file")"
    curl -sf "$api_url" -o "$spec_file" || { echo "Error: failed to fetch spec from $api_url"; exit 1; }
  fi

  if [ ! -f "$spec_file" ]; then
    echo "Error: spec file not found: $spec_file"
    exit 1
  fi

  rm -rf "$output_dir"

  # --- Spec validation ---
  echo "Validating spec: $spec_file"
  local validate_output
  validate_output=$(openapi-generator-cli validate -i "$spec_file" 2>&1) || {
    echo "$validate_output" | grep -v "Unused model:"
    exit 1
  }

  # --- Duplicate operationId detection (GEN-09) ---
  # ThingsBoard's spec generator appends _1, _2, etc. for duplicates; warn (not fail).
  local duplicates
  duplicates=$(grep -o '"operationId" *: *"[^"]*"' "$spec_file" | sed 's/.*: *"//;s/"//' | grep -E '_[0-9]+$' || true)
  if [ -n "$duplicates" ]; then
    echo "Warning: spec contains duplicate operationIds (suffixed by ThingsBoard):"
    echo "$duplicates" | sed 's/^/  /'
    echo "These will generate methods with numeric suffixes. Consider fixing @ApiOperation annotations."
  fi

  # --- Python client generation (per-controller output (one file per OpenAPI tag)) ---
  echo "Generating Python client for edition: $edition from $spec_file"
  if [ "$VERBOSE" = true ]; then
    java -jar "$GENERATOR_JAR" generate \
      -i "$spec_file" \
      -g python \
      -o "$output_dir" \
      --package-name "tb_${edition}_client" \
      --additional-properties hideGenerationTimestamp=true,generateSourceCodeOnly=true \
      --global-property apiTests=false,modelTests=false,modelDocs=false,apiDocs=false
  else
    java -jar "$GENERATOR_JAR" generate \
      -i "$spec_file" \
      -g python \
      -o "$output_dir" \
      --package-name "tb_${edition}_client" \
      --additional-properties hideGenerationTimestamp=true,generateSourceCodeOnly=true \
      --global-property apiTests=false,modelTests=false,modelDocs=false,apiDocs=false \
      > /dev/null 2>&1
  fi

  if [ "$DRY_RUN" = true ]; then
    echo "Dry run: generated client is in $output_dir"
    echo "Skipping copy to package directory, common overlay, and post-processing."
  else
    # --- Copy generated package to edition directory (GEN-01/02/03/04) ---
    # With generateSourceCodeOnly=true, the package is directly in output_dir/tb_${edition}_client
    rm -rf "$module_dir/tb_${edition}_client"
    cp -r "$output_dir/tb_${edition}_client" "$module_dir/tb_${edition}_client"
    rm -rf "$module_dir/tb_${edition}_client/docs"
    echo "Copied generated package to $module_dir/tb_${edition}_client"

    # --- Common module overlay (GEN-10), excluding docs/ (handled separately) ---
    local common_dir="$SCRIPT_DIR/common"
    if [ -d "$common_dir" ] && [ -n "$(ls -A "$common_dir" 2>/dev/null)" ]; then
      find "$common_dir" -maxdepth 1 -mindepth 1 -not -name docs | while read -r item; do
        cp -r "$item" "$module_dir/tb_${edition}_client/"
      done
      echo "Copied common module overlay to $module_dir/tb_${edition}_client"
    fi

    # --- Post-processing (GEN-06, GEN-07, GEN-08) ---
    echo "Running post-processor for $edition..."
    python3 "$SCRIPT_DIR/scripts/post_process.py" "$module_dir/tb_${edition}_client" "tb_${edition}_client"
  fi

  # --- Metrics output ---
  local pkg_dir
  if [ "$DRY_RUN" = true ]; then
    pkg_dir="$output_dir/tb_${edition}_client"
  else
    pkg_dir="$module_dir/tb_${edition}_client"
  fi

  if [ -d "$pkg_dir" ]; then
    echo ""
    echo "=== Metrics: $edition ==="
    local total_files
    total_files=$(find "$pkg_dir" -name "*.py" | wc -l | tr -d ' ')
    echo "  Python files: $total_files"

    local total_lines
    total_lines=$(find "$pkg_dir" -name "*.py" -exec wc -l {} + 2>/dev/null | tail -1 | awk '{print $1}')
    echo "  Total lines:  $total_lines"

    # Per-controller metrics (SPLIT-01, SPLIT-03)
    local api_count
    api_count=$(find "$pkg_dir/api" -name "*.py" ! -name "__init__.py" 2>/dev/null | wc -l | tr -d ' ')
    echo "  Controllers:  $api_count files"

    local method_count
    method_count=$(find "$pkg_dir/api" -name "*.py" ! -name "__init__.py" \
      -exec grep -c "^    def [^_]" {} + 2>/dev/null | awk -F: '{s+=$2} END {print s+0}')
    echo "  API methods:  $method_count (public, sync)"

    # Minimum controller threshold assertion (SPLIT-03)
    local min_count
    case "$edition" in
      ce) min_count=55 ;;
      pe) min_count=78 ;;
      paas) min_count=83 ;;
      *) min_count=0 ;;
    esac
    if [ -n "$min_count" ] && [ "$api_count" -lt "$min_count" ]; then
      echo "Error: $edition generated $api_count controller files (minimum: $min_count)"
      exit 1
    fi

    local model_count
    model_count=$(find "$pkg_dir" -path "*/models/*.py" -not -name "__init__.py" 2>/dev/null | wc -l | tr -d ' ')
    echo "  Models:       $model_count"

    # GEN-05: Verify Pydantic v2 patterns
    local sample_model
    sample_model=$(grep -rl -m1 "model_config = ConfigDict" "$pkg_dir/models" 2>/dev/null || true)
    if [ -n "$sample_model" ]; then
      echo "  Pydantic v2:  OK (model_config = ConfigDict confirmed in $(basename "$sample_model"))"
    else
      local pydantic_model
      pydantic_model=$(grep -rl -m1 "from pydantic import" "$pkg_dir/models" 2>/dev/null || true)
      if [ -n "$pydantic_model" ]; then
        echo "  Pydantic v2:  OK (pydantic imports found in $(basename "$pydantic_model"))"
      else
        echo "  Pydantic v2:  WARNING — no Pydantic patterns found in models/"
      fi
    fi

    echo "  Import time:  time python3 -c \"import tb_${edition}_client\""
    echo ""
  fi

  # --- Run 2: Per-controller/model documentation (DGEN-01) ---
  local docs_output_dir="$SCRIPT_DIR/$edition/target/generated-docs"
  rm -rf "$docs_output_dir"

  echo "Generating per-controller and per-model docs for edition: $edition"
  if [ "$VERBOSE" = true ]; then
    java -jar "$GENERATOR_JAR" generate \
      -i "$spec_file" \
      -g python \
      -o "$docs_output_dir" \
      --package-name "tb_${edition}_client" \
      --additional-properties hideGenerationTimestamp=true,generateSourceCodeOnly=true \
      --global-property apis,models,supportingFiles=false,apiTests=false,modelTests=false \
      -t "$SCRIPT_DIR/openapi"
  else
    java -jar "$GENERATOR_JAR" generate \
      -i "$spec_file" \
      -g python \
      -o "$docs_output_dir" \
      --package-name "tb_${edition}_client" \
      --additional-properties hideGenerationTimestamp=true,generateSourceCodeOnly=true \
      --global-property apis,models,supportingFiles=false,apiTests=false,modelTests=false \
      -t "$SCRIPT_DIR/openapi" \
      > /dev/null 2>&1
  fi

  if [ "$DRY_RUN" = false ]; then
    rm -rf "$module_dir/docs"
    cp -r "$docs_output_dir/tb_${edition}_client/docs" "$module_dir/docs"
    echo "Copied docs to $module_dir/docs"
    # --- Common docs overlay ---
    local common_docs_dir="$SCRIPT_DIR/common/docs"
    if [ -d "$common_docs_dir" ] && [ -n "$(ls -A "$common_docs_dir" 2>/dev/null)" ]; then
      cp "$common_docs_dir/"* "$module_dir/docs/"
      echo "Copied common/docs overlay to $module_dir/docs"
    fi

    # --- Flatten model docs: inline referenced types ---
    echo "Flattening model docs for $edition..."
    python3 "$SCRIPT_DIR/scripts/flatten_docs.py" "$module_dir/docs"
  fi

  local docs_dir
  if [ "$DRY_RUN" = true ]; then
    docs_dir="$docs_output_dir/tb_${edition}_client/docs"
  else
    docs_dir="$module_dir/docs"
  fi

  if [ -d "$docs_dir" ]; then
    local doc_count api_doc_count model_doc_count
    doc_count=$(find "$docs_dir" -name "*.md" 2>/dev/null | wc -l | tr -d ' ')
    api_doc_count=$(find "$docs_dir" -name "*Api.md" 2>/dev/null | wc -l | tr -d ' ')
    model_doc_count=$((doc_count - api_doc_count))
    echo ""
    echo "=== Doc Metrics: $edition ==="
    echo "  Total docs:       $doc_count markdown files"
    echo "  Controller docs:  $api_doc_count"
    echo "  Model docs:       $model_doc_count"

    # Minimum doc count assertion (analogous to controller threshold)
    local min_doc_count
    case "$edition" in
      ce) min_doc_count=700 ;;
      pe) min_doc_count=900 ;;
      paas) min_doc_count=900 ;;
      *) min_doc_count=0 ;;
    esac
    if [ "$min_doc_count" -gt 0 ] && [ "$doc_count" -lt "$min_doc_count" ]; then
      echo "Error: $edition generated $doc_count doc files (minimum: $min_doc_count)"
      exit 1
    fi
    echo ""
  fi
}

# -------------------------------------------------------------------
# Entry point
# -------------------------------------------------------------------
if [ "$EDITION" = "all" ]; then
  if [ -n "$BASE_URL" ]; then
    echo "Error: base-url is not supported with 'all'. Run per edition instead."
    exit 1
  fi
  OPTS=""
  [ "$VERBOSE" = true ] && OPTS="$OPTS --verbose"
  [ "$DRY_RUN" = true ] && OPTS="$OPTS --dry-run"
  for e in "${EDITIONS[@]}"; do
    "$0" $OPTS "$e"
  done
else
  if [[ ! " ${EDITIONS[*]} " =~ " ${EDITION} " ]]; then
    echo "Error: unknown edition '$EDITION'. Must be one of: ${EDITIONS[*]} all"
    exit 1
  fi
  generate "$EDITION"
fi
