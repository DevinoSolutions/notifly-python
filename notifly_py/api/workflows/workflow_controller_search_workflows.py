from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.direction_enum import DirectionEnum
from ...models.error_dto import ErrorDto
from ...models.list_workflow_response import ListWorkflowResponse
from ...models.validation_error_dto import ValidationErrorDto
from ...models.workflow_response_dto_sort_field import WorkflowResponseDtoSortField
from ...models.workflow_status_enum import WorkflowStatusEnum
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: float | Unset = UNSET,
    offset: float | Unset = UNSET,
    order_direction: DirectionEnum | Unset = UNSET,
    order_by: WorkflowResponseDtoSortField | Unset = UNSET,
    query: str | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
    status: list[WorkflowStatusEnum] | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["idempotency-key"] = idempotency_key

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    json_order_direction: str | Unset = UNSET
    if not isinstance(order_direction, Unset):
        json_order_direction = order_direction.value

    params["orderDirection"] = json_order_direction

    json_order_by: str | Unset = UNSET
    if not isinstance(order_by, Unset):
        json_order_by = order_by.value

    params["orderBy"] = json_order_by

    params["query"] = query

    json_tags: list[str] | Unset = UNSET
    if not isinstance(tags, Unset):
        json_tags = tags

    params["tags"] = json_tags

    json_status: list[str] | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = []
        for status_item_data in status:
            status_item = status_item_data.value
            json_status.append(status_item)

    params["status"] = json_status

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v2/workflows",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorDto | ListWorkflowResponse | ValidationErrorDto | str | None:
    if response.status_code == 200:
        response_200 = ListWorkflowResponse.from_dict(response.json())

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
) -> Response[ErrorDto | ListWorkflowResponse | ValidationErrorDto | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    limit: float | Unset = UNSET,
    offset: float | Unset = UNSET,
    order_direction: DirectionEnum | Unset = UNSET,
    order_by: WorkflowResponseDtoSortField | Unset = UNSET,
    query: str | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
    status: list[WorkflowStatusEnum] | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> Response[ErrorDto | ListWorkflowResponse | ValidationErrorDto | str]:
    """List all workflows

     Retrieves a list of workflows with optional filtering and pagination

    Args:
        limit (float | Unset):
        offset (float | Unset):
        order_direction (DirectionEnum | Unset):
        order_by (WorkflowResponseDtoSortField | Unset):
        query (str | Unset):
        tags (list[str] | Unset):
        status (list[WorkflowStatusEnum] | Unset):
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorDto | ListWorkflowResponse | ValidationErrorDto | str]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        order_direction=order_direction,
        order_by=order_by,
        query=query,
        tags=tags,
        status=status,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    limit: float | Unset = UNSET,
    offset: float | Unset = UNSET,
    order_direction: DirectionEnum | Unset = UNSET,
    order_by: WorkflowResponseDtoSortField | Unset = UNSET,
    query: str | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
    status: list[WorkflowStatusEnum] | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> ErrorDto | ListWorkflowResponse | ValidationErrorDto | str | None:
    """List all workflows

     Retrieves a list of workflows with optional filtering and pagination

    Args:
        limit (float | Unset):
        offset (float | Unset):
        order_direction (DirectionEnum | Unset):
        order_by (WorkflowResponseDtoSortField | Unset):
        query (str | Unset):
        tags (list[str] | Unset):
        status (list[WorkflowStatusEnum] | Unset):
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorDto | ListWorkflowResponse | ValidationErrorDto | str
    """

    return sync_detailed(
        client=client,
        limit=limit,
        offset=offset,
        order_direction=order_direction,
        order_by=order_by,
        query=query,
        tags=tags,
        status=status,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: float | Unset = UNSET,
    offset: float | Unset = UNSET,
    order_direction: DirectionEnum | Unset = UNSET,
    order_by: WorkflowResponseDtoSortField | Unset = UNSET,
    query: str | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
    status: list[WorkflowStatusEnum] | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> Response[ErrorDto | ListWorkflowResponse | ValidationErrorDto | str]:
    """List all workflows

     Retrieves a list of workflows with optional filtering and pagination

    Args:
        limit (float | Unset):
        offset (float | Unset):
        order_direction (DirectionEnum | Unset):
        order_by (WorkflowResponseDtoSortField | Unset):
        query (str | Unset):
        tags (list[str] | Unset):
        status (list[WorkflowStatusEnum] | Unset):
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorDto | ListWorkflowResponse | ValidationErrorDto | str]
    """

    kwargs = _get_kwargs(
        limit=limit,
        offset=offset,
        order_direction=order_direction,
        order_by=order_by,
        query=query,
        tags=tags,
        status=status,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: float | Unset = UNSET,
    offset: float | Unset = UNSET,
    order_direction: DirectionEnum | Unset = UNSET,
    order_by: WorkflowResponseDtoSortField | Unset = UNSET,
    query: str | Unset = UNSET,
    tags: list[str] | Unset = UNSET,
    status: list[WorkflowStatusEnum] | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> ErrorDto | ListWorkflowResponse | ValidationErrorDto | str | None:
    """List all workflows

     Retrieves a list of workflows with optional filtering and pagination

    Args:
        limit (float | Unset):
        offset (float | Unset):
        order_direction (DirectionEnum | Unset):
        order_by (WorkflowResponseDtoSortField | Unset):
        query (str | Unset):
        tags (list[str] | Unset):
        status (list[WorkflowStatusEnum] | Unset):
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorDto | ListWorkflowResponse | ValidationErrorDto | str
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            offset=offset,
            order_direction=order_direction,
            order_by=order_by,
            query=query,
            tags=tags,
            status=status,
            idempotency_key=idempotency_key,
        )
    ).parsed
