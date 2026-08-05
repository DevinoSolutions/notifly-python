from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_ms_teams_channel_endpoint_dto import CreateMsTeamsChannelEndpointDto
from ...models.create_ms_teams_user_endpoint_dto import CreateMsTeamsUserEndpointDto
from ...models.create_phone_endpoint_dto import CreatePhoneEndpointDto
from ...models.create_slack_channel_endpoint_dto import CreateSlackChannelEndpointDto
from ...models.create_slack_user_endpoint_dto import CreateSlackUserEndpointDto
from ...models.create_telegram_chat_endpoint_dto import CreateTelegramChatEndpointDto
from ...models.create_webhook_endpoint_dto import CreateWebhookEndpointDto
from ...models.error_dto import ErrorDto
from ...models.get_channel_endpoint_response_dto import GetChannelEndpointResponseDto
from ...models.validation_error_dto import ValidationErrorDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CreateMsTeamsChannelEndpointDto
    | CreateMsTeamsUserEndpointDto
    | CreatePhoneEndpointDto
    | CreateSlackChannelEndpointDto
    | CreateSlackUserEndpointDto
    | CreateTelegramChatEndpointDto
    | CreateWebhookEndpointDto,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["idempotency-key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/channel-endpoints",
    }

    if isinstance(body, CreateSlackChannelEndpointDto):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, CreateSlackUserEndpointDto):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, CreateWebhookEndpointDto):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, CreatePhoneEndpointDto):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, CreateMsTeamsChannelEndpointDto):
        _kwargs["json"] = body.to_dict()
    elif isinstance(body, CreateMsTeamsUserEndpointDto):
        _kwargs["json"] = body.to_dict()
    else:
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorDto | GetChannelEndpointResponseDto | ValidationErrorDto | str | None:
    if response.status_code == 201:
        response_201 = GetChannelEndpointResponseDto.from_dict(response.json())

        return response_201

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
) -> Response[ErrorDto | GetChannelEndpointResponseDto | ValidationErrorDto | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateMsTeamsChannelEndpointDto
    | CreateMsTeamsUserEndpointDto
    | CreatePhoneEndpointDto
    | CreateSlackChannelEndpointDto
    | CreateSlackUserEndpointDto
    | CreateTelegramChatEndpointDto
    | CreateWebhookEndpointDto,
    idempotency_key: str | Unset = UNSET,
) -> Response[ErrorDto | GetChannelEndpointResponseDto | ValidationErrorDto | str]:
    """Create a channel endpoint

     Create a new channel endpoint for a resource.

    Args:
        idempotency_key (str | Unset):
        body (CreateMsTeamsChannelEndpointDto | CreateMsTeamsUserEndpointDto |
            CreatePhoneEndpointDto | CreateSlackChannelEndpointDto | CreateSlackUserEndpointDto |
            CreateTelegramChatEndpointDto | CreateWebhookEndpointDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorDto | GetChannelEndpointResponseDto | ValidationErrorDto | str]
    """

    kwargs = _get_kwargs(
        body=body,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: CreateMsTeamsChannelEndpointDto
    | CreateMsTeamsUserEndpointDto
    | CreatePhoneEndpointDto
    | CreateSlackChannelEndpointDto
    | CreateSlackUserEndpointDto
    | CreateTelegramChatEndpointDto
    | CreateWebhookEndpointDto,
    idempotency_key: str | Unset = UNSET,
) -> ErrorDto | GetChannelEndpointResponseDto | ValidationErrorDto | str | None:
    """Create a channel endpoint

     Create a new channel endpoint for a resource.

    Args:
        idempotency_key (str | Unset):
        body (CreateMsTeamsChannelEndpointDto | CreateMsTeamsUserEndpointDto |
            CreatePhoneEndpointDto | CreateSlackChannelEndpointDto | CreateSlackUserEndpointDto |
            CreateTelegramChatEndpointDto | CreateWebhookEndpointDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorDto | GetChannelEndpointResponseDto | ValidationErrorDto | str
    """

    return sync_detailed(
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateMsTeamsChannelEndpointDto
    | CreateMsTeamsUserEndpointDto
    | CreatePhoneEndpointDto
    | CreateSlackChannelEndpointDto
    | CreateSlackUserEndpointDto
    | CreateTelegramChatEndpointDto
    | CreateWebhookEndpointDto,
    idempotency_key: str | Unset = UNSET,
) -> Response[ErrorDto | GetChannelEndpointResponseDto | ValidationErrorDto | str]:
    """Create a channel endpoint

     Create a new channel endpoint for a resource.

    Args:
        idempotency_key (str | Unset):
        body (CreateMsTeamsChannelEndpointDto | CreateMsTeamsUserEndpointDto |
            CreatePhoneEndpointDto | CreateSlackChannelEndpointDto | CreateSlackUserEndpointDto |
            CreateTelegramChatEndpointDto | CreateWebhookEndpointDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorDto | GetChannelEndpointResponseDto | ValidationErrorDto | str]
    """

    kwargs = _get_kwargs(
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CreateMsTeamsChannelEndpointDto
    | CreateMsTeamsUserEndpointDto
    | CreatePhoneEndpointDto
    | CreateSlackChannelEndpointDto
    | CreateSlackUserEndpointDto
    | CreateTelegramChatEndpointDto
    | CreateWebhookEndpointDto,
    idempotency_key: str | Unset = UNSET,
) -> ErrorDto | GetChannelEndpointResponseDto | ValidationErrorDto | str | None:
    """Create a channel endpoint

     Create a new channel endpoint for a resource.

    Args:
        idempotency_key (str | Unset):
        body (CreateMsTeamsChannelEndpointDto | CreateMsTeamsUserEndpointDto |
            CreatePhoneEndpointDto | CreateSlackChannelEndpointDto | CreateSlackUserEndpointDto |
            CreateTelegramChatEndpointDto | CreateWebhookEndpointDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorDto | GetChannelEndpointResponseDto | ValidationErrorDto | str
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
