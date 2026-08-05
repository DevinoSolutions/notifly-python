from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_update_topic_request_dto import CreateUpdateTopicRequestDto
from ...models.error_dto import ErrorDto
from ...models.topic_response_dto import TopicResponseDto
from ...models.validation_error_dto import ValidationErrorDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CreateUpdateTopicRequestDto,
    fail_if_exists: bool | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["idempotency-key"] = idempotency_key

    params: dict[str, Any] = {}

    params["failIfExists"] = fail_if_exists

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v2/topics",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorDto | TopicResponseDto | ValidationErrorDto | str | None:
    if response.status_code == 200:
        response_200 = TopicResponseDto.from_dict(response.json())

        return response_200

    if response.status_code == 201:
        response_201 = TopicResponseDto.from_dict(response.json())

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
        response_409 = TopicResponseDto.from_dict(response.json())

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
) -> Response[ErrorDto | TopicResponseDto | ValidationErrorDto | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateUpdateTopicRequestDto,
    fail_if_exists: bool | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> Response[ErrorDto | TopicResponseDto | ValidationErrorDto | str]:
    """Create a topic

     Creates a new topic if it does not exist, or updates an existing topic if it already exists. Use
    ?failIfExists=true to prevent updates.

    Args:
        fail_if_exists (bool | Unset):
        idempotency_key (str | Unset):
        body (CreateUpdateTopicRequestDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorDto | TopicResponseDto | ValidationErrorDto | str]
    """

    kwargs = _get_kwargs(
        body=body,
        fail_if_exists=fail_if_exists,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: CreateUpdateTopicRequestDto,
    fail_if_exists: bool | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> ErrorDto | TopicResponseDto | ValidationErrorDto | str | None:
    """Create a topic

     Creates a new topic if it does not exist, or updates an existing topic if it already exists. Use
    ?failIfExists=true to prevent updates.

    Args:
        fail_if_exists (bool | Unset):
        idempotency_key (str | Unset):
        body (CreateUpdateTopicRequestDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorDto | TopicResponseDto | ValidationErrorDto | str
    """

    return sync_detailed(
        client=client,
        body=body,
        fail_if_exists=fail_if_exists,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateUpdateTopicRequestDto,
    fail_if_exists: bool | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> Response[ErrorDto | TopicResponseDto | ValidationErrorDto | str]:
    """Create a topic

     Creates a new topic if it does not exist, or updates an existing topic if it already exists. Use
    ?failIfExists=true to prevent updates.

    Args:
        fail_if_exists (bool | Unset):
        idempotency_key (str | Unset):
        body (CreateUpdateTopicRequestDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorDto | TopicResponseDto | ValidationErrorDto | str]
    """

    kwargs = _get_kwargs(
        body=body,
        fail_if_exists=fail_if_exists,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: CreateUpdateTopicRequestDto,
    fail_if_exists: bool | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> ErrorDto | TopicResponseDto | ValidationErrorDto | str | None:
    """Create a topic

     Creates a new topic if it does not exist, or updates an existing topic if it already exists. Use
    ?failIfExists=true to prevent updates.

    Args:
        fail_if_exists (bool | Unset):
        idempotency_key (str | Unset):
        body (CreateUpdateTopicRequestDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorDto | TopicResponseDto | ValidationErrorDto | str
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            fail_if_exists=fail_if_exists,
            idempotency_key=idempotency_key,
        )
    ).parsed
