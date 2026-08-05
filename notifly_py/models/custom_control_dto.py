from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_control_dto_custom import CustomControlDtoCustom


T = TypeVar("T", bound="CustomControlDto")


@_attrs_define
class CustomControlDto:
    """
    Attributes:
        custom (CustomControlDtoCustom | Unset): Custom control values for the step.
    """

    custom: CustomControlDtoCustom | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        custom: dict[str, Any] | Unset = UNSET
        if not isinstance(self.custom, Unset):
            custom = self.custom.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if custom is not UNSET:
            field_dict["custom"] = custom

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.custom_control_dto_custom import CustomControlDtoCustom

        d = dict(src_dict)
        _custom = d.pop("custom", UNSET)
        custom: CustomControlDtoCustom | Unset
        if isinstance(_custom, Unset):
            custom = UNSET
        else:
            custom = CustomControlDtoCustom.from_dict(_custom)

        custom_control_dto = cls(
            custom=custom,
        )

        custom_control_dto.additional_properties = d
        return custom_control_dto

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
