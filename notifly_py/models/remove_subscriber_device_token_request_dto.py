from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RemoveSubscriberDeviceTokenRequestDto")


@_attrs_define
class RemoveSubscriberDeviceTokenRequestDto:
    """
    Attributes:
        token (str): The device/push token to remove. Sent in the body (not the path) because tokens can contain URL-
            hostile characters (e.g. a JSON-stringified web-push subscription). Only this token is removed; the rest of the
            channel is left intact.
        integration_identifier (str | Unset): Disambiguate when the environment has multiple active integrations for
            this provider.
    """

    token: str
    integration_identifier: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token = self.token

        integration_identifier = self.integration_identifier

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "token": token,
            }
        )
        if integration_identifier is not UNSET:
            field_dict["integrationIdentifier"] = integration_identifier

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        token = d.pop("token")

        integration_identifier = d.pop("integrationIdentifier", UNSET)

        remove_subscriber_device_token_request_dto = cls(
            token=token,
            integration_identifier=integration_identifier,
        )

        remove_subscriber_device_token_request_dto.additional_properties = d
        return remove_subscriber_device_token_request_dto

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
