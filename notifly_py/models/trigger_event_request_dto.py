from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.subscriber_payload_dto import SubscriberPayloadDto
    from ..models.tenant_payload_dto import TenantPayloadDto
    from ..models.topic_payload_dto import TopicPayloadDto
    from ..models.trigger_event_request_dto_context import TriggerEventRequestDtoContext
    from ..models.trigger_event_request_dto_payload import TriggerEventRequestDtoPayload
    from ..models.trigger_overrides import TriggerOverrides


T = TypeVar("T", bound="TriggerEventRequestDto")


@_attrs_define
class TriggerEventRequestDto:
    """
    Attributes:
        name (str): The trigger identifier of the workflow you wish to send. This identifier can be found on the
            workflow page. Example: workflow_identifier.
        to (list[str | SubscriberPayloadDto | TopicPayloadDto] | str | SubscriberPayloadDto | TopicPayloadDto): The
            recipients list of people who will receive the notification. Maximum number of recipients can be 100.
        payload (TriggerEventRequestDtoPayload | Unset): The payload object is used to pass additional custom
            information that could be
                used to render the workflow, or perform routing rules based on it.
                  This data will also be available when fetching the notifications feed from the API to display certain
            parts of the UI. Example: {'comment_id': 'string', 'post': {'text': 'string'}}.
        overrides (TriggerOverrides | Unset):
        transaction_id (str | Unset): A unique identifier for deduplication. If the same **transactionId** is sent
            again,
                  the trigger is ignored. Useful to prevent duplicate notifications. The retention period depends on your
            billing tier.
        actor (str | SubscriberPayloadDto | Unset): It is used to display the Avatar of the provided actor's subscriber
            id or actor object.
                If a new actor object is provided, we will create a new subscriber in our system
        tenant (str | TenantPayloadDto | Unset): It is used to specify a tenant context during trigger event.
                Existing tenants will be updated with the provided details.
        context (TriggerEventRequestDtoContext | Unset):
    """

    name: str
    to: list[str | SubscriberPayloadDto | TopicPayloadDto] | str | SubscriberPayloadDto | TopicPayloadDto
    payload: TriggerEventRequestDtoPayload | Unset = UNSET
    overrides: TriggerOverrides | Unset = UNSET
    transaction_id: str | Unset = UNSET
    actor: str | SubscriberPayloadDto | Unset = UNSET
    tenant: str | TenantPayloadDto | Unset = UNSET
    context: TriggerEventRequestDtoContext | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.subscriber_payload_dto import SubscriberPayloadDto
        from ..models.tenant_payload_dto import TenantPayloadDto
        from ..models.topic_payload_dto import TopicPayloadDto

        name = self.name

        to: dict[str, Any] | list[dict[str, Any] | str] | str
        if isinstance(self.to, list):
            to = []
            for to_type_0_item_data in self.to:
                to_type_0_item: dict[str, Any] | str
                if isinstance(to_type_0_item_data, SubscriberPayloadDto):
                    to_type_0_item = to_type_0_item_data.to_dict()
                elif isinstance(to_type_0_item_data, TopicPayloadDto):
                    to_type_0_item = to_type_0_item_data.to_dict()
                else:
                    to_type_0_item = to_type_0_item_data
                to.append(to_type_0_item)

        elif isinstance(self.to, SubscriberPayloadDto):
            to = self.to.to_dict()
        elif isinstance(self.to, TopicPayloadDto):
            to = self.to.to_dict()
        else:
            to = self.to

        payload: dict[str, Any] | Unset = UNSET
        if not isinstance(self.payload, Unset):
            payload = self.payload.to_dict()

        overrides: dict[str, Any] | Unset = UNSET
        if not isinstance(self.overrides, Unset):
            overrides = self.overrides.to_dict()

        transaction_id = self.transaction_id

        actor: dict[str, Any] | str | Unset
        if isinstance(self.actor, Unset):
            actor = UNSET
        elif isinstance(self.actor, SubscriberPayloadDto):
            actor = self.actor.to_dict()
        else:
            actor = self.actor

        tenant: dict[str, Any] | str | Unset
        if isinstance(self.tenant, Unset):
            tenant = UNSET
        elif isinstance(self.tenant, TenantPayloadDto):
            tenant = self.tenant.to_dict()
        else:
            tenant = self.tenant

        context: dict[str, Any] | Unset = UNSET
        if not isinstance(self.context, Unset):
            context = self.context.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "to": to,
            }
        )
        if payload is not UNSET:
            field_dict["payload"] = payload
        if overrides is not UNSET:
            field_dict["overrides"] = overrides
        if transaction_id is not UNSET:
            field_dict["transactionId"] = transaction_id
        if actor is not UNSET:
            field_dict["actor"] = actor
        if tenant is not UNSET:
            field_dict["tenant"] = tenant
        if context is not UNSET:
            field_dict["context"] = context

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.subscriber_payload_dto import SubscriberPayloadDto
        from ..models.tenant_payload_dto import TenantPayloadDto
        from ..models.topic_payload_dto import TopicPayloadDto
        from ..models.trigger_event_request_dto_context import TriggerEventRequestDtoContext
        from ..models.trigger_event_request_dto_payload import TriggerEventRequestDtoPayload
        from ..models.trigger_overrides import TriggerOverrides

        d = dict(src_dict)
        name = d.pop("name")

        def _parse_to(
            data: object,
        ) -> list[str | SubscriberPayloadDto | TopicPayloadDto] | str | SubscriberPayloadDto | TopicPayloadDto:
            try:
                if not isinstance(data, list):
                    raise TypeError()
                to_type_0 = []
                _to_type_0 = data
                for to_type_0_item_data in _to_type_0:

                    def _parse_to_type_0_item(data: object) -> str | SubscriberPayloadDto | TopicPayloadDto:
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            to_type_0_item_type_0 = SubscriberPayloadDto.from_dict(data)

                            return to_type_0_item_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            to_type_0_item_type_1 = TopicPayloadDto.from_dict(data)

                            return to_type_0_item_type_1
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        return cast(str | SubscriberPayloadDto | TopicPayloadDto, data)

                    to_type_0_item = _parse_to_type_0_item(to_type_0_item_data)

                    to_type_0.append(to_type_0_item)

                return to_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                to_type_2 = SubscriberPayloadDto.from_dict(data)

                return to_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                to_type_3 = TopicPayloadDto.from_dict(data)

                return to_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[str | SubscriberPayloadDto | TopicPayloadDto] | str | SubscriberPayloadDto | TopicPayloadDto, data
            )

        to = _parse_to(d.pop("to"))

        _payload = d.pop("payload", UNSET)
        payload: TriggerEventRequestDtoPayload | Unset
        if isinstance(_payload, Unset):
            payload = UNSET
        else:
            payload = TriggerEventRequestDtoPayload.from_dict(_payload)

        _overrides = d.pop("overrides", UNSET)
        overrides: TriggerOverrides | Unset
        if isinstance(_overrides, Unset):
            overrides = UNSET
        else:
            overrides = TriggerOverrides.from_dict(_overrides)

        transaction_id = d.pop("transactionId", UNSET)

        def _parse_actor(data: object) -> str | SubscriberPayloadDto | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                actor_type_1 = SubscriberPayloadDto.from_dict(data)

                return actor_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(str | SubscriberPayloadDto | Unset, data)

        actor = _parse_actor(d.pop("actor", UNSET))

        def _parse_tenant(data: object) -> str | TenantPayloadDto | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                tenant_type_1 = TenantPayloadDto.from_dict(data)

                return tenant_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(str | TenantPayloadDto | Unset, data)

        tenant = _parse_tenant(d.pop("tenant", UNSET))

        _context = d.pop("context", UNSET)
        context: TriggerEventRequestDtoContext | Unset
        if isinstance(_context, Unset):
            context = UNSET
        else:
            context = TriggerEventRequestDtoContext.from_dict(_context)

        trigger_event_request_dto = cls(
            name=name,
            to=to,
            payload=payload,
            overrides=overrides,
            transaction_id=transaction_id,
            actor=actor,
            tenant=tenant,
            context=context,
        )

        trigger_event_request_dto.additional_properties = d
        return trigger_event_request_dto

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
