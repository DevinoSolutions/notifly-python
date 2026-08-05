from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.message_failed_error_dto import MessageFailedErrorDto
    from ..models.webhook_message_failed_dto_object import WebhookMessageFailedDtoObject


T = TypeVar("T", bound="WebhookMessageFailedDto")


@_attrs_define
class WebhookMessageFailedDto:
    """
    Attributes:
        object_ (WebhookMessageFailedDtoObject): Current message state
        error (MessageFailedErrorDto):
    """

    object_: WebhookMessageFailedDtoObject
    error: MessageFailedErrorDto
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_ = self.object_.to_dict()

        error = self.error.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "object": object_,
                "error": error,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.message_failed_error_dto import MessageFailedErrorDto
        from ..models.webhook_message_failed_dto_object import WebhookMessageFailedDtoObject

        d = dict(src_dict)
        object_ = WebhookMessageFailedDtoObject.from_dict(d.pop("object"))

        error = MessageFailedErrorDto.from_dict(d.pop("error"))

        webhook_message_failed_dto = cls(
            object_=object_,
            error=error,
        )

        webhook_message_failed_dto.additional_properties = d
        return webhook_message_failed_dto

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
