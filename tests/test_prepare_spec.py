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
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import prepare_spec


@pytest.fixture(scope="module")
def committed_spec() -> dict[str, Any]:
    return json.loads((REPO_ROOT / "openapi.json").read_text(encoding="utf-8"))


def _reaction(spec: dict[str, Any]) -> dict[str, Any]:
    reaction: dict[str, Any] = spec["components"]["schemas"]["AgentBehaviorDto"]["properties"]["reactionOnResolved"]
    return reaction


def test_the_committed_spec_still_has_the_defect_the_fix_targets(committed_spec: dict[str, Any]) -> None:
    reaction = _reaction(committed_spec)

    assert reaction["type"] == "object"
    assert reaction["default"] == "check"


def test_the_fix_turns_the_string_default_into_a_string_typed_property(committed_spec: dict[str, Any]) -> None:
    patched = prepare_spec.prepare_spec(copy.deepcopy(committed_spec))

    reaction = _reaction(patched)
    assert reaction["type"] == "string"
    assert reaction["nullable"] is True
    assert reaction["default"] == "check"


def test_preparing_never_touches_anything_but_the_targeted_property(committed_spec: dict[str, Any]) -> None:
    patched = prepare_spec.prepare_spec(copy.deepcopy(committed_spec))
    _reaction(patched)["type"] = "object"

    assert patched == committed_spec


def test_a_fix_that_no_longer_matches_fails_loudly(committed_spec: dict[str, Any]) -> None:
    already_fixed = prepare_spec.prepare_spec(copy.deepcopy(committed_spec))

    with pytest.raises(prepare_spec.SpecFixError, match="delete fix_agent_reaction_on_resolved_type"):
        prepare_spec.prepare_spec(already_fixed)


def test_main_writes_the_patched_document_and_leaves_the_source_alone(tmp_path: Path) -> None:
    destination = tmp_path / "patched.json"
    source = REPO_ROOT / "openapi.json"
    before = source.read_bytes()

    assert prepare_spec.main([str(source), str(destination)]) == 0

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
