from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.bulk_update_subscriber_preferences_dto_context_additional_property_type_1 import (
        BulkUpdateSubscriberPreferencesDtoContextAdditionalPropertyType1,
    )


T = TypeVar("T", bound="BulkUpdateSubscriberPreferencesDtoContext")


@_attrs_define
class BulkUpdateSubscriberPreferencesDtoContext:
    """ """

    additional_properties: dict[str, BulkUpdateSubscriberPreferencesDtoContextAdditionalPropertyType1 | str] = (
        _attrs_field(init=False, factory=dict)
    )

    def to_dict(self) -> dict[str, Any]:
        from ..models.bulk_update_subscriber_preferences_dto_context_additional_property_type_1 import (
            BulkUpdateSubscriberPreferencesDtoContextAdditionalPropertyType1,
        )

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            if isinstance(prop, BulkUpdateSubscriberPreferencesDtoContextAdditionalPropertyType1):
                field_dict[prop_name] = prop.to_dict()
            else:
                field_dict[prop_name] = prop

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bulk_update_subscriber_preferences_dto_context_additional_property_type_1 import (
            BulkUpdateSubscriberPreferencesDtoContextAdditionalPropertyType1,
        )

        d = dict(src_dict)
        bulk_update_subscriber_preferences_dto_context = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():

            def _parse_additional_property(
                data: object,
            ) -> BulkUpdateSubscriberPreferencesDtoContextAdditionalPropertyType1 | str:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    additional_property_type_1 = (
                        BulkUpdateSubscriberPreferencesDtoContextAdditionalPropertyType1.from_dict(data)
                    )

                    return additional_property_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                return cast(BulkUpdateSubscriberPreferencesDtoContextAdditionalPropertyType1 | str, data)

            additional_property = _parse_additional_property(prop_dict)

            additional_properties[prop_name] = additional_property

        bulk_update_subscriber_preferences_dto_context.additional_properties = additional_properties
        return bulk_update_subscriber_preferences_dto_context

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> BulkUpdateSubscriberPreferencesDtoContextAdditionalPropertyType1 | str:
        return self.additional_properties[key]

    def __setitem__(
        self, key: str, value: BulkUpdateSubscriberPreferencesDtoContextAdditionalPropertyType1 | str
    ) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
