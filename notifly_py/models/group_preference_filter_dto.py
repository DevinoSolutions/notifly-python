from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.group_preference_filter_details_dto import GroupPreferenceFilterDetailsDto
    from ..models.group_preference_filter_dto_condition import GroupPreferenceFilterDtoCondition


T = TypeVar("T", bound="GroupPreferenceFilterDto")


@_attrs_define
class GroupPreferenceFilterDto:
    """
    Attributes:
        filter_ (GroupPreferenceFilterDetailsDto):
        enabled (bool | Unset): Whether the preference is enabled. Used when condition is not provided. Example: True.
        condition (GroupPreferenceFilterDtoCondition | Unset): Optional condition using JSON Logic rules Example:
            {'and': [{'===': [{'var': 'tier'}, 'premium']}]}.
    """

    filter_: GroupPreferenceFilterDetailsDto
    enabled: bool | Unset = UNSET
    condition: GroupPreferenceFilterDtoCondition | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        filter_ = self.filter_.to_dict()

        enabled = self.enabled

        condition: dict[str, Any] | Unset = UNSET
        if not isinstance(self.condition, Unset):
            condition = self.condition.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "filter": filter_,
            }
        )
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if condition is not UNSET:
            field_dict["condition"] = condition

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.group_preference_filter_details_dto import GroupPreferenceFilterDetailsDto
        from ..models.group_preference_filter_dto_condition import GroupPreferenceFilterDtoCondition

        d = dict(src_dict)
        filter_ = GroupPreferenceFilterDetailsDto.from_dict(d.pop("filter"))

        enabled = d.pop("enabled", UNSET)

        _condition = d.pop("condition", UNSET)
        condition: GroupPreferenceFilterDtoCondition | Unset
        if isinstance(_condition, Unset):
            condition = UNSET
        else:
            condition = GroupPreferenceFilterDtoCondition.from_dict(_condition)

        group_preference_filter_dto = cls(
            filter_=filter_,
            enabled=enabled,
            condition=condition,
        )

        group_preference_filter_dto.additional_properties = d
        return group_preference_filter_dto

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
