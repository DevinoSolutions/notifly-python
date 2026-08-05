from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InboxSubscriberResponseDto")


@_attrs_define
class InboxSubscriberResponseDto:
    """
    Attributes:
        id (str): Unique identifier of the subscriber
        subscriber_id (str): External subscriber identifier
        first_name (str | Unset): First name of the subscriber
        last_name (str | Unset): Last name of the subscriber
        avatar (str | Unset): Avatar URL of the subscriber
    """

    id: str
    subscriber_id: str
    first_name: str | Unset = UNSET
    last_name: str | Unset = UNSET
    avatar: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        subscriber_id = self.subscriber_id

        first_name = self.first_name

        last_name = self.last_name

        avatar = self.avatar

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "subscriberId": subscriber_id,
            }
        )
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if avatar is not UNSET:
            field_dict["avatar"] = avatar

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        subscriber_id = d.pop("subscriberId")

        first_name = d.pop("firstName", UNSET)

        last_name = d.pop("lastName", UNSET)

        avatar = d.pop("avatar", UNSET)

        inbox_subscriber_response_dto = cls(
            id=id,
            subscriber_id=subscriber_id,
            first_name=first_name,
            last_name=last_name,
            avatar=avatar,
        )

        inbox_subscriber_response_dto.additional_properties = d
        return inbox_subscriber_response_dto

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
