from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.activity_controller_get_logs_source import ActivityControllerGetLogsSource
from ...models.get_requests_response_dto import GetRequestsResponseDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: float | Unset = UNSET,
    limit: float | Unset = UNSET,
    status_codes: list[float] | Unset = UNSET,
    url_pattern: str | Unset = UNSET,
    transaction_id: str | Unset = UNSET,
    created_gte: float | Unset = UNSET,
    source: ActivityControllerGetLogsSource | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["idempotency-key"] = idempotency_key

    params: dict[str, Any] = {}

    params["page"] = page

    params["limit"] = limit

    json_status_codes: list[float] | Unset = UNSET
    if not isinstance(status_codes, Unset):
        json_status_codes = status_codes

    params["statusCodes"] = json_status_codes

    params["urlPattern"] = url_pattern

    params["transactionId"] = transaction_id

    params["createdGte"] = created_gte

    json_source: str | Unset = UNSET
    if not isinstance(source, Unset):
        json_source = source.value

    params["source"] = json_source

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/activity/requests",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetRequestsResponseDto | None:
    if response.status_code == 200:
        response_200 = GetRequestsResponseDto.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetRequestsResponseDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    page: float | Unset = UNSET,
    limit: float | Unset = UNSET,
    status_codes: list[float] | Unset = UNSET,
    url_pattern: str | Unset = UNSET,
    transaction_id: str | Unset = UNSET,
    created_gte: float | Unset = UNSET,
    source: ActivityControllerGetLogsSource | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> Response[GetRequestsResponseDto]:
    """List activity requests

     Retrieve a list of activity requests with optional filtering and pagination.

    Args:
        page (float | Unset):
        limit (float | Unset):
        status_codes (list[float] | Unset):
        url_pattern (str | Unset):
        transaction_id (str | Unset):
        created_gte (float | Unset):
        source (ActivityControllerGetLogsSource | Unset):
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetRequestsResponseDto]
    """

    kwargs = _get_kwargs(
        page=page,
        limit=limit,
        status_codes=status_codes,
        url_pattern=url_pattern,
        transaction_id=transaction_id,
        created_gte=created_gte,
        source=source,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    page: float | Unset = UNSET,
    limit: float | Unset = UNSET,
    status_codes: list[float] | Unset = UNSET,
    url_pattern: str | Unset = UNSET,
    transaction_id: str | Unset = UNSET,
    created_gte: float | Unset = UNSET,
    source: ActivityControllerGetLogsSource | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> GetRequestsResponseDto | None:
    """List activity requests

     Retrieve a list of activity requests with optional filtering and pagination.

    Args:
        page (float | Unset):
        limit (float | Unset):
        status_codes (list[float] | Unset):
        url_pattern (str | Unset):
        transaction_id (str | Unset):
        created_gte (float | Unset):
        source (ActivityControllerGetLogsSource | Unset):
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetRequestsResponseDto
    """

    return sync_detailed(
        client=client,
        page=page,
        limit=limit,
        status_codes=status_codes,
        url_pattern=url_pattern,
        transaction_id=transaction_id,
        created_gte=created_gte,
        source=source,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    page: float | Unset = UNSET,
    limit: float | Unset = UNSET,
    status_codes: list[float] | Unset = UNSET,
    url_pattern: str | Unset = UNSET,
    transaction_id: str | Unset = UNSET,
    created_gte: float | Unset = UNSET,
    source: ActivityControllerGetLogsSource | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> Response[GetRequestsResponseDto]:
    """List activity requests

     Retrieve a list of activity requests with optional filtering and pagination.

    Args:
        page (float | Unset):
        limit (float | Unset):
        status_codes (list[float] | Unset):
        url_pattern (str | Unset):
        transaction_id (str | Unset):
        created_gte (float | Unset):
        source (ActivityControllerGetLogsSource | Unset):
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetRequestsResponseDto]
    """

    kwargs = _get_kwargs(
        page=page,
        limit=limit,
        status_codes=status_codes,
        url_pattern=url_pattern,
        transaction_id=transaction_id,
        created_gte=created_gte,
        source=source,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    page: float | Unset = UNSET,
    limit: float | Unset = UNSET,
    status_codes: list[float] | Unset = UNSET,
    url_pattern: str | Unset = UNSET,
    transaction_id: str | Unset = UNSET,
    created_gte: float | Unset = UNSET,
    source: ActivityControllerGetLogsSource | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> GetRequestsResponseDto | None:
    """List activity requests

     Retrieve a list of activity requests with optional filtering and pagination.

    Args:
        page (float | Unset):
        limit (float | Unset):
        status_codes (list[float] | Unset):
        url_pattern (str | Unset):
        transaction_id (str | Unset):
        created_gte (float | Unset):
        source (ActivityControllerGetLogsSource | Unset):
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetRequestsResponseDto
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            limit=limit,
            status_codes=status_codes,
            url_pattern=url_pattern,
            transaction_id=transaction_id,
            created_gte=created_gte,
            source=source,
            idempotency_key=idempotency_key,
        )
    ).parsed
