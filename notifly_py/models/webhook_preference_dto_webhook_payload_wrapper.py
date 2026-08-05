from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.webhook_preference_dto_webhook_payload_wrapper_object import (
    WebhookPreferenceDtoWebhookPayloadWrapperObject,
)
from ..models.webhook_preference_dto_webhook_payload_wrapper_type import WebhookPreferenceDtoWebhookPayloadWrapperType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.webhook_preference_dto import WebhookPreferenceDto


T = TypeVar("T", bound="WebhookPreferenceDtoWebhookPayloadWrapper")


@_attrs_define
class WebhookPreferenceDtoWebhookPayloadWrapper:
    """
    Attributes:
        type_ (WebhookPreferenceDtoWebhookPayloadWrapperType): The type of the webhook event.
        data (WebhookPreferenceDto):
        timestamp (datetime.datetime): ISO timestamp of when the event occurred.
        environment_id (str): The ID of the environment associated with the event.
        object_ (WebhookPreferenceDtoWebhookPayloadWrapperObject): The type of object the event relates to.
        id (str | Unset): Unique identifier of the webhook event (evt_✱).
    """

    type_: WebhookPreferenceDtoWebhookPayloadWrapperType
    data: WebhookPreferenceDto
    timestamp: datetime.datetime
    environment_id: str
    object_: WebhookPreferenceDtoWebhookPayloadWrapperObject
    id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        data = self.data.to_dict()

        timestamp = self.timestamp.isoformat()

        environment_id = self.environment_id

        object_ = self.object_.value

        id = self.id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "data": data,
                "timestamp": timestamp,
                "environmentId": environment_id,
                "object": object_,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webhook_preference_dto import WebhookPreferenceDto

        d = dict(src_dict)
        type_ = WebhookPreferenceDtoWebhookPayloadWrapperType(d.pop("type"))

        data = WebhookPreferenceDto.from_dict(d.pop("data"))

        timestamp = datetime.datetime.fromisoformat(d.pop("timestamp"))

        environment_id = d.pop("environmentId")

        object_ = WebhookPreferenceDtoWebhookPayloadWrapperObject(d.pop("object"))

        id = d.pop("id", UNSET)

        webhook_preference_dto_webhook_payload_wrapper = cls(
            type_=type_,
            data=data,
            timestamp=timestamp,
            environment_id=environment_id,
            object_=object_,
            id=id,
        )

        webhook_preference_dto_webhook_payload_wrapper.additional_properties = d
        return webhook_preference_dto_webhook_payload_wrapper

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
