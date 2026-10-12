"""Union order pinning in ``scripts/prepare_spec.py`` and the class numbering it keeps stable.

openapi-python-client names the classes of an inline ``oneOf`` variant by position. These tests pin the
rule (known variants keep their order, new ones go last) and the one place it matters today:
``GeneratePreviewResponseDto.result``, where ``...ResultType7`` is the delay preview and ``...ResultType8``
the digest preview in every release, and the tool preview added in 0.2.0 is ``...ResultType9``.
"""

from __future__ import annotations

import copy
import json
import sys
from pathlib import Path
from typing import Any

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
PINS_PATH = REPO_ROOT / "scripts" / "union_order.json"
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import prepare_spec

from notifly_py.models import (
    CreateWorkflowDto,
    GeneratePreviewResponseDtoResultType7,
    GeneratePreviewResponseDtoResultType7Type,
    GeneratePreviewResponseDtoResultType8,
    GeneratePreviewResponseDtoResultType8Type,
    GeneratePreviewResponseDtoResultType9,
    GeneratePreviewResponseDtoResultType9Type,
    ToolStepUpsertDto,
    UpdateWorkflowDto,
)

RESULT_UNION = "components > schemas > GeneratePreviewResponseDto > properties > result > oneOf"
HOLDER_UNION = "components > schemas > Holder > properties > value > oneOf"


def _ref(name: str) -> dict[str, str]:
    return {"$ref": f"#/components/schemas/{name}"}


def _inline(type_: str) -> dict[str, Any]:
    return {"type": "object", "properties": {"type": {"type": "string", "enum": [type_]}}}


def _spec_with(variants: list[dict[str, Any]]) -> dict[str, Any]:
    return {"components": {"schemas": {"Holder": {"properties": {"value": {"oneOf": variants}}}}}}


@pytest.fixture(scope="module")
def committed_spec() -> dict[str, Any]:
    return json.loads((REPO_ROOT / "openapi.json").read_text(encoding="utf-8"))  # type: ignore[no-any-return]


@pytest.fixture(scope="module")
def pins() -> dict[str, list[str]]:
    return json.loads(PINS_PATH.read_text(encoding="utf-8"))  # type: ignore[no-any-return]


def test_variant_ids_key_refs_by_name_and_inline_variants_by_type_and_occurrence() -> None:
    ids = prepare_spec.variant_ids([_ref("A"), _inline("email"), _inline("sms"), _inline("email"), {"type": "object"}])

    assert ids == ["A", "inline:email#0", "inline:sms#0", "inline:email#1", "inline:#0"]


def test_a_new_variant_inserted_in_the_middle_is_moved_to_the_end() -> None:
    spec = _spec_with([_ref("A"), _ref("B"), _ref("New"), _ref("C")])

    prepare_spec.pin_union_order(spec, {HOLDER_UNION: ["A", "B", "C"]})

    assert prepare_spec.current_union_order(spec)[HOLDER_UNION] == ["A", "B", "C", "New"]


def test_known_variants_keep_their_pinned_order_even_if_the_api_reorders_them() -> None:
    spec = _spec_with([_ref("C"), _ref("A"), _ref("B")])

    prepare_spec.pin_union_order(spec, {HOLDER_UNION: ["A", "B", "C"]})

    assert prepare_spec.current_union_order(spec)[HOLDER_UNION] == ["A", "B", "C"]


def test_several_new_variants_keep_their_relative_order_at_the_end() -> None:
    spec = _spec_with([_ref("N1"), _ref("A"), _ref("N2"), _ref("B")])

    prepare_spec.pin_union_order(spec, {HOLDER_UNION: ["A", "B"]})

    assert prepare_spec.current_union_order(spec)[HOLDER_UNION] == ["A", "B", "N1", "N2"]


def test_a_variant_the_api_removed_is_simply_skipped() -> None:
    spec = _spec_with([_ref("A"), _ref("C")])

    prepare_spec.pin_union_order(spec, {HOLDER_UNION: ["A", "B", "C"]})

    assert prepare_spec.current_union_order(spec)[HOLDER_UNION] == ["A", "C"]


def test_inline_variants_are_pinned_by_their_type_not_their_position() -> None:
    spec = _spec_with([_inline("tool"), _inline("delay"), _inline("digest")])

    prepare_spec.pin_union_order(spec, {HOLDER_UNION: ["inline:delay#0", "inline:digest#0"]})

    assert prepare_spec.current_union_order(spec)[HOLDER_UNION] == ["inline:delay#0", "inline:digest#0", "inline:tool#0"]


def test_unpinned_unions_are_left_exactly_as_the_api_sent_them() -> None:
    spec = _spec_with([_ref("B"), _ref("A")])
    before = copy.deepcopy(spec)

    prepare_spec.pin_union_order(spec, {"components > schemas > Other > oneOf": ["A", "B"]})

    assert spec == before


def test_pinning_is_idempotent() -> None:
    spec = _spec_with([_ref("A"), _ref("New"), _ref("B")])
    pins = {HOLDER_UNION: ["A", "B"]}

    prepare_spec.pin_union_order(spec, pins)
    once = copy.deepcopy(spec)
    prepare_spec.pin_union_order(spec, pins)

    assert spec == once


def test_the_committed_pins_file_matches_the_committed_spec(
    committed_spec: dict[str, Any], pins: dict[str, list[str]]
) -> None:
    prepared = prepare_spec.prepare_spec(copy.deepcopy(committed_spec), pins)

    assert prepare_spec.current_union_order(prepared) == pins, (
        "scripts/union_order.json is stale: run scripts/regenerate.sh (it rewrites the pins) and review the diff"
    )


def test_the_committed_spec_inserts_the_tool_preview_in_the_middle_and_pinning_moves_it_last(
    committed_spec: dict[str, Any], pins: dict[str, list[str]]
) -> None:
    raw = prepare_spec.current_union_order(committed_spec)[RESULT_UNION]
    prepared = prepare_spec.current_union_order(prepare_spec.prepare_spec(copy.deepcopy(committed_spec), pins))[
        RESULT_UNION
    ]

    assert raw.index("inline:tool#0") < raw.index("inline:delay#0")
    assert prepared[-1] == "inline:tool#0"
    assert prepared.index("inline:delay#0") == 7
    assert prepared.index("inline:digest#0") == 8


def test_delay_digest_and_tool_previews_keep_their_class_numbers() -> None:
    delay = GeneratePreviewResponseDtoResultType7.from_dict({"type": "delay"})
    digest = GeneratePreviewResponseDtoResultType8.from_dict({"type": "digest"})
    tool = GeneratePreviewResponseDtoResultType9.from_dict({"type": "tool"})

    assert delay.type_ is GeneratePreviewResponseDtoResultType7Type.DELAY
    assert digest.type_ is GeneratePreviewResponseDtoResultType8Type.DIGEST
    assert tool.type_ is GeneratePreviewResponseDtoResultType9Type.TOOL
    assert delay.to_dict()["type"] == "delay"
    assert digest.to_dict()["type"] == "digest"
    assert tool.to_dict()["type"] == "tool"


def test_each_numbered_preview_rejects_the_other_previews_type_value() -> None:
    with pytest.raises(ValueError):
        GeneratePreviewResponseDtoResultType7.from_dict({"type": "digest"})
    with pytest.raises(ValueError):
        GeneratePreviewResponseDtoResultType8.from_dict({"type": "tool"})
    with pytest.raises(ValueError):
        GeneratePreviewResponseDtoResultType9.from_dict({"type": "delay"})


@pytest.mark.parametrize(
    "location",
    [
        "components > schemas > CreateWorkflowDto > properties > steps > items > oneOf",
        "components > schemas > UpdateWorkflowDto > properties > steps > items > oneOf",
    ],
)
def test_the_tool_step_is_last_in_the_workflow_step_unions(pins: dict[str, list[str]], location: str) -> None:
    assert pins[location][-1] == "ToolStepUpsertDto"


def test_the_workflow_dtos_accept_a_tool_step() -> None:
    assert "ToolStepUpsertDto" in str(CreateWorkflowDto.__annotations__["steps"])
    assert "ToolStepUpsertDto" in str(UpdateWorkflowDto.__annotations__["steps"])
    assert ToolStepUpsertDto.__name__ == "ToolStepUpsertDto"
