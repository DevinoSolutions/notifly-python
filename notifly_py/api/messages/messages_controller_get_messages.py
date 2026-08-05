from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.channel_type_enum import ChannelTypeEnum
from ...models.error_dto import ErrorDto
from ...models.messages_response_dto import MessagesResponseDto
from ...models.validation_error_dto import ValidationErrorDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    channel: ChannelTypeEnum | Unset = UNSET,
    subscriber_id: str | Unset = UNSET,
    transaction_id: list[str] | Unset = UNSET,
    context_keys: list[str] | Unset = UNSET,
    page: float | Unset = 0.0,
    limit: float | Unset = 10.0,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["idempotency-key"] = idempotency_key

    params: dict[str, Any] = {}

    json_channel: str | Unset = UNSET
    if not isinstance(channel, Unset):
        json_channel = channel.value

    params["channel"] = json_channel

    params["subscriberId"] = subscriber_id

    json_transaction_id: list[str] | Unset = UNSET
    if not isinstance(transaction_id, Unset):
        json_transaction_id = transaction_id

    params["transactionId"] = json_transaction_id

    json_context_keys: list[str] | Unset = UNSET
    if not isinstance(context_keys, Unset):
        json_context_keys = context_keys

    params["contextKeys"] = json_context_keys

    params["page"] = page

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/messages",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorDto | MessagesResponseDto | ValidationErrorDto | str | None:
    if response.status_code == 200:
        response_200 = MessagesResponseDto.from_dict(response.json())

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
) -> Response[ErrorDto | MessagesResponseDto | ValidationErrorDto | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    channel: ChannelTypeEnum | Unset = UNSET,
    subscriber_id: str | Unset = UNSET,
    transaction_id: list[str] | Unset = UNSET,
    context_keys: list[str] | Unset = UNSET,
    page: float | Unset = 0.0,
    limit: float | Unset = 10.0,
    idempotency_key: str | Unset = UNSET,
) -> Response[ErrorDto | MessagesResponseDto | ValidationErrorDto | str]:
    """List all messages

     List all messages for the current environment.
        This API supports filtering by **channel**, **subscriberId**, and **transactionId**.
        This API returns a paginated list of messages.

    Args:
        channel (ChannelTypeEnum | Unset): Channel type through which the message is sent
        subscriber_id (str | Unset):
        transaction_id (list[str] | Unset):
        context_keys (list[str] | Unset):
        page (float | Unset):  Default: 0.0.
        limit (float | Unset):  Default: 10.0.
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorDto | MessagesResponseDto | ValidationErrorDto | str]
    """

    kwargs = _get_kwargs(
        channel=channel,
        subscriber_id=subscriber_id,
        transaction_id=transaction_id,
        context_keys=context_keys,
        page=page,
        limit=limit,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    channel: ChannelTypeEnum | Unset = UNSET,
    subscriber_id: str | Unset = UNSET,
    transaction_id: list[str] | Unset = UNSET,
    context_keys: list[str] | Unset = UNSET,
    page: float | Unset = 0.0,
    limit: float | Unset = 10.0,
    idempotency_key: str | Unset = UNSET,
) -> ErrorDto | MessagesResponseDto | ValidationErrorDto | str | None:
    """List all messages

     List all messages for the current environment.
        This API supports filtering by **channel**, **subscriberId**, and **transactionId**.
        This API returns a paginated list of messages.

    Args:
        channel (ChannelTypeEnum | Unset): Channel type through which the message is sent
        subscriber_id (str | Unset):
        transaction_id (list[str] | Unset):
        context_keys (list[str] | Unset):
        page (float | Unset):  Default: 0.0.
        limit (float | Unset):  Default: 10.0.
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorDto | MessagesResponseDto | ValidationErrorDto | str
    """

    return sync_detailed(
        client=client,
        channel=channel,
        subscriber_id=subscriber_id,
        transaction_id=transaction_id,
        context_keys=context_keys,
        page=page,
        limit=limit,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    channel: ChannelTypeEnum | Unset = UNSET,
    subscriber_id: str | Unset = UNSET,
    transaction_id: list[str] | Unset = UNSET,
    context_keys: list[str] | Unset = UNSET,
    page: float | Unset = 0.0,
    limit: float | Unset = 10.0,
    idempotency_key: str | Unset = UNSET,
) -> Response[ErrorDto | MessagesResponseDto | ValidationErrorDto | str]:
    """List all messages

     List all messages for the current environment.
        This API supports filtering by **channel**, **subscriberId**, and **transactionId**.
        This API returns a paginated list of messages.

    Args:
        channel (ChannelTypeEnum | Unset): Channel type through which the message is sent
        subscriber_id (str | Unset):
        transaction_id (list[str] | Unset):
        context_keys (list[str] | Unset):
        page (float | Unset):  Default: 0.0.
        limit (float | Unset):  Default: 10.0.
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorDto | MessagesResponseDto | ValidationErrorDto | str]
    """

    kwargs = _get_kwargs(
        channel=channel,
        subscriber_id=subscriber_id,
        transaction_id=transaction_id,
        context_keys=context_keys,
        page=page,
        limit=limit,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    channel: ChannelTypeEnum | Unset = UNSET,
    subscriber_id: str | Unset = UNSET,
    transaction_id: list[str] | Unset = UNSET,
    context_keys: list[str] | Unset = UNSET,
    page: float | Unset = 0.0,
    limit: float | Unset = 10.0,
    idempotency_key: str | Unset = UNSET,
) -> ErrorDto | MessagesResponseDto | ValidationErrorDto | str | None:
    """List all messages

     List all messages for the current environment.
        This API supports filtering by **channel**, **subscriberId**, and **transactionId**.
        This API returns a paginated list of messages.

    Args:
        channel (ChannelTypeEnum | Unset): Channel type through which the message is sent
        subscriber_id (str | Unset):
        transaction_id (list[str] | Unset):
        context_keys (list[str] | Unset):
        page (float | Unset):  Default: 0.0.
        limit (float | Unset):  Default: 10.0.
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorDto | MessagesResponseDto | ValidationErrorDto | str
    """

    return (
        await asyncio_detailed(
            client=client,
            channel=channel,
            subscriber_id=subscriber_id,
            transaction_id=transaction_id,
            context_keys=context_keys,
            page=page,
            limit=limit,
            idempotency_key=idempotency_key,
        )
    ).parsed
