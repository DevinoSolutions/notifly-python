from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bulk_trigger_event_dto import BulkTriggerEventDto
from ...models.error_dto import ErrorDto
from ...models.payload_validation_exception_dto import PayloadValidationExceptionDto
from ...models.trigger_event_response_dto import TriggerEventResponseDto
from ...models.validation_error_dto import ValidationErrorDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: BulkTriggerEventDto,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["idempotency-key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/events/trigger/bulk",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorDto | PayloadValidationExceptionDto | ValidationErrorDto | list[TriggerEventResponseDto] | str | None:
    if response.status_code == 201:
        response_201 = []
        _response_201 = response.json()
        for response_201_item_data in _response_201:
            response_201_item = TriggerEventResponseDto.from_dict(response_201_item_data)

            response_201.append(response_201_item)

        return response_201

    if response.status_code == 400:
        response_400 = PayloadValidationExceptionDto.from_dict(response.json())

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
) -> Response[ErrorDto | PayloadValidationExceptionDto | ValidationErrorDto | list[TriggerEventResponseDto] | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: BulkTriggerEventDto,
    idempotency_key: str | Unset = UNSET,
) -> Response[ErrorDto | PayloadValidationExceptionDto | ValidationErrorDto | list[TriggerEventResponseDto] | str]:
    """Bulk trigger event


          Using this endpoint you can trigger multiple events at once, to avoid multiple calls to the
    API.
          The bulk API is limited to 100 events per request.


    Args:
        idempotency_key (str | Unset):
        body (BulkTriggerEventDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorDto | PayloadValidationExceptionDto | ValidationErrorDto | list[TriggerEventResponseDto] | str]
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
    body: BulkTriggerEventDto,
    idempotency_key: str | Unset = UNSET,
) -> ErrorDto | PayloadValidationExceptionDto | ValidationErrorDto | list[TriggerEventResponseDto] | str | None:
    """Bulk trigger event


          Using this endpoint you can trigger multiple events at once, to avoid multiple calls to the
    API.
          The bulk API is limited to 100 events per request.


    Args:
        idempotency_key (str | Unset):
        body (BulkTriggerEventDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorDto | PayloadValidationExceptionDto | ValidationErrorDto | list[TriggerEventResponseDto] | str
    """

    return sync_detailed(
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: BulkTriggerEventDto,
    idempotency_key: str | Unset = UNSET,
) -> Response[ErrorDto | PayloadValidationExceptionDto | ValidationErrorDto | list[TriggerEventResponseDto] | str]:
    """Bulk trigger event


          Using this endpoint you can trigger multiple events at once, to avoid multiple calls to the
    API.
          The bulk API is limited to 100 events per request.


    Args:
        idempotency_key (str | Unset):
        body (BulkTriggerEventDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorDto | PayloadValidationExceptionDto | ValidationErrorDto | list[TriggerEventResponseDto] | str]
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
    body: BulkTriggerEventDto,
    idempotency_key: str | Unset = UNSET,
) -> ErrorDto | PayloadValidationExceptionDto | ValidationErrorDto | list[TriggerEventResponseDto] | str | None:
    """Bulk trigger event


          Using this endpoint you can trigger multiple events at once, to avoid multiple calls to the
    API.
          The bulk API is limited to 100 events per request.


    Args:
        idempotency_key (str | Unset):
        body (BulkTriggerEventDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorDto | PayloadValidationExceptionDto | ValidationErrorDto | list[TriggerEventResponseDto] | str
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
