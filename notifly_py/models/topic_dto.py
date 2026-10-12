from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.topic_dto_data import TopicDtoData


T = TypeVar("T", bound="TopicDto")


@_attrs_define
class TopicDto:
    """
    Attributes:
        field_id (str): The internal unique identifier of the topic Example: 64f5e95d3d7946d80d0cb677.
        key (str): The key identifier of the topic used in your application. Should be unique on the environment level.
            Example: product-updates.
        name (str | Unset): The name of the topic Example: Product Updates.
        data (TopicDtoData | Unset): Additional custom data associated with the topic Example: {'category': 'product',
            'priority': 1}.
    """

    field_id: str
    key: str
    name: str | Unset = UNSET
    data: TopicDtoData | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_id = self.field_id

        key = self.key

        name = self.name

        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

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

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.topic_dto_data import TopicDtoData

        d = dict(src_dict)
        field_id = d.pop("_id")

        key = d.pop("key")

        name = d.pop("name", UNSET)

        _data = d.pop("data", UNSET)
        data: TopicDtoData | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = TopicDtoData.from_dict(_data)

        topic_dto = cls(
            field_id=field_id,
            key=key,
            name=name,
            data=data,
        )

        topic_dto.additional_properties = d
        return topic_dto

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
