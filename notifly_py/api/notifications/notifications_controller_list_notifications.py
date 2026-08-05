from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.activities_response_dto import ActivitiesResponseDto
from ...models.channel_type_enum import ChannelTypeEnum
from ...models.error_dto import ErrorDto
from ...models.validation_error_dto import ValidationErrorDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    channels: list[ChannelTypeEnum] | Unset = UNSET,
    templates: list[str] | Unset = UNSET,
    emails: list[str] | Unset = UNSET,
    search: str | Unset = UNSET,
    subscriber_ids: list[str] | Unset = UNSET,
    severity: list[str] | Unset = UNSET,
    page: float | Unset = 0.0,
    limit: float | Unset = 10.0,
    transaction_id: str | Unset = UNSET,
    topic_key: str | Unset = UNSET,
    subscription_id: str | Unset = UNSET,
    context_keys: list[str] | Unset = UNSET,
    after: str | Unset = UNSET,
    before: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["idempotency-key"] = idempotency_key

    params: dict[str, Any] = {}

    json_channels: list[str] | Unset = UNSET
    if not isinstance(channels, Unset):
        json_channels = []
        for channels_item_data in channels:
            channels_item = channels_item_data.value
            json_channels.append(channels_item)

    params["channels"] = json_channels

    json_templates: list[str] | Unset = UNSET
    if not isinstance(templates, Unset):
        json_templates = templates

    params["templates"] = json_templates

    json_emails: list[str] | Unset = UNSET
    if not isinstance(emails, Unset):
        json_emails = emails

    params["emails"] = json_emails

    params["search"] = search

    json_subscriber_ids: list[str] | Unset = UNSET
    if not isinstance(subscriber_ids, Unset):
        json_subscriber_ids = subscriber_ids

    params["subscriberIds"] = json_subscriber_ids

    json_severity: list[str] | Unset = UNSET
    if not isinstance(severity, Unset):
        json_severity = severity

    params["severity"] = json_severity

    params["page"] = page

    params["limit"] = limit

    params["transactionId"] = transaction_id

    params["topicKey"] = topic_key

    params["subscriptionId"] = subscription_id

    json_context_keys: list[str] | Unset = UNSET
    if not isinstance(context_keys, Unset):
        json_context_keys = context_keys

    params["contextKeys"] = json_context_keys

    params["after"] = after

    params["before"] = before

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/notifications",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ActivitiesResponseDto | ErrorDto | ValidationErrorDto | str | None:
    if response.status_code == 200:
        response_200 = ActivitiesResponseDto.from_dict(response.json())

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
) -> Response[ActivitiesResponseDto | ErrorDto | ValidationErrorDto | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    channels: list[ChannelTypeEnum] | Unset = UNSET,
    templates: list[str] | Unset = UNSET,
    emails: list[str] | Unset = UNSET,
    search: str | Unset = UNSET,
    subscriber_ids: list[str] | Unset = UNSET,
    severity: list[str] | Unset = UNSET,
    page: float | Unset = 0.0,
    limit: float | Unset = 10.0,
    transaction_id: str | Unset = UNSET,
    topic_key: str | Unset = UNSET,
    subscription_id: str | Unset = UNSET,
    context_keys: list[str] | Unset = UNSET,
    after: str | Unset = UNSET,
    before: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> Response[ActivitiesResponseDto | ErrorDto | ValidationErrorDto | str]:
    """List all events

     List all notification events (triggered events) for the current environment.
        This API supports filtering by **channels**, **templates**, **emails**, **subscriberIds**,
    **transactionId**, **topicKey**, **severity**, **contextKeys**.
        Checkout all available filters in the query section.
        This API returns event triggers, to list each channel notifications, check messages APIs.

    Args:
        channels (list[ChannelTypeEnum] | Unset):
        templates (list[str] | Unset):
        emails (list[str] | Unset):
        search (str | Unset):
        subscriber_ids (list[str] | Unset):
        severity (list[str] | Unset):
        page (float | Unset):  Default: 0.0.
        limit (float | Unset):  Default: 10.0.
        transaction_id (str | Unset):
        topic_key (str | Unset):
        subscription_id (str | Unset):
        context_keys (list[str] | Unset):
        after (str | Unset):
        before (str | Unset):
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActivitiesResponseDto | ErrorDto | ValidationErrorDto | str]
    """

    kwargs = _get_kwargs(
        channels=channels,
        templates=templates,
        emails=emails,
        search=search,
        subscriber_ids=subscriber_ids,
        severity=severity,
        page=page,
        limit=limit,
        transaction_id=transaction_id,
        topic_key=topic_key,
        subscription_id=subscription_id,
        context_keys=context_keys,
        after=after,
        before=before,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    channels: list[ChannelTypeEnum] | Unset = UNSET,
    templates: list[str] | Unset = UNSET,
    emails: list[str] | Unset = UNSET,
    search: str | Unset = UNSET,
    subscriber_ids: list[str] | Unset = UNSET,
    severity: list[str] | Unset = UNSET,
    page: float | Unset = 0.0,
    limit: float | Unset = 10.0,
    transaction_id: str | Unset = UNSET,
    topic_key: str | Unset = UNSET,
    subscription_id: str | Unset = UNSET,
    context_keys: list[str] | Unset = UNSET,
    after: str | Unset = UNSET,
    before: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> ActivitiesResponseDto | ErrorDto | ValidationErrorDto | str | None:
    """List all events

     List all notification events (triggered events) for the current environment.
        This API supports filtering by **channels**, **templates**, **emails**, **subscriberIds**,
    **transactionId**, **topicKey**, **severity**, **contextKeys**.
        Checkout all available filters in the query section.
        This API returns event triggers, to list each channel notifications, check messages APIs.

    Args:
        channels (list[ChannelTypeEnum] | Unset):
        templates (list[str] | Unset):
        emails (list[str] | Unset):
        search (str | Unset):
        subscriber_ids (list[str] | Unset):
        severity (list[str] | Unset):
        page (float | Unset):  Default: 0.0.
        limit (float | Unset):  Default: 10.0.
        transaction_id (str | Unset):
        topic_key (str | Unset):
        subscription_id (str | Unset):
        context_keys (list[str] | Unset):
        after (str | Unset):
        before (str | Unset):
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActivitiesResponseDto | ErrorDto | ValidationErrorDto | str
    """

    return sync_detailed(
        client=client,
        channels=channels,
        templates=templates,
        emails=emails,
        search=search,
        subscriber_ids=subscriber_ids,
        severity=severity,
        page=page,
        limit=limit,
        transaction_id=transaction_id,
        topic_key=topic_key,
        subscription_id=subscription_id,
        context_keys=context_keys,
        after=after,
        before=before,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    channels: list[ChannelTypeEnum] | Unset = UNSET,
    templates: list[str] | Unset = UNSET,
    emails: list[str] | Unset = UNSET,
    search: str | Unset = UNSET,
    subscriber_ids: list[str] | Unset = UNSET,
    severity: list[str] | Unset = UNSET,
    page: float | Unset = 0.0,
    limit: float | Unset = 10.0,
    transaction_id: str | Unset = UNSET,
    topic_key: str | Unset = UNSET,
    subscription_id: str | Unset = UNSET,
    context_keys: list[str] | Unset = UNSET,
    after: str | Unset = UNSET,
    before: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> Response[ActivitiesResponseDto | ErrorDto | ValidationErrorDto | str]:
    """List all events

     List all notification events (triggered events) for the current environment.
        This API supports filtering by **channels**, **templates**, **emails**, **subscriberIds**,
    **transactionId**, **topicKey**, **severity**, **contextKeys**.
        Checkout all available filters in the query section.
        This API returns event triggers, to list each channel notifications, check messages APIs.

    Args:
        channels (list[ChannelTypeEnum] | Unset):
        templates (list[str] | Unset):
        emails (list[str] | Unset):
        search (str | Unset):
        subscriber_ids (list[str] | Unset):
        severity (list[str] | Unset):
        page (float | Unset):  Default: 0.0.
        limit (float | Unset):  Default: 10.0.
        transaction_id (str | Unset):
        topic_key (str | Unset):
        subscription_id (str | Unset):
        context_keys (list[str] | Unset):
        after (str | Unset):
        before (str | Unset):
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ActivitiesResponseDto | ErrorDto | ValidationErrorDto | str]
    """

    kwargs = _get_kwargs(
        channels=channels,
        templates=templates,
        emails=emails,
        search=search,
        subscriber_ids=subscriber_ids,
        severity=severity,
        page=page,
        limit=limit,
        transaction_id=transaction_id,
        topic_key=topic_key,
        subscription_id=subscription_id,
        context_keys=context_keys,
        after=after,
        before=before,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    channels: list[ChannelTypeEnum] | Unset = UNSET,
    templates: list[str] | Unset = UNSET,
    emails: list[str] | Unset = UNSET,
    search: str | Unset = UNSET,
    subscriber_ids: list[str] | Unset = UNSET,
    severity: list[str] | Unset = UNSET,
    page: float | Unset = 0.0,
    limit: float | Unset = 10.0,
    transaction_id: str | Unset = UNSET,
    topic_key: str | Unset = UNSET,
    subscription_id: str | Unset = UNSET,
    context_keys: list[str] | Unset = UNSET,
    after: str | Unset = UNSET,
    before: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> ActivitiesResponseDto | ErrorDto | ValidationErrorDto | str | None:
    """List all events

     List all notification events (triggered events) for the current environment.
        This API supports filtering by **channels**, **templates**, **emails**, **subscriberIds**,
    **transactionId**, **topicKey**, **severity**, **contextKeys**.
        Checkout all available filters in the query section.
        This API returns event triggers, to list each channel notifications, check messages APIs.

    Args:
        channels (list[ChannelTypeEnum] | Unset):
        templates (list[str] | Unset):
        emails (list[str] | Unset):
        search (str | Unset):
        subscriber_ids (list[str] | Unset):
        severity (list[str] | Unset):
        page (float | Unset):  Default: 0.0.
        limit (float | Unset):  Default: 10.0.
        transaction_id (str | Unset):
        topic_key (str | Unset):
        subscription_id (str | Unset):
        context_keys (list[str] | Unset):
        after (str | Unset):
        before (str | Unset):
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ActivitiesResponseDto | ErrorDto | ValidationErrorDto | str
    """

    return (
        await asyncio_detailed(
            client=client,
            channels=channels,
            templates=templates,
            emails=emails,
            search=search,
            subscriber_ids=subscriber_ids,
            severity=severity,
            page=page,
            limit=limit,
            transaction_id=transaction_id,
            topic_key=topic_key,
            subscription_id=subscription_id,
            context_keys=context_keys,
            after=after,
            before=before,
            idempotency_key=idempotency_key,
        )
    ).parsed
