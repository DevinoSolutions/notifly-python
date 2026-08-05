from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.auto_configure_integration_response_dto_integration import (
        AutoConfigureIntegrationResponseDtoIntegration,
    )


T = TypeVar("T", bound="AutoConfigureIntegrationResponseDto")


@_attrs_define
class AutoConfigureIntegrationResponseDto:
    """
    Attributes:
        success (bool): Indicates whether the auto-configuration was successful
        message (str | Unset): Optional message describing the result or any errors that occurred
        integration (AutoConfigureIntegrationResponseDtoIntegration | Unset): The updated configurations after auto-
            configuration
    """

    success: bool
    message: str | Unset = UNSET
    integration: AutoConfigureIntegrationResponseDtoIntegration | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        success = self.success

        message = self.message

        integration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.integration, Unset):
            integration = self.integration.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "success": success,
            }
        )
        if message is not UNSET:
            field_dict["message"] = message
        if integration is not UNSET:
            field_dict["integration"] = integration

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.auto_configure_integration_response_dto_integration import (
            AutoConfigureIntegrationResponseDtoIntegration,
        )

        d = dict(src_dict)
        success = d.pop("success")

        message = d.pop("message", UNSET)

        _integration = d.pop("integration", UNSET)
        integration: AutoConfigureIntegrationResponseDtoIntegration | Unset
        if isinstance(_integration, Unset):
            integration = UNSET
        else:
            integration = AutoConfigureIntegrationResponseDtoIntegration.from_dict(_integration)

        auto_configure_integration_response_dto = cls(
            success=success,
            message=message,
            integration=integration,
        )

        auto_configure_integration_response_dto.additional_properties = d
        return auto_configure_integration_response_dto

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
