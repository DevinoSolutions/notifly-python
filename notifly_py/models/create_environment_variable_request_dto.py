from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_environment_variable_request_dto_type import CreateEnvironmentVariableRequestDtoType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.environment_variable_value_dto import EnvironmentVariableValueDto


T = TypeVar("T", bound="CreateEnvironmentVariableRequestDto")


@_attrs_define
class CreateEnvironmentVariableRequestDto:
    """
    Attributes:
        key (str): Unique key for the variable. Must start with a letter and contain only letters, digits, and
            underscores.
        type_ (CreateEnvironmentVariableRequestDtoType | Unset): The type of the variable
        is_secret (bool | Unset): Whether this variable is a secret (encrypted at rest, masked in responses)
        values (list[EnvironmentVariableValueDto] | Unset):
    """

    key: str
    type_: CreateEnvironmentVariableRequestDtoType | Unset = UNSET
    is_secret: bool | Unset = UNSET
    values: list[EnvironmentVariableValueDto] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        is_secret = self.is_secret

        values: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.values, Unset):
            values = []
            for values_item_data in self.values:
                values_item = values_item_data.to_dict()
                values.append(values_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_
        if is_secret is not UNSET:
            field_dict["isSecret"] = is_secret
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.environment_variable_value_dto import EnvironmentVariableValueDto

        d = dict(src_dict)
        key = d.pop("key")

        _type_ = d.pop("type", UNSET)
        type_: CreateEnvironmentVariableRequestDtoType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = CreateEnvironmentVariableRequestDtoType(_type_)

        is_secret = d.pop("isSecret", UNSET)

        _values = d.pop("values", UNSET)
        values: list[EnvironmentVariableValueDto] | Unset = UNSET
        if _values is not UNSET:
            values = []
            for values_item_data in _values:
                values_item = EnvironmentVariableValueDto.from_dict(values_item_data)

                values.append(values_item)

        create_environment_variable_request_dto = cls(
            key=key,
            type_=type_,
            is_secret=is_secret,
            values=values,
        )

        create_environment_variable_request_dto.additional_properties = d
        return create_environment_variable_request_dto

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
