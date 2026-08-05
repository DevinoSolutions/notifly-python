from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_dto import ErrorDto
from ...models.get_subscriber_notifications_response_dto import GetSubscriberNotificationsResponseDto
from ...models.subscribers_controller_get_subscriber_notifications_severity_item import (
    SubscribersControllerGetSubscriberNotificationsSeverityItem,
)
from ...models.validation_error_dto import ValidationErrorDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    subscriber_id: str,
    *,
    limit: float | Unset = 10.0,
    after: str | Unset = UNSET,
    offset: float | Unset = UNSET,
    read: bool | Unset = UNSET,
    archived: bool | Unset = UNSET,
    snoozed: bool | Unset = UNSET,
    seen: bool | Unset = UNSET,
    data: str | Unset = UNSET,
    severity: list[SubscribersControllerGetSubscriberNotificationsSeverityItem] | Unset = UNSET,
    created_gte: float | Unset = UNSET,
    created_lte: float | Unset = UNSET,
    context_keys: list[str] | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["idempotency-key"] = idempotency_key

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["after"] = after

    params["offset"] = offset

    params["read"] = read

    params["archived"] = archived

    params["snoozed"] = snoozed

    params["seen"] = seen

    params["data"] = data

    json_severity: list[str] | Unset = UNSET
    if not isinstance(severity, Unset):
        json_severity = []
        for severity_item_data in severity:
            severity_item = severity_item_data.value
            json_severity.append(severity_item)

    params["severity"] = json_severity

    params["createdGte"] = created_gte

    params["createdLte"] = created_lte

    json_context_keys: list[str] | Unset = UNSET
    if not isinstance(context_keys, Unset):
        json_context_keys = context_keys

    params["contextKeys"] = json_context_keys

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/subscribers/{subscriber_id}/notifications".format(
            subscriber_id=quote(str(subscriber_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorDto | GetSubscriberNotificationsResponseDto | ValidationErrorDto | str | None:
    if response.status_code == 200:
        response_200 = GetSubscriberNotificationsResponseDto.from_dict(response.json())

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
) -> Response[ErrorDto | GetSubscriberNotificationsResponseDto | ValidationErrorDto | str]:
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
    limit: float | Unset = 10.0,
    after: str | Unset = UNSET,
    offset: float | Unset = UNSET,
    read: bool | Unset = UNSET,
    archived: bool | Unset = UNSET,
    snoozed: bool | Unset = UNSET,
    seen: bool | Unset = UNSET,
    data: str | Unset = UNSET,
    severity: list[SubscribersControllerGetSubscriberNotificationsSeverityItem] | Unset = UNSET,
    created_gte: float | Unset = UNSET,
    created_lte: float | Unset = UNSET,
    context_keys: list[str] | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> Response[ErrorDto | GetSubscriberNotificationsResponseDto | ValidationErrorDto | str]:
    """Retrieve subscriber notifications

     Retrieve in-app (inbox) notifications for a subscriber by its unique key identifier
    **subscriberId**.
        Supports filtering by tags, read/archived/snoozed/seen state, data attributes, severity, date
    range, and context keys.

    Args:
        subscriber_id (str):
        limit (float | Unset):  Default: 10.0.
        after (str | Unset):
        offset (float | Unset):
        read (bool | Unset):
        archived (bool | Unset):
        snoozed (bool | Unset):
        seen (bool | Unset):
        data (str | Unset):
        severity (list[SubscribersControllerGetSubscriberNotificationsSeverityItem] | Unset):
        created_gte (float | Unset):
        created_lte (float | Unset):
        context_keys (list[str] | Unset):
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorDto | GetSubscriberNotificationsResponseDto | ValidationErrorDto | str]
    """

    kwargs = _get_kwargs(
        subscriber_id=subscriber_id,
        limit=limit,
        after=after,
        offset=offset,
        read=read,
        archived=archived,
        snoozed=snoozed,
        seen=seen,
        data=data,
        severity=severity,
        created_gte=created_gte,
        created_lte=created_lte,
        context_keys=context_keys,
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
    limit: float | Unset = 10.0,
    after: str | Unset = UNSET,
    offset: float | Unset = UNSET,
    read: bool | Unset = UNSET,
    archived: bool | Unset = UNSET,
    snoozed: bool | Unset = UNSET,
    seen: bool | Unset = UNSET,
    data: str | Unset = UNSET,
    severity: list[SubscribersControllerGetSubscriberNotificationsSeverityItem] | Unset = UNSET,
    created_gte: float | Unset = UNSET,
    created_lte: float | Unset = UNSET,
    context_keys: list[str] | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> ErrorDto | GetSubscriberNotificationsResponseDto | ValidationErrorDto | str | None:
    """Retrieve subscriber notifications

     Retrieve in-app (inbox) notifications for a subscriber by its unique key identifier
    **subscriberId**.
        Supports filtering by tags, read/archived/snoozed/seen state, data attributes, severity, date
    range, and context keys.

    Args:
        subscriber_id (str):
        limit (float | Unset):  Default: 10.0.
        after (str | Unset):
        offset (float | Unset):
        read (bool | Unset):
        archived (bool | Unset):
        snoozed (bool | Unset):
        seen (bool | Unset):
        data (str | Unset):
        severity (list[SubscribersControllerGetSubscriberNotificationsSeverityItem] | Unset):
        created_gte (float | Unset):
        created_lte (float | Unset):
        context_keys (list[str] | Unset):
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorDto | GetSubscriberNotificationsResponseDto | ValidationErrorDto | str
    """

    return sync_detailed(
        subscriber_id=subscriber_id,
        client=client,
        limit=limit,
        after=after,
        offset=offset,
        read=read,
        archived=archived,
        snoozed=snoozed,
        seen=seen,
        data=data,
        severity=severity,
        created_gte=created_gte,
        created_lte=created_lte,
        context_keys=context_keys,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    subscriber_id: str,
    *,
    client: AuthenticatedClient,
    limit: float | Unset = 10.0,
    after: str | Unset = UNSET,
    offset: float | Unset = UNSET,
    read: bool | Unset = UNSET,
    archived: bool | Unset = UNSET,
    snoozed: bool | Unset = UNSET,
    seen: bool | Unset = UNSET,
    data: str | Unset = UNSET,
    severity: list[SubscribersControllerGetSubscriberNotificationsSeverityItem] | Unset = UNSET,
    created_gte: float | Unset = UNSET,
    created_lte: float | Unset = UNSET,
    context_keys: list[str] | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> Response[ErrorDto | GetSubscriberNotificationsResponseDto | ValidationErrorDto | str]:
    """Retrieve subscriber notifications

     Retrieve in-app (inbox) notifications for a subscriber by its unique key identifier
    **subscriberId**.
        Supports filtering by tags, read/archived/snoozed/seen state, data attributes, severity, date
    range, and context keys.

    Args:
        subscriber_id (str):
        limit (float | Unset):  Default: 10.0.
        after (str | Unset):
        offset (float | Unset):
        read (bool | Unset):
        archived (bool | Unset):
        snoozed (bool | Unset):
        seen (bool | Unset):
        data (str | Unset):
        severity (list[SubscribersControllerGetSubscriberNotificationsSeverityItem] | Unset):
        created_gte (float | Unset):
        created_lte (float | Unset):
        context_keys (list[str] | Unset):
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorDto | GetSubscriberNotificationsResponseDto | ValidationErrorDto | str]
    """

    kwargs = _get_kwargs(
        subscriber_id=subscriber_id,
        limit=limit,
        after=after,
        offset=offset,
        read=read,
        archived=archived,
        snoozed=snoozed,
        seen=seen,
        data=data,
        severity=severity,
        created_gte=created_gte,
        created_lte=created_lte,
        context_keys=context_keys,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    subscriber_id: str,
    *,
    client: AuthenticatedClient,
    limit: float | Unset = 10.0,
    after: str | Unset = UNSET,
    offset: float | Unset = UNSET,
    read: bool | Unset = UNSET,
    archived: bool | Unset = UNSET,
    snoozed: bool | Unset = UNSET,
    seen: bool | Unset = UNSET,
    data: str | Unset = UNSET,
    severity: list[SubscribersControllerGetSubscriberNotificationsSeverityItem] | Unset = UNSET,
    created_gte: float | Unset = UNSET,
    created_lte: float | Unset = UNSET,
    context_keys: list[str] | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> ErrorDto | GetSubscriberNotificationsResponseDto | ValidationErrorDto | str | None:
    """Retrieve subscriber notifications

     Retrieve in-app (inbox) notifications for a subscriber by its unique key identifier
    **subscriberId**.
        Supports filtering by tags, read/archived/snoozed/seen state, data attributes, severity, date
    range, and context keys.

    Args:
        subscriber_id (str):
        limit (float | Unset):  Default: 10.0.
        after (str | Unset):
        offset (float | Unset):
        read (bool | Unset):
        archived (bool | Unset):
        snoozed (bool | Unset):
        seen (bool | Unset):
        data (str | Unset):
        severity (list[SubscribersControllerGetSubscriberNotificationsSeverityItem] | Unset):
        created_gte (float | Unset):
        created_lte (float | Unset):
        context_keys (list[str] | Unset):
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorDto | GetSubscriberNotificationsResponseDto | ValidationErrorDto | str
    """

    return (
        await asyncio_detailed(
            subscriber_id=subscriber_id,
            client=client,
            limit=limit,
            after=after,
            offset=offset,
            read=read,
            archived=archived,
            snoozed=snoozed,
            seen=seen,
            data=data,
            severity=severity,
            created_gte=created_gte,
            created_lte=created_lte,
            context_keys=context_keys,
            idempotency_key=idempotency_key,
        )
    ).parsed
