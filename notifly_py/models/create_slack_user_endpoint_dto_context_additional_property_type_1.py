from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_slack_user_endpoint_dto_context_additional_property_type_1_data import (
        CreateSlackUserEndpointDtoContextAdditionalPropertyType1Data,
    )


T = TypeVar("T", bound="CreateSlackUserEndpointDtoContextAdditionalPropertyType1")


@_attrs_define
class CreateSlackUserEndpointDtoContextAdditionalPropertyType1:
    """Rich context object with id and optional data

    Attributes:
        id (str):  Example: org-acme.
        data (CreateSlackUserEndpointDtoContextAdditionalPropertyType1Data | Unset): Optional additional context data
            Example: {'name': 'Acme Corp', 'region': 'us-east-1'}.
    """

    id: str
    data: CreateSlackUserEndpointDtoContextAdditionalPropertyType1Data | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_slack_user_endpoint_dto_context_additional_property_type_1_data import (
            CreateSlackUserEndpointDtoContextAdditionalPropertyType1Data,
        )

        d = dict(src_dict)
        id = d.pop("id")

        _data = d.pop("data", UNSET)
        data: CreateSlackUserEndpointDtoContextAdditionalPropertyType1Data | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = CreateSlackUserEndpointDtoContextAdditionalPropertyType1Data.from_dict(_data)

        create_slack_user_endpoint_dto_context_additional_property_type_1 = cls(
            id=id,
            data=data,
        )

        create_slack_user_endpoint_dto_context_additional_property_type_1.additional_properties = d
        return create_slack_user_endpoint_dto_context_additional_property_type_1

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
