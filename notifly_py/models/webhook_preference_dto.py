from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.webhook_preference_dto_object import WebhookPreferenceDtoObject


T = TypeVar("T", bound="WebhookPreferenceDto")


@_attrs_define
class WebhookPreferenceDto:
    """
    Attributes:
        object_ (WebhookPreferenceDtoObject): Current preference state
        subscriber_id (str): Subscriber ID
    """

    object_: WebhookPreferenceDtoObject
    subscriber_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_ = self.object_.to_dict()

        subscriber_id = self.subscriber_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "object": object_,
                "subscriberId": subscriber_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.webhook_preference_dto_object import WebhookPreferenceDtoObject

        d = dict(src_dict)
        object_ = WebhookPreferenceDtoObject.from_dict(d.pop("object"))

        subscriber_id = d.pop("subscriberId")

        webhook_preference_dto = cls(
            object_=object_,
            subscriber_id=subscriber_id,
        )

        webhook_preference_dto.additional_properties = d
        return webhook_preference_dto

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
