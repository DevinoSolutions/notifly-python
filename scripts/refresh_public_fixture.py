"""Regenerate ``tests/fixtures/public_openapi_subset.json`` from the live public document.

The fixture keeps only what the drift tests reason about — operationIds, security, and
whether each success response wraps its payload in ``data`` — so the 1.3 MB live document
does not have to live in the repo.

Usage::

    python scripts/refresh_public_fixture.py
    python scripts/refresh_public_fixture.py --live-file downloaded.json
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from check_drift import HTTP_METHODS, LIVE_SPEC_URL, REPO_ROOT, load_spec, resolve

FIXTURE_PATH = REPO_ROOT / "tests" / "fixtures" / "public_openapi_subset.json"
DESCRIPTION = (
    "Trimmed fixture of the public Notifly OpenAPI document (operationIds, security and "
    "response envelope shape only). Regenerate with scripts/refresh_public_fixture.py."
)


def build_fixture(live: dict[str, Any]) -> dict[str, Any]:
    paths: dict[str, Any] = {}
    for path, path_item in live.get("paths", {}).items():
        entry: dict[str, Any] = {}
        for method, operation in path_item.items():
            if method not in HTTP_METHODS or not isinstance(operation, dict) or not operation.get("operationId"):
                continue
            responses: dict[str, Any] = {}
            for status_code, response in operation.get("responses", {}).items():
                schema = response.get("content", {}).get("application/json", {}).get("schema")
                resolved = resolve(live, schema) or {}
                wraps = str(status_code).startswith("2") and "data" in (resolved.get("properties") or {})
                if wraps:
                    responses[status_code] = {
                        "description": "",
                        "content": {
                            "application/json": {
                                "schema": {"type": "object", "properties": {"data": {"type": "object"}}}
                            }
                        },
                    }
                else:
                    responses[status_code] = {"description": ""}
            entry[method] = {
                "operationId": operation["operationId"],
                "security": operation.get("security"),
                "responses": responses or {"200": {"description": ""}},
            }
        if entry:
            paths[path] = entry

    return {
        "openapi": live["openapi"],
        "info": {"title": live["info"]["title"], "version": live["info"]["version"], "description": DESCRIPTION},
        "servers": live.get("servers"),
        "security": live.get("security"),
        "components": {"securitySchemes": live["components"]["securitySchemes"], "schemas": {}},
        "paths": paths,
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--live-file", default=None, help="use a local file instead of fetching the live document")
    parser.add_argument("--output", default=str(FIXTURE_PATH))
    args = parser.parse_args(argv)

    fixture = build_fixture(load_spec(args.live_file or LIVE_SPEC_URL))
    Path(args.output).write_text(json.dumps(fixture, indent=1, ensure_ascii=False), encoding="utf-8")
    operations = sum(len(path_item) for path_item in fixture["paths"].values())
    print(f"wrote {args.output} ({operations} operations)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
