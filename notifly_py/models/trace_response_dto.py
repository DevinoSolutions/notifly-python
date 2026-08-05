from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.trace_response_dto_external_subscriber_id_type_0 import TraceResponseDtoExternalSubscriberIdType0
    from ..models.trace_response_dto_message_type_0 import TraceResponseDtoMessageType0
    from ..models.trace_response_dto_raw_data_type_0 import TraceResponseDtoRawDataType0
    from ..models.trace_response_dto_subscriber_id_type_0 import TraceResponseDtoSubscriberIdType0
    from ..models.trace_response_dto_user_id_type_0 import TraceResponseDtoUserIdType0


T = TypeVar("T", bound="TraceResponseDto")


@_attrs_define
class TraceResponseDto:
    """
    Attributes:
        id (str): Trace identifier
        created_at (str): Creation timestamp
        event_type (str): Event type (e.g., request_received, workflow_execution_started)
        title (str): Human readable title/message
        status (str): Trace status (success, error, warning, pending)
        entity_type (str): Entity type (request, workflow_run, step_run)
        entity_id (str): Entity identifier
        organization_id (str): Organization identifier
        environment_id (str): Environment identifier
        message (None | TraceResponseDtoMessageType0 | Unset): Detailed message
        raw_data (None | TraceResponseDtoRawDataType0 | Unset): Raw data associated with trace
        user_id (None | TraceResponseDtoUserIdType0 | Unset): User identifier
        external_subscriber_id (None | TraceResponseDtoExternalSubscriberIdType0 | Unset): External subscriber
            identifier
        subscriber_id (None | TraceResponseDtoSubscriberIdType0 | Unset): Subscriber identifier
    """

    id: str
    created_at: str
    event_type: str
    title: str
    status: str
    entity_type: str
    entity_id: str
    organization_id: str
    environment_id: str
    message: None | TraceResponseDtoMessageType0 | Unset = UNSET
    raw_data: None | TraceResponseDtoRawDataType0 | Unset = UNSET
    user_id: None | TraceResponseDtoUserIdType0 | Unset = UNSET
    external_subscriber_id: None | TraceResponseDtoExternalSubscriberIdType0 | Unset = UNSET
    subscriber_id: None | TraceResponseDtoSubscriberIdType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.trace_response_dto_external_subscriber_id_type_0 import TraceResponseDtoExternalSubscriberIdType0
        from ..models.trace_response_dto_message_type_0 import TraceResponseDtoMessageType0
        from ..models.trace_response_dto_raw_data_type_0 import TraceResponseDtoRawDataType0
        from ..models.trace_response_dto_subscriber_id_type_0 import TraceResponseDtoSubscriberIdType0
        from ..models.trace_response_dto_user_id_type_0 import TraceResponseDtoUserIdType0

        id = self.id

        created_at = self.created_at

        event_type = self.event_type

        title = self.title

        status = self.status

        entity_type = self.entity_type

        entity_id = self.entity_id

        organization_id = self.organization_id

        environment_id = self.environment_id

        message: dict[str, Any] | None | Unset
        if isinstance(self.message, Unset):
            message = UNSET
        elif isinstance(self.message, TraceResponseDtoMessageType0):
            message = self.message.to_dict()
        else:
            message = self.message

        raw_data: dict[str, Any] | None | Unset
        if isinstance(self.raw_data, Unset):
            raw_data = UNSET
        elif isinstance(self.raw_data, TraceResponseDtoRawDataType0):
            raw_data = self.raw_data.to_dict()
        else:
            raw_data = self.raw_data

        user_id: dict[str, Any] | None | Unset
        if isinstance(self.user_id, Unset):
            user_id = UNSET
        elif isinstance(self.user_id, TraceResponseDtoUserIdType0):
            user_id = self.user_id.to_dict()
        else:
            user_id = self.user_id

        external_subscriber_id: dict[str, Any] | None | Unset
        if isinstance(self.external_subscriber_id, Unset):
            external_subscriber_id = UNSET
        elif isinstance(self.external_subscriber_id, TraceResponseDtoExternalSubscriberIdType0):
            external_subscriber_id = self.external_subscriber_id.to_dict()
        else:
            external_subscriber_id = self.external_subscriber_id

        subscriber_id: dict[str, Any] | None | Unset
        if isinstance(self.subscriber_id, Unset):
            subscriber_id = UNSET
        elif isinstance(self.subscriber_id, TraceResponseDtoSubscriberIdType0):
            subscriber_id = self.subscriber_id.to_dict()
        else:
            subscriber_id = self.subscriber_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "createdAt": created_at,
                "eventType": event_type,
                "title": title,
                "status": status,
                "entityType": entity_type,
                "entityId": entity_id,
                "organizationId": organization_id,
                "environmentId": environment_id,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message
        if raw_data is not UNSET:
            field_dict["rawData"] = raw_data
        if user_id is not UNSET:
            field_dict["userId"] = user_id
        if external_subscriber_id is not UNSET:
            field_dict["externalSubscriberId"] = external_subscriber_id
        if subscriber_id is not UNSET:
            field_dict["subscriberId"] = subscriber_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.trace_response_dto_external_subscriber_id_type_0 import TraceResponseDtoExternalSubscriberIdType0
        from ..models.trace_response_dto_message_type_0 import TraceResponseDtoMessageType0
        from ..models.trace_response_dto_raw_data_type_0 import TraceResponseDtoRawDataType0
        from ..models.trace_response_dto_subscriber_id_type_0 import TraceResponseDtoSubscriberIdType0
        from ..models.trace_response_dto_user_id_type_0 import TraceResponseDtoUserIdType0

        d = dict(src_dict)
        id = d.pop("id")

        created_at = d.pop("createdAt")

        event_type = d.pop("eventType")

        title = d.pop("title")

        status = d.pop("status")

        entity_type = d.pop("entityType")

        entity_id = d.pop("entityId")

        organization_id = d.pop("organizationId")

        environment_id = d.pop("environmentId")

        def _parse_message(data: object) -> None | TraceResponseDtoMessageType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                message_type_0 = TraceResponseDtoMessageType0.from_dict(data)

                return message_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TraceResponseDtoMessageType0 | Unset, data)

        message = _parse_message(d.pop("message", UNSET))

        def _parse_raw_data(data: object) -> None | TraceResponseDtoRawDataType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                raw_data_type_0 = TraceResponseDtoRawDataType0.from_dict(data)

                return raw_data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TraceResponseDtoRawDataType0 | Unset, data)

        raw_data = _parse_raw_data(d.pop("rawData", UNSET))

        def _parse_user_id(data: object) -> None | TraceResponseDtoUserIdType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                user_id_type_0 = TraceResponseDtoUserIdType0.from_dict(data)

                return user_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TraceResponseDtoUserIdType0 | Unset, data)

        user_id = _parse_user_id(d.pop("userId", UNSET))

        def _parse_external_subscriber_id(data: object) -> None | TraceResponseDtoExternalSubscriberIdType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                external_subscriber_id_type_0 = TraceResponseDtoExternalSubscriberIdType0.from_dict(data)

                return external_subscriber_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TraceResponseDtoExternalSubscriberIdType0 | Unset, data)

        external_subscriber_id = _parse_external_subscriber_id(d.pop("externalSubscriberId", UNSET))

        def _parse_subscriber_id(data: object) -> None | TraceResponseDtoSubscriberIdType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                subscriber_id_type_0 = TraceResponseDtoSubscriberIdType0.from_dict(data)

                return subscriber_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TraceResponseDtoSubscriberIdType0 | Unset, data)

        subscriber_id = _parse_subscriber_id(d.pop("subscriberId", UNSET))

        trace_response_dto = cls(
            id=id,
            created_at=created_at,
            event_type=event_type,
            title=title,
            status=status,
            entity_type=entity_type,
            entity_id=entity_id,
            organization_id=organization_id,
            environment_id=environment_id,
            message=message,
            raw_data=raw_data,
            user_id=user_id,
            external_subscriber_id=external_subscriber_id,
            subscriber_id=subscriber_id,
        )

        trace_response_dto.additional_properties = d
        return trace_response_dto

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
