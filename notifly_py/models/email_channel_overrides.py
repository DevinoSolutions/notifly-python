from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EmailChannelOverrides")


@_attrs_define
class EmailChannelOverrides:
    """
    Attributes:
        layout_id (None | str | Unset): Override or remove the layout for all email steps in the workflow Example:
            promotional-layout-2024.
    """

    layout_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        layout_id: None | str | Unset
        if isinstance(self.layout_id, Unset):
            layout_id = UNSET
        else:
            layout_id = self.layout_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if layout_id is not UNSET:
            field_dict["layoutId"] = layout_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_layout_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        layout_id = _parse_layout_id(d.pop("layoutId", UNSET))

        email_channel_overrides = cls(
            layout_id=layout_id,
        )

        email_channel_overrides.additional_properties = d
        return email_channel_overrides

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
