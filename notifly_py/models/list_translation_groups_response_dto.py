from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.translation_group_dto import TranslationGroupDto


T = TypeVar("T", bound="ListTranslationGroupsResponseDto")


@_attrs_define
class ListTranslationGroupsResponseDto:
    """
    Attributes:
        data (list[TranslationGroupDto]): Translation groups for the current environment
        total (float): Total number of translation groups matching the query
        limit (float): Page size used for this listing
        offset (float): Offset used for this listing
    """

    data: list[TranslationGroupDto]
    total: float
    limit: float
    offset: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        total = self.total

        limit = self.limit

        offset = self.offset

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "total": total,
                "limit": limit,
                "offset": offset,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.translation_group_dto import TranslationGroupDto

        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = TranslationGroupDto.from_dict(data_item_data)

            data.append(data_item)

        total = d.pop("total")

        limit = d.pop("limit")

        offset = d.pop("offset")

        list_translation_groups_response_dto = cls(
            data=data,
            total=total,
            limit=limit,
            offset=offset,
        )

        list_translation_groups_response_dto.additional_properties = d
        return list_translation_groups_response_dto

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
