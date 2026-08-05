from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_workflow_run_response_dto import GetWorkflowRunResponseDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    workflow_run_id: str,
    *,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["idempotency-key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/activity/workflow-runs/{workflow_run_id}".format(
            workflow_run_id=quote(str(workflow_run_id), safe=""),
        ),
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetWorkflowRunResponseDto | None:
    if response.status_code == 200:
        response_200 = GetWorkflowRunResponseDto.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetWorkflowRunResponseDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    workflow_run_id: str,
    *,
    client: AuthenticatedClient,
    idempotency_key: str | Unset = UNSET,
) -> Response[GetWorkflowRunResponseDto]:
    """Retrieve workflow run

     Retrieve detailed information for a specific workflow run by ID.

    Args:
        workflow_run_id (str):
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetWorkflowRunResponseDto]
    """

    kwargs = _get_kwargs(
        workflow_run_id=workflow_run_id,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    workflow_run_id: str,
    *,
    client: AuthenticatedClient,
    idempotency_key: str | Unset = UNSET,
) -> GetWorkflowRunResponseDto | None:
    """Retrieve workflow run

     Retrieve detailed information for a specific workflow run by ID.

    Args:
        workflow_run_id (str):
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetWorkflowRunResponseDto
    """

    return sync_detailed(
        workflow_run_id=workflow_run_id,
        client=client,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    workflow_run_id: str,
    *,
    client: AuthenticatedClient,
    idempotency_key: str | Unset = UNSET,
) -> Response[GetWorkflowRunResponseDto]:
    """Retrieve workflow run

     Retrieve detailed information for a specific workflow run by ID.

    Args:
        workflow_run_id (str):
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetWorkflowRunResponseDto]
    """

    kwargs = _get_kwargs(
        workflow_run_id=workflow_run_id,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    workflow_run_id: str,
    *,
    client: AuthenticatedClient,
    idempotency_key: str | Unset = UNSET,
) -> GetWorkflowRunResponseDto | None:
    """Retrieve workflow run

     Retrieve detailed information for a specific workflow run by ID.

    Args:
        workflow_run_id (str):
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetWorkflowRunResponseDto
    """

    return (
        await asyncio_detailed(
            workflow_run_id=workflow_run_id,
            client=client,
            idempotency_key=idempotency_key,
        )
    ).parsed
