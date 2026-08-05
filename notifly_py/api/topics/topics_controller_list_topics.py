from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_dto import ErrorDto
from ...models.list_topics_response_dto import ListTopicsResponseDto
from ...models.topics_controller_list_topics_order_direction import TopicsControllerListTopicsOrderDirection
from ...models.validation_error_dto import ValidationErrorDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    after: str | Unset = UNSET,
    before: str | Unset = UNSET,
    limit: float | Unset = UNSET,
    order_direction: TopicsControllerListTopicsOrderDirection | Unset = UNSET,
    order_by: str | Unset = UNSET,
    include_cursor: bool | Unset = UNSET,
    key: str | Unset = UNSET,
    name: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["idempotency-key"] = idempotency_key

    params: dict[str, Any] = {}

    params["after"] = after

    params["before"] = before

    params["limit"] = limit

    json_order_direction: str | Unset = UNSET
    if not isinstance(order_direction, Unset):
        json_order_direction = order_direction.value

    params["orderDirection"] = json_order_direction

    params["orderBy"] = order_by

    params["includeCursor"] = include_cursor

    params["key"] = key

    params["name"] = name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/topics",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorDto | ListTopicsResponseDto | ValidationErrorDto | str | None:
    if response.status_code == 200:
        response_200 = ListTopicsResponseDto.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorDto.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorDto.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ErrorDto.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ErrorDto.from_dict(response.json())

        return response_404

    if response.status_code == 405:
        response_405 = ErrorDto.from_dict(response.json())

        return response_405

    if response.status_code == 409:
        response_409 = ErrorDto.from_dict(response.json())

        return response_409

    if response.status_code == 413:
        response_413 = ErrorDto.from_dict(response.json())

        return response_413

    if response.status_code == 414:
        response_414 = ErrorDto.from_dict(response.json())

        return response_414

    if response.status_code == 415:
        response_415 = ErrorDto.from_dict(response.json())

        return response_415

    if response.status_code == 422:
        response_422 = ValidationErrorDto.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = cast(str, response.json())
        return response_429

    if response.status_code == 500:
        response_500 = ErrorDto.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = cast(str, response.json())
        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorDto | ListTopicsResponseDto | ValidationErrorDto | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    after: str | Unset = UNSET,
    before: str | Unset = UNSET,
    limit: float | Unset = UNSET,
    order_direction: TopicsControllerListTopicsOrderDirection | Unset = UNSET,
    order_by: str | Unset = UNSET,
    include_cursor: bool | Unset = UNSET,
    key: str | Unset = UNSET,
    name: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> Response[ErrorDto | ListTopicsResponseDto | ValidationErrorDto | str]:
    """List all topics

     This api returns a paginated list of topics.
        Topics can be filtered by **key**, **name**, or **includeCursor** to paginate through the list.
        Checkout all available filters in the query section.

    Args:
        after (str | Unset):
        before (str | Unset):
        limit (float | Unset):
        order_direction (TopicsControllerListTopicsOrderDirection | Unset):
        order_by (str | Unset):
        include_cursor (bool | Unset):
        key (str | Unset):
        name (str | Unset):
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorDto | ListTopicsResponseDto | ValidationErrorDto | str]
    """

    kwargs = _get_kwargs(
        after=after,
        before=before,
        limit=limit,
        order_direction=order_direction,
        order_by=order_by,
        include_cursor=include_cursor,
        key=key,
        name=name,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    after: str | Unset = UNSET,
    before: str | Unset = UNSET,
    limit: float | Unset = UNSET,
    order_direction: TopicsControllerListTopicsOrderDirection | Unset = UNSET,
    order_by: str | Unset = UNSET,
    include_cursor: bool | Unset = UNSET,
    key: str | Unset = UNSET,
    name: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> ErrorDto | ListTopicsResponseDto | ValidationErrorDto | str | None:
    """List all topics

     This api returns a paginated list of topics.
        Topics can be filtered by **key**, **name**, or **includeCursor** to paginate through the list.
        Checkout all available filters in the query section.

    Args:
        after (str | Unset):
        before (str | Unset):
        limit (float | Unset):
        order_direction (TopicsControllerListTopicsOrderDirection | Unset):
        order_by (str | Unset):
        include_cursor (bool | Unset):
        key (str | Unset):
        name (str | Unset):
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorDto | ListTopicsResponseDto | ValidationErrorDto | str
    """

    return sync_detailed(
        client=client,
        after=after,
        before=before,
        limit=limit,
        order_direction=order_direction,
        order_by=order_by,
        include_cursor=include_cursor,
        key=key,
        name=name,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    after: str | Unset = UNSET,
    before: str | Unset = UNSET,
    limit: float | Unset = UNSET,
    order_direction: TopicsControllerListTopicsOrderDirection | Unset = UNSET,
    order_by: str | Unset = UNSET,
    include_cursor: bool | Unset = UNSET,
    key: str | Unset = UNSET,
    name: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> Response[ErrorDto | ListTopicsResponseDto | ValidationErrorDto | str]:
    """List all topics

     This api returns a paginated list of topics.
        Topics can be filtered by **key**, **name**, or **includeCursor** to paginate through the list.
        Checkout all available filters in the query section.

    Args:
        after (str | Unset):
        before (str | Unset):
        limit (float | Unset):
        order_direction (TopicsControllerListTopicsOrderDirection | Unset):
        order_by (str | Unset):
        include_cursor (bool | Unset):
        key (str | Unset):
        name (str | Unset):
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorDto | ListTopicsResponseDto | ValidationErrorDto | str]
    """

    kwargs = _get_kwargs(
        after=after,
        before=before,
        limit=limit,
        order_direction=order_direction,
        order_by=order_by,
        include_cursor=include_cursor,
        key=key,
        name=name,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    after: str | Unset = UNSET,
    before: str | Unset = UNSET,
    limit: float | Unset = UNSET,
    order_direction: TopicsControllerListTopicsOrderDirection | Unset = UNSET,
    order_by: str | Unset = UNSET,
    include_cursor: bool | Unset = UNSET,
    key: str | Unset = UNSET,
    name: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> ErrorDto | ListTopicsResponseDto | ValidationErrorDto | str | None:
    """List all topics

     This api returns a paginated list of topics.
        Topics can be filtered by **key**, **name**, or **includeCursor** to paginate through the list.
        Checkout all available filters in the query section.

    Args:
        after (str | Unset):
        before (str | Unset):
        limit (float | Unset):
        order_direction (TopicsControllerListTopicsOrderDirection | Unset):
        order_by (str | Unset):
        include_cursor (bool | Unset):
        key (str | Unset):
        name (str | Unset):
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorDto | ListTopicsResponseDto | ValidationErrorDto | str
    """

    return (
        await asyncio_detailed(
            client=client,
            after=after,
            before=before,
            limit=limit,
            order_direction=order_direction,
            order_by=order_by,
            include_cursor=include_cursor,
            key=key,
            name=name,
            idempotency_key=idempotency_key,
        )
    ).parsed
