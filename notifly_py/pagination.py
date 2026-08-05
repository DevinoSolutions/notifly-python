"""Auto-pagination helpers over the three paging styles the Notifly API uses.

HAND-WRITTEN — not produced by ``openapi-python-client``. See ``scripts/regenerate.sh``.

============  ===========================================  ==============================
Style         Request params                               Response shape
============  ===========================================  ==============================
cursor        ``after`` / ``limit``                        ``data`` + ``next_`` cursor
offset        ``offset`` / ``limit``                       named list + ``total_count``
page-number   ``page`` / ``limit``                         ``data`` + ``has_more``
============  ===========================================  ==============================

Each helper takes a ``fetch`` callable that performs a single page request and returns the
parsed page model, and yields the individual items across pages. The facade
(:mod:`notifly_py.facade`) wires these up as ``iter_*`` methods, so most callers never touch
this module directly.
"""

from __future__ import annotations

from collections.abc import AsyncIterator, Awaitable, Callable, Iterator
from typing import Any

from .types import Unset

DEFAULT_PAGE_SIZE = 50


def _plain(value: Any) -> Any:
    return None if isinstance(value, Unset) else value


def _items(page: Any, items_attr: str) -> list[Any]:
    items = _plain(getattr(page, items_attr, None))
    return list(items) if isinstance(items, list) else []


def _has_more(page: Any, items: list[Any], limit: int) -> bool:
    has_more = _plain(getattr(page, "has_more", None))
    if isinstance(has_more, bool):
        return has_more
    return len(items) >= limit


def _cursor_params(limit: int | None, cursor: str | None) -> dict[str, Any]:
    params: dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    if cursor is not None:
        params["after"] = cursor
    return params


def iterate_cursor(
    fetch: Callable[..., Any],
    *,
    limit: int | None = DEFAULT_PAGE_SIZE,
    after: str | None = None,
    max_pages: int | None = None,
    items_attr: str = "data",
    cursor_attr: str = "next_",
) -> Iterator[Any]:
    """Yield every item of a cursor-paginated endpoint (``after``/``next``)."""
    cursor, pages, seen = after, 0, set()
    while True:
        page = fetch(**_cursor_params(limit, cursor))
        yield from _items(page, items_attr)
        pages += 1
        cursor = _plain(getattr(page, cursor_attr, None))
        if not cursor or cursor in seen or (max_pages is not None and pages >= max_pages):
            return
        seen.add(cursor)


async def aiterate_cursor(
    fetch: Callable[..., Awaitable[Any]],
    *,
    limit: int | None = DEFAULT_PAGE_SIZE,
    after: str | None = None,
    max_pages: int | None = None,
    items_attr: str = "data",
    cursor_attr: str = "next_",
) -> AsyncIterator[Any]:
    """Async twin of :func:`iterate_cursor`."""
    cursor, pages, seen = after, 0, set()
    while True:
        page = await fetch(**_cursor_params(limit, cursor))
        for item in _items(page, items_attr):
            yield item
        pages += 1
        cursor = _plain(getattr(page, cursor_attr, None))
        if not cursor or cursor in seen or (max_pages is not None and pages >= max_pages):
            return
        seen.add(cursor)


def iterate_offset(
    fetch: Callable[..., Any],
    *,
    limit: int = DEFAULT_PAGE_SIZE,
    offset: int = 0,
    max_pages: int | None = None,
    items_attr: str = "data",
) -> Iterator[Any]:
    """Yield every item of an ``offset``/``limit`` endpoint."""
    pages = 0
    while True:
        page = fetch(limit=limit, offset=offset)
        items = _items(page, items_attr)
        yield from items
        pages += 1
        offset += len(items)
        if len(items) < limit or not items or (max_pages is not None and pages >= max_pages):
            return


async def aiterate_offset(
    fetch: Callable[..., Awaitable[Any]],
    *,
    limit: int = DEFAULT_PAGE_SIZE,
    offset: int = 0,
    max_pages: int | None = None,
    items_attr: str = "data",
) -> AsyncIterator[Any]:
    """Async twin of :func:`iterate_offset`."""
    pages = 0
    while True:
        page = await fetch(limit=limit, offset=offset)
        items = _items(page, items_attr)
        for item in items:
            yield item
        pages += 1
        offset += len(items)
        if len(items) < limit or not items or (max_pages is not None and pages >= max_pages):
            return


def iterate_pages(
    fetch: Callable[..., Any],
    *,
    limit: int = DEFAULT_PAGE_SIZE,
    page: int = 0,
    max_pages: int | None = None,
    items_attr: str = "data",
) -> Iterator[Any]:
    """Yield every item of a page-number endpoint (``page``/``limit`` + ``has_more``)."""
    pages = 0
    while True:
        result = fetch(page=page, limit=limit)
        items = _items(result, items_attr)
        yield from items
        pages += 1
        if not _has_more(result, items, limit) or not items or (max_pages is not None and pages >= max_pages):
            return
        page += 1


async def aiterate_pages(
    fetch: Callable[..., Awaitable[Any]],
    *,
    limit: int = DEFAULT_PAGE_SIZE,
    page: int = 0,
    max_pages: int | None = None,
    items_attr: str = "data",
) -> AsyncIterator[Any]:
    """Async twin of :func:`iterate_pages`."""
    pages = 0
    while True:
        result = await fetch(page=page, limit=limit)
        items = _items(result, items_attr)
        for item in items:
            yield item
        pages += 1
        if not _has_more(result, items, limit) or not items or (max_pages is not None and pages >= max_pages):
            return
        page += 1


__all__ = [
    "DEFAULT_PAGE_SIZE",
    "aiterate_cursor",
    "aiterate_offset",
    "aiterate_pages",
    "iterate_cursor",
    "iterate_offset",
    "iterate_pages",
]
