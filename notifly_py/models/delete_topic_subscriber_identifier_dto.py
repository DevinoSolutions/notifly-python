from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeleteTopicSubscriberIdentifierDto")


@_attrs_define
class DeleteTopicSubscriberIdentifierDto:
    """
    Attributes:
        identifier (str | Unset): Unique identifier for this subscription. If provided, deletes only this specific
            subscription. Example: subscriber-123-subscription-a.
        subscriber_id (str | Unset): The subscriber ID. If provided without identifier, deletes all subscriptions for
            this subscriber within the topic. Example: subscriber-123.
    """

    identifier: str | Unset = UNSET
    subscriber_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        identifier = self.identifier

        subscriber_id = self.subscriber_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if subscriber_id is not UNSET:
            field_dict["subscriberId"] = subscriber_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        identifier = d.pop("identifier", UNSET)

        subscriber_id = d.pop("subscriberId", UNSET)

        delete_topic_subscriber_identifier_dto = cls(
            identifier=identifier,
            subscriber_id=subscriber_id,
        )

        delete_topic_subscriber_identifier_dto.additional_properties = d
        return delete_topic_subscriber_identifier_dto

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
