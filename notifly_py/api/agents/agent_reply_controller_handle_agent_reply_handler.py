from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.agent_reply_payload_dto import AgentReplyPayloadDto
from ...models.error_dto import ErrorDto
from ...models.sent_message_info_dto import SentMessageInfoDto
from ...models.validation_error_dto import ValidationErrorDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    agent_id: str,
    *,
    body: AgentReplyPayloadDto,
    idempotency_key: str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(idempotency_key, Unset):
        headers["idempotency-key"] = idempotency_key

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/agents/{agent_id}/reply".format(
            agent_id=quote(str(agent_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | ErrorDto | None | SentMessageInfoDto | ValidationErrorDto | str | None:
    if response.status_code == 200:

        def _parse_response_200(data: object) -> None | SentMessageInfoDto:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_1 = SentMessageInfoDto.from_dict(data)

                return response_200_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SentMessageInfoDto, data)

        response_200 = _parse_response_200(response.json())

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
) -> Response[Any | ErrorDto | None | SentMessageInfoDto | ValidationErrorDto | str]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    agent_id: str,
    *,
    client: AuthenticatedClient,
    body: AgentReplyPayloadDto,
    idempotency_key: str | Unset = UNSET,
) -> Response[Any | ErrorDto | None | SentMessageInfoDto | ValidationErrorDto | str]:
    r"""Send an agent reply

     Send a message or side-effect into an existing agent conversation from your backend.

    Use this endpoint when you are not using `@notifly/framework` (for example Python, Go, PHP, .NET, or
    Java SDKs),
    or when a server process outside the bridge needs to post into a live conversation.

    **Message actions**
    - `reply` — markdown, interactive card, or tool-approval card (optional `files`)
    - `edit` — update a previously delivered message in place
    - `deleteMessages` — remove rendered platform messages (history is kept)
    - `addReactions` — add emoji reactions to existing messages

    **Turn control**
    - `typing` — `{ status?: string }` to set status, or `\"stop\"` to clear
    - `resolve` — mark the conversation resolved (optionally with a final reply)
    - `error: true` — report a customer-runtime failure (cannot combine with other actions)

    **Signals & tools**
    - `signals` — metadata set/delete/clear, or trigger a Novu workflow
    - `toolResults` — persist tool outputs into conversation history
    - `toolApprovalRequest` — ledger a gated tool call (pair with an approval card reply)

    Returns `{ data: { messageId, platformThreadId } }` when a reply or edit is delivered;
    otherwise `{ data: null }`.

    Args:
        agent_id (str):
        idempotency_key (str | Unset):
        body (AgentReplyPayloadDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorDto | None | SentMessageInfoDto | ValidationErrorDto | str]
    """

    kwargs = _get_kwargs(
        agent_id=agent_id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    agent_id: str,
    *,
    client: AuthenticatedClient,
    body: AgentReplyPayloadDto,
    idempotency_key: str | Unset = UNSET,
) -> Any | ErrorDto | None | SentMessageInfoDto | ValidationErrorDto | str | None:
    r"""Send an agent reply

     Send a message or side-effect into an existing agent conversation from your backend.

    Use this endpoint when you are not using `@notifly/framework` (for example Python, Go, PHP, .NET, or
    Java SDKs),
    or when a server process outside the bridge needs to post into a live conversation.

    **Message actions**
    - `reply` — markdown, interactive card, or tool-approval card (optional `files`)
    - `edit` — update a previously delivered message in place
    - `deleteMessages` — remove rendered platform messages (history is kept)
    - `addReactions` — add emoji reactions to existing messages

    **Turn control**
    - `typing` — `{ status?: string }` to set status, or `\"stop\"` to clear
    - `resolve` — mark the conversation resolved (optionally with a final reply)
    - `error: true` — report a customer-runtime failure (cannot combine with other actions)

    **Signals & tools**
    - `signals` — metadata set/delete/clear, or trigger a Novu workflow
    - `toolResults` — persist tool outputs into conversation history
    - `toolApprovalRequest` — ledger a gated tool call (pair with an approval card reply)

    Returns `{ data: { messageId, platformThreadId } }` when a reply or edit is delivered;
    otherwise `{ data: null }`.

    Args:
        agent_id (str):
        idempotency_key (str | Unset):
        body (AgentReplyPayloadDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorDto | None | SentMessageInfoDto | ValidationErrorDto | str
    """

    return sync_detailed(
        agent_id=agent_id,
        client=client,
        body=body,
        idempotency_key=idempotency_key,
    ).parsed


async def asyncio_detailed(
    agent_id: str,
    *,
    client: AuthenticatedClient,
    body: AgentReplyPayloadDto,
    idempotency_key: str | Unset = UNSET,
) -> Response[Any | ErrorDto | None | SentMessageInfoDto | ValidationErrorDto | str]:
    r"""Send an agent reply

     Send a message or side-effect into an existing agent conversation from your backend.

    Use this endpoint when you are not using `@notifly/framework` (for example Python, Go, PHP, .NET, or
    Java SDKs),
    or when a server process outside the bridge needs to post into a live conversation.

    **Message actions**
    - `reply` — markdown, interactive card, or tool-approval card (optional `files`)
    - `edit` — update a previously delivered message in place
    - `deleteMessages` — remove rendered platform messages (history is kept)
    - `addReactions` — add emoji reactions to existing messages

    **Turn control**
    - `typing` — `{ status?: string }` to set status, or `\"stop\"` to clear
    - `resolve` — mark the conversation resolved (optionally with a final reply)
    - `error: true` — report a customer-runtime failure (cannot combine with other actions)

    **Signals & tools**
    - `signals` — metadata set/delete/clear, or trigger a Novu workflow
    - `toolResults` — persist tool outputs into conversation history
    - `toolApprovalRequest` — ledger a gated tool call (pair with an approval card reply)

    Returns `{ data: { messageId, platformThreadId } }` when a reply or edit is delivered;
    otherwise `{ data: null }`.

    Args:
        agent_id (str):
        idempotency_key (str | Unset):
        body (AgentReplyPayloadDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorDto | None | SentMessageInfoDto | ValidationErrorDto | str]
    """

    kwargs = _get_kwargs(
        agent_id=agent_id,
        body=body,
        idempotency_key=idempotency_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    agent_id: str,
    *,
    client: AuthenticatedClient,
    body: AgentReplyPayloadDto,
    idempotency_key: str | Unset = UNSET,
) -> Any | ErrorDto | None | SentMessageInfoDto | ValidationErrorDto | str | None:
    r"""Send an agent reply

     Send a message or side-effect into an existing agent conversation from your backend.

    Use this endpoint when you are not using `@notifly/framework` (for example Python, Go, PHP, .NET, or
    Java SDKs),
    or when a server process outside the bridge needs to post into a live conversation.

    **Message actions**
    - `reply` — markdown, interactive card, or tool-approval card (optional `files`)
    - `edit` — update a previously delivered message in place
    - `deleteMessages` — remove rendered platform messages (history is kept)
    - `addReactions` — add emoji reactions to existing messages

    **Turn control**
    - `typing` — `{ status?: string }` to set status, or `\"stop\"` to clear
    - `resolve` — mark the conversation resolved (optionally with a final reply)
    - `error: true` — report a customer-runtime failure (cannot combine with other actions)

    **Signals & tools**
    - `signals` — metadata set/delete/clear, or trigger a Novu workflow
    - `toolResults` — persist tool outputs into conversation history
    - `toolApprovalRequest` — ledger a gated tool call (pair with an approval card reply)

    Returns `{ data: { messageId, platformThreadId } }` when a reply or edit is delivered;
    otherwise `{ data: null }`.

    Args:
        agent_id (str):
        idempotency_key (str | Unset):
        body (AgentReplyPayloadDto):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorDto | None | SentMessageInfoDto | ValidationErrorDto | str
    """

    return (
        await asyncio_detailed(
            agent_id=agent_id,
            client=client,
            body=body,
            idempotency_key=idempotency_key,
        )
    ).parsed
