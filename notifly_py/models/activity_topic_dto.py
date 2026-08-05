from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ActivityTopicDto")


@_attrs_define
class ActivityTopicDto:
    """
    Attributes:
        field_topic_id (str): Internal Topic ID of the notification
        topic_key (str): Topic Key of the notification
    """

    field_topic_id: str
    topic_key: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_topic_id = self.field_topic_id

        topic_key = self.topic_key

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "_topicId": field_topic_id,
                "topicKey": topic_key,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_topic_id = d.pop("_topicId")

        topic_key = d.pop("topicKey")

        activity_topic_dto = cls(
            field_topic_id=field_topic_id,
            topic_key=topic_key,
        )

        activity_topic_dto.additional_properties = d
        return activity_topic_dto

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
