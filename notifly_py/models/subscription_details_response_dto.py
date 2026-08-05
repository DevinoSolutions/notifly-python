from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.subscription_preference_dto import SubscriptionPreferenceDto


T = TypeVar("T", bound="SubscriptionDetailsResponseDto")


@_attrs_define
class SubscriptionDetailsResponseDto:
    """
    Attributes:
        id (str): The unique identifier of the subscription Example: 64f5e95d3d7946d80d0cb679.
        identifier (str | Unset): The identifier of the subscription Example: subscription-identifier.
        name (str | Unset): The name of the subscription Example: My Subscription.
        preferences (list[SubscriptionPreferenceDto] | Unset): The preferences/rules for the subscription
        context_keys (list[str] | Unset): Context keys that scope this subscription (e.g., tenant:org-a,
            project:proj-123) Example: ['tenant:org-a', 'project:proj-123'].
    """

    id: str
    identifier: str | Unset = UNSET
    name: str | Unset = UNSET
    preferences: list[SubscriptionPreferenceDto] | Unset = UNSET
    context_keys: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        identifier = self.identifier

        name = self.name

        preferences: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.preferences, Unset):
            preferences = []
            for preferences_item_data in self.preferences:
                preferences_item = preferences_item_data.to_dict()
                preferences.append(preferences_item)

        context_keys: list[str] | Unset = UNSET
        if not isinstance(self.context_keys, Unset):
            context_keys = self.context_keys

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if name is not UNSET:
            field_dict["name"] = name
        if preferences is not UNSET:
            field_dict["preferences"] = preferences
        if context_keys is not UNSET:
            field_dict["contextKeys"] = context_keys

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.subscription_preference_dto import SubscriptionPreferenceDto

        d = dict(src_dict)
        id = d.pop("id")

        identifier = d.pop("identifier", UNSET)

        name = d.pop("name", UNSET)

        _preferences = d.pop("preferences", UNSET)
        preferences: list[SubscriptionPreferenceDto] | Unset = UNSET
        if _preferences is not UNSET:
            preferences = []
            for preferences_item_data in _preferences:
                preferences_item = SubscriptionPreferenceDto.from_dict(preferences_item_data)

                preferences.append(preferences_item)

        context_keys = cast(list[str], d.pop("contextKeys", UNSET))

        subscription_details_response_dto = cls(
            id=id,
            identifier=identifier,
            name=name,
            preferences=preferences,
            context_keys=context_keys,
        )

        subscription_details_response_dto.additional_properties = d
        return subscription_details_response_dto

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
