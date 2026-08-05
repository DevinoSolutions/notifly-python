from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.translation_response_dto import TranslationResponseDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    resource_type: str,
    resource_id: str,
    locale: str,
    *,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["idempotency-key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/translations/{resource_type}/{resource_id}/{locale}".format(
            resource_type=quote(str(resource_type), safe=""),
            resource_id=quote(str(resource_id), safe=""),
            locale=quote(str(locale), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> TranslationResponseDto | None:
    if response.status_code == 200:
        response_200 = TranslationResponseDto.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[TranslationResponseDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    resource_type: str,
    resource_id: str,
    locale: str,
    *,
    client: AuthenticatedClient,
    idempotency_key: str | Unset = UNSET,
) -> Response[TranslationResponseDto]:
    """
    Args:
        resource_type (str):
        resource_id (str):
        locale (str):
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TranslationResponseDto]
    """

    kwargs = _get_kwargs(
        resource_type=resource_type,
        resource_id=resource_id,
        locale=locale,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    resource_type: str,
    resource_id: str,
    locale: str,
    *,
    client: AuthenticatedClient,
    idempotency_key: str | Unset = UNSET,
) -> TranslationResponseDto | None:
    """
    Args:
        resource_type (str):
        resource_id (str):
        locale (str):
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TranslationResponseDto
    """

    return sync_detailed(
        resource_type=resource_type,
        resource_id=resource_id,
        locale=locale,
        client=client,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    resource_type: str,
    resource_id: str,
    locale: str,
    *,
    client: AuthenticatedClient,
    idempotency_key: str | Unset = UNSET,
) -> Response[TranslationResponseDto]:
    """
    Args:
        resource_type (str):
        resource_id (str):
        locale (str):
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TranslationResponseDto]
    """

    kwargs = _get_kwargs(
        resource_type=resource_type,
        resource_id=resource_id,
        locale=locale,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    resource_type: str,
    resource_id: str,
    locale: str,
    *,
    client: AuthenticatedClient,
    idempotency_key: str | Unset = UNSET,
) -> TranslationResponseDto | None:
    """
    Args:
        resource_type (str):
        resource_id (str):
        locale (str):
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TranslationResponseDto
    """

    return (
        await asyncio_detailed(
            resource_type=resource_type,
            resource_id=resource_id,
            locale=locale,
            client=client,
            idempotency_key=idempotency_key,
        )
    ).parsed
