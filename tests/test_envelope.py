"""Unit matrix for the envelope predicate and body rewriter.

These tests pin the exact contract the TypeScript SDK's runtime hook implements:
unwrap **only** a JSON object with exactly one key named ``data``.
"""

from __future__ import annotations

import json

import pytest

from notifly_py._envelope import is_enveloped, is_json_content_type, unwrap_body, unwrap_payload


@pytest.mark.parametrize(
    ("payload", "expected"),
    [
        ({"data": {"_id": "1"}}, True),
        ({"data": []}, True),
        ({"data": "string-value"}, True),
        ({"data": 0}, True),
        ({"data": False}, True),
        # paginated bodies keep their wrapper: more than one key
        ({"data": [], "totalCount": 0, "page": 0}, False),
        ({"data": [], "next": None, "previous": None}, False),
        # null data is never unwrapped: it would crash from_dict instead of losing fields
        ({"data": None}, False),
        ({}, False),
        ({"acknowledged": True}, False),
        ([{"data": 1}], False),
        ("data", False),
        (None, False),
    ],
)
def test_is_enveloped_matches_the_single_key_data_contract(payload: object, expected: bool) -> None:
    assert is_enveloped(payload) is expected


def test_unwrap_payload_returns_envelope_contents() -> None:
    assert unwrap_payload({"data": {"_id": "abc"}}) == {"_id": "abc"}


def test_unwrap_payload_passes_non_envelopes_through_unchanged() -> None:
    paginated = {"data": [1, 2], "totalCount": 2}
    assert unwrap_payload(paginated) is paginated


def test_unwrap_body_rewrites_single_entity_envelopes() -> None:
    rewritten = unwrap_body(json.dumps({"data": {"acknowledged": True}}).encode())
    assert rewritten is not None
    assert json.loads(rewritten) == {"acknowledged": True}


@pytest.mark.parametrize(
    "content",
    [
        b"",
        b"not json at all",
        b"<html><body>502 Bad Gateway</body></html>",
        json.dumps({"data": [1], "totalCount": 1}).encode(),
        json.dumps([1, 2, 3]).encode(),
        json.dumps({"data": None}).encode(),
        b'{"truncated": ',
    ],
)
def test_unwrap_body_returns_none_when_the_body_must_not_change(content: bytes) -> None:
    assert unwrap_body(content) is None


def test_unwrap_body_preserves_unicode() -> None:
    rewritten = unwrap_body(json.dumps({"data": {"name": "Ada Löve"}}).encode())
    assert rewritten is not None
    assert json.loads(rewritten)["name"] == "Ada Löve"


@pytest.mark.parametrize(
    ("content_type", "expected"),
    [
        ("application/json", True),
        ("application/json; charset=utf-8", True),
        ("application/problem+json", True),
        ("text/json", True),
        ("APPLICATION/JSON", True),
        ("text/html; charset=utf-8", False),
        ("application/octet-stream", False),
        ("text/csv", False),
        ("", False),
        (None, False),
    ],
)
def test_is_json_content_type(content_type: str | None, expected: bool) -> None:
    assert is_json_content_type(content_type) is expected
