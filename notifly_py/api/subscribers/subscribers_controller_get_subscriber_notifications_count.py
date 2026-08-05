from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_dto import ErrorDto
from ...models.get_subscriber_notifications_count_response_dto import GetSubscriberNotificationsCountResponseDto
from ...models.validation_error_dto import ValidationErrorDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    subscriber_id: str,
    *,
    filters: str,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["idempotency-key"] = idempotency_key

    params: dict[str, Any] = {}

    params["filters"] = filters

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/subscribers/{subscriber_id}/notifications/count".format(
            subscriber_id=quote(str(subscriber_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorDto | ValidationErrorDto | list[GetSubscriberNotificationsCountResponseDto] | str | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = GetSubscriberNotificationsCountResponseDto.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[ErrorDto | ValidationErrorDto | list[GetSubscriberNotificationsCountResponseDto] | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    subscriber_id: str,
    *,
    client: AuthenticatedClient,
    filters: str,
    idempotency_key: str | Unset = UNSET,
) -> Response[ErrorDto | ValidationErrorDto | list[GetSubscriberNotificationsCountResponseDto] | str]:
    """Retrieve subscriber notifications count

     Retrieve count of in-app (inbox) notifications for a subscriber by its unique key identifier
    **subscriberId**.
        Supports multiple filters to count in-app (inbox) notifications by different criteria, including
    context keys.

    Args:
        subscriber_id (str):
        filters (str):
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorDto | ValidationErrorDto | list[GetSubscriberNotificationsCountResponseDto] | str]
    """

    kwargs = _get_kwargs(
        subscriber_id=subscriber_id,
        filters=filters,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    subscriber_id: str,
    *,
    client: AuthenticatedClient,
    filters: str,
    idempotency_key: str | Unset = UNSET,
) -> ErrorDto | ValidationErrorDto | list[GetSubscriberNotificationsCountResponseDto] | str | None:
    """Retrieve subscriber notifications count

     Retrieve count of in-app (inbox) notifications for a subscriber by its unique key identifier
    **subscriberId**.
        Supports multiple filters to count in-app (inbox) notifications by different criteria, including
    context keys.

    Args:
        subscriber_id (str):
        filters (str):
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorDto | ValidationErrorDto | list[GetSubscriberNotificationsCountResponseDto] | str
    """

    return sync_detailed(
        subscriber_id=subscriber_id,
        client=client,
        filters=filters,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    subscriber_id: str,
    *,
    client: AuthenticatedClient,
    filters: str,
    idempotency_key: str | Unset = UNSET,
) -> Response[ErrorDto | ValidationErrorDto | list[GetSubscriberNotificationsCountResponseDto] | str]:
    """Retrieve subscriber notifications count

     Retrieve count of in-app (inbox) notifications for a subscriber by its unique key identifier
    **subscriberId**.
        Supports multiple filters to count in-app (inbox) notifications by different criteria, including
    context keys.

    Args:
        subscriber_id (str):
        filters (str):
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorDto | ValidationErrorDto | list[GetSubscriberNotificationsCountResponseDto] | str]
    """

    kwargs = _get_kwargs(
        subscriber_id=subscriber_id,
        filters=filters,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    subscriber_id: str,
    *,
    client: AuthenticatedClient,
    filters: str,
    idempotency_key: str | Unset = UNSET,
) -> ErrorDto | ValidationErrorDto | list[GetSubscriberNotificationsCountResponseDto] | str | None:
    """Retrieve subscriber notifications count

     Retrieve count of in-app (inbox) notifications for a subscriber by its unique key identifier
    **subscriberId**.
        Supports multiple filters to count in-app (inbox) notifications by different criteria, including
    context keys.

    Args:
        subscriber_id (str):
        filters (str):
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorDto | ValidationErrorDto | list[GetSubscriberNotificationsCountResponseDto] | str
    """

    return (
        await asyncio_detailed(
            subscriber_id=subscriber_id,
            client=client,
            filters=filters,
            idempotency_key=idempotency_key,
        )
    ).parsed
