from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AddAgentIntegrationRequestDto")


@_attrs_define
class AddAgentIntegrationRequestDto:
    """
    Attributes:
        integration_identifier (str | Unset): The integration identifier (same as in the integration store), not the
            internal document _id.
        provider_id (str | Unset): Provider ID to auto-create a dedicated integration (e.g. novu-agent-email). When set,
            the server creates the integration if one does not already exist for this agent.
    """

    integration_identifier: str | Unset = UNSET
    provider_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        integration_identifier = self.integration_identifier

        provider_id = self.provider_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if integration_identifier is not UNSET:
            field_dict["integrationIdentifier"] = integration_identifier
        if provider_id is not UNSET:
            field_dict["providerId"] = provider_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        integration_identifier = d.pop("integrationIdentifier", UNSET)

        provider_id = d.pop("providerId", UNSET)

        add_agent_integration_request_dto = cls(
            integration_identifier=integration_identifier,
            provider_id=provider_id,
        )

        add_agent_integration_request_dto.additional_properties = d
        return add_agent_integration_request_dto

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
