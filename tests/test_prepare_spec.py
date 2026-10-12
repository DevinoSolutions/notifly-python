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


def test_the_committed_spec_still_has_the_defects_the_fixes_target(committed_spec: dict[str, Any]) -> None:
    reaction = _reaction(committed_spec)

    assert reaction["type"] == "object"
    assert reaction["default"] == "check"
    assert _behavior_properties(committed_spec)["acknowledgeOnReceived"]["default"] is True


def test_the_fixes_type_reaction_on_resolved_as_a_string_and_drop_the_server_side_defaults(
    committed_spec: dict[str, Any],
) -> None:
    patched = prepare_spec.prepare_spec(copy.deepcopy(committed_spec))

    properties = _behavior_properties(patched)
    assert properties["reactionOnResolved"]["type"] == "string"
    assert properties["reactionOnResolved"]["nullable"] is True
    assert "default" not in properties["reactionOnResolved"]
    assert "default" not in properties["acknowledgeOnReceived"]


def test_preparing_never_touches_anything_but_the_targeted_properties(committed_spec: dict[str, Any]) -> None:
    patched = prepare_spec.prepare_spec(copy.deepcopy(committed_spec))
    properties = _behavior_properties(patched)
    properties["reactionOnResolved"]["type"] = "object"
    properties["reactionOnResolved"]["default"] = "check"
    properties["acknowledgeOnReceived"]["default"] = True

    assert patched == committed_spec


def test_a_fix_that_no_longer_matches_fails_loudly(committed_spec: dict[str, Any]) -> None:
    already_fixed = prepare_spec.prepare_spec(copy.deepcopy(committed_spec))

    with pytest.raises(prepare_spec.SpecFixError, match="delete fix_agent_reaction_on_resolved_type"):
        prepare_spec.prepare_spec(already_fixed)


def test_the_defaults_fix_fails_loudly_once_the_api_drops_the_defaults(committed_spec: dict[str, Any]) -> None:
    fixed_upstream = copy.deepcopy(committed_spec)
    properties = _behavior_properties(fixed_upstream)
    properties["reactionOnResolved"]["type"] = "string"
    properties["reactionOnResolved"].pop("default")

    spec = copy.deepcopy(fixed_upstream)
    with pytest.raises(prepare_spec.SpecFixError, match="delete fix_agent_reaction_on_resolved_type"):
        prepare_spec.prepare_spec(spec)
    with pytest.raises(prepare_spec.SpecFixError, match="delete fix_agent_behavior_defaults_are_server_side"):
        prepare_spec.fix_agent_behavior_defaults_are_server_side(fixed_upstream)


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
