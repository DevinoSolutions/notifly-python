"""Spec-drift gate: compare the committed SDK spec against the live public document.

HAND-WRITTEN — run by ``.github/workflows/spec-drift.yml`` on a schedule.

Three things are checked, in order of how badly they would hurt:

1. **The envelope contract.** The SDK unwraps single-key ``{"data": ...}`` bodies at runtime
   (:mod:`notifly_py._envelope`). That is only correct while the API keeps wrapping. The live
   *public* document is the one flavor that still declares the wrapper, so counting how many
   of its operations wrap ``data`` is a direct, machine-checkable proxy for the contract. If
   that count collapses, the Phase-1 fix has inverted into a bug and the SDK must change.
2. **Route coverage.** Every live operation should exist in the committed spec; new ones mean
   the SDK is stale and should be regenerated.
3. **The bearer-only set.** ``notifly_py.internal_ops`` claims a specific list of
   dashboard-session operations. Operations the public document drops are exactly that list;
   if the API opens one up (or locks another down), the registry and the facade must follow.

Usage::

    python scripts/check_drift.py                          # fetch the live document
    python scripts/check_drift.py --live-file live.json    # offline, for tests
    python scripts/check_drift.py --format markdown        # issue-ready report
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_SPEC = REPO_ROOT / "openapi.json"
LIVE_SPEC_URL = "https://api.notifly.io/openapi.json"
HTTP_METHODS = ("get", "post", "put", "patch", "delete", "head", "options")

# Measured on 2026-08-05 against notifly 3.17.1: 63 operations whose live (public) success
# schema wraps its payload in `data` while the SDK spec declares the payload directly. The
# floor sits well below that baseline — this gate is here to catch the contract *collapsing*,
# not to churn on a handful of endpoints changing shape.
MEASURED_WRAPPED_OPERATIONS = 63
MIN_WRAPPED_OPERATIONS = 40


@dataclass
class DriftReport:
    live_version: str = ""
    sdk_version: str = ""
    wrapped_operations: int = 0
    comparable_operations: int = 0
    missing_from_sdk: list[str] = field(default_factory=list)
    bearer_only_added: list[str] = field(default_factory=list)
    bearer_only_removed: list[str] = field(default_factory=list)
    findings: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.findings


def load_spec(source: str) -> dict[str, Any]:
    """Load an OpenAPI document from a path or an ``http(s)`` URL."""
    if source.startswith("http://") or source.startswith("https://"):
        with urllib.request.urlopen(source, timeout=60) as response:  # noqa: S310 - fixed https host
            data: dict[str, Any] = json.loads(response.read().decode("utf-8"))
            return data
    return json.loads(Path(source).read_text(encoding="utf-8"))


def normalize_operation_id(operation_id: str) -> str:
    """``LayoutsController__delete`` and ``LayoutsController_delete`` are the same operation."""
    return operation_id.replace("__", "_")


def iter_operations(spec: dict[str, Any]) -> dict[str, dict[str, Any]]:
    operations: dict[str, dict[str, Any]] = {}
    for path, path_item in spec.get("paths", {}).items():
        for method, operation in path_item.items():
            if method not in HTTP_METHODS or not isinstance(operation, dict):
                continue
            operation_id = operation.get("operationId")
            if not operation_id:
                continue
            operations[normalize_operation_id(operation_id)] = {**operation, "_method": method, "_path": path}
    return operations


def resolve(spec: dict[str, Any], schema: Any, depth: int = 0) -> dict[str, Any] | None:
    if not isinstance(schema, dict) or depth > 8:
        return None
    ref = schema.get("$ref")
    if isinstance(ref, str):
        name = ref.rsplit("/", 1)[-1]
        return resolve(spec, spec.get("components", {}).get("schemas", {}).get(name), depth + 1)
    return schema


def success_schema(spec: dict[str, Any], operation: dict[str, Any]) -> tuple[Any, dict[str, Any] | None]:
    for status_code, response in sorted(operation.get("responses", {}).items()):
        if not str(status_code).startswith("2"):
            continue
        schema = response.get("content", {}).get("application/json", {}).get("schema")
        if schema is not None:
            return schema, resolve(spec, schema)
    return None, None


def wraps_data(spec: dict[str, Any], operation: dict[str, Any]) -> bool:
    _, resolved = success_schema(spec, operation)
    return bool(resolved and "data" in (resolved.get("properties") or {}))


def bearer_only_operations(spec: dict[str, Any]) -> set[str]:
    api_key_schemes = {
        name
        for name, scheme in spec.get("components", {}).get("securitySchemes", {}).items()
        if scheme.get("type") == "apiKey"
    }
    result: set[str] = set()
    for operation_id, operation in iter_operations(spec).items():
        security = operation.get("security") or spec.get("security") or []
        schemes = {name for requirement in security for name in requirement}
        if not (schemes & api_key_schemes):
            result.add(operation_id)
    return result


def check_drift(sdk_spec: dict[str, Any], live_spec: dict[str, Any], registry: set[str]) -> DriftReport:
    report = DriftReport(
        live_version=str(live_spec.get("info", {}).get("version", "")),
        sdk_version=str(sdk_spec.get("info", {}).get("version", "")),
    )
    sdk_operations = iter_operations(sdk_spec)
    live_operations = iter_operations(live_spec)

    report.missing_from_sdk = sorted(set(live_operations) - set(sdk_operations))
    if report.missing_from_sdk:
        report.findings.append(
            f"{len(report.missing_from_sdk)} live operation(s) are missing from the committed spec — "
            "regenerate the SDK: " + ", ".join(report.missing_from_sdk[:10])
        )

    for operation_id, live_operation in live_operations.items():
        sdk_operation = sdk_operations.get(operation_id)
        if sdk_operation is None:
            continue
        report.comparable_operations += 1
        if wraps_data(live_spec, live_operation) and not wraps_data(sdk_spec, sdk_operation):
            report.wrapped_operations += 1

    if report.wrapped_operations < MIN_WRAPPED_OPERATIONS:
        report.findings.append(
            f"ENVELOPE CONTRACT CHANGED: only {report.wrapped_operations} operation(s) still wrap their "
            f"payload in `data` (expected at least {MIN_WRAPPED_OPERATIONS}). notifly_py._envelope unwraps "
            "single-key `data` bodies at runtime — if the API stopped wrapping, that unwrap is now a bug."
        )

    live_bearer_only = set(sdk_operations) - set(live_operations)
    report.bearer_only_added = sorted(live_bearer_only - registry)
    report.bearer_only_removed = sorted(registry - live_bearer_only)
    if report.bearer_only_added:
        report.findings.append(
            "operation(s) dropped from the public document but absent from notifly_py.internal_ops: "
            + ", ".join(report.bearer_only_added)
        )
    if report.bearer_only_removed:
        report.findings.append(
            "operation(s) listed in notifly_py.internal_ops are now public — they can be added to the "
            "facade: " + ", ".join(report.bearer_only_removed)
        )
    if report.live_version and report.sdk_version and report.live_version != report.sdk_version:
        report.findings.append(
            f"API version changed: live {report.live_version} vs committed {report.sdk_version} — "
            "review the diff and regenerate."
        )
    return report


def render(report: DriftReport, fmt: str) -> str:
    lines = [
        f"live spec version:      {report.live_version or 'unknown'}",
        f"committed spec version: {report.sdk_version or 'unknown'}",
        f"comparable operations:  {report.comparable_operations}",
        f"data-wrapped responses: {report.wrapped_operations} (floor {MIN_WRAPPED_OPERATIONS})",
        f"missing from SDK spec:  {len(report.missing_from_sdk)}",
    ]
    if report.findings:
        lines.append("")
        lines.extend(f"- {finding}" for finding in report.findings)
    else:
        lines.append("")
        lines.append("no drift detected")
    body = "\n".join(lines)
    if fmt == "markdown":
        title = "Notifly API drift detected" if report.findings else "No Notifly API drift"
        return f"## {title}\n\n```\n{body}\n```\n"
    return body


def registry_operation_ids() -> set[str]:
    sys.path.insert(0, str(REPO_ROOT))
    from notifly_py.internal_ops import INTERNAL_ONLY_OPERATIONS

    return {normalize_operation_id(operation_id) for operation_id in INTERNAL_ONLY_OPERATIONS}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--spec", default=str(DEFAULT_SPEC), help="committed OpenAPI document")
    parser.add_argument("--live", default=LIVE_SPEC_URL, help="live public OpenAPI document URL")
    parser.add_argument("--live-file", default=None, help="use a local file instead of fetching --live")
    parser.add_argument("--format", choices=("text", "markdown"), default="text")
    parser.add_argument("--output", default=None, help="also write the report to this file")
    args = parser.parse_args(argv)

    report = check_drift(
        load_spec(args.spec),
        load_spec(args.live_file or args.live),
        registry_operation_ids(),
    )
    rendered = render(report, args.format)
    print(rendered)
    if args.output:
        Path(args.output).write_text(rendered, encoding="utf-8")
    return 0 if report.ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
