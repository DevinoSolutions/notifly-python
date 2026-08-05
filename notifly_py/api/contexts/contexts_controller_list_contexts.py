from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.contexts_controller_list_contexts_order_direction import ContextsControllerListContextsOrderDirection
from ...models.error_dto import ErrorDto
from ...models.list_contexts_response_dto import ListContextsResponseDto
from ...models.validation_error_dto import ValidationErrorDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    after: str | Unset = UNSET,
    before: str | Unset = UNSET,
    limit: float | Unset = UNSET,
    order_direction: ContextsControllerListContextsOrderDirection | Unset = UNSET,
    order_by: str | Unset = UNSET,
    include_cursor: bool | Unset = UNSET,
    type_: str | Unset = UNSET,
    id: str | Unset = UNSET,
    search: str | Unset = UNSET,
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

    params["type"] = type_

    params["id"] = id

    params["search"] = search

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/contexts",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorDto | ListContextsResponseDto | ValidationErrorDto | str | None:
    if response.status_code == 200:
        response_200 = ListContextsResponseDto.from_dict(response.json())

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
) -> Response[ErrorDto | ListContextsResponseDto | ValidationErrorDto | str]:
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
    order_direction: ContextsControllerListContextsOrderDirection | Unset = UNSET,
    order_by: str | Unset = UNSET,
    include_cursor: bool | Unset = UNSET,
    type_: str | Unset = UNSET,
    id: str | Unset = UNSET,
    search: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> Response[ErrorDto | ListContextsResponseDto | ValidationErrorDto | str]:
    """List all contexts

     Retrieve a paginated list of all contexts, optionally filtered by type and key pattern.
          **type** and **id** are optional fields, if provided, only contexts with the matching type and
    id will be returned.
          **search** is an optional field, if provided, only contexts with the matching key pattern will
    be returned.
          Checkout all possible parameters in the query section below for more details

    Args:
        after (str | Unset):
        before (str | Unset):
        limit (float | Unset):
        order_direction (ContextsControllerListContextsOrderDirection | Unset):
        order_by (str | Unset):
        include_cursor (bool | Unset):
        type_ (str | Unset):
        id (str | Unset):
        search (str | Unset):
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorDto | ListContextsResponseDto | ValidationErrorDto | str]
    """

    kwargs = _get_kwargs(
        after=after,
        before=before,
        limit=limit,
        order_direction=order_direction,
        order_by=order_by,
        include_cursor=include_cursor,
        type_=type_,
        id=id,
        search=search,
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
    order_direction: ContextsControllerListContextsOrderDirection | Unset = UNSET,
    order_by: str | Unset = UNSET,
    include_cursor: bool | Unset = UNSET,
    type_: str | Unset = UNSET,
    id: str | Unset = UNSET,
    search: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> ErrorDto | ListContextsResponseDto | ValidationErrorDto | str | None:
    """List all contexts

     Retrieve a paginated list of all contexts, optionally filtered by type and key pattern.
          **type** and **id** are optional fields, if provided, only contexts with the matching type and
    id will be returned.
          **search** is an optional field, if provided, only contexts with the matching key pattern will
    be returned.
          Checkout all possible parameters in the query section below for more details

    Args:
        after (str | Unset):
        before (str | Unset):
        limit (float | Unset):
        order_direction (ContextsControllerListContextsOrderDirection | Unset):
        order_by (str | Unset):
        include_cursor (bool | Unset):
        type_ (str | Unset):
        id (str | Unset):
        search (str | Unset):
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorDto | ListContextsResponseDto | ValidationErrorDto | str
    """

    return sync_detailed(
        client=client,
        after=after,
        before=before,
        limit=limit,
        order_direction=order_direction,
        order_by=order_by,
        include_cursor=include_cursor,
        type_=type_,
        id=id,
        search=search,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    after: str | Unset = UNSET,
    before: str | Unset = UNSET,
    limit: float | Unset = UNSET,
    order_direction: ContextsControllerListContextsOrderDirection | Unset = UNSET,
    order_by: str | Unset = UNSET,
    include_cursor: bool | Unset = UNSET,
    type_: str | Unset = UNSET,
    id: str | Unset = UNSET,
    search: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> Response[ErrorDto | ListContextsResponseDto | ValidationErrorDto | str]:
    """List all contexts

     Retrieve a paginated list of all contexts, optionally filtered by type and key pattern.
          **type** and **id** are optional fields, if provided, only contexts with the matching type and
    id will be returned.
          **search** is an optional field, if provided, only contexts with the matching key pattern will
    be returned.
          Checkout all possible parameters in the query section below for more details

    Args:
        after (str | Unset):
        before (str | Unset):
        limit (float | Unset):
        order_direction (ContextsControllerListContextsOrderDirection | Unset):
        order_by (str | Unset):
        include_cursor (bool | Unset):
        type_ (str | Unset):
        id (str | Unset):
        search (str | Unset):
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorDto | ListContextsResponseDto | ValidationErrorDto | str]
    """

    kwargs = _get_kwargs(
        after=after,
        before=before,
        limit=limit,
        order_direction=order_direction,
        order_by=order_by,
        include_cursor=include_cursor,
        type_=type_,
        id=id,
        search=search,
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
    order_direction: ContextsControllerListContextsOrderDirection | Unset = UNSET,
    order_by: str | Unset = UNSET,
    include_cursor: bool | Unset = UNSET,
    type_: str | Unset = UNSET,
    id: str | Unset = UNSET,
    search: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> ErrorDto | ListContextsResponseDto | ValidationErrorDto | str | None:
    """List all contexts

     Retrieve a paginated list of all contexts, optionally filtered by type and key pattern.
          **type** and **id** are optional fields, if provided, only contexts with the matching type and
    id will be returned.
          **search** is an optional field, if provided, only contexts with the matching key pattern will
    be returned.
          Checkout all possible parameters in the query section below for more details

    Args:
        after (str | Unset):
        before (str | Unset):
        limit (float | Unset):
        order_direction (ContextsControllerListContextsOrderDirection | Unset):
        order_by (str | Unset):
        include_cursor (bool | Unset):
        type_ (str | Unset):
        id (str | Unset):
        search (str | Unset):
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorDto | ListContextsResponseDto | ValidationErrorDto | str
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
            type_=type_,
            id=id,
            search=search,
            idempotency_key=idempotency_key,
        )
    ).parsed
