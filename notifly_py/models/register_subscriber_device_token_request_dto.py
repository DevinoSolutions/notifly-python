from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RegisterSubscriberDeviceTokenRequestDto")


@_attrs_define
class RegisterSubscriberDeviceTokenRequestDto:
    """
    Attributes:
        token (str): The device/push token to register. Sent in the body (not the path) because tokens can contain URL-
            hostile characters (e.g. a JSON-stringified web-push subscription).
        previous_token (str | Unset): The token the device previously held. When supplied, it is atomically removed as
            the new token is added (device token rotation), leaving no stale token behind.
        integration_identifier (str | Unset): Disambiguate when the environment has multiple active integrations for
            this provider.
        max_device_tokens (float | Unset): Maximum device tokens to retain for this subscriber/provider. On overflow the
            OLDEST tokens are dropped. Defaults to the environment/system limit when omitted.
    """

    token: str
    previous_token: str | Unset = UNSET
    integration_identifier: str | Unset = UNSET
    max_device_tokens: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token = self.token

        previous_token = self.previous_token

        integration_identifier = self.integration_identifier

        max_device_tokens = self.max_device_tokens

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "token": token,
            }
        )
        if previous_token is not UNSET:
            field_dict["previousToken"] = previous_token
        if integration_identifier is not UNSET:
            field_dict["integrationIdentifier"] = integration_identifier
        if max_device_tokens is not UNSET:
            field_dict["maxDeviceTokens"] = max_device_tokens

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        token = d.pop("token")

        previous_token = d.pop("previousToken", UNSET)

        integration_identifier = d.pop("integrationIdentifier", UNSET)

        max_device_tokens = d.pop("maxDeviceTokens", UNSET)

        register_subscriber_device_token_request_dto = cls(
            token=token,
            previous_token=previous_token,
            integration_identifier=integration_identifier,
            max_device_tokens=max_device_tokens,
        )

        register_subscriber_device_token_request_dto.additional_properties = d
        return register_subscriber_device_token_request_dto

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
