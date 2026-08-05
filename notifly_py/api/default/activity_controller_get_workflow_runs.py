from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.activity_controller_get_workflow_runs_severity_item import ActivityControllerGetWorkflowRunsSeverityItem
from ...models.activity_controller_get_workflow_runs_statuses_item import ActivityControllerGetWorkflowRunsStatusesItem
from ...models.get_workflow_runs_response_dto import GetWorkflowRunsResponseDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    limit: float = 10.0,
    cursor: str | Unset = UNSET,
    workflow_ids: list[str] | Unset = UNSET,
    subscriber_ids: list[str] | Unset = UNSET,
    transaction_ids: list[str] | Unset = UNSET,
    statuses: list[ActivityControllerGetWorkflowRunsStatusesItem] | Unset = UNSET,
    channels: list[str] | Unset = UNSET,
    topic_key: str | Unset = UNSET,
    subscription_id: str | Unset = UNSET,
    created_gte: str | Unset = UNSET,
    created_lte: str | Unset = UNSET,
    severity: list[ActivityControllerGetWorkflowRunsSeverityItem] | Unset = UNSET,
    context_keys: list[str] | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["idempotency-key"] = idempotency_key

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["cursor"] = cursor

    json_workflow_ids: list[str] | Unset = UNSET
    if not isinstance(workflow_ids, Unset):
        json_workflow_ids = workflow_ids

    params["workflowIds"] = json_workflow_ids

    json_subscriber_ids: list[str] | Unset = UNSET
    if not isinstance(subscriber_ids, Unset):
        json_subscriber_ids = subscriber_ids

    params["subscriberIds"] = json_subscriber_ids

    json_transaction_ids: list[str] | Unset = UNSET
    if not isinstance(transaction_ids, Unset):
        json_transaction_ids = transaction_ids

    params["transactionIds"] = json_transaction_ids

    json_statuses: list[str] | Unset = UNSET
    if not isinstance(statuses, Unset):
        json_statuses = []
        for statuses_item_data in statuses:
            statuses_item = statuses_item_data.value
            json_statuses.append(statuses_item)

    params["statuses"] = json_statuses

    json_channels: list[str] | Unset = UNSET
    if not isinstance(channels, Unset):
        json_channels = channels

    params["channels"] = json_channels

    params["topicKey"] = topic_key

    params["subscriptionId"] = subscription_id

    params["createdGte"] = created_gte

    params["createdLte"] = created_lte

    json_severity: list[str] | Unset = UNSET
    if not isinstance(severity, Unset):
        json_severity = []
        for severity_item_data in severity:
            severity_item = severity_item_data.value
            json_severity.append(severity_item)

    params["severity"] = json_severity

    json_context_keys: list[str] | Unset = UNSET
    if not isinstance(context_keys, Unset):
        json_context_keys = context_keys

    params["contextKeys"] = json_context_keys

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/activity/workflow-runs",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> GetWorkflowRunsResponseDto | None:
    if response.status_code == 200:
        response_200 = GetWorkflowRunsResponseDto.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetWorkflowRunsResponseDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    limit: float = 10.0,
    cursor: str | Unset = UNSET,
    workflow_ids: list[str] | Unset = UNSET,
    subscriber_ids: list[str] | Unset = UNSET,
    transaction_ids: list[str] | Unset = UNSET,
    statuses: list[ActivityControllerGetWorkflowRunsStatusesItem] | Unset = UNSET,
    channels: list[str] | Unset = UNSET,
    topic_key: str | Unset = UNSET,
    subscription_id: str | Unset = UNSET,
    created_gte: str | Unset = UNSET,
    created_lte: str | Unset = UNSET,
    severity: list[ActivityControllerGetWorkflowRunsSeverityItem] | Unset = UNSET,
    context_keys: list[str] | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> Response[GetWorkflowRunsResponseDto]:
    """List workflow runs

     Retrieve a list of workflow runs with optional filtering and pagination.

    Args:
        limit (float):  Default: 10.0.
        cursor (str | Unset):
        workflow_ids (list[str] | Unset):
        subscriber_ids (list[str] | Unset):
        transaction_ids (list[str] | Unset):
        statuses (list[ActivityControllerGetWorkflowRunsStatusesItem] | Unset):
        channels (list[str] | Unset):
        topic_key (str | Unset):
        subscription_id (str | Unset):
        created_gte (str | Unset):
        created_lte (str | Unset):
        severity (list[ActivityControllerGetWorkflowRunsSeverityItem] | Unset):
        context_keys (list[str] | Unset):
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetWorkflowRunsResponseDto]
    """

    kwargs = _get_kwargs(
        limit=limit,
        cursor=cursor,
        workflow_ids=workflow_ids,
        subscriber_ids=subscriber_ids,
        transaction_ids=transaction_ids,
        statuses=statuses,
        channels=channels,
        topic_key=topic_key,
        subscription_id=subscription_id,
        created_gte=created_gte,
        created_lte=created_lte,
        severity=severity,
        context_keys=context_keys,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    limit: float = 10.0,
    cursor: str | Unset = UNSET,
    workflow_ids: list[str] | Unset = UNSET,
    subscriber_ids: list[str] | Unset = UNSET,
    transaction_ids: list[str] | Unset = UNSET,
    statuses: list[ActivityControllerGetWorkflowRunsStatusesItem] | Unset = UNSET,
    channels: list[str] | Unset = UNSET,
    topic_key: str | Unset = UNSET,
    subscription_id: str | Unset = UNSET,
    created_gte: str | Unset = UNSET,
    created_lte: str | Unset = UNSET,
    severity: list[ActivityControllerGetWorkflowRunsSeverityItem] | Unset = UNSET,
    context_keys: list[str] | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> GetWorkflowRunsResponseDto | None:
    """List workflow runs

     Retrieve a list of workflow runs with optional filtering and pagination.

    Args:
        limit (float):  Default: 10.0.
        cursor (str | Unset):
        workflow_ids (list[str] | Unset):
        subscriber_ids (list[str] | Unset):
        transaction_ids (list[str] | Unset):
        statuses (list[ActivityControllerGetWorkflowRunsStatusesItem] | Unset):
        channels (list[str] | Unset):
        topic_key (str | Unset):
        subscription_id (str | Unset):
        created_gte (str | Unset):
        created_lte (str | Unset):
        severity (list[ActivityControllerGetWorkflowRunsSeverityItem] | Unset):
        context_keys (list[str] | Unset):
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetWorkflowRunsResponseDto
    """

    return sync_detailed(
        client=client,
        limit=limit,
        cursor=cursor,
        workflow_ids=workflow_ids,
        subscriber_ids=subscriber_ids,
        transaction_ids=transaction_ids,
        statuses=statuses,
        channels=channels,
        topic_key=topic_key,
        subscription_id=subscription_id,
        created_gte=created_gte,
        created_lte=created_lte,
        severity=severity,
        context_keys=context_keys,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    limit: float = 10.0,
    cursor: str | Unset = UNSET,
    workflow_ids: list[str] | Unset = UNSET,
    subscriber_ids: list[str] | Unset = UNSET,
    transaction_ids: list[str] | Unset = UNSET,
    statuses: list[ActivityControllerGetWorkflowRunsStatusesItem] | Unset = UNSET,
    channels: list[str] | Unset = UNSET,
    topic_key: str | Unset = UNSET,
    subscription_id: str | Unset = UNSET,
    created_gte: str | Unset = UNSET,
    created_lte: str | Unset = UNSET,
    severity: list[ActivityControllerGetWorkflowRunsSeverityItem] | Unset = UNSET,
    context_keys: list[str] | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> Response[GetWorkflowRunsResponseDto]:
    """List workflow runs

     Retrieve a list of workflow runs with optional filtering and pagination.

    Args:
        limit (float):  Default: 10.0.
        cursor (str | Unset):
        workflow_ids (list[str] | Unset):
        subscriber_ids (list[str] | Unset):
        transaction_ids (list[str] | Unset):
        statuses (list[ActivityControllerGetWorkflowRunsStatusesItem] | Unset):
        channels (list[str] | Unset):
        topic_key (str | Unset):
        subscription_id (str | Unset):
        created_gte (str | Unset):
        created_lte (str | Unset):
        severity (list[ActivityControllerGetWorkflowRunsSeverityItem] | Unset):
        context_keys (list[str] | Unset):
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetWorkflowRunsResponseDto]
    """

    kwargs = _get_kwargs(
        limit=limit,
        cursor=cursor,
        workflow_ids=workflow_ids,
        subscriber_ids=subscriber_ids,
        transaction_ids=transaction_ids,
        statuses=statuses,
        channels=channels,
        topic_key=topic_key,
        subscription_id=subscription_id,
        created_gte=created_gte,
        created_lte=created_lte,
        severity=severity,
        context_keys=context_keys,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    limit: float = 10.0,
    cursor: str | Unset = UNSET,
    workflow_ids: list[str] | Unset = UNSET,
    subscriber_ids: list[str] | Unset = UNSET,
    transaction_ids: list[str] | Unset = UNSET,
    statuses: list[ActivityControllerGetWorkflowRunsStatusesItem] | Unset = UNSET,
    channels: list[str] | Unset = UNSET,
    topic_key: str | Unset = UNSET,
    subscription_id: str | Unset = UNSET,
    created_gte: str | Unset = UNSET,
    created_lte: str | Unset = UNSET,
    severity: list[ActivityControllerGetWorkflowRunsSeverityItem] | Unset = UNSET,
    context_keys: list[str] | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> GetWorkflowRunsResponseDto | None:
    """List workflow runs

     Retrieve a list of workflow runs with optional filtering and pagination.

    Args:
        limit (float):  Default: 10.0.
        cursor (str | Unset):
        workflow_ids (list[str] | Unset):
        subscriber_ids (list[str] | Unset):
        transaction_ids (list[str] | Unset):
        statuses (list[ActivityControllerGetWorkflowRunsStatusesItem] | Unset):
        channels (list[str] | Unset):
        topic_key (str | Unset):
        subscription_id (str | Unset):
        created_gte (str | Unset):
        created_lte (str | Unset):
        severity (list[ActivityControllerGetWorkflowRunsSeverityItem] | Unset):
        context_keys (list[str] | Unset):
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetWorkflowRunsResponseDto
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            cursor=cursor,
            workflow_ids=workflow_ids,
            subscriber_ids=subscriber_ids,
            transaction_ids=transaction_ids,
            statuses=statuses,
            channels=channels,
            topic_key=topic_key,
            subscription_id=subscription_id,
            created_gte=created_gte,
            created_lte=created_lte,
            severity=severity,
            context_keys=context_keys,
            idempotency_key=idempotency_key,
        )
    ).parsed
