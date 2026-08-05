"""The ergonomic, hand-written surface over the generated client.

HAND-WRITTEN — not produced by ``openapi-python-client``. See ``scripts/regenerate.sh``.

::

    from notifly_py import Notifly

    notifly = Notifly("<secret key>")
    result = notifly.events.trigger(workflow="welcome", to="subscriber_123", payload={"name": "Ada"})

Design rules:

* **Grouped, human names.** ``notifly.events.trigger(...)`` instead of
  ``events_controller_trigger.sync(client=client, body=...)``.
* **Errors raise.** Every method returns the success model or raises a
  :mod:`notifly_py.exceptions` subclass — no fourteen-member unions to narrow.
* **The escape hatch stays open.** ``notifly.client`` is the underlying
  :class:`notifly_py.NotiflyClient`; every generated module still accepts it.
* **Public surface only.** The sixteen bearer-only operations listed in
  :mod:`notifly_py.internal_ops` are deliberately absent.
* ``**kwargs`` on a method is forwarded verbatim to the underlying generated operation, so
  every documented query parameter remains reachable; ``None`` values are dropped.
"""

from __future__ import annotations

from collections.abc import AsyncIterator, Iterator, Mapping, Sequence
from typing import Any

from .api.events import events_controller_broadcast_event_to_all as _events_broadcast
from .api.events import events_controller_cancel as _events_cancel
from .api.events import events_controller_trigger as _events_trigger
from .api.events import events_controller_trigger_bulk as _events_trigger_bulk
from .api.integrations import integrations_controller_create_integration as _integrations_create
from .api.integrations import integrations_controller_get_active_integrations as _integrations_active
from .api.integrations import integrations_controller_list_integrations as _integrations_list
from .api.integrations import integrations_controller_remove_integration as _integrations_remove
from .api.integrations import integrations_controller_set_integration_as_primary as _integrations_set_primary
from .api.integrations import integrations_controller_update_integration_by_id as _integrations_update
from .api.messages import messages_controller_delete_message as _messages_delete
from .api.messages import messages_controller_delete_messages_by_transaction_id as _messages_delete_by_transaction
from .api.messages import messages_controller_get_messages as _messages_list
from .api.notifications import notifications_controller_get_notification as _notifications_get
from .api.notifications import notifications_controller_list_notifications as _notifications_list
from .api.subscribers import subscribers_controller_create_subscriber as _subscribers_create
from .api.subscribers import subscribers_controller_get_subscriber as _subscribers_get
from .api.subscribers import subscribers_controller_get_subscriber_notifications as _subscribers_notifications
from .api.subscribers import subscribers_controller_get_subscriber_preferences as _subscribers_get_preferences
from .api.subscribers import subscribers_controller_list_subscriber_topics as _subscribers_topics
from .api.subscribers import subscribers_controller_patch_subscriber as _subscribers_patch
from .api.subscribers import subscribers_controller_remove_subscriber as _subscribers_remove
from .api.subscribers import subscribers_controller_search_subscribers as _subscribers_search
from .api.subscribers import subscribers_controller_update_subscriber_preferences as _subscribers_update_preferences
from .api.subscribers import subscribers_v1_controller_register_subscriber_device_token as _subscribers_device_token
from .api.topics import topics_controller_create_topic_subscriptions as _topics_subscribe
from .api.topics import topics_controller_delete_topic as _topics_delete
from .api.topics import topics_controller_delete_topic_subscriptions as _topics_unsubscribe
from .api.topics import topics_controller_get_topic as _topics_get
from .api.topics import topics_controller_list_topic_subscriptions as _topics_list_subscriptions
from .api.topics import topics_controller_list_topics as _topics_list
from .api.topics import topics_controller_update_topic as _topics_update
from .api.topics import topics_controller_upsert_topic as _topics_upsert
from .api.workflows import workflow_controller_create as _workflows_create
from .api.workflows import workflow_controller_get_workflow as _workflows_get
from .api.workflows import workflow_controller_patch_workflow as _workflows_patch
from .api.workflows import workflow_controller_remove_workflow as _workflows_remove
from .api.workflows import workflow_controller_search_workflows as _workflows_search
from .api.workflows import workflow_controller_sync as _workflows_sync
from .api.workflows import workflow_controller_update as _workflows_update
from .exceptions import raise_for_response
from .models.bulk_trigger_event_dto import BulkTriggerEventDto
from .models.create_subscriber_request_dto import CreateSubscriberRequestDto
from .models.create_topic_subscriptions_request_dto import CreateTopicSubscriptionsRequestDto
from .models.create_update_topic_request_dto import CreateUpdateTopicRequestDto
from .models.delete_topic_subscriptions_request_dto import DeleteTopicSubscriptionsRequestDto
from .models.patch_subscriber_request_dto import PatchSubscriberRequestDto
from .models.trigger_event_request_dto import TriggerEventRequestDto
from .models.trigger_event_request_dto_context import TriggerEventRequestDtoContext
from .models.trigger_event_request_dto_payload import TriggerEventRequestDtoPayload
from .models.trigger_overrides import TriggerOverrides
from .models.update_topic_request_dto import UpdateTopicRequestDto
from .notifly_client import DEFAULT_BASE_URL, NotiflyClient, from_secret_key
from .pagination import (
    DEFAULT_PAGE_SIZE,
    aiterate_cursor,
    aiterate_offset,
    aiterate_pages,
    iterate_cursor,
    iterate_offset,
    iterate_pages,
)


def _drop_none(values: Mapping[str, Any]) -> dict[str, Any]:
    """Generated operations expect ``UNSET`` rather than ``None`` for omitted parameters."""
    return {key: value for key, value in values.items() if value is not None}


def _model(model_cls: Any, body: Any, fields: Mapping[str, Any]) -> Any:
    """Return ``body`` when given, else build ``model_cls`` from keyword fields."""
    if body is not None:
        return body if not isinstance(body, Mapping) else model_cls.from_dict(dict(body))
    return model_cls(**_drop_none(fields))


def _free_form(model_cls: Any, value: Any) -> Any:
    if value is None or isinstance(value, model_cls):
        return value
    return model_cls.from_dict(dict(value))


def _trigger_body(
    body: Any,
    workflow: str | None,
    to: Any,
    payload: Any,
    overrides: Any,
    transaction_id: str | None,
    actor: Any,
    tenant: Any,
    context: Any,
) -> TriggerEventRequestDto:
    if body is not None:
        return body if not isinstance(body, Mapping) else TriggerEventRequestDto.from_dict(dict(body))
    if workflow is None or to is None:
        raise TypeError("trigger() requires either body=... or both workflow=... and to=...")
    return TriggerEventRequestDto(
        name=workflow,
        to=to,
        **_drop_none(
            {
                "payload": _free_form(TriggerEventRequestDtoPayload, payload),
                "overrides": _free_form(TriggerOverrides, overrides),
                "transaction_id": transaction_id,
                "actor": actor,
                "tenant": tenant,
                "context": _free_form(TriggerEventRequestDtoContext, context),
            }
        ),
    )


class _Resource:
    """Base class holding the client shared by every resource group."""

    __slots__ = ("_client",)

    def __init__(self, client: NotiflyClient) -> None:
        self._client = client


class _SyncResource(_Resource):
    def _call(self, module: Any, **kwargs: Any) -> Any:
        return raise_for_response(module.sync_detailed(client=self._client, **_drop_none(kwargs)))


class _AsyncResource(_Resource):
    async def _call(self, module: Any, **kwargs: Any) -> Any:
        return raise_for_response(await module.asyncio_detailed(client=self._client, **_drop_none(kwargs)))


# --------------------------------------------------------------------------------------
# Events
# --------------------------------------------------------------------------------------
class EventsResource(_SyncResource):
    """Trigger and cancel notifications — ``notifly.events``."""

    def trigger(
        self,
        workflow: str | None = None,
        to: Any = None,
        payload: Mapping[str, Any] | None = None,
        *,
        overrides: Any = None,
        transaction_id: str | None = None,
        actor: Any = None,
        tenant: Any = None,
        context: Any = None,
        body: TriggerEventRequestDto | Mapping[str, Any] | None = None,
        idempotency_key: str | None = None,
    ) -> Any:
        """Trigger a workflow for one or more recipients (max 100).

        ``workflow`` is the workflow's trigger identifier; ``to`` is a subscriber id, a
        subscriber/topic payload, or a list of them. Pass ``body=`` to supply a fully built
        :class:`~notifly_py.models.TriggerEventRequestDto` instead.
        """
        return self._call(
            _events_trigger,
            body=_trigger_body(body, workflow, to, payload, overrides, transaction_id, actor, tenant, context),
            idempotency_key=idempotency_key,
        )

    def trigger_bulk(
        self,
        events: Sequence[TriggerEventRequestDto] | BulkTriggerEventDto,
        *,
        idempotency_key: str | None = None,
    ) -> Any:
        """Trigger up to 100 events in a single request."""
        body = events if isinstance(events, BulkTriggerEventDto) else BulkTriggerEventDto(events=list(events))
        return self._call(_events_trigger_bulk, body=body, idempotency_key=idempotency_key)

    def broadcast(self, body: Any, *, idempotency_key: str | None = None) -> Any:
        """Trigger a workflow for every subscriber in the environment."""
        return self._call(_events_broadcast, body=body, idempotency_key=idempotency_key)

    def cancel(self, transaction_id: str, *, idempotency_key: str | None = None) -> Any:
        """Cancel a not-yet-delivered trigger by its transaction id."""
        return self._call(_events_cancel, transaction_id=transaction_id, idempotency_key=idempotency_key)


class AsyncEventsResource(_AsyncResource):
    """Async twin of :class:`EventsResource`."""

    async def trigger(
        self,
        workflow: str | None = None,
        to: Any = None,
        payload: Mapping[str, Any] | None = None,
        *,
        overrides: Any = None,
        transaction_id: str | None = None,
        actor: Any = None,
        tenant: Any = None,
        context: Any = None,
        body: TriggerEventRequestDto | Mapping[str, Any] | None = None,
        idempotency_key: str | None = None,
    ) -> Any:
        return await self._call(
            _events_trigger,
            body=_trigger_body(body, workflow, to, payload, overrides, transaction_id, actor, tenant, context),
            idempotency_key=idempotency_key,
        )

    async def trigger_bulk(
        self,
        events: Sequence[TriggerEventRequestDto] | BulkTriggerEventDto,
        *,
        idempotency_key: str | None = None,
    ) -> Any:
        body = events if isinstance(events, BulkTriggerEventDto) else BulkTriggerEventDto(events=list(events))
        return await self._call(_events_trigger_bulk, body=body, idempotency_key=idempotency_key)

    async def broadcast(self, body: Any, *, idempotency_key: str | None = None) -> Any:
        return await self._call(_events_broadcast, body=body, idempotency_key=idempotency_key)

    async def cancel(self, transaction_id: str, *, idempotency_key: str | None = None) -> Any:
        return await self._call(_events_cancel, transaction_id=transaction_id, idempotency_key=idempotency_key)


# --------------------------------------------------------------------------------------
# Subscribers
# --------------------------------------------------------------------------------------
class SubscribersResource(_SyncResource):
    """Manage subscribers, their preferences and their inbox — ``notifly.subscribers``."""

    def create(
        self,
        body: CreateSubscriberRequestDto | Mapping[str, Any] | None = None,
        *,
        fail_if_exists: bool | None = None,
        idempotency_key: str | None = None,
        **fields: Any,
    ) -> Any:
        """Create a subscriber, e.g. ``create(subscriber_id="u_1", email="ada@example.com")``."""
        return self._call(
            _subscribers_create,
            body=_model(CreateSubscriberRequestDto, body, fields),
            fail_if_exists=fail_if_exists,
            idempotency_key=idempotency_key,
        )

    def get(self, subscriber_id: str, *, idempotency_key: str | None = None) -> Any:
        """Fetch a single subscriber."""
        return self._call(_subscribers_get, subscriber_id=subscriber_id, idempotency_key=idempotency_key)

    def update(
        self,
        subscriber_id: str,
        body: PatchSubscriberRequestDto | Mapping[str, Any] | None = None,
        *,
        idempotency_key: str | None = None,
        **fields: Any,
    ) -> Any:
        """Partially update a subscriber."""
        return self._call(
            _subscribers_patch,
            subscriber_id=subscriber_id,
            body=_model(PatchSubscriberRequestDto, body, fields),
            idempotency_key=idempotency_key,
        )

    def delete(self, subscriber_id: str, *, idempotency_key: str | None = None) -> Any:
        """Delete a subscriber."""
        return self._call(_subscribers_remove, subscriber_id=subscriber_id, idempotency_key=idempotency_key)

    def list(self, **filters: Any) -> Any:
        """Return one page of subscribers (cursor paginated: ``after``, ``limit``, ...)."""
        return self._call(_subscribers_search, **filters)

    def iter_all(
        self, *, limit: int = DEFAULT_PAGE_SIZE, max_pages: int | None = None, **filters: Any
    ) -> Iterator[Any]:
        """Iterate every subscriber, following the ``next`` cursor across pages."""
        return iterate_cursor(
            lambda **params: self.list(**{**filters, **params}), limit=limit, max_pages=max_pages
        )

    def get_preferences(self, subscriber_id: str, **kwargs: Any) -> Any:
        """Fetch a subscriber's workflow/channel preferences."""
        return self._call(_subscribers_get_preferences, subscriber_id=subscriber_id, **kwargs)

    def update_preferences(self, subscriber_id: str, body: Any, **kwargs: Any) -> Any:
        """Update a subscriber's preferences."""
        return self._call(_subscribers_update_preferences, subscriber_id=subscriber_id, body=body, **kwargs)

    def list_notifications(self, subscriber_id: str, **filters: Any) -> Any:
        """Return one page of a subscriber's inbox notifications."""
        return self._call(_subscribers_notifications, subscriber_id=subscriber_id, **filters)

    def iter_notifications(
        self, subscriber_id: str, *, limit: int = DEFAULT_PAGE_SIZE, max_pages: int | None = None, **filters: Any
    ) -> Iterator[Any]:
        """Iterate a subscriber's inbox notifications across pages."""
        return iterate_offset(
            lambda **params: self.list_notifications(subscriber_id, **{**filters, **params}),
            limit=limit,
            max_pages=max_pages,
        )

    def list_topics(self, subscriber_id: str, **filters: Any) -> Any:
        """Return one page of the topics a subscriber is subscribed to."""
        return self._call(_subscribers_topics, subscriber_id=subscriber_id, **filters)

    def register_device_token(self, subscriber_id: str, provider_id: str, body: Any, **kwargs: Any) -> Any:
        """Register a push device token against a subscriber's provider credentials."""
        return self._call(
            _subscribers_device_token,
            subscriber_id=subscriber_id,
            provider_id=provider_id,
            body=body,
            **kwargs,
        )


class AsyncSubscribersResource(_AsyncResource):
    """Async twin of :class:`SubscribersResource`."""

    async def create(
        self,
        body: CreateSubscriberRequestDto | Mapping[str, Any] | None = None,
        *,
        fail_if_exists: bool | None = None,
        idempotency_key: str | None = None,
        **fields: Any,
    ) -> Any:
        return await self._call(
            _subscribers_create,
            body=_model(CreateSubscriberRequestDto, body, fields),
            fail_if_exists=fail_if_exists,
            idempotency_key=idempotency_key,
        )

    async def get(self, subscriber_id: str, *, idempotency_key: str | None = None) -> Any:
        return await self._call(_subscribers_get, subscriber_id=subscriber_id, idempotency_key=idempotency_key)

    async def update(
        self,
        subscriber_id: str,
        body: PatchSubscriberRequestDto | Mapping[str, Any] | None = None,
        *,
        idempotency_key: str | None = None,
        **fields: Any,
    ) -> Any:
        return await self._call(
            _subscribers_patch,
            subscriber_id=subscriber_id,
            body=_model(PatchSubscriberRequestDto, body, fields),
            idempotency_key=idempotency_key,
        )

    async def delete(self, subscriber_id: str, *, idempotency_key: str | None = None) -> Any:
        return await self._call(_subscribers_remove, subscriber_id=subscriber_id, idempotency_key=idempotency_key)

    async def list(self, **filters: Any) -> Any:
        return await self._call(_subscribers_search, **filters)

    def iter_all(
        self, *, limit: int = DEFAULT_PAGE_SIZE, max_pages: int | None = None, **filters: Any
    ) -> AsyncIterator[Any]:
        return aiterate_cursor(
            lambda **params: self.list(**{**filters, **params}), limit=limit, max_pages=max_pages
        )

    async def get_preferences(self, subscriber_id: str, **kwargs: Any) -> Any:
        return await self._call(_subscribers_get_preferences, subscriber_id=subscriber_id, **kwargs)

    async def update_preferences(self, subscriber_id: str, body: Any, **kwargs: Any) -> Any:
        return await self._call(_subscribers_update_preferences, subscriber_id=subscriber_id, body=body, **kwargs)

    async def list_notifications(self, subscriber_id: str, **filters: Any) -> Any:
        return await self._call(_subscribers_notifications, subscriber_id=subscriber_id, **filters)

    def iter_notifications(
        self, subscriber_id: str, *, limit: int = DEFAULT_PAGE_SIZE, max_pages: int | None = None, **filters: Any
    ) -> AsyncIterator[Any]:
        return aiterate_offset(
            lambda **params: self.list_notifications(subscriber_id, **{**filters, **params}),
            limit=limit,
            max_pages=max_pages,
        )

    async def list_topics(self, subscriber_id: str, **filters: Any) -> Any:
        return await self._call(_subscribers_topics, subscriber_id=subscriber_id, **filters)

    async def register_device_token(self, subscriber_id: str, provider_id: str, body: Any, **kwargs: Any) -> Any:
        return await self._call(
            _subscribers_device_token,
            subscriber_id=subscriber_id,
            provider_id=provider_id,
            body=body,
            **kwargs,
        )


# --------------------------------------------------------------------------------------
# Topics
# --------------------------------------------------------------------------------------
class TopicsResource(_SyncResource):
    """Create topics and manage their subscriptions — ``notifly.topics``."""

    def upsert(
        self,
        body: CreateUpdateTopicRequestDto | Mapping[str, Any] | None = None,
        *,
        fail_if_exists: bool | None = None,
        idempotency_key: str | None = None,
        **fields: Any,
    ) -> Any:
        """Create or update a topic, e.g. ``upsert(key="product-updates", name="Product")``."""
        return self._call(
            _topics_upsert,
            body=_model(CreateUpdateTopicRequestDto, body, fields),
            fail_if_exists=fail_if_exists,
            idempotency_key=idempotency_key,
        )

    def get(self, topic_key: str, **kwargs: Any) -> Any:
        """Fetch a topic by key."""
        return self._call(_topics_get, topic_key=topic_key, **kwargs)

    def update(
        self,
        topic_key: str,
        body: UpdateTopicRequestDto | Mapping[str, Any] | None = None,
        *,
        idempotency_key: str | None = None,
        **fields: Any,
    ) -> Any:
        """Rename a topic."""
        return self._call(
            _topics_update,
            topic_key=topic_key,
            body=_model(UpdateTopicRequestDto, body, fields),
            idempotency_key=idempotency_key,
        )

    def delete(self, topic_key: str, **kwargs: Any) -> Any:
        """Delete a topic."""
        return self._call(_topics_delete, topic_key=topic_key, **kwargs)

    def list(self, **filters: Any) -> Any:
        """Return one page of topics (cursor paginated)."""
        return self._call(_topics_list, **filters)

    def iter_all(
        self, *, limit: int = DEFAULT_PAGE_SIZE, max_pages: int | None = None, **filters: Any
    ) -> Iterator[Any]:
        """Iterate every topic across pages."""
        return iterate_cursor(
            lambda **params: self.list(**{**filters, **params}), limit=limit, max_pages=max_pages
        )

    def subscribe(
        self,
        topic_key: str,
        subscriber_ids: Sequence[str] | None = None,
        *,
        body: CreateTopicSubscriptionsRequestDto | Mapping[str, Any] | None = None,
        idempotency_key: str | None = None,
        **fields: Any,
    ) -> Any:
        """Subscribe subscribers to a topic."""
        if subscriber_ids is not None:
            fields.setdefault("subscriber_ids", list(subscriber_ids))
        return self._call(
            _topics_subscribe,
            topic_key=topic_key,
            body=_model(CreateTopicSubscriptionsRequestDto, body, fields),
            idempotency_key=idempotency_key,
        )

    def unsubscribe(
        self,
        topic_key: str,
        subscriber_ids: Sequence[str] | None = None,
        *,
        body: DeleteTopicSubscriptionsRequestDto | Mapping[str, Any] | None = None,
        idempotency_key: str | None = None,
        **fields: Any,
    ) -> Any:
        """Remove subscribers from a topic."""
        if subscriber_ids is not None:
            fields.setdefault("subscriber_ids", list(subscriber_ids))
        return self._call(
            _topics_unsubscribe,
            topic_key=topic_key,
            body=_model(DeleteTopicSubscriptionsRequestDto, body, fields),
            idempotency_key=idempotency_key,
        )

    def list_subscriptions(self, topic_key: str, **filters: Any) -> Any:
        """Return one page of a topic's subscriptions."""
        return self._call(_topics_list_subscriptions, topic_key=topic_key, **filters)

    def iter_subscriptions(
        self, topic_key: str, *, limit: int = DEFAULT_PAGE_SIZE, max_pages: int | None = None, **filters: Any
    ) -> Iterator[Any]:
        """Iterate a topic's subscriptions across pages."""
        return iterate_cursor(
            lambda **params: self.list_subscriptions(topic_key, **{**filters, **params}),
            limit=limit,
            max_pages=max_pages,
        )


class AsyncTopicsResource(_AsyncResource):
    """Async twin of :class:`TopicsResource`."""

    async def upsert(
        self,
        body: CreateUpdateTopicRequestDto | Mapping[str, Any] | None = None,
        *,
        fail_if_exists: bool | None = None,
        idempotency_key: str | None = None,
        **fields: Any,
    ) -> Any:
        return await self._call(
            _topics_upsert,
            body=_model(CreateUpdateTopicRequestDto, body, fields),
            fail_if_exists=fail_if_exists,
            idempotency_key=idempotency_key,
        )

    async def get(self, topic_key: str, **kwargs: Any) -> Any:
        return await self._call(_topics_get, topic_key=topic_key, **kwargs)

    async def update(
        self,
        topic_key: str,
        body: UpdateTopicRequestDto | Mapping[str, Any] | None = None,
        *,
        idempotency_key: str | None = None,
        **fields: Any,
    ) -> Any:
        return await self._call(
            _topics_update,
            topic_key=topic_key,
            body=_model(UpdateTopicRequestDto, body, fields),
            idempotency_key=idempotency_key,
        )

    async def delete(self, topic_key: str, **kwargs: Any) -> Any:
        return await self._call(_topics_delete, topic_key=topic_key, **kwargs)

    async def list(self, **filters: Any) -> Any:
        return await self._call(_topics_list, **filters)

    def iter_all(
        self, *, limit: int = DEFAULT_PAGE_SIZE, max_pages: int | None = None, **filters: Any
    ) -> AsyncIterator[Any]:
        return aiterate_cursor(
            lambda **params: self.list(**{**filters, **params}), limit=limit, max_pages=max_pages
        )

    async def subscribe(
        self,
        topic_key: str,
        subscriber_ids: Sequence[str] | None = None,
        *,
        body: CreateTopicSubscriptionsRequestDto | Mapping[str, Any] | None = None,
        idempotency_key: str | None = None,
        **fields: Any,
    ) -> Any:
        if subscriber_ids is not None:
            fields.setdefault("subscriber_ids", list(subscriber_ids))
        return await self._call(
            _topics_subscribe,
            topic_key=topic_key,
            body=_model(CreateTopicSubscriptionsRequestDto, body, fields),
            idempotency_key=idempotency_key,
        )

    async def unsubscribe(
        self,
        topic_key: str,
        subscriber_ids: Sequence[str] | None = None,
        *,
        body: DeleteTopicSubscriptionsRequestDto | Mapping[str, Any] | None = None,
        idempotency_key: str | None = None,
        **fields: Any,
    ) -> Any:
        if subscriber_ids is not None:
            fields.setdefault("subscriber_ids", list(subscriber_ids))
        return await self._call(
            _topics_unsubscribe,
            topic_key=topic_key,
            body=_model(DeleteTopicSubscriptionsRequestDto, body, fields),
            idempotency_key=idempotency_key,
        )

    async def list_subscriptions(self, topic_key: str, **filters: Any) -> Any:
        return await self._call(_topics_list_subscriptions, topic_key=topic_key, **filters)

    def iter_subscriptions(
        self, topic_key: str, *, limit: int = DEFAULT_PAGE_SIZE, max_pages: int | None = None, **filters: Any
    ) -> AsyncIterator[Any]:
        return aiterate_cursor(
            lambda **params: self.list_subscriptions(topic_key, **{**filters, **params}),
            limit=limit,
            max_pages=max_pages,
        )


# --------------------------------------------------------------------------------------
# Workflows
# --------------------------------------------------------------------------------------
class WorkflowsResource(_SyncResource):
    """Create and manage workflows — ``notifly.workflows``."""

    def create(self, body: Any, **kwargs: Any) -> Any:
        """Create a workflow."""
        return self._call(_workflows_create, body=body, **kwargs)

    def get(self, workflow_id: str, **kwargs: Any) -> Any:
        """Fetch a workflow by id or trigger identifier."""
        return self._call(_workflows_get, workflow_id=workflow_id, **kwargs)

    def update(self, workflow_id: str, body: Any, **kwargs: Any) -> Any:
        """Replace a workflow (PUT)."""
        return self._call(_workflows_update, workflow_id=workflow_id, body=body, **kwargs)

    def patch(self, workflow_id: str, body: Any, **kwargs: Any) -> Any:
        """Partially update a workflow (PATCH)."""
        return self._call(_workflows_patch, workflow_id=workflow_id, body=body, **kwargs)

    def delete(self, workflow_id: str, **kwargs: Any) -> Any:
        """Delete a workflow."""
        return self._call(_workflows_remove, workflow_id=workflow_id, **kwargs)

    def sync(self, workflow_id: str, body: Any, **kwargs: Any) -> Any:
        """Sync a workflow to another environment."""
        return self._call(_workflows_sync, workflow_id=workflow_id, body=body, **kwargs)

    def list(self, **filters: Any) -> Any:
        """Return one page of workflows (offset paginated)."""
        return self._call(_workflows_search, **filters)

    def iter_all(
        self, *, limit: int = DEFAULT_PAGE_SIZE, max_pages: int | None = None, **filters: Any
    ) -> Iterator[Any]:
        """Iterate every workflow across pages."""
        return iterate_offset(
            lambda **params: self.list(**{**filters, **params}),
            limit=limit,
            max_pages=max_pages,
            items_attr="workflows",
        )


class AsyncWorkflowsResource(_AsyncResource):
    """Async twin of :class:`WorkflowsResource`."""

    async def create(self, body: Any, **kwargs: Any) -> Any:
        return await self._call(_workflows_create, body=body, **kwargs)

    async def get(self, workflow_id: str, **kwargs: Any) -> Any:
        return await self._call(_workflows_get, workflow_id=workflow_id, **kwargs)

    async def update(self, workflow_id: str, body: Any, **kwargs: Any) -> Any:
        return await self._call(_workflows_update, workflow_id=workflow_id, body=body, **kwargs)

    async def patch(self, workflow_id: str, body: Any, **kwargs: Any) -> Any:
        return await self._call(_workflows_patch, workflow_id=workflow_id, body=body, **kwargs)

    async def delete(self, workflow_id: str, **kwargs: Any) -> Any:
        return await self._call(_workflows_remove, workflow_id=workflow_id, **kwargs)

    async def sync(self, workflow_id: str, body: Any, **kwargs: Any) -> Any:
        return await self._call(_workflows_sync, workflow_id=workflow_id, body=body, **kwargs)

    async def list(self, **filters: Any) -> Any:
        return await self._call(_workflows_search, **filters)

    def iter_all(
        self, *, limit: int = DEFAULT_PAGE_SIZE, max_pages: int | None = None, **filters: Any
    ) -> AsyncIterator[Any]:
        return aiterate_offset(
            lambda **params: self.list(**{**filters, **params}),
            limit=limit,
            max_pages=max_pages,
            items_attr="workflows",
        )


# --------------------------------------------------------------------------------------
# Messages / Notifications / Integrations
# --------------------------------------------------------------------------------------
class MessagesResource(_SyncResource):
    """Delivered message records — ``notifly.messages``."""

    def list(self, **filters: Any) -> Any:
        """Return one page of messages (page-number paginated)."""
        return self._call(_messages_list, **filters)

    def iter_all(self, *, limit: int = 10, max_pages: int | None = None, **filters: Any) -> Iterator[Any]:
        """Iterate every message across pages."""
        return iterate_pages(
            lambda **params: self.list(**{**filters, **params}), limit=limit, max_pages=max_pages
        )

    def delete(self, message_id: str, **kwargs: Any) -> Any:
        """Delete a single message."""
        return self._call(_messages_delete, message_id=message_id, **kwargs)

    def delete_by_transaction_id(self, transaction_id: str, **kwargs: Any) -> Any:
        """Delete every message produced by one trigger."""
        return self._call(_messages_delete_by_transaction, transaction_id=transaction_id, **kwargs)


class AsyncMessagesResource(_AsyncResource):
    """Async twin of :class:`MessagesResource`."""

    async def list(self, **filters: Any) -> Any:
        return await self._call(_messages_list, **filters)

    def iter_all(self, *, limit: int = 10, max_pages: int | None = None, **filters: Any) -> AsyncIterator[Any]:
        return aiterate_pages(
            lambda **params: self.list(**{**filters, **params}), limit=limit, max_pages=max_pages
        )

    async def delete(self, message_id: str, **kwargs: Any) -> Any:
        return await self._call(_messages_delete, message_id=message_id, **kwargs)

    async def delete_by_transaction_id(self, transaction_id: str, **kwargs: Any) -> Any:
        return await self._call(_messages_delete_by_transaction, transaction_id=transaction_id, **kwargs)


class NotificationsResource(_SyncResource):
    """Activity feed of triggered notifications — ``notifly.notifications``."""

    def list(self, **filters: Any) -> Any:
        """Return one page of the activity feed."""
        return self._call(_notifications_list, **filters)

    def iter_all(self, *, limit: int = 10, max_pages: int | None = None, **filters: Any) -> Iterator[Any]:
        """Iterate the activity feed across pages."""
        return iterate_pages(
            lambda **params: self.list(**{**filters, **params}), limit=limit, max_pages=max_pages
        )

    def get(self, notification_id: str, **kwargs: Any) -> Any:
        """Fetch one activity-feed entry."""
        return self._call(_notifications_get, notification_id=notification_id, **kwargs)


class AsyncNotificationsResource(_AsyncResource):
    """Async twin of :class:`NotificationsResource`."""

    async def list(self, **filters: Any) -> Any:
        return await self._call(_notifications_list, **filters)

    def iter_all(self, *, limit: int = 10, max_pages: int | None = None, **filters: Any) -> AsyncIterator[Any]:
        return aiterate_pages(
            lambda **params: self.list(**{**filters, **params}), limit=limit, max_pages=max_pages
        )

    async def get(self, notification_id: str, **kwargs: Any) -> Any:
        return await self._call(_notifications_get, notification_id=notification_id, **kwargs)


class IntegrationsResource(_SyncResource):
    """Provider integrations — ``notifly.integrations``."""

    def list(self, **kwargs: Any) -> Any:
        """List every integration in the environment."""
        return self._call(_integrations_list, **kwargs)

    def list_active(self, **kwargs: Any) -> Any:
        """List only the active integrations."""
        return self._call(_integrations_active, **kwargs)

    def create(self, body: Any, **kwargs: Any) -> Any:
        """Create an integration."""
        return self._call(_integrations_create, body=body, **kwargs)

    def update(self, integration_id: str, body: Any, **kwargs: Any) -> Any:
        """Update an integration."""
        return self._call(_integrations_update, integration_id=integration_id, body=body, **kwargs)

    def delete(self, integration_id: str, **kwargs: Any) -> Any:
        """Delete an integration."""
        return self._call(_integrations_remove, integration_id=integration_id, **kwargs)

    def set_primary(self, integration_id: str, **kwargs: Any) -> Any:
        """Make an integration the primary one for its channel."""
        return self._call(_integrations_set_primary, integration_id=integration_id, **kwargs)


class AsyncIntegrationsResource(_AsyncResource):
    """Async twin of :class:`IntegrationsResource`."""

    async def list(self, **kwargs: Any) -> Any:
        return await self._call(_integrations_list, **kwargs)

    async def list_active(self, **kwargs: Any) -> Any:
        return await self._call(_integrations_active, **kwargs)

    async def create(self, body: Any, **kwargs: Any) -> Any:
        return await self._call(_integrations_create, body=body, **kwargs)

    async def update(self, integration_id: str, body: Any, **kwargs: Any) -> Any:
        return await self._call(_integrations_update, integration_id=integration_id, body=body, **kwargs)

    async def delete(self, integration_id: str, **kwargs: Any) -> Any:
        return await self._call(_integrations_remove, integration_id=integration_id, **kwargs)

    async def set_primary(self, integration_id: str, **kwargs: Any) -> Any:
        return await self._call(_integrations_set_primary, integration_id=integration_id, **kwargs)


# --------------------------------------------------------------------------------------
# Facades
# --------------------------------------------------------------------------------------
class Notifly:
    """The synchronous Notifly client.

    ::

        with Notifly("<secret key>") as notifly:
            notifly.events.trigger(workflow="welcome", to="subscriber_123")
    """

    def __init__(
        self,
        secret_key: str | None = None,
        *,
        base_url: str = DEFAULT_BASE_URL,
        client: NotiflyClient | None = None,
        **client_kwargs: Any,
    ) -> None:
        if client is None:
            if secret_key is None:
                raise TypeError("Notifly() requires a secret_key or an existing client=")
            client = from_secret_key(secret_key, base_url=base_url, **client_kwargs)
        self.client = client
        self.events = EventsResource(client)
        self.subscribers = SubscribersResource(client)
        self.topics = TopicsResource(client)
        self.workflows = WorkflowsResource(client)
        self.messages = MessagesResource(client)
        self.notifications = NotificationsResource(client)
        self.integrations = IntegrationsResource(client)

    def __enter__(self) -> Notifly:
        self.client.__enter__()
        return self

    def __exit__(self, *args: Any) -> None:
        self.client.__exit__(*args)

    def close(self) -> None:
        """Close the underlying HTTP connection pool."""
        self.client.get_httpx_client().close()


class AsyncNotifly:
    """The asynchronous Notifly client — same surface as :class:`Notifly`, awaited.

    ::

        async with AsyncNotifly("<secret key>") as notifly:
            await notifly.events.trigger(workflow="welcome", to="subscriber_123")
    """

    def __init__(
        self,
        secret_key: str | None = None,
        *,
        base_url: str = DEFAULT_BASE_URL,
        client: NotiflyClient | None = None,
        **client_kwargs: Any,
    ) -> None:
        if client is None:
            if secret_key is None:
                raise TypeError("AsyncNotifly() requires a secret_key or an existing client=")
            client = from_secret_key(secret_key, base_url=base_url, **client_kwargs)
        self.client = client
        self.events = AsyncEventsResource(client)
        self.subscribers = AsyncSubscribersResource(client)
        self.topics = AsyncTopicsResource(client)
        self.workflows = AsyncWorkflowsResource(client)
        self.messages = AsyncMessagesResource(client)
        self.notifications = AsyncNotificationsResource(client)
        self.integrations = AsyncIntegrationsResource(client)

    async def __aenter__(self) -> AsyncNotifly:
        await self.client.__aenter__()
        return self

    async def __aexit__(self, *args: Any) -> None:
        await self.client.__aexit__(*args)

    async def aclose(self) -> None:
        """Close the underlying HTTP connection pool."""
        await self.client.get_async_httpx_client().aclose()


__all__ = [
    "AsyncEventsResource",
    "AsyncIntegrationsResource",
    "AsyncMessagesResource",
    "AsyncNotifly",
    "AsyncNotificationsResource",
    "AsyncSubscribersResource",
    "AsyncTopicsResource",
    "AsyncWorkflowsResource",
    "EventsResource",
    "IntegrationsResource",
    "MessagesResource",
    "Notifly",
    "NotificationsResource",
    "SubscribersResource",
    "TopicsResource",
    "WorkflowsResource",
]
