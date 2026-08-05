from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TopicSubscriberDto")


@_attrs_define
class TopicSubscriberDto:
    """
    Attributes:
        field_organization_id (str): Unique identifier for the organization Example: org_123456789.
        field_environment_id (str): Unique identifier for the environment Example: env_123456789.
        field_subscriber_id (str): Unique identifier for the subscriber Example: sub_123456789.
        field_topic_id (str): Unique identifier for the topic Example: topic_123456789.
        topic_key (str): Key associated with the topic Example: my_topic_key.
        external_subscriber_id (str): External identifier for the subscriber Example: external_subscriber_123.
    """

    field_organization_id: str
    field_environment_id: str
    field_subscriber_id: str
    field_topic_id: str
    topic_key: str
    external_subscriber_id: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_organization_id = self.field_organization_id

        field_environment_id = self.field_environment_id

        field_subscriber_id = self.field_subscriber_id

        field_topic_id = self.field_topic_id

        topic_key = self.topic_key

        external_subscriber_id = self.external_subscriber_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "_organizationId": field_organization_id,
                "_environmentId": field_environment_id,
                "_subscriberId": field_subscriber_id,
                "_topicId": field_topic_id,
                "topicKey": topic_key,
                "externalSubscriberId": external_subscriber_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_organization_id = d.pop("_organizationId")

        field_environment_id = d.pop("_environmentId")

        field_subscriber_id = d.pop("_subscriberId")

        field_topic_id = d.pop("_topicId")

        topic_key = d.pop("topicKey")

        external_subscriber_id = d.pop("externalSubscriberId")

        topic_subscriber_dto = cls(
            field_organization_id=field_organization_id,
            field_environment_id=field_environment_id,
            field_subscriber_id=field_subscriber_id,
            field_topic_id=field_topic_id,
            topic_key=topic_key,
            external_subscriber_id=external_subscriber_id,
        )

        topic_subscriber_dto.additional_properties = d
        return topic_subscriber_dto

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
