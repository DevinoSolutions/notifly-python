#!/usr/bin/env bash
# Regenerate the notifly_py package from openapi.yaml.
# Root files (pyproject.toml, README.md, LICENSE, workflows) are preserved —
# only the generated package directory is replaced. Review the diff and bump
# the version in pyproject.toml before releasing.
set -euo pipefail

GENERATOR_VERSION="0.29.0"
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TMP_OUT="$(mktemp -d)/notifly-py-gen"

uvx "openapi-python-client@${GENERATOR_VERSION}" generate \
  --path "${REPO_ROOT}/openapi.yaml" \
  --config "${REPO_ROOT}/gen-config.yaml" \
  --meta uv \
  --output-path "${TMP_OUT}" \
  --overwrite

rm -rf "${REPO_ROOT}/notifly_py"
cp -r "${TMP_OUT}/notifly_py" "${REPO_ROOT}/notifly_py"

echo "Regenerated notifly_py from openapi.yaml (openapi-python-client ${GENERATOR_VERSION})."
echo "Review the diff, then bump version in pyproject.toml."
