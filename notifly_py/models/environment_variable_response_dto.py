from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.environment_variable_response_dto_type import EnvironmentVariableResponseDtoType

if TYPE_CHECKING:
    from ..models.environment_variable_value_response_dto import EnvironmentVariableValueResponseDto


T = TypeVar("T", bound="EnvironmentVariableResponseDto")


@_attrs_define
class EnvironmentVariableResponseDto:
    """
    Attributes:
        field_id (str):
        field_organization_id (str):
        key (str):
        type_ (EnvironmentVariableResponseDtoType):
        is_secret (bool):
        values (list[EnvironmentVariableValueResponseDto]):
        created_at (str):
        updated_at (str):
    """

    field_id: str
    field_organization_id: str
    key: str
    type_: EnvironmentVariableResponseDtoType
    is_secret: bool
    values: list[EnvironmentVariableValueResponseDto]
    created_at: str
    updated_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_id = self.field_id

        field_organization_id = self.field_organization_id

        key = self.key

        type_ = self.type_.value

        is_secret = self.is_secret

        values = []
        for values_item_data in self.values:
            values_item = values_item_data.to_dict()
            values.append(values_item)

        created_at = self.created_at

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "_id": field_id,
                "_organizationId": field_organization_id,
                "key": key,
                "type": type_,
                "isSecret": is_secret,
                "values": values,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.environment_variable_value_response_dto import EnvironmentVariableValueResponseDto

        d = dict(src_dict)
        field_id = d.pop("_id")

        field_organization_id = d.pop("_organizationId")

        key = d.pop("key")

        type_ = EnvironmentVariableResponseDtoType(d.pop("type"))

        is_secret = d.pop("isSecret")

        values = []
        _values = d.pop("values")
        for values_item_data in _values:
            values_item = EnvironmentVariableValueResponseDto.from_dict(values_item_data)

            values.append(values_item)

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        environment_variable_response_dto = cls(
            field_id=field_id,
            field_organization_id=field_organization_id,
            key=key,
            type_=type_,
            is_secret=is_secret,
            values=values,
            created_at=created_at,
            updated_at=updated_at,
        )

        environment_variable_response_dto.additional_properties = d
        return environment_variable_response_dto

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
