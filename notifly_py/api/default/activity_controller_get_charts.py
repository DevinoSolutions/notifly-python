from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.activity_controller_get_charts_report_type_item import ActivityControllerGetChartsReportTypeItem
from ...models.activity_controller_get_charts_statuses_item import ActivityControllerGetChartsStatusesItem
from ...models.get_charts_response_dto import GetChartsResponseDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    created_at_gte: str | Unset = UNSET,
    created_at_lte: str | Unset = UNSET,
    report_type: list[ActivityControllerGetChartsReportTypeItem],
    workflow_ids: list[str] | Unset = UNSET,
    subscriber_ids: list[str] | Unset = UNSET,
    transaction_ids: list[str] | Unset = UNSET,
    statuses: list[ActivityControllerGetChartsStatusesItem] | Unset = UNSET,
    channels: list[str] | Unset = UNSET,
    topic_key: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["idempotency-key"] = idempotency_key

    params: dict[str, Any] = {}

    params["createdAtGte"] = created_at_gte

    params["createdAtLte"] = created_at_lte

    json_report_type = []
    for report_type_item_data in report_type:
        report_type_item = report_type_item_data.value
        json_report_type.append(report_type_item)

    params["reportType"] = json_report_type

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

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/activity/charts",
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GetChartsResponseDto | None:
    if response.status_code == 200:
        response_200 = GetChartsResponseDto.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[GetChartsResponseDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    created_at_gte: str | Unset = UNSET,
    created_at_lte: str | Unset = UNSET,
    report_type: list[ActivityControllerGetChartsReportTypeItem],
    workflow_ids: list[str] | Unset = UNSET,
    subscriber_ids: list[str] | Unset = UNSET,
    transaction_ids: list[str] | Unset = UNSET,
    statuses: list[ActivityControllerGetChartsStatusesItem] | Unset = UNSET,
    channels: list[str] | Unset = UNSET,
    topic_key: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> Response[GetChartsResponseDto]:
    """Retrieve activity charts

     Retrieve chart data for activity analytics and metrics visualization.

    Args:
        created_at_gte (str | Unset):
        created_at_lte (str | Unset):
        report_type (list[ActivityControllerGetChartsReportTypeItem]):
        workflow_ids (list[str] | Unset):
        subscriber_ids (list[str] | Unset):
        transaction_ids (list[str] | Unset):
        statuses (list[ActivityControllerGetChartsStatusesItem] | Unset):
        channels (list[str] | Unset):
        topic_key (str | Unset):
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetChartsResponseDto]
    """

    kwargs = _get_kwargs(
        created_at_gte=created_at_gte,
        created_at_lte=created_at_lte,
        report_type=report_type,
        workflow_ids=workflow_ids,
        subscriber_ids=subscriber_ids,
        transaction_ids=transaction_ids,
        statuses=statuses,
        channels=channels,
        topic_key=topic_key,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    created_at_gte: str | Unset = UNSET,
    created_at_lte: str | Unset = UNSET,
    report_type: list[ActivityControllerGetChartsReportTypeItem],
    workflow_ids: list[str] | Unset = UNSET,
    subscriber_ids: list[str] | Unset = UNSET,
    transaction_ids: list[str] | Unset = UNSET,
    statuses: list[ActivityControllerGetChartsStatusesItem] | Unset = UNSET,
    channels: list[str] | Unset = UNSET,
    topic_key: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> GetChartsResponseDto | None:
    """Retrieve activity charts

     Retrieve chart data for activity analytics and metrics visualization.

    Args:
        created_at_gte (str | Unset):
        created_at_lte (str | Unset):
        report_type (list[ActivityControllerGetChartsReportTypeItem]):
        workflow_ids (list[str] | Unset):
        subscriber_ids (list[str] | Unset):
        transaction_ids (list[str] | Unset):
        statuses (list[ActivityControllerGetChartsStatusesItem] | Unset):
        channels (list[str] | Unset):
        topic_key (str | Unset):
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetChartsResponseDto
    """

    return sync_detailed(
        client=client,
        created_at_gte=created_at_gte,
        created_at_lte=created_at_lte,
        report_type=report_type,
        workflow_ids=workflow_ids,
        subscriber_ids=subscriber_ids,
        transaction_ids=transaction_ids,
        statuses=statuses,
        channels=channels,
        topic_key=topic_key,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    created_at_gte: str | Unset = UNSET,
    created_at_lte: str | Unset = UNSET,
    report_type: list[ActivityControllerGetChartsReportTypeItem],
    workflow_ids: list[str] | Unset = UNSET,
    subscriber_ids: list[str] | Unset = UNSET,
    transaction_ids: list[str] | Unset = UNSET,
    statuses: list[ActivityControllerGetChartsStatusesItem] | Unset = UNSET,
    channels: list[str] | Unset = UNSET,
    topic_key: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> Response[GetChartsResponseDto]:
    """Retrieve activity charts

     Retrieve chart data for activity analytics and metrics visualization.

    Args:
        created_at_gte (str | Unset):
        created_at_lte (str | Unset):
        report_type (list[ActivityControllerGetChartsReportTypeItem]):
        workflow_ids (list[str] | Unset):
        subscriber_ids (list[str] | Unset):
        transaction_ids (list[str] | Unset):
        statuses (list[ActivityControllerGetChartsStatusesItem] | Unset):
        channels (list[str] | Unset):
        topic_key (str | Unset):
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetChartsResponseDto]
    """

    kwargs = _get_kwargs(
        created_at_gte=created_at_gte,
        created_at_lte=created_at_lte,
        report_type=report_type,
        workflow_ids=workflow_ids,
        subscriber_ids=subscriber_ids,
        transaction_ids=transaction_ids,
        statuses=statuses,
        channels=channels,
        topic_key=topic_key,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    created_at_gte: str | Unset = UNSET,
    created_at_lte: str | Unset = UNSET,
    report_type: list[ActivityControllerGetChartsReportTypeItem],
    workflow_ids: list[str] | Unset = UNSET,
    subscriber_ids: list[str] | Unset = UNSET,
    transaction_ids: list[str] | Unset = UNSET,
    statuses: list[ActivityControllerGetChartsStatusesItem] | Unset = UNSET,
    channels: list[str] | Unset = UNSET,
    topic_key: str | Unset = UNSET,
    idempotency_key: str | Unset = UNSET,
) -> GetChartsResponseDto | None:
    """Retrieve activity charts

     Retrieve chart data for activity analytics and metrics visualization.

    Args:
        created_at_gte (str | Unset):
        created_at_lte (str | Unset):
        report_type (list[ActivityControllerGetChartsReportTypeItem]):
        workflow_ids (list[str] | Unset):
        subscriber_ids (list[str] | Unset):
        transaction_ids (list[str] | Unset):
        statuses (list[ActivityControllerGetChartsStatusesItem] | Unset):
        channels (list[str] | Unset):
        topic_key (str | Unset):
        idempotency_key (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetChartsResponseDto
    """

    return (
        await asyncio_detailed(
            client=client,
            created_at_gte=created_at_gte,
            created_at_lte=created_at_lte,
            report_type=report_type,
            workflow_ids=workflow_ids,
            subscriber_ids=subscriber_ids,
            transaction_ids=transaction_ids,
            statuses=statuses,
            channels=channels,
            topic_key=topic_key,
            idempotency_key=idempotency_key,
        )
    ).parsed
