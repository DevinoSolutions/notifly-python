"""``scripts/prepare_spec.py``: the named spec fixes applied before generation.

The committed ``openapi.json`` is a verbatim export of the API; the generator reads a patched copy.
Each fix must apply to the committed document and must refuse to apply once the API fixes its side.
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


@pytest.fixture(scope="module")
def committed_spec() -> dict[str, Any]:
    return json.loads((REPO_ROOT / "openapi.json").read_text(encoding="utf-8"))


def _reaction(spec: dict[str, Any]) -> dict[str, Any]:
    reaction: dict[str, Any] = spec["components"]["schemas"]["AgentBehaviorDto"]["properties"]["reactionOnResolved"]
    return reaction


def _behavior_properties(spec: dict[str, Any]) -> dict[str, Any]:
    properties: dict[str, Any] = spec["components"]["schemas"]["AgentBehaviorDto"]["properties"]
    return properties


def _schema_properties(spec: dict[str, Any], name: str) -> dict[str, Any]:
    properties: dict[str, Any] = spec["components"]["schemas"][name]["properties"]
    return properties


#: Every optional property reachable from a PUT / PATCH body whose ``default`` the generator would turn into a value
#: the caller never set. Pinned so a spec change that adds or removes one is reviewed, not absorbed.
STRIPPED_DEFAULTS = {
    "AgentBehaviorDto.acknowledgeOnReceived",
    "AgentBehaviorDto.reactionOnResolved",
    "EmailControlDto.disableOutputSanitization",
    "EmailControlDto.editorType",
    "InAppControlDto.disableOutputSanitization",
    "ThrottleControlDto.threshold",
    "UpdateLayoutDto.isTranslationEnabled",
    "UpdateWorkflowDto.active",
    "UpdateWorkflowDto.isTranslationEnabled",
}


def _changes(before: Any, after: Any, path: str = "") -> list[str]:
    """Where ``after`` differs from ``before``: ``-default`` for a removed default, ``~key`` for anything else."""
    if isinstance(before, dict) and isinstance(after, dict):
        found: list[str] = []
        for key in before.keys() | after.keys():
            if key not in after:
                found.append(f"{path}.{key}" if key == "default" else f"{path}.-{key}")
            elif key not in before:
                found.append(f"{path}.+{key}")
            else:
                found.extend(_changes(before[key], after[key], f"{path}.{key}"))
        return found
    if isinstance(before, list) and isinstance(after, list) and len(before) == len(after):
        return [
            change
            for index, pair in enumerate(zip(before, after, strict=True))
            for change in _changes(*pair, f"{path}[{index}]")
        ]
    return [] if before == after else [f"~{path}"]


def test_the_committed_spec_still_has_the_defects_the_fixes_target(committed_spec: dict[str, Any]) -> None:
    reaction = _reaction(committed_spec)

    assert reaction["type"] == "object"
    assert reaction["default"] == "check"
    assert _behavior_properties(committed_spec)["acknowledgeOnReceived"]["default"] is True
    assert _schema_properties(committed_spec, "UpdateLayoutDto")["isTranslationEnabled"]["default"] is False
    assert _schema_properties(committed_spec, "UpdateWorkflowDto")["active"]["default"] is False


def test_the_fixes_type_reaction_on_resolved_as_a_string_and_drop_the_server_side_defaults(
    committed_spec: dict[str, Any],
) -> None:
    patched = prepare_spec.prepare_spec(copy.deepcopy(committed_spec))

    properties = _behavior_properties(patched)
    assert properties["reactionOnResolved"]["type"] == "string"
    assert properties["reactionOnResolved"]["nullable"] is True
    assert "default" not in properties["reactionOnResolved"]
    assert "default" not in properties["acknowledgeOnReceived"]


def test_update_bodies_stop_declaring_defaults_for_fields_the_caller_may_leave_unset(
    committed_spec: dict[str, Any],
) -> None:
    patched = prepare_spec.prepare_spec(copy.deepcopy(committed_spec))

    assert "default" not in _schema_properties(patched, "UpdateLayoutDto")["isTranslationEnabled"]
    assert "default" not in _schema_properties(patched, "UpdateWorkflowDto")["active"]
    assert "default" not in _schema_properties(patched, "UpdateWorkflowDto")["isTranslationEnabled"]


def test_defaults_survive_where_no_update_body_reaches_the_schema_or_the_property_is_required(
    committed_spec: dict[str, Any],
) -> None:
    patched = prepare_spec.prepare_spec(copy.deepcopy(committed_spec))

    # Create bodies are not update bodies: the caller names the whole entity there.
    assert _schema_properties(patched, "CreateLayoutDto")["isTranslationEnabled"]["default"] is False
    assert _schema_properties(patched, "CreateWorkflowDto")["active"]["default"] is False
    assert _schema_properties(patched, "CreateAgentRequestDto")["active"]["default"] is True
    # Required properties are always sent, so removing the default would only make the argument mandatory.
    assert _schema_properties(patched, "ThrottleControlDto")["type"]["default"] == "fixed"
    assert _schema_properties(patched, "WorkflowPreferenceDto")["enabled"]["default"] is True


def test_preparing_changes_nothing_but_the_reaction_type_and_the_pinned_defaults(
    committed_spec: dict[str, Any],
) -> None:
    patched = prepare_spec.prepare_spec(copy.deepcopy(committed_spec))

    changes = set(_changes(committed_spec, patched))

    stripped = {
        change.removeprefix(".components.schemas.").replace(".properties.", ".").removesuffix(".default")
        for change in changes
        if change.endswith(".default")
    }
    assert stripped == STRIPPED_DEFAULTS
    assert changes - {change for change in changes if change.endswith(".default")} == {
        "~.components.schemas.AgentBehaviorDto.properties.reactionOnResolved.type"
    }


def test_a_fix_that_no_longer_matches_fails_loudly(committed_spec: dict[str, Any]) -> None:
    already_fixed = prepare_spec.prepare_spec(copy.deepcopy(committed_spec))

    with pytest.raises(prepare_spec.SpecFixError, match="delete fix_agent_reaction_on_resolved_type"):
        prepare_spec.prepare_spec(already_fixed)


def test_the_reaction_fix_fails_loudly_once_the_api_types_it_itself(committed_spec: dict[str, Any]) -> None:
    fixed_upstream = copy.deepcopy(committed_spec)
    reaction = _reaction(fixed_upstream)
    reaction["type"] = "string"
    reaction.pop("default")

    with pytest.raises(prepare_spec.SpecFixError, match="delete fix_agent_reaction_on_resolved_type"):
        prepare_spec.prepare_spec(fixed_upstream)


def test_the_update_defaults_fix_fails_loudly_once_no_update_body_declares_a_default(
    committed_spec: dict[str, Any],
) -> None:
    patched = prepare_spec.prepare_spec(copy.deepcopy(committed_spec))

    with pytest.raises(prepare_spec.SpecFixError, match="delete fix_update_bodies_omit_unset_fields"):
        prepare_spec.fix_update_bodies_omit_unset_fields(patched)


def test_main_writes_the_patched_document_and_leaves_the_source_alone(tmp_path: Path) -> None:
    destination = tmp_path / "patched.json"
    source = REPO_ROOT / "openapi.json"
    before = source.read_bytes()

    assert prepare_spec.main([str(source), str(destination), "--pins", str(PINS_PATH)]) == 0

    assert source.read_bytes() == before
    assert _reaction(json.loads(destination.read_text(encoding="utf-8")))["type"] == "string"


def test_main_exits_non_zero_and_writes_nothing_when_a_fix_is_stale(
    tmp_path: Path, committed_spec: dict[str, Any], capsys: pytest.CaptureFixture[str]
) -> None:
    stale = tmp_path / "stale.json"
    stale.write_text(json.dumps(prepare_spec.prepare_spec(copy.deepcopy(committed_spec))), encoding="utf-8")
    destination = tmp_path / "out.json"

    assert prepare_spec.main([str(stale), str(destination)]) == 1

    assert not destination.exists()
    assert "delete fix_agent_reaction_on_resolved_type" in capsys.readouterr().err
