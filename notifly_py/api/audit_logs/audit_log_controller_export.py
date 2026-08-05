from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.audit_log_controller_export_format import AuditLogControllerExportFormat
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    resource: str | Unset = UNSET,
    action: str | Unset = UNSET,
    actor_id: str | Unset = UNSET,
    start_date: str | Unset = UNSET,
    end_date: str | Unset = UNSET,
    format_: AuditLogControllerExportFormat | Unset = AuditLogControllerExportFormat.CSV,
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

    json_format_: str | Unset = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_.value

    params["format"] = json_format_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/audit-logs/export",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == 200:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any]:
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
    format_: AuditLogControllerExportFormat | Unset = AuditLogControllerExportFormat.CSV,
    idempotency_key: str | Unset = UNSET,
) -> Response[Any]:
    """Export audit logs

     Stream the organization audit trail as CSV or NDJSON for compliance evidence or SIEM ingestion.
    Accepts the same filters as the list endpoint.

    Args:
        resource (str | Unset):
        action (str | Unset):
        actor_id (str | Unset):
        start_date (str | Unset):
        end_date (str | Unset):
        format_ (AuditLogControllerExportFormat | Unset):  Default:
            AuditLogControllerExportFormat.CSV.
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        resource=resource,
        action=action,
        actor_id=actor_id,
        start_date=start_date,
        end_date=end_date,
        format_=format_,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    resource: str | Unset = UNSET,
    action: str | Unset = UNSET,
    actor_id: str | Unset = UNSET,
    start_date: str | Unset = UNSET,
    end_date: str | Unset = UNSET,
    format_: AuditLogControllerExportFormat | Unset = AuditLogControllerExportFormat.CSV,
    idempotency_key: str | Unset = UNSET,
) -> Response[Any]:
    """Export audit logs

     Stream the organization audit trail as CSV or NDJSON for compliance evidence or SIEM ingestion.
    Accepts the same filters as the list endpoint.

    Args:
        resource (str | Unset):
        action (str | Unset):
        actor_id (str | Unset):
        start_date (str | Unset):
        end_date (str | Unset):
        format_ (AuditLogControllerExportFormat | Unset):  Default:
            AuditLogControllerExportFormat.CSV.
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        resource=resource,
        action=action,
        actor_id=actor_id,
        start_date=start_date,
        end_date=end_date,
        format_=format_,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
