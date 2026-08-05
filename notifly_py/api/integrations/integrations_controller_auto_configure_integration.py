from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.auto_configure_integration_response_dto import AutoConfigureIntegrationResponseDto
from ...models.error_dto import ErrorDto
from ...models.validation_error_dto import ValidationErrorDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    integration_id: str,
    *,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["idempotency-key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/integrations/{integration_id}/auto-configure".format(
            integration_id=quote(str(integration_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | AutoConfigureIntegrationResponseDto | ErrorDto | ValidationErrorDto | str | None:
    if response.status_code == 200:
        response_200 = AutoConfigureIntegrationResponseDto.from_dict(response.json())

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
        response_404 = cast(Any, None)
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
) -> Response[Any | AutoConfigureIntegrationResponseDto | ErrorDto | ValidationErrorDto | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    integration_id: str,
    *,
    client: AuthenticatedClient,
    idempotency_key: str | Unset = UNSET,
) -> Response[Any | AutoConfigureIntegrationResponseDto | ErrorDto | ValidationErrorDto | str]:
    """Auto-configure an integration for inbound webhooks

     Auto-configure an integration by its unique key identifier **integrationId** for inbound webhook
    support.
        This will automatically generate required webhook signing keys and configure webhook endpoints.
    Only integration metadata is returned, credentials field is returned as an empty object.

    Args:
        integration_id (str):
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | AutoConfigureIntegrationResponseDto | ErrorDto | ValidationErrorDto | str]
    """

    kwargs = _get_kwargs(
        integration_id=integration_id,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    integration_id: str,
    *,
    client: AuthenticatedClient,
    idempotency_key: str | Unset = UNSET,
) -> Any | AutoConfigureIntegrationResponseDto | ErrorDto | ValidationErrorDto | str | None:
    """Auto-configure an integration for inbound webhooks

     Auto-configure an integration by its unique key identifier **integrationId** for inbound webhook
    support.
        This will automatically generate required webhook signing keys and configure webhook endpoints.
    Only integration metadata is returned, credentials field is returned as an empty object.

    Args:
        integration_id (str):
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | AutoConfigureIntegrationResponseDto | ErrorDto | ValidationErrorDto | str
    """

    return sync_detailed(
        integration_id=integration_id,
        client=client,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    integration_id: str,
    *,
    client: AuthenticatedClient,
    idempotency_key: str | Unset = UNSET,
) -> Response[Any | AutoConfigureIntegrationResponseDto | ErrorDto | ValidationErrorDto | str]:
    """Auto-configure an integration for inbound webhooks

     Auto-configure an integration by its unique key identifier **integrationId** for inbound webhook
    support.
        This will automatically generate required webhook signing keys and configure webhook endpoints.
    Only integration metadata is returned, credentials field is returned as an empty object.

    Args:
        integration_id (str):
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | AutoConfigureIntegrationResponseDto | ErrorDto | ValidationErrorDto | str]
    """

    kwargs = _get_kwargs(
        integration_id=integration_id,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    integration_id: str,
    *,
    client: AuthenticatedClient,
    idempotency_key: str | Unset = UNSET,
) -> Any | AutoConfigureIntegrationResponseDto | ErrorDto | ValidationErrorDto | str | None:
    """Auto-configure an integration for inbound webhooks

     Auto-configure an integration by its unique key identifier **integrationId** for inbound webhook
    support.
        This will automatically generate required webhook signing keys and configure webhook endpoints.
    Only integration metadata is returned, credentials field is returned as an empty object.

    Args:
        integration_id (str):
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | AutoConfigureIntegrationResponseDto | ErrorDto | ValidationErrorDto | str
    """

    return (
        await asyncio_detailed(
            integration_id=integration_id,
            client=client,
            idempotency_key=idempotency_key,
        )
    ).parsed
