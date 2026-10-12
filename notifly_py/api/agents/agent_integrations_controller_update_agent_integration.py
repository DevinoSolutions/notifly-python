from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.agent_integration_response_dto import AgentIntegrationResponseDto
from ...models.error_dto import ErrorDto
from ...models.update_agent_integration_request_dto import UpdateAgentIntegrationRequestDto
from ...models.validation_error_dto import ValidationErrorDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    identifier: str,
    agent_integration_id: str,
    *,
    body: UpdateAgentIntegrationRequestDto,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["idempotency-key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/v1/agents/{identifier}/integrations/{agent_integration_id}".format(
            identifier=quote(str(identifier), safe=""),
            agent_integration_id=quote(str(agent_integration_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AgentIntegrationResponseDto | Any | ErrorDto | ValidationErrorDto | str | None:
    if response.status_code == 200:
        response_200 = AgentIntegrationResponseDto.from_dict(response.json())

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
        response_404 = cast(Any, None)
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
) -> Response[AgentIntegrationResponseDto | Any | ErrorDto | ValidationErrorDto | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    identifier: str,
    agent_integration_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateAgentIntegrationRequestDto,
    idempotency_key: str | Unset = UNSET,
) -> Response[AgentIntegrationResponseDto | Any | ErrorDto | ValidationErrorDto | str]:
    """Update an agent integration

     Update which integration a link points to (by integration **identifier**, not the internal _id).

    Args:
        identifier (str):
        agent_integration_id (str):
        idempotency_key (str | Unset):
        body (UpdateAgentIntegrationRequestDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentIntegrationResponseDto | Any | ErrorDto | ValidationErrorDto | str]
    """

    kwargs = _get_kwargs(
        identifier=identifier,
        agent_integration_id=agent_integration_id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    identifier: str,
    agent_integration_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateAgentIntegrationRequestDto,
    idempotency_key: str | Unset = UNSET,
) -> AgentIntegrationResponseDto | Any | ErrorDto | ValidationErrorDto | str | None:
    """Update an agent integration

     Update which integration a link points to (by integration **identifier**, not the internal _id).

    Args:
        identifier (str):
        agent_integration_id (str):
        idempotency_key (str | Unset):
        body (UpdateAgentIntegrationRequestDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentIntegrationResponseDto | Any | ErrorDto | ValidationErrorDto | str
    """

    return sync_detailed(
        identifier=identifier,
        agent_integration_id=agent_integration_id,
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    identifier: str,
    agent_integration_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateAgentIntegrationRequestDto,
    idempotency_key: str | Unset = UNSET,
) -> Response[AgentIntegrationResponseDto | Any | ErrorDto | ValidationErrorDto | str]:
    """Update an agent integration

     Update which integration a link points to (by integration **identifier**, not the internal _id).

    Args:
        identifier (str):
        agent_integration_id (str):
        idempotency_key (str | Unset):
        body (UpdateAgentIntegrationRequestDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AgentIntegrationResponseDto | Any | ErrorDto | ValidationErrorDto | str]
    """

    kwargs = _get_kwargs(
        identifier=identifier,
        agent_integration_id=agent_integration_id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    identifier: str,
    agent_integration_id: str,
    *,
    client: AuthenticatedClient,
    body: UpdateAgentIntegrationRequestDto,
    idempotency_key: str | Unset = UNSET,
) -> AgentIntegrationResponseDto | Any | ErrorDto | ValidationErrorDto | str | None:
    """Update an agent integration

     Update which integration a link points to (by integration **identifier**, not the internal _id).

    Args:
        identifier (str):
        agent_integration_id (str):
        idempotency_key (str | Unset):
        body (UpdateAgentIntegrationRequestDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AgentIntegrationResponseDto | Any | ErrorDto | ValidationErrorDto | str
    """

    return (
        await asyncio_detailed(
            identifier=identifier,
            agent_integration_id=agent_integration_id,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
