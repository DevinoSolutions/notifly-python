from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.audit_log_controller_list_response_200 import AuditLogControllerListResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    resource: str | Unset = UNSET,
    action: str | Unset = UNSET,
    actor_id: str | Unset = UNSET,
    start_date: str | Unset = UNSET,
    end_date: str | Unset = UNSET,
    page: float | Unset = 0.0,
    limit: float | Unset = 20.0,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["idempotency-key"] = idempotency_key

    params: dict[str, Any] = {}

    params["resource"] = resource

    params["action"] = action

    params["actorId"] = actor_id

    params["startDate"] = start_date

    params["endDate"] = end_date

    params["page"] = page

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/audit-logs",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AuditLogControllerListResponse200 | None:
    if response.status_code == 200:
        response_200 = AuditLogControllerListResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AuditLogControllerListResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    resource: str | Unset = UNSET,
    action: str | Unset = UNSET,
    actor_id: str | Unset = UNSET,
    start_date: str | Unset = UNSET,
    end_date: str | Unset = UNSET,
    page: float | Unset = 0.0,
    limit: float | Unset = 20.0,
    idempotency_key: str | Unset = UNSET,
) -> Response[AuditLogControllerListResponse200]:
    """List audit logs

     Retrieve a paginated list of audit log entries for the current organization.

    Args:
        resource (str | Unset):
        action (str | Unset):
        actor_id (str | Unset):
        start_date (str | Unset):
        end_date (str | Unset):
        page (float | Unset):  Default: 0.0.
        limit (float | Unset):  Default: 20.0.
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuditLogControllerListResponse200]
    """

    kwargs = _get_kwargs(
        resource=resource,
        action=action,
        actor_id=actor_id,
        start_date=start_date,
        end_date=end_date,
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
    resource: str | Unset = UNSET,
    action: str | Unset = UNSET,
    actor_id: str | Unset = UNSET,
    start_date: str | Unset = UNSET,
    end_date: str | Unset = UNSET,
    page: float | Unset = 0.0,
    limit: float | Unset = 20.0,
    idempotency_key: str | Unset = UNSET,
) -> AuditLogControllerListResponse200 | None:
    """List audit logs

     Retrieve a paginated list of audit log entries for the current organization.

    Args:
        resource (str | Unset):
        action (str | Unset):
        actor_id (str | Unset):
        start_date (str | Unset):
        end_date (str | Unset):
        page (float | Unset):  Default: 0.0.
        limit (float | Unset):  Default: 20.0.
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuditLogControllerListResponse200
    """

    return sync_detailed(
        client=client,
        resource=resource,
        action=action,
        actor_id=actor_id,
        start_date=start_date,
        end_date=end_date,
        page=page,
        limit=limit,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    resource: str | Unset = UNSET,
    action: str | Unset = UNSET,
    actor_id: str | Unset = UNSET,
    start_date: str | Unset = UNSET,
    end_date: str | Unset = UNSET,
    page: float | Unset = 0.0,
    limit: float | Unset = 20.0,
    idempotency_key: str | Unset = UNSET,
) -> Response[AuditLogControllerListResponse200]:
    """List audit logs

     Retrieve a paginated list of audit log entries for the current organization.

    Args:
        resource (str | Unset):
        action (str | Unset):
        actor_id (str | Unset):
        start_date (str | Unset):
        end_date (str | Unset):
        page (float | Unset):  Default: 0.0.
        limit (float | Unset):  Default: 20.0.
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuditLogControllerListResponse200]
    """

    kwargs = _get_kwargs(
        resource=resource,
        action=action,
        actor_id=actor_id,
        start_date=start_date,
        end_date=end_date,
        page=page,
        limit=limit,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    resource: str | Unset = UNSET,
    action: str | Unset = UNSET,
    actor_id: str | Unset = UNSET,
    start_date: str | Unset = UNSET,
    end_date: str | Unset = UNSET,
    page: float | Unset = 0.0,
    limit: float | Unset = 20.0,
    idempotency_key: str | Unset = UNSET,
) -> AuditLogControllerListResponse200 | None:
    """List audit logs

     Retrieve a paginated list of audit log entries for the current organization.

    Args:
        resource (str | Unset):
        action (str | Unset):
        actor_id (str | Unset):
        start_date (str | Unset):
        end_date (str | Unset):
        page (float | Unset):  Default: 0.0.
        limit (float | Unset):  Default: 20.0.
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuditLogControllerListResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            resource=resource,
            action=action,
            actor_id=actor_id,
            start_date=start_date,
            end_date=end_date,
            page=page,
            limit=limit,
            idempotency_key=idempotency_key,
        )
    ).parsed
