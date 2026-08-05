from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.resource_origin_enum import ResourceOriginEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.notification_trigger_dto import NotificationTriggerDto


T = TypeVar("T", bound="ActivityNotificationTemplateResponseDto")


@_attrs_define
class ActivityNotificationTemplateResponseDto:
    """
    Attributes:
        name (str): Name of the template
        triggers (list[NotificationTriggerDto]): Triggers of the template
        field_id (str | Unset): Unique identifier of the template
        origin (ResourceOriginEnum | Unset): Origin of the layout
    """

    name: str
    triggers: list[NotificationTriggerDto]
    field_id: str | Unset = UNSET
    origin: ResourceOriginEnum | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        triggers = []
        for triggers_item_data in self.triggers:
            triggers_item = triggers_item_data.to_dict()
            triggers.append(triggers_item)

        field_id = self.field_id

        origin: str | Unset = UNSET
        if not isinstance(self.origin, Unset):
            origin = self.origin.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "triggers": triggers,
            }
        )
        if field_id is not UNSET:
            field_dict["_id"] = field_id
        if origin is not UNSET:
            field_dict["origin"] = origin

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.notification_trigger_dto import NotificationTriggerDto

        d = dict(src_dict)
        name = d.pop("name")

        triggers = []
        _triggers = d.pop("triggers")
        for triggers_item_data in _triggers:
            triggers_item = NotificationTriggerDto.from_dict(triggers_item_data)

            triggers.append(triggers_item)

        field_id = d.pop("_id", UNSET)

        _origin = d.pop("origin", UNSET)
        origin: ResourceOriginEnum | Unset
        if isinstance(_origin, Unset):
            origin = UNSET
        else:
            origin = ResourceOriginEnum(_origin)

        activity_notification_template_response_dto = cls(
            name=name,
            triggers=triggers,
            field_id=field_id,
            origin=origin,
        )

        activity_notification_template_response_dto.additional_properties = d
        return activity_notification_template_response_dto

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
