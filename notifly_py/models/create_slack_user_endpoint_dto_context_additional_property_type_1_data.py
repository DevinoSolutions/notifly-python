from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CreateSlackUserEndpointDtoContextAdditionalPropertyType1Data")


@_attrs_define
class CreateSlackUserEndpointDtoContextAdditionalPropertyType1Data:
    """Optional additional context data

    Example:
        {'name': 'Acme Corp', 'region': 'us-east-1'}

    """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        create_slack_user_endpoint_dto_context_additional_property_type_1_data = cls()

        create_slack_user_endpoint_dto_context_additional_property_type_1_data.additional_properties = d
        return create_slack_user_endpoint_dto_context_additional_property_type_1_data

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
