from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.actor_type_enum import ActorTypeEnum

T = TypeVar("T", bound="ActorFeedItemDto")


@_attrs_define
class ActorFeedItemDto:
    """
    Attributes:
        data (None | str): The data associated with the actor, can be null if not applicable.
        type_ (ActorTypeEnum): The type of the actor, indicating the role in the notification process.
    """

    data: None | str
    type_: ActorTypeEnum
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data: None | str
        data = self.data

        type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_data(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        data = _parse_data(d.pop("data"))

        type_ = ActorTypeEnum(d.pop("type"))

        actor_feed_item_dto = cls(
            data=data,
            type_=type_,
        )

        actor_feed_item_dto.additional_properties = d
        return actor_feed_item_dto

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
