#!/usr/bin/env bash
# Regenerate the notifly_py package from openapi.json.
#
# Root files (pyproject.toml, README.md, LICENSE, workflows) are preserved, and so are the
# HAND-WRITTEN modules listed in HANDWRITTEN below: they are saved before the generated tree
# replaces the package and restored afterwards. Everything under notifly_py/api/ and
# notifly_py/models/ is generated and must never be edited by hand.
#
# The generator reads a patched COPY of openapi.json (scripts/prepare_spec.py applies the named
# spec fixes); the committed openapi.json stays a verbatim export of the API.
#
# After regenerating: run `uv run pytest` (the envelope regression suite is the gate that
# catches a generator change breaking the runtime unwrap), review the diff, and bump the
# version in pyproject.toml before releasing.
set -euo pipefail

GENERATOR_VERSION="0.29.0"
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TMP_DIR="$(mktemp -d)"
TMP_OUT="${TMP_DIR}/notifly-sdk-gen"
PATCHED_SPEC="${TMP_DIR}/openapi.patched.json"
BACKUP="$(mktemp -d)/notifly-sdk-handwritten"

# Hand-written modules layered on top of the generated client. Keep in sync with the
# "HAND-WRITTEN" banner in each file.
HANDWRITTEN=(
  "__init__.py"
  "_envelope.py"
  "_transport.py"
  "_version.py"
  "exceptions.py"
  "facade.py"
  "internal_ops.py"
  "notifly_client.py"
  "pagination.py"
)

mkdir -p "${BACKUP}"
for file in "${HANDWRITTEN[@]}"; do
  if [[ ! -f "${REPO_ROOT}/notifly_py/${file}" ]]; then
    echo "error: hand-written module notifly_py/${file} is missing — refusing to regenerate." >&2
    exit 1
  fi
  cp "${REPO_ROOT}/notifly_py/${file}" "${BACKUP}/${file}"
done

uv run --no-project python "${REPO_ROOT}/scripts/prepare_spec.py" "${REPO_ROOT}/openapi.json" "${PATCHED_SPEC}"

uvx "openapi-python-client@${GENERATOR_VERSION}" generate \
  --path "${PATCHED_SPEC}" \
  --config "${REPO_ROOT}/gen-config.yaml" \
  --meta uv \
  --output-path "${TMP_OUT}" \
  --overwrite

rm -rf "${REPO_ROOT}/notifly_py"
cp -r "${TMP_OUT}/notifly_py" "${REPO_ROOT}/notifly_py"

for file in "${HANDWRITTEN[@]}"; do
  cp "${BACKUP}/${file}" "${REPO_ROOT}/notifly_py/${file}"
done

echo "Regenerated notifly_py from openapi.json (openapi-python-client ${GENERATOR_VERSION})."
echo "Restored ${#HANDWRITTEN[@]} hand-written modules."
echo "Next: uv run ruff check . && uv run mypy && uv run pytest, then review the diff."
