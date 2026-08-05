from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.webhook_created_workflow_dto_webhook_payload_wrapper_object import (
    WebhookCreatedWorkflowDtoWebhookPayloadWrapperObject,
)
from ..models.webhook_created_workflow_dto_webhook_payload_wrapper_type import (
    WebhookCreatedWorkflowDtoWebhookPayloadWrapperType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.webhook_created_workflow_dto import WebhookCreatedWorkflowDto


T = TypeVar("T", bound="WebhookCreatedWorkflowDtoWebhookPayloadWrapper")


@_attrs_define
class WebhookCreatedWorkflowDtoWebhookPayloadWrapper:
    """
    Attributes:
        type_ (WebhookCreatedWorkflowDtoWebhookPayloadWrapperType): The type of the webhook event.
        data (WebhookCreatedWorkflowDto):
        timestamp (datetime.datetime): ISO timestamp of when the event occurred.
        environment_id (str): The ID of the environment associated with the event.
        object_ (WebhookCreatedWorkflowDtoWebhookPayloadWrapperObject): The type of object the event relates to.
        id (str | Unset): Unique identifier of the webhook event (evt_✱).
    """

    type_: WebhookCreatedWorkflowDtoWebhookPayloadWrapperType
    data: WebhookCreatedWorkflowDto
    timestamp: datetime.datetime
    environment_id: str
    object_: WebhookCreatedWorkflowDtoWebhookPayloadWrapperObject
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
        from ..models.webhook_created_workflow_dto import WebhookCreatedWorkflowDto

        d = dict(src_dict)
        type_ = WebhookCreatedWorkflowDtoWebhookPayloadWrapperType(d.pop("type"))

        data = WebhookCreatedWorkflowDto.from_dict(d.pop("data"))

        timestamp = datetime.datetime.fromisoformat(d.pop("timestamp"))

        environment_id = d.pop("environmentId")

        object_ = WebhookCreatedWorkflowDtoWebhookPayloadWrapperObject(d.pop("object"))

        id = d.pop("id", UNSET)

        webhook_created_workflow_dto_webhook_payload_wrapper = cls(
            type_=type_,
            data=data,
            timestamp=timestamp,
            environment_id=environment_id,
            object_=object_,
            id=id,
        )

        webhook_created_workflow_dto_webhook_payload_wrapper.additional_properties = d
        return webhook_created_workflow_dto_webhook_payload_wrapper

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
