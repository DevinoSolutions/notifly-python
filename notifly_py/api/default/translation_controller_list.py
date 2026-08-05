from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_translation_groups_response_dto import ListTranslationGroupsResponseDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    query: str,
    limit: str,
    offset: str,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["idempotency-key"] = idempotency_key

    params: dict[str, Any] = {}

    params["query"] = query

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/translations/list",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ListTranslationGroupsResponseDto | None:
    if response.status_code == 200:
        response_200 = ListTranslationGroupsResponseDto.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ListTranslationGroupsResponseDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    query: str,
    limit: str,
    offset: str,
    idempotency_key: str | Unset = UNSET,
) -> Response[ListTranslationGroupsResponseDto]:
    """
    Args:
        query (str):
        limit (str):
        offset (str):
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListTranslationGroupsResponseDto]
    """

    kwargs = _get_kwargs(
        query=query,
        limit=limit,
        offset=offset,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    query: str,
    limit: str,
    offset: str,
    idempotency_key: str | Unset = UNSET,
) -> ListTranslationGroupsResponseDto | None:
    """
    Args:
        query (str):
        limit (str):
        offset (str):
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListTranslationGroupsResponseDto
    """

    return sync_detailed(
        client=client,
        query=query,
        limit=limit,
        offset=offset,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    query: str,
    limit: str,
    offset: str,
    idempotency_key: str | Unset = UNSET,
) -> Response[ListTranslationGroupsResponseDto]:
    """
    Args:
        query (str):
        limit (str):
        offset (str):
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListTranslationGroupsResponseDto]
    """

    kwargs = _get_kwargs(
        query=query,
        limit=limit,
        offset=offset,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    query: str,
    limit: str,
    offset: str,
    idempotency_key: str | Unset = UNSET,
) -> ListTranslationGroupsResponseDto | None:
    """
    Args:
        query (str):
        limit (str):
        offset (str):
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListTranslationGroupsResponseDto
    """

    return (
        await asyncio_detailed(
            client=client,
            query=query,
            limit=limit,
            offset=offset,
            idempotency_key=idempotency_key,
        )
    ).parsed
