from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.resource_diff_dto_diffs_new_type_0 import ResourceDiffDtoDiffsNewType0
    from ..models.resource_diff_dto_diffs_previous_type_0 import ResourceDiffDtoDiffsPreviousType0


T = TypeVar("T", bound="ResourceDiffDtoDiffs")


@_attrs_define
class ResourceDiffDtoDiffs:
    """Detailed changes (only for modified resources)

    Attributes:
        previous (None | ResourceDiffDtoDiffsPreviousType0 | Unset): Previous state of the resource (null for added
            resources)
        new (None | ResourceDiffDtoDiffsNewType0 | Unset): New state of the resource (null for deleted resources)
    """

    previous: None | ResourceDiffDtoDiffsPreviousType0 | Unset = UNSET
    new: None | ResourceDiffDtoDiffsNewType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.resource_diff_dto_diffs_new_type_0 import ResourceDiffDtoDiffsNewType0
        from ..models.resource_diff_dto_diffs_previous_type_0 import ResourceDiffDtoDiffsPreviousType0

        previous: dict[str, Any] | None | Unset
        if isinstance(self.previous, Unset):
            previous = UNSET
        elif isinstance(self.previous, ResourceDiffDtoDiffsPreviousType0):
            previous = self.previous.to_dict()
        else:
            previous = self.previous

        new: dict[str, Any] | None | Unset
        if isinstance(self.new, Unset):
            new = UNSET
        elif isinstance(self.new, ResourceDiffDtoDiffsNewType0):
            new = self.new.to_dict()
        else:
            new = self.new

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if previous is not UNSET:
            field_dict["previous"] = previous
        if new is not UNSET:
            field_dict["new"] = new

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.resource_diff_dto_diffs_new_type_0 import ResourceDiffDtoDiffsNewType0
        from ..models.resource_diff_dto_diffs_previous_type_0 import ResourceDiffDtoDiffsPreviousType0

        d = dict(src_dict)

        def _parse_previous(data: object) -> None | ResourceDiffDtoDiffsPreviousType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                previous_type_0 = ResourceDiffDtoDiffsPreviousType0.from_dict(data)

                return previous_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ResourceDiffDtoDiffsPreviousType0 | Unset, data)

        previous = _parse_previous(d.pop("previous", UNSET))

        def _parse_new(data: object) -> None | ResourceDiffDtoDiffsNewType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                new_type_0 = ResourceDiffDtoDiffsNewType0.from_dict(data)

                return new_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ResourceDiffDtoDiffsNewType0 | Unset, data)

        new = _parse_new(d.pop("new", UNSET))

        resource_diff_dto_diffs = cls(
            previous=previous,
            new=new,
        )

        resource_diff_dto_diffs.additional_properties = d
        return resource_diff_dto_diffs

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
