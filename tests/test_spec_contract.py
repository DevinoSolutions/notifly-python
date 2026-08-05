"""Contract tests between the committed spec, the generated package and the drift gate.

These run offline against ``openapi.json`` and a fixture copy of the public document, so the
guarantees they encode (the internal-op registry, the envelope assumption, the drift gate's
own ability to detect drift) hold in CI without network access.
"""

from __future__ import annotations

import copy
import json
from pathlib import Path
from typing import Any

import pytest

from notifly_py.internal_ops import INTERNAL_ONLY_OPERATIONS, is_internal_module, is_internal_operation

REPO_ROOT = Path(__file__).resolve().parent.parent
SPEC_PATH = REPO_ROOT / "openapi.json"
FIXTURE_PUBLIC_SPEC = Path(__file__).parent / "fixtures" / "public_openapi_subset.json"
HTTP_METHODS = ("get", "post", "put", "patch", "delete")


@pytest.fixture(scope="module")
def sdk_spec() -> dict[str, Any]:
    return json.loads(SPEC_PATH.read_text(encoding="utf-8"))


@pytest.fixture(scope="module")
def public_spec() -> dict[str, Any]:
    return json.loads(FIXTURE_PUBLIC_SPEC.read_text(encoding="utf-8"))


def _operations(spec: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {
        operation["operationId"]: operation
        for path_item in spec.get("paths", {}).values()
        for method, operation in path_item.items()
        if method in HTTP_METHODS and operation.get("operationId")
    }


def test_the_committed_spec_is_the_internal_notifly_flavor(sdk_spec: dict[str, Any]) -> None:
    assert sdk_spec["info"]["title"] == "Notifly API"
    assert sdk_spec["servers"][0]["url"] == "https://api.notifly.io"
    assert "secretKey" in sdk_spec["components"]["securitySchemes"]


def test_internal_ops_registry_matches_the_bearer_only_operations_in_the_spec(sdk_spec: dict[str, Any]) -> None:
    """G7: the registry is derived from the spec, not from folklore."""
    bearer_only = {
        operation_id
        for operation_id, operation in _operations(sdk_spec).items()
        if operation.get("security") == [{"bearerAuth": []}]
    }
    assert bearer_only == set(INTERNAL_ONLY_OPERATIONS)


def test_every_registered_internal_module_exists() -> None:
    import importlib

    for operation_id, module_path in INTERNAL_ONLY_OPERATIONS.items():
        module = importlib.import_module(module_path)
        assert hasattr(module, "sync_detailed"), f"{module_path} is not a generated operation module"
        assert is_internal_operation(operation_id)
        assert is_internal_module(module_path)


def test_only_one_operation_has_an_ambiguous_data_only_success_schema(sdk_spec: dict[str, Any]) -> None:
    """The single-key ``data`` heuristic is safe because exactly one operation could collide.

    ``ActivityController_getCharts`` is bearer-only and excluded from the public surface, so
    no supported call path can be affected by the ambiguity.
    """
    schemas = sdk_spec["components"]["schemas"]

    def resolve(schema: Any, depth: int = 0) -> dict[str, Any] | None:
        if not isinstance(schema, dict) or depth > 5:
            return None
        if "$ref" in schema:
            return resolve(schemas.get(schema["$ref"].rsplit("/", 1)[-1]), depth + 1)
        return schema

    ambiguous = []
    for operation_id, operation in _operations(sdk_spec).items():
        for status_code, response in operation.get("responses", {}).items():
            if not str(status_code).startswith("2"):
                continue
            resolved = resolve(response.get("content", {}).get("application/json", {}).get("schema"))
            if resolved and list((resolved.get("properties") or {}).keys()) == ["data"]:
                ambiguous.append(operation_id)

    assert ambiguous == ["ActivityController_getCharts"]
    assert set(ambiguous) <= set(INTERNAL_ONLY_OPERATIONS)


def test_every_operation_accepts_an_idempotency_key(sdk_spec: dict[str, Any]) -> None:
    """D4: the header the retry policy relies on for POST/PATCH replay is universal."""
    for operation_id, operation in _operations(sdk_spec).items():
        names = {parameter.get("name") for parameter in operation.get("parameters", [])}
        assert "idempotency-key" in names, f"{operation_id} has no idempotency-key parameter"


# --------------------------------------------------------------------------------------
# The drift gate itself
# --------------------------------------------------------------------------------------
def _check(sdk_spec: dict[str, Any], live_spec: dict[str, Any]) -> Any:
    import sys

    sys.path.insert(0, str(REPO_ROOT / "scripts"))
    from check_drift import check_drift, normalize_operation_id

    registry = {normalize_operation_id(operation_id) for operation_id in INTERNAL_ONLY_OPERATIONS}
    return check_drift(sdk_spec, live_spec, registry)


def test_drift_gate_is_quiet_against_the_current_public_document(
    sdk_spec: dict[str, Any], public_spec: dict[str, Any]
) -> None:
    report = _check(sdk_spec, public_spec)
    assert report.ok, report.findings
    assert report.wrapped_operations > 0


def test_drift_gate_flags_a_new_live_operation(sdk_spec: dict[str, Any], public_spec: dict[str, Any]) -> None:
    mutated = copy.deepcopy(public_spec)
    mutated["paths"]["/v2/brand-new"] = {
        "get": {"operationId": "BrandNewController_list", "responses": {"200": {"description": ""}}}
    }

    report = _check(sdk_spec, mutated)

    assert not report.ok
    assert report.missing_from_sdk == ["BrandNewController_list"]
    assert any("missing from the committed spec" in finding for finding in report.findings)


def test_drift_gate_flags_the_envelope_contract_disappearing(
    sdk_spec: dict[str, Any], public_spec: dict[str, Any]
) -> None:
    """If the API ever stops wrapping, the runtime unwrap becomes a bug — this must scream."""
    mutated = copy.deepcopy(public_spec)
    for schema in mutated["components"]["schemas"].values():
        properties = schema.get("properties")
        if isinstance(properties, dict):
            properties.pop("data", None)
    for path_item in mutated["paths"].values():
        for method, operation in path_item.items():
            if method not in HTTP_METHODS:
                continue
            for response in operation.get("responses", {}).values():
                schema = response.get("content", {}).get("application/json", {}).get("schema")
                if isinstance(schema, dict):
                    (schema.get("properties") or {}).pop("data", None)

    report = _check(sdk_spec, mutated)

    assert not report.ok
    assert any("ENVELOPE CONTRACT CHANGED" in finding for finding in report.findings)


def test_drift_gate_flags_an_internal_operation_becoming_public(
    sdk_spec: dict[str, Any], public_spec: dict[str, Any]
) -> None:
    mutated = copy.deepcopy(public_spec)
    mutated["paths"]["/v1/audit-logs"] = {
        "get": {"operationId": "AuditLogController_list", "responses": {"200": {"description": ""}}}
    }

    report = _check(sdk_spec, mutated)

    assert not report.ok
    assert report.bearer_only_removed == ["AuditLogController_list"]


def test_drift_gate_flags_a_version_bump(sdk_spec: dict[str, Any], public_spec: dict[str, Any]) -> None:
    mutated = copy.deepcopy(public_spec)
    mutated["info"]["version"] = "4.0.0"

    report = _check(sdk_spec, mutated)

    assert not report.ok
    assert any("API version changed" in finding for finding in report.findings)
