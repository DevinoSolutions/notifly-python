"""Runtime handling of the Notifly ``{"data": ...}`` response envelope.

HAND-WRITTEN — not produced by ``openapi-python-client``. See ``scripts/regenerate.sh``.

Why this module exists
----------------------
The Notifly API wraps every response body at runtime::

    single entity  -> {"data": {...}}                       # exactly one key
    paginated      -> {"data": [...], "totalCount": 1, ...}  # several keys

The OpenAPI document the SDK is generated from is the *internal SDK* flavor, which runs
``unwrapDataAttribute()`` and therefore describes the **unwrapped** payload. The generated
code consequently calls ``Model.from_dict(response.json())`` with the *enveloped* body.
Because generated attrs models tolerate unknown keys through ``additional_properties``,
that does not raise — it silently returns a model whose documented fields are all ``UNSET``
and whose real payload is buried in ``additional_properties["data"]``.

The official TypeScript SDK (``@notiflyio/api``) compensates with a runtime response hook::

    if (jsonResponse && Object.keys(jsonResponse).length === 1 && 'data' in jsonResponse) {
        return new Response(JSON.stringify(jsonResponse.data), { ... });
    }

This module is the Python equivalent, installed as an httpx transport layer
(:mod:`notifly_py._transport`) so that it applies to all operations without editing a
single generated file.

Contract
--------
A body is unwrapped **only** when it is a JSON object with exactly one key, ``data``,
whose value is not ``null``. Everything else — paginated bodies, bare arrays, scalars,
empty bodies, non-JSON bodies — is passed through byte-for-byte.
"""

from __future__ import annotations

import json
from typing import Any

DATA_KEY = "data"
"""The envelope key added by the API's response interceptor."""


def is_enveloped(payload: Any) -> bool:
    """Return ``True`` when ``payload`` is a single-entity ``{"data": ...}`` envelope.

    ``{"data": None}`` is deliberately **not** treated as an envelope: unwrapping it would
    hand ``None`` to a generated ``from_dict`` and turn silent data loss into a crash.
    """
    return (
        isinstance(payload, dict) and len(payload) == 1 and DATA_KEY in payload and payload[DATA_KEY] is not None
    )


def unwrap_payload(payload: Any) -> Any:
    """Return the envelope's contents, or ``payload`` unchanged when it is not an envelope."""
    return payload[DATA_KEY] if is_enveloped(payload) else payload


def unwrap_body(content: bytes) -> bytes | None:
    """Return rewritten body bytes, or ``None`` when the body must be left untouched.

    ``None`` (rather than the original bytes) is returned for the pass-through case so that
    callers can avoid rebuilding a response they do not need to change.
    """
    if not content:
        return None
    try:
        payload = json.loads(content)
    except (ValueError, UnicodeDecodeError):
        return None
    if not is_enveloped(payload):
        return None
    return json.dumps(payload[DATA_KEY], separators=(",", ":")).encode("utf-8")


def is_json_content_type(content_type: str | None) -> bool:
    """Return ``True`` for ``application/json`` and friends (``+json`` suffixes included)."""
    if not content_type:
        return False
    media_type = content_type.split(";", 1)[0].strip().lower()
    return media_type == "application/json" or media_type.endswith("+json") or media_type == "text/json"


__all__ = ["DATA_KEY", "is_enveloped", "is_json_content_type", "unwrap_body", "unwrap_payload"]
