"""Auto-pagination across the three paging styles (PRD G5)."""

from __future__ import annotations

from typing import Any

from .conftest import json_response


def _subscriber(subscriber_id: str) -> dict[str, Any]:
    return {
        "_id": f"id_{subscriber_id}",
        "subscriberId": subscriber_id,
        "_organizationId": "org_1",
        "_environmentId": "env_1",
        "deleted": False,
        "createdAt": "2026-08-05T10:00:00.000Z",
        "updatedAt": "2026-08-05T10:00:00.000Z",
    }


def _subscriber_page(ids: list[str], next_cursor: str | None) -> dict[str, Any]:
    return {
        "data": [_subscriber(i) for i in ids],
        "next": next_cursor,
        "previous": None,
        "totalCount": 3,
        "totalCountCapped": False,
    }


def test_iter_all_walks_cursor_pages_and_flattens_items(notifly_factory: Any) -> None:
    notifly, recorder = notifly_factory(
        [
            json_response(200, _subscriber_page(["s_1", "s_2"], "cursor_2")),
            json_response(200, _subscriber_page(["s_3"], None)),
        ]
    )

    ids = [subscriber.subscriber_id for subscriber in notifly.subscribers.iter_all(limit=2)]

    assert ids == ["s_1", "s_2", "s_3"]
    assert recorder.call_count == 2
    assert recorder.requests[0].url.params["limit"] == "2"
    assert "after" not in recorder.requests[0].url.params
    assert recorder.requests[1].url.params["after"] == "cursor_2"


def test_iter_all_stops_at_max_pages(notifly_factory: Any) -> None:
    notifly, recorder = notifly_factory([json_response(200, _subscriber_page(["s_1"], "cursor_next"))])

    ids = [s.subscriber_id for s in notifly.subscribers.iter_all(limit=1, max_pages=2)]

    assert ids == ["s_1", "s_1"]
    assert recorder.call_count == 2


def test_iter_all_forwards_filters_to_every_page(notifly_factory: Any) -> None:
    notifly, recorder = notifly_factory(
        [
            json_response(200, _subscriber_page(["s_1"], "cursor_2")),
            json_response(200, _subscriber_page(["s_2"], None)),
        ]
    )

    list(notifly.subscribers.iter_all(limit=1, email="ada@example.com"))

    assert all(request.url.params["email"] == "ada@example.com" for request in recorder.requests)


async def test_async_iter_all_walks_cursor_pages(async_notifly_factory: Any) -> None:
    notifly, recorder = async_notifly_factory(
        [
            json_response(200, _subscriber_page(["s_1", "s_2"], "cursor_2")),
            json_response(200, _subscriber_page(["s_3"], None)),
        ]
    )

    ids = [subscriber.subscriber_id async for subscriber in notifly.subscribers.iter_all(limit=2)]

    assert ids == ["s_1", "s_2", "s_3"]
    assert recorder.call_count == 2


def test_topics_iteration_uses_the_same_cursor_contract(notifly_factory: Any) -> None:
    page_1 = {
        "data": [{"_id": "t1", "key": "product", "name": "Product"}],
        "next": "cursor_2",
        "previous": None,
        "totalCount": 2,
        "totalCountCapped": False,
    }
    page_2 = {
        "data": [{"_id": "t2", "key": "billing", "name": "Billing"}],
        "next": None,
        "previous": "cursor_1",
        "totalCount": 2,
        "totalCountCapped": False,
    }
    notifly, recorder = notifly_factory([json_response(200, page_1), json_response(200, page_2)])

    keys = [topic.key for topic in notifly.topics.iter_all(limit=1)]

    assert keys == ["product", "billing"]
    assert recorder.call_count == 2


def test_workflow_iteration_uses_offset_paging(notifly_factory: Any) -> None:
    def workflow(name: str) -> dict[str, Any]:
        return {
            "_id": f"wf_{name}",
            "workflowId": name,
            "slug": name,
            "name": name,
            "updatedAt": "2026-08-05T10:00:00.000Z",
            "createdAt": "2026-08-05T10:00:00.000Z",
            "status": "ACTIVE",
            "origin": "novu-cloud",
            "stepTypeOverviews": ["email"],
            "steps": [{"slug": f"{name}-step", "type": "email"}],
        }

    notifly, recorder = notifly_factory(
        [
            json_response(200, {"workflows": [workflow("a"), workflow("b")], "totalCount": 3}),
            json_response(200, {"workflows": [workflow("c")], "totalCount": 3}),
        ]
    )

    names = [wf.name for wf in notifly.workflows.iter_all(limit=2)]

    assert names == ["a", "b", "c"]
    assert recorder.requests[0].url.params["offset"] == "0"
    assert recorder.requests[1].url.params["offset"] == "2"


def test_message_iteration_uses_page_numbers_and_has_more(notifly_factory: Any) -> None:
    def message(message_id: str) -> dict[str, Any]:
        return {
            "_id": message_id,
            "_environmentId": "env_1",
            "_organizationId": "org_1",
            "_notificationId": "ntf_1",
            "_subscriberId": "sub_1",
            "createdAt": "2026-08-05T10:00:00.000Z",
            "transactionId": "txn_1",
            "channel": "email",
            "read": False,
            "seen": False,
            "cta": {},
            "status": "sent",
        }

    notifly, recorder = notifly_factory(
        [
            json_response(200, {"hasMore": True, "data": [message("m1")], "pageSize": 1, "page": 0}),
            json_response(200, {"hasMore": False, "data": [message("m2")], "pageSize": 1, "page": 1}),
        ]
    )

    ids = [m.field_id for m in notifly.messages.iter_all(limit=1)]

    assert ids == ["m1", "m2"]
    assert recorder.requests[0].url.params["page"] == "0"
    assert recorder.requests[1].url.params["page"] == "1"


def test_pagination_stops_on_a_repeated_cursor(notifly_factory: Any) -> None:
    """A server that keeps echoing the same cursor must not spin forever."""
    notifly, recorder = notifly_factory([json_response(200, _subscriber_page(["s_1"], "same"))])

    ids = [s.subscriber_id for s in notifly.subscribers.iter_all(limit=1)]

    assert ids == ["s_1", "s_1"]
    assert recorder.call_count == 2
