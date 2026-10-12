"""Update (PUT / PATCH) calls send only the fields the caller set.

The API documents defaults (``UpdateWorkflowDto.active`` ``false``, ``UpdateLayoutDto.isTranslationEnabled``
``false``, ...) and applies them itself. A generated model that carries such a default sends it on every
request, so ``UpdateLayoutDto(name="x")`` used to switch layout translations off. ``scripts/prepare_spec.py``
strips those defaults before generation; the guard at the bottom fails if a regeneration ever brings one back.
"""

from __future__ import annotations

import importlib
import json
import pkgutil
import re
import typing
from pathlib import Path
from typing import Any

import attrs
import httpx
import pytest
import respx

import notifly_py.api as generated_api
import notifly_py.models as generated_models
from notifly_py import Notifly, NotiflyClient, RetryConfig
from notifly_py.api.layouts import layouts_controller_update
from notifly_py.models import (
    EmailControlDto,
    InAppControlDto,
    PatchWorkflowDto,
    PreferencesRequestDto,
    ThrottleControlDto,
    UpdateAgentRequestDto,
    UpdateLayoutDto,
    UpdateWorkflowDto,
)
from notifly_py.types import UNSET

from .test_generated_coverage import HTTP_METHODS, _snake

REPO_ROOT = Path(__file__).resolve().parent.parent
BASE_URL = "https://api.notifly.test"
TIMESTAMP = "2026-10-12T10:00:00.000Z"

WORKFLOW = {
    "name": "Welcome",
    "_id": "wf_1",
    "workflowId": "welcome",
    "slug": "welcome",
    "updatedAt": TIMESTAMP,
    "createdAt": TIMESTAMP,
    "steps": [],
    "origin": "novu-cloud",
    "preferences": {"default": {"all": {"enabled": True, "readOnly": False}, "channels": {}}},
    "status": "ACTIVE",
    "severity": "none",
}
LAYOUT = {
    "_id": "ly_1",
    "layoutId": "main",
    "slug": "main",
    "name": "Main",
    "isDefault": False,
    "isTranslationEnabled": True,
    "updatedAt": TIMESTAMP,
    "createdAt": TIMESTAMP,
    "origin": "novu-cloud",
    "type": "REGULAR",
    "controls": {"values": {}},
}
SUBSCRIBER = {
    "_id": "6650f0a1c1a2b3d4e5f60001",
    "subscriberId": "s_1",
    "_organizationId": "org_1",
    "_environmentId": "env_1",
    "deleted": False,
    "createdAt": TIMESTAMP,
    "updatedAt": TIMESTAMP,
}


def _notifly() -> Notifly:
    return Notifly(client=NotiflyClient(base_url=BASE_URL, token="sk_test", retry_config=RetryConfig(max_retries=0)))


def _update_workflow_dto(**fields: Any) -> UpdateWorkflowDto:
    return UpdateWorkflowDto(name="Welcome", steps=[], preferences=PreferencesRequestDto(), **fields)


# --------------------------------------------------------------------------------------
# The DTOs that used to resend defaults
# --------------------------------------------------------------------------------------
@pytest.mark.parametrize(
    ("dto", "expected"),
    [
        (UpdateLayoutDto(name="Main"), {"name": "Main"}),
        (_update_workflow_dto(), {"name": "Welcome", "steps": [], "preferences": {}}),
        (_update_workflow_dto(description="d"), {"name": "Welcome", "steps": [], "preferences": {}, "description": "d"}),
        (InAppControlDto(), {}),
        (InAppControlDto(body="hi"), {"body": "hi"}),
        (EmailControlDto(subject="s"), {"subject": "s", "body": ""}),
        (ThrottleControlDto(), {"type": "fixed"}),
        (ThrottleControlDto(threshold=3), {"type": "fixed", "threshold": 3}),
        (UpdateAgentRequestDto(name="x"), {"name": "x"}),
        (PatchWorkflowDto(name="x"), {"name": "x"}),
    ],
    ids=lambda value: value.__class__.__name__ if not isinstance(value, dict) else "->",
)
def test_a_dto_built_with_one_field_serializes_only_that_field(dto: Any, expected: dict[str, Any]) -> None:
    assert dto.to_dict() == expected


@pytest.mark.parametrize(
    ("dto", "expected"),
    [
        (UpdateLayoutDto(name="Main", is_translation_enabled=False), {"name": "Main", "isTranslationEnabled": False}),
        (_update_workflow_dto(active=False), {"name": "Welcome", "steps": [], "preferences": {}, "active": False}),
        (
            _update_workflow_dto(is_translation_enabled=False),
            {"name": "Welcome", "steps": [], "preferences": {}, "isTranslationEnabled": False},
        ),
        (InAppControlDto(disable_output_sanitization=False), {"disableOutputSanitization": False}),
    ],
    ids=["layout", "workflow-active", "workflow-translation", "in-app-sanitization"],
)
def test_an_explicit_false_is_still_sent(dto: Any, expected: dict[str, Any]) -> None:
    assert dto.to_dict() == expected


def test_building_a_dto_from_a_mapping_keeps_the_absent_fields_absent() -> None:
    assert UpdateLayoutDto.from_dict({"name": "Main"}).to_dict() == {"name": "Main"}
    assert PatchWorkflowDto.from_dict({"name": "x"}).to_dict() == {"name": "x"}


# --------------------------------------------------------------------------------------
# What actually reaches the wire
# --------------------------------------------------------------------------------------
@respx.mock
def test_workflows_update_sends_only_the_fields_set_on_the_dto() -> None:
    route = respx.put(f"{BASE_URL}/v2/workflows/welcome").mock(
        return_value=httpx.Response(200, json={"data": WORKFLOW})
    )

    _notifly().workflows.update("welcome", _update_workflow_dto())

    body = json.loads(route.calls.last.request.content)
    assert set(body) == {"name", "steps", "preferences"}
    assert "active" not in body
    assert "isTranslationEnabled" not in body


@respx.mock
def test_workflows_update_sends_active_false_when_the_caller_sets_it() -> None:
    route = respx.put(f"{BASE_URL}/v2/workflows/welcome").mock(
        return_value=httpx.Response(200, json={"data": WORKFLOW})
    )

    _notifly().workflows.update("welcome", _update_workflow_dto(active=False))

    assert json.loads(route.calls.last.request.content)["active"] is False


@respx.mock
def test_workflows_update_accepts_a_mapping_body_without_adding_fields() -> None:
    route = respx.put(f"{BASE_URL}/v2/workflows/welcome").mock(
        return_value=httpx.Response(200, json={"data": WORKFLOW})
    )

    _notifly().workflows.update("welcome", {"name": "Welcome", "steps": [], "preferences": {}})

    assert json.loads(route.calls.last.request.content) == {"name": "Welcome", "steps": [], "preferences": {}}


@respx.mock
def test_workflows_patch_builds_the_body_from_keyword_fields_only() -> None:
    route = respx.patch(f"{BASE_URL}/v2/workflows/welcome").mock(
        return_value=httpx.Response(200, json={"data": WORKFLOW})
    )
    notifly = _notifly()

    notifly.workflows.patch("welcome", active=False)
    notifly.workflows.patch("welcome", PatchWorkflowDto(name="Renamed"), idempotency_key="idem_1")
    notifly.workflows.patch("welcome", tags=None)

    bodies = [json.loads(call.request.content) for call in route.calls]
    assert bodies == [{"active": False}, {"name": "Renamed"}, {}]
    assert route.calls[1].request.headers["idempotency-key"] == "idem_1"


@respx.mock
async def test_async_workflows_update_and_patch_send_only_what_the_caller_passed() -> None:
    from notifly_py import AsyncNotifly

    put = respx.put(f"{BASE_URL}/v2/workflows/welcome").mock(return_value=httpx.Response(200, json={"data": WORKFLOW}))
    patch = respx.patch(f"{BASE_URL}/v2/workflows/welcome").mock(
        return_value=httpx.Response(200, json={"data": WORKFLOW})
    )
    notifly = AsyncNotifly(
        client=NotiflyClient(base_url=BASE_URL, token="sk_test", retry_config=RetryConfig(max_retries=0))
    )

    await notifly.workflows.update("welcome", _update_workflow_dto())
    await notifly.workflows.patch("welcome", is_translation_enabled=True)

    assert set(json.loads(put.calls.last.request.content)) == {"name", "steps", "preferences"}
    assert json.loads(patch.calls.last.request.content) == {"isTranslationEnabled": True}


@respx.mock
def test_a_layout_update_through_the_generated_operation_sends_only_the_name() -> None:
    route = respx.put(f"{BASE_URL}/v2/layouts/main").mock(return_value=httpx.Response(200, json={"data": LAYOUT}))

    layouts_controller_update.sync(layout_id="main", client=_notifly().client, body=UpdateLayoutDto(name="Main"))

    assert json.loads(route.calls.last.request.content) == {"name": "Main"}


@respx.mock
def test_subscribers_update_sends_only_the_passed_fields() -> None:
    route = respx.patch(f"{BASE_URL}/v2/subscribers/s_1").mock(
        return_value=httpx.Response(200, json={"data": SUBSCRIBER})
    )

    _notifly().subscribers.update("s_1", first_name="Ada", email=None)

    assert json.loads(route.calls.last.request.content) == {"firstName": "Ada"}


@respx.mock
def test_topics_update_sends_only_the_passed_fields() -> None:
    route = respx.patch(f"{BASE_URL}/v2/topics/product-updates").mock(
        return_value=httpx.Response(200, json={"data": {"_id": "topic_1", "key": "product-updates", "name": "New"}})
    )

    _notifly().topics.update("product-updates", name="New")

    assert json.loads(route.calls.last.request.content) == {"name": "New"}


# --------------------------------------------------------------------------------------
# Guard: no regeneration may bring a default back
# --------------------------------------------------------------------------------------
#: Properties the API marks ``required`` that keep a constructor default. They are always on the wire whatever
#: the caller does, so the default only spares them a mandatory argument. ``(class, attribute) -> JSON key``.
REQUIRED_WITH_DEFAULT = {
    ("ChannelPreferenceDto", "enabled"): "enabled",
    ("DelayControlDto", "type_"): "type",
    ("EmailControlDto", "body"): "body",
    ("ThrottleControlDto", "type_"): "type",
    ("WorkflowPreferenceDto", "enabled"): "enabled",
    ("WorkflowPreferenceDto", "read_only"): "readOnly",
}


def _attrs_classes(annotation: Any) -> set[type]:
    if isinstance(annotation, type) and attrs.has(annotation):
        return {annotation}
    return {cls for argument in typing.get_args(annotation) for cls in _attrs_classes(argument)}


def _reachable_models(root: type, seen: set[type]) -> None:
    if root in seen:
        return
    seen.add(root)
    hints = typing.get_type_hints(root, localns=vars(generated_models))
    for field in attrs.fields(root):
        for nested in _attrs_classes(hints[field.name]):
            _reachable_models(nested, seen)


def _update_operations() -> dict[str, Any]:
    """Generated modules whose request is a PUT or a PATCH with a body, keyed by module name."""
    modules: dict[str, Any] = {}
    for info in pkgutil.walk_packages(generated_api.__path__, "notifly_py.api."):
        if info.ispkg:
            continue
        module = importlib.import_module(info.name)
        method = re.search(r'"method": "(\w+)"', Path(module.__file__ or "").read_text(encoding="utf-8"))
        assert method is not None, f"{info.name} has no request method"
        if method.group(1) in ("put", "patch") and "body" in typing.get_type_hints(module._get_kwargs):
            modules[info.name.rsplit(".", 1)[-1]] = module
    return modules


def _models_reachable_from_update_bodies() -> set[type]:
    reachable: set[type] = set()
    for module in _update_operations().values():
        body = typing.get_type_hints(module._get_kwargs, localns=vars(generated_models))["body"]
        for root in _attrs_classes(body):
            _reachable_models(root, reachable)
    return reachable


def _defaulted_fields() -> set[tuple[str, str]]:
    return {
        (model.__name__, field.name)
        for model in _models_reachable_from_update_bodies()
        for field in attrs.fields(model)
        if field.init and field.default is not attrs.NOTHING and field.default is not UNSET
    }


def test_the_guard_scans_every_put_and_patch_operation_with_a_json_body() -> None:
    spec = json.loads((REPO_ROOT / "openapi.json").read_text(encoding="utf-8"))
    expected = {
        _snake(operation["operationId"])
        for path_item in spec["paths"].values()
        for method, operation in path_item.items()
        if method in HTTP_METHODS
        and method in ("put", "patch")
        and "application/json" in (operation.get("requestBody") or {}).get("content", {})
    }

    assert set(_update_operations()) == expected
    assert len(expected) >= 20
    assert {"UpdateLayoutDto", "UpdateWorkflowDto", "UpdateAgentRequestDto", "PatchWorkflowDto"} <= {
        model.__name__ for model in _models_reachable_from_update_bodies()
    }


def test_no_model_reachable_from_an_update_body_sends_a_default_the_caller_never_set() -> None:
    offenders = sorted(_defaulted_fields() - set(REQUIRED_WITH_DEFAULT))

    assert not offenders, (
        f"{offenders} serialize a default the caller never set, so an update would silently overwrite server "
        "state. The spec's `default:` must be stripped in scripts/prepare_spec.py "
        "(fix_update_bodies_omit_unset_fields); do not edit the generated model."
    )


def test_every_allowed_required_default_is_still_there_and_still_required_by_the_api() -> None:
    spec = json.loads((REPO_ROOT / "openapi.json").read_text(encoding="utf-8"))
    schemas = spec["components"]["schemas"]

    assert set(REQUIRED_WITH_DEFAULT) == _defaulted_fields() & set(REQUIRED_WITH_DEFAULT), "stale allowlist entry"
    for (model_name, _attribute), json_key in REQUIRED_WITH_DEFAULT.items():
        assert json_key in schemas[model_name]["required"], f"{model_name}.{json_key} is optional in the API now"
