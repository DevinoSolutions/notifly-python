from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.webhook_deleted_workflow_dto_webhook_payload_wrapper_object import (
    WebhookDeletedWorkflowDtoWebhookPayloadWrapperObject,
)
from ..models.webhook_deleted_workflow_dto_webhook_payload_wrapper_type import (
    WebhookDeletedWorkflowDtoWebhookPayloadWrapperType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.webhook_deleted_workflow_dto import WebhookDeletedWorkflowDto


T = TypeVar("T", bound="WebhookDeletedWorkflowDtoWebhookPayloadWrapper")


@_attrs_define
class WebhookDeletedWorkflowDtoWebhookPayloadWrapper:
    """
    Attributes:
        type_ (WebhookDeletedWorkflowDtoWebhookPayloadWrapperType): The type of the webhook event.
        data (WebhookDeletedWorkflowDto):
        timestamp (datetime.datetime): ISO timestamp of when the event occurred.
        environment_id (str): The ID of the environment associated with the event.
        object_ (WebhookDeletedWorkflowDtoWebhookPayloadWrapperObject): The type of object the event relates to.
        id (str | Unset): Unique identifier of the webhook event (evt_✱).
    """

    type_: WebhookDeletedWorkflowDtoWebhookPayloadWrapperType
    data: WebhookDeletedWorkflowDto
    timestamp: datetime.datetime
    environment_id: str
    object_: WebhookDeletedWorkflowDtoWebhookPayloadWrapperObject
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
        from ..models.webhook_deleted_workflow_dto import WebhookDeletedWorkflowDto

        d = dict(src_dict)
        type_ = WebhookDeletedWorkflowDtoWebhookPayloadWrapperType(d.pop("type"))

        data = WebhookDeletedWorkflowDto.from_dict(d.pop("data"))

        timestamp = datetime.datetime.fromisoformat(d.pop("timestamp"))

        environment_id = d.pop("environmentId")

        object_ = WebhookDeletedWorkflowDtoWebhookPayloadWrapperObject(d.pop("object"))

        id = d.pop("id", UNSET)

        webhook_deleted_workflow_dto_webhook_payload_wrapper = cls(
            type_=type_,
            data=data,
            timestamp=timestamp,
            environment_id=environment_id,
            object_=object_,
            id=id,
        )

        webhook_deleted_workflow_dto_webhook_payload_wrapper.additional_properties = d
        return webhook_deleted_workflow_dto_webhook_payload_wrapper

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
