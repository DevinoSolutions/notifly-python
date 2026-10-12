"""Write the OpenAPI document the generator actually consumes: ``openapi.json`` plus known spec fixes.

HAND-WRITTEN — run by ``scripts/regenerate.sh`` before ``openapi-python-client``. The committed
``openapi.json`` stays a verbatim export of the API (the drift gate and the contract tests read
it), so everything done to it lives here. Two kinds of change:

* **Named fixes** for defects in the API's document. Each has a precondition that fails loudly once
  the API no longer has the defect; a fix that stops matching must be deleted, not left behind.
* **Union order pinning.** openapi-python-client names the classes of an inline ``oneOf`` / ``anyOf``
  variant by position (``GeneratePreviewResponseDtoResultType7``), so a variant the API inserts in the
  middle silently renumbers every class after it: ``isinstance(result, ...Type7)`` then matches a
  different step and enum members vanish. ``scripts/union_order.json`` records the variant order of
  the last release; known variants keep their relative order and new ones go to the END, so existing
  class names never change meaning. ``--update-pins`` rewrites the file after a regeneration, and the
  diff is reviewed with the rest of the release.

Usage::

    python scripts/prepare_spec.py openapi.json patched-openapi.json --pins scripts/union_order.json
    python scripts/prepare_spec.py openapi.json patched-openapi.json --pins scripts/union_order.json --update-pins
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from collections.abc import Callable
from pathlib import Path
from typing import Any

UNION_KEYS = ("oneOf", "anyOf")
SPARSE_UPDATE_METHODS = ("put", "patch")
PATH_SEPARATOR = " > "


class SpecFixError(RuntimeError):
    """A fix's precondition no longer holds: the API changed, so the fix is stale."""


# --------------------------------------------------------------------------------------
# Named fixes
# --------------------------------------------------------------------------------------
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


def fix_update_bodies_omit_unset_fields(spec: dict[str, Any]) -> None:
    """Drop ``default`` from every optional property reachable from a ``PUT`` / ``PATCH`` request body.

    The API documents defaults that it applies itself when a field is absent (``UpdateWorkflowDto.active``
    ``false``, ``isTranslationEnabled`` ``false``, ``AgentBehaviorDto.acknowledgeOnReceived`` ``true``, ...).
    openapi-python-client turns each into a non-``Unset`` Python default, so
    ``UpdateLayoutDto(name="x")`` serializes ``{"name": "x", "isTranslationEnabled": false}`` and an update
    that names one field silently resets the others to their defaults on the server. Without the default an
    unset field is ``UNSET`` and stays out of the request body, while an explicit value (``None`` included
    where the property is nullable) is still sent.

    Required properties keep their default: they are sent regardless, and removing it would turn a
    defaulted constructor argument into a mandatory one. Response parsing is unaffected, because every
    generated ``from_dict`` reads an absent optional field as ``UNSET`` whatever the constructor default is.
    Nested schemas are shared with the create operations (``EmailControlDto`` ...), so the same fields also
    stop being sent by default there; the server applies the same defaults on create.
    """
    schemas = spec["components"]["schemas"]
    stripped: list[str] = []
    visited: set[str] = set()

    def walk(node: Any, location: str) -> None:
        if not isinstance(node, dict):
            return
        reference = node.get("$ref")
        if isinstance(reference, str):
            name = reference.rsplit("/", 1)[-1]
            if name not in visited:
                visited.add(name)
                walk(schemas[name], name)
            return
        required = set(node.get("required", ()))
        for property_name, property_schema in (node.get("properties") or {}).items():
            if isinstance(property_schema, dict) and "default" in property_schema and property_name not in required:
                del property_schema["default"]
                stripped.append(f"{location}.{property_name}")
            walk(property_schema, f"{location}.{property_name}")
        for key in (*UNION_KEYS, "allOf"):
            for variant in node.get(key, ()):
                walk(variant, location)
        walk(node.get("items"), location)
        walk(node.get("additionalProperties"), location)

    for path, path_item in spec["paths"].items():
        for method in SPARSE_UPDATE_METHODS:
            operation = path_item.get(method)
            if operation is None:
                continue
            body = (operation.get("requestBody") or {}).get("content", {}).get("application/json", {})
            walk(body.get("schema"), f"{method.upper()} {path}")
    if not stripped:
        raise SpecFixError(
            "No PUT / PATCH request body declares an optional property with a default any more; "
            "the API stopped doing that, so delete fix_update_bodies_omit_unset_fields from scripts/prepare_spec.py."
        )


FIXES: tuple[Callable[[dict[str, Any]], None], ...] = (
    fix_agent_reaction_on_resolved_type,
    fix_update_bodies_omit_unset_fields,
)


# --------------------------------------------------------------------------------------
# Union order pinning
# --------------------------------------------------------------------------------------
def variant_ids(variants: list[Any]) -> list[str]:
    """A stable identity per variant: the ``$ref`` name, else ``inline:<type enum>#<n-th with that name>``.

    Inline variants have no name, so they are keyed by their ``type`` discriminator and occurrence
    (the two inline ``email`` previews are ``inline:email#0`` and ``inline:email#1``). Keying by content
    would make any field the API adds to a variant look like a brand-new variant and move it.
    """
    seen: Counter[str] = Counter()
    ids: list[str] = []
    for variant in variants:
        if isinstance(variant, dict) and "$ref" in variant:
            ids.append(str(variant["$ref"]).rsplit("/", 1)[-1])
            continue
        discriminator = ""
        if isinstance(variant, dict):
            enum = (variant.get("properties") or {}).get("type", {}).get("enum")
            if isinstance(enum, list):
                discriminator = ",".join(str(value) for value in enum)
        base = f"inline:{discriminator}"
        ids.append(f"{base}#{seen[base]}")
        seen[base] += 1
    return ids


def iter_unions(node: Any, path: tuple[str, ...] = ()) -> list[tuple[str, list[Any]]]:
    """Every ``oneOf`` / ``anyOf`` list in the document with a stable location string."""
    found: list[tuple[str, list[Any]]] = []
    if isinstance(node, dict):
        for key, value in node.items():
            if key in UNION_KEYS and isinstance(value, list):
                found.append((PATH_SEPARATOR.join((*path, key)), value))
            found.extend(iter_unions(value, (*path, key)))
    elif isinstance(node, list):
        for index, value in enumerate(node):
            found.extend(iter_unions(value, (*path, str(index))))
    return found


def current_union_order(spec: dict[str, Any]) -> dict[str, list[str]]:
    return {location: variant_ids(variants) for location, variants in iter_unions(spec)}


def pin_union_order(spec: dict[str, Any], pins: dict[str, list[str]]) -> dict[str, list[str]]:
    """Reorder every pinned union in place (pinned variants first, in pinned order; new ones appended).

    Returns the union order after pinning, which is what ``--update-pins`` writes back.
    """
    for location, variants in iter_unions(spec):
        pinned = pins.get(location)
        if pinned is None:
            continue
        ids = variant_ids(variants)
        rank = {variant_id: index for index, variant_id in enumerate(pinned)}
        order = sorted(range(len(variants)), key=lambda index: (rank.get(ids[index], len(pinned)), index))
        variants[:] = [variants[index] for index in order]
    return current_union_order(spec)


def prepare_spec(spec: dict[str, Any], pins: dict[str, list[str]] | None = None) -> dict[str, Any]:
    """Apply every fix and the union pinning in place and return the document."""
    for fix in FIXES:
        fix(spec)
    if pins is not None:
        pin_union_order(spec, pins)
    return spec


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("source", type=Path, help="committed OpenAPI document (openapi.json)")
    parser.add_argument("destination", type=Path, help="where to write the generator input")
    parser.add_argument("--pins", type=Path, help="union order file (scripts/union_order.json)")
    parser.add_argument(
        "--update-pins", action="store_true", help="rewrite --pins with the union order of this document"
    )
    args = parser.parse_args(argv)
    if args.update_pins and args.pins is None:
        parser.error("--update-pins needs --pins")

    spec = json.loads(args.source.read_text(encoding="utf-8"))
    pins = json.loads(args.pins.read_text(encoding="utf-8")) if args.pins and args.pins.exists() else None
    try:
        prepare_spec(spec, pins)
    except SpecFixError as error:
        print(f"error: {error}", file=sys.stderr)
        return 1
    args.destination.write_text(json.dumps(spec, indent=2), encoding="utf-8")
    if args.update_pins and args.pins is not None:
        args.pins.write_text(json.dumps(current_union_order(spec), indent=2) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
