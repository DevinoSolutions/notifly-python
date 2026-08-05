from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_dto import ErrorDto
from ...models.messages_controller_delete_messages_by_transaction_id_channel import (
    MessagesControllerDeleteMessagesByTransactionIdChannel,
)
from ...models.validation_error_dto import ValidationErrorDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    transaction_id: str,
    *,
    channel: MessagesControllerDeleteMessagesByTransactionIdChannel | Unset = UNSET,
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

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/v1/messages/transaction/{transaction_id}".format(
            transaction_id=quote(str(transaction_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ErrorDto | ValidationErrorDto | str | None:
    if response.status_code == 204:
        response_204 = cast(Any, None)
        return response_204

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
) -> Response[Any | ErrorDto | ValidationErrorDto | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    transaction_id: str,
    *,
    client: AuthenticatedClient,
    channel: MessagesControllerDeleteMessagesByTransactionIdChannel | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> Response[Any | ErrorDto | ValidationErrorDto | str]:
    """Delete messages by transactionId

     Delete multiple messages from the Notifly platform using **transactionId** of triggered event.
        This API supports filtering by **channel** and delete all messages associated with the
    **transactionId**.

    Args:
        transaction_id (str):
        channel (MessagesControllerDeleteMessagesByTransactionIdChannel | Unset):
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorDto | ValidationErrorDto | str]
    """

    kwargs = _get_kwargs(
        transaction_id=transaction_id,
        channel=channel,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    transaction_id: str,
    *,
    client: AuthenticatedClient,
    channel: MessagesControllerDeleteMessagesByTransactionIdChannel | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> Any | ErrorDto | ValidationErrorDto | str | None:
    """Delete messages by transactionId

     Delete multiple messages from the Notifly platform using **transactionId** of triggered event.
        This API supports filtering by **channel** and delete all messages associated with the
    **transactionId**.

    Args:
        transaction_id (str):
        channel (MessagesControllerDeleteMessagesByTransactionIdChannel | Unset):
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorDto | ValidationErrorDto | str
    """

    return sync_detailed(
        transaction_id=transaction_id,
        client=client,
        channel=channel,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    transaction_id: str,
    *,
    client: AuthenticatedClient,
    channel: MessagesControllerDeleteMessagesByTransactionIdChannel | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> Response[Any | ErrorDto | ValidationErrorDto | str]:
    """Delete messages by transactionId

     Delete multiple messages from the Notifly platform using **transactionId** of triggered event.
        This API supports filtering by **channel** and delete all messages associated with the
    **transactionId**.

    Args:
        transaction_id (str):
        channel (MessagesControllerDeleteMessagesByTransactionIdChannel | Unset):
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorDto | ValidationErrorDto | str]
    """

    kwargs = _get_kwargs(
        transaction_id=transaction_id,
        channel=channel,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    transaction_id: str,
    *,
    client: AuthenticatedClient,
    channel: MessagesControllerDeleteMessagesByTransactionIdChannel | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> Any | ErrorDto | ValidationErrorDto | str | None:
    """Delete messages by transactionId

     Delete multiple messages from the Notifly platform using **transactionId** of triggered event.
        This API supports filtering by **channel** and delete all messages associated with the
    **transactionId**.

    Args:
        transaction_id (str):
        channel (MessagesControllerDeleteMessagesByTransactionIdChannel | Unset):
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorDto | ValidationErrorDto | str
    """

    return (
        await asyncio_detailed(
            transaction_id=transaction_id,
            client=client,
            channel=channel,
            idempotency_key=idempotency_key,
        )
    ).parsed
