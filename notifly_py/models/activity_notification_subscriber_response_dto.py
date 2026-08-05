from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivityNotificationSubscriberResponseDto")


@_attrs_define
class ActivityNotificationSubscriberResponseDto:
    """
    Attributes:
        subscriber_id (str): External unique identifier of the subscriber
        field_id (str): Internal to Notifly unique identifier of the subscriber
        first_name (str | Unset): First name of the subscriber
        last_name (str | Unset): Last name of the subscriber
        email (str | Unset): Email address of the subscriber
        phone (str | Unset): Phone number of the subscriber
    """

    subscriber_id: str
    field_id: str
    first_name: str | Unset = UNSET
    last_name: str | Unset = UNSET
    email: str | Unset = UNSET
    phone: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        subscriber_id = self.subscriber_id

        field_id = self.field_id

        first_name = self.first_name

        last_name = self.last_name

        email = self.email

        phone = self.phone

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "subscriberId": subscriber_id,
                "_id": field_id,
            }
        )
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if email is not UNSET:
            field_dict["email"] = email
        if phone is not UNSET:
            field_dict["phone"] = phone

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        subscriber_id = d.pop("subscriberId")

        field_id = d.pop("_id")

        first_name = d.pop("firstName", UNSET)

        last_name = d.pop("lastName", UNSET)

        email = d.pop("email", UNSET)

        phone = d.pop("phone", UNSET)

        activity_notification_subscriber_response_dto = cls(
            subscriber_id=subscriber_id,
            field_id=field_id,
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
        )

        activity_notification_subscriber_response_dto.additional_properties = d
        return activity_notification_subscriber_response_dto

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
