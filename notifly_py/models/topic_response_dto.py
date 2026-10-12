from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.topic_response_dto_data import TopicResponseDtoData


T = TypeVar("T", bound="TopicResponseDto")


@_attrs_define
class TopicResponseDto:
    """
    Attributes:
        field_id (str): The identifier of the topic Example: 64da692e9a94fb2e6449ad06.
        key (str): The unique key of the topic Example: product-updates.
        name (str | Unset): The name of the topic Example: Product Updates.
        data (TopicResponseDtoData | Unset): Additional custom data associated with the topic Example: {'category':
            'product', 'priority': 1}.
        created_at (str | Unset): The date the topic was created Example: 2023-08-15T00:00:00.000Z.
        updated_at (str | Unset): The date the topic was last updated Example: 2023-08-15T00:00:00.000Z.
    """

    field_id: str
    key: str
    name: str | Unset = UNSET
    data: TopicResponseDtoData | Unset = UNSET
    created_at: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_id = self.field_id

        key = self.key

        name = self.name

        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        created_at = self.created_at

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "_id": field_id,
                "key": key,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if data is not UNSET:
            field_dict["data"] = data
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.topic_response_dto_data import TopicResponseDtoData

        d = dict(src_dict)
        field_id = d.pop("_id")

        key = d.pop("key")

        name = d.pop("name", UNSET)

        _data = d.pop("data", UNSET)
        data: TopicResponseDtoData | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = TopicResponseDtoData.from_dict(_data)

        created_at = d.pop("createdAt", UNSET)

        updated_at = d.pop("updatedAt", UNSET)

        topic_response_dto = cls(
            field_id=field_id,
            key=key,
            name=name,
            data=data,
            created_at=created_at,
            updated_at=updated_at,
        )

        topic_response_dto.additional_properties = d
        return topic_response_dto

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
