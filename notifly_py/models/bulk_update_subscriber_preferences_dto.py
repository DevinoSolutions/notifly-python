from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bulk_update_subscriber_preference_item_dto import BulkUpdateSubscriberPreferenceItemDto
    from ..models.bulk_update_subscriber_preferences_dto_context import BulkUpdateSubscriberPreferencesDtoContext


T = TypeVar("T", bound="BulkUpdateSubscriberPreferencesDto")


@_attrs_define
class BulkUpdateSubscriberPreferencesDto:
    """
    Attributes:
        preferences (list[BulkUpdateSubscriberPreferenceItemDto]): Array of workflow preferences to update (maximum 100
            items)
        context (BulkUpdateSubscriberPreferencesDtoContext | Unset):
    """

    preferences: list[BulkUpdateSubscriberPreferenceItemDto]
    context: BulkUpdateSubscriberPreferencesDtoContext | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        preferences = []
        for preferences_item_data in self.preferences:
            preferences_item = preferences_item_data.to_dict()
            preferences.append(preferences_item)

        context: dict[str, Any] | Unset = UNSET
        if not isinstance(self.context, Unset):
            context = self.context.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "preferences": preferences,
            }
        )
        if context is not UNSET:
            field_dict["context"] = context

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bulk_update_subscriber_preference_item_dto import BulkUpdateSubscriberPreferenceItemDto
        from ..models.bulk_update_subscriber_preferences_dto_context import BulkUpdateSubscriberPreferencesDtoContext

        d = dict(src_dict)
        preferences = []
        _preferences = d.pop("preferences")
        for preferences_item_data in _preferences:
            preferences_item = BulkUpdateSubscriberPreferenceItemDto.from_dict(preferences_item_data)

            preferences.append(preferences_item)

        _context = d.pop("context", UNSET)
        context: BulkUpdateSubscriberPreferencesDtoContext | Unset
        if isinstance(_context, Unset):
            context = UNSET
        else:
            context = BulkUpdateSubscriberPreferencesDtoContext.from_dict(_context)

        bulk_update_subscriber_preferences_dto = cls(
            preferences=preferences,
            context=context,
        )

        bulk_update_subscriber_preferences_dto.additional_properties = d
        return bulk_update_subscriber_preferences_dto

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
