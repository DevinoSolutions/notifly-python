from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_dto import ErrorDto
from ...models.get_layout_usage_response_dto import GetLayoutUsageResponseDto
from ...models.validation_error_dto import ValidationErrorDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    layout_id: str,
    *,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["idempotency-key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/layouts/{layout_id}/usage".format(
            layout_id=quote(str(layout_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorDto | GetLayoutUsageResponseDto | ValidationErrorDto | str | None:
    if response.status_code == 200:
        response_200 = GetLayoutUsageResponseDto.from_dict(response.json())

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
) -> Response[ErrorDto | GetLayoutUsageResponseDto | ValidationErrorDto | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    layout_id: str,
    *,
    client: AuthenticatedClient,
    idempotency_key: str | Unset = UNSET,
) -> Response[ErrorDto | GetLayoutUsageResponseDto | ValidationErrorDto | str]:
    """Get layout usage

     Retrieves information about workflows that use the specified layout by its unique identifier
    **layoutId**

    Args:
        layout_id (str):
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorDto | GetLayoutUsageResponseDto | ValidationErrorDto | str]
    """

    kwargs = _get_kwargs(
        layout_id=layout_id,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    layout_id: str,
    *,
    client: AuthenticatedClient,
    idempotency_key: str | Unset = UNSET,
) -> ErrorDto | GetLayoutUsageResponseDto | ValidationErrorDto | str | None:
    """Get layout usage

     Retrieves information about workflows that use the specified layout by its unique identifier
    **layoutId**

    Args:
        layout_id (str):
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorDto | GetLayoutUsageResponseDto | ValidationErrorDto | str
    """

    return sync_detailed(
        layout_id=layout_id,
        client=client,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    layout_id: str,
    *,
    client: AuthenticatedClient,
    idempotency_key: str | Unset = UNSET,
) -> Response[ErrorDto | GetLayoutUsageResponseDto | ValidationErrorDto | str]:
    """Get layout usage

     Retrieves information about workflows that use the specified layout by its unique identifier
    **layoutId**

    Args:
        layout_id (str):
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorDto | GetLayoutUsageResponseDto | ValidationErrorDto | str]
    """

    kwargs = _get_kwargs(
        layout_id=layout_id,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    layout_id: str,
    *,
    client: AuthenticatedClient,
    idempotency_key: str | Unset = UNSET,
) -> ErrorDto | GetLayoutUsageResponseDto | ValidationErrorDto | str | None:
    """Get layout usage

     Retrieves information about workflows that use the specified layout by its unique identifier
    **layoutId**

    Args:
        layout_id (str):
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorDto | GetLayoutUsageResponseDto | ValidationErrorDto | str
    """

    return (
        await asyncio_detailed(
            layout_id=layout_id,
            client=client,
            idempotency_key=idempotency_key,
        )
    ).parsed
