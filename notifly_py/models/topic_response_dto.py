from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TopicResponseDto")


@_attrs_define
class TopicResponseDto:
    """
    Attributes:
        field_id (str): The identifier of the topic Example: 64da692e9a94fb2e6449ad06.
        key (str): The unique key of the topic Example: product-updates.
        name (str | Unset): The name of the topic Example: Product Updates.
        created_at (str | Unset): The date the topic was created Example: 2023-08-15T00:00:00.000Z.
        updated_at (str | Unset): The date the topic was last updated Example: 2023-08-15T00:00:00.000Z.
    """

    field_id: str
    key: str
    name: str | Unset = UNSET
    created_at: str | Unset = UNSET
    updated_at: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_id = self.field_id

        key = self.key

        name = self.name

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
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_id = d.pop("_id")

        key = d.pop("key")

        name = d.pop("name", UNSET)

        created_at = d.pop("createdAt", UNSET)

        updated_at = d.pop("updatedAt", UNSET)

        topic_response_dto = cls(
            field_id=field_id,
            key=key,
            name=name,
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
