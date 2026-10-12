"""Write the OpenAPI document the generator actually consumes: ``openapi.json`` plus known spec fixes.

HAND-WRITTEN — run by ``scripts/regenerate.sh`` before ``openapi-python-client``. The committed
``openapi.json`` stays a verbatim export of the API (the drift gate and the contract tests read
it), so every fix lives here, named, with a precondition that fails loudly when the API's
document no longer has the defect. A fix that stops matching must be deleted, not left behind.

Usage::

    python scripts/prepare_spec.py openapi.json patched-openapi.json
"""

from __future__ import annotations

import argparse
import json
import sys
from collections.abc import Callable
from pathlib import Path
from typing import Any


class SpecFixError(RuntimeError):
    """A fix's precondition no longer holds: the API changed, so the fix is stale."""


def fix_agent_reaction_on_resolved_type(spec: dict[str, Any]) -> None:
    """``AgentBehaviorDto.reactionOnResolved`` is declared ``type: object`` with the string default ``"check"``.

    openapi-python-client rejects a non-null default on an object ("Value check is not valid, only
    None is allowed") and, instead of failing, drops ``AgentBehaviorDto`` and everything that
    references it: ``AgentResponseDto``, ``ListAgentsResponseDto`` and ``UpdateAgentRequestDto``. That
    silently removes ``PATCH /v1/agents/{identifier}`` and the typed responses of four more Agents
    operations. The description ("Cross-platform emoji name … Default: 'check'") shows the real
    type is a nullable string.
    """
    reaction = spec["components"]["schemas"]["AgentBehaviorDto"]["properties"]["reactionOnResolved"]
    if reaction.get("type") != "object" or reaction.get("default") != "check":
        raise SpecFixError(
            "AgentBehaviorDto.reactionOnResolved is no longer `type: object` with default 'check' "
            f"(got type={reaction.get('type')!r}, default={reaction.get('default')!r}); the API fixed it, "
            "so delete fix_agent_reaction_on_resolved_type from scripts/prepare_spec.py."
        )
    reaction["type"] = "string"


FIXES: tuple[Callable[[dict[str, Any]], None], ...] = (fix_agent_reaction_on_resolved_type,)


def prepare_spec(spec: dict[str, Any]) -> dict[str, Any]:
    """Apply every fix in place and return the document."""
    for fix in FIXES:
        fix(spec)
    return spec


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path, help="committed OpenAPI document (openapi.json)")
    parser.add_argument("destination", type=Path, help="where to write the generator input")
    args = parser.parse_args(argv)

    spec = json.loads(args.source.read_text(encoding="utf-8"))
    try:
        prepare_spec(spec)
    except SpecFixError as error:
        print(f"error: {error}", file=sys.stderr)
        return 1
    args.destination.write_text(json.dumps(spec, indent=2), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
