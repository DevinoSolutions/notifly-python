from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TopicSubscriberIdentifierDto")


@_attrs_define
class TopicSubscriberIdentifierDto:
    """
    Attributes:
        identifier (str): Unique identifier for this subscription Example: subscriber-123-subscription-a.
        subscriber_id (str): The subscriber ID Example: subscriber-123.
        name (str | Unset): The name of the subscription Example: My Subscription.
    """

    identifier: str
    subscriber_id: str
    name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        identifier = self.identifier

        subscriber_id = self.subscriber_id

        name = self.name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "identifier": identifier,
                "subscriberId": subscriber_id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        identifier = d.pop("identifier")

        subscriber_id = d.pop("subscriberId")

        name = d.pop("name", UNSET)

        topic_subscriber_identifier_dto = cls(
            identifier=identifier,
            subscriber_id=subscriber_id,
            name=name,
        )

        topic_subscriber_identifier_dto.additional_properties = d
        return topic_subscriber_identifier_dto

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
