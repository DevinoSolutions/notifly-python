from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.opsgenie_integration_endpoint_dto_region import OpsgenieIntegrationEndpointDtoRegion

T = TypeVar("T", bound="OpsgenieIntegrationEndpointDto")


@_attrs_define
class OpsgenieIntegrationEndpointDto:
    """
    Attributes:
        api_key (str): Opsgenie API integration key (GenieKey) in UUID format. Encrypted at rest on the channel endpoint
            (`endpoint` field). Example: abcdefg-a25a-4652-883c-73703b12345.
        region (OpsgenieIntegrationEndpointDtoRegion): Opsgenie account region that determines the alert API data-center
            endpoint. Example: us.
    """

    api_key: str
    region: OpsgenieIntegrationEndpointDtoRegion
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        api_key = self.api_key

        region = self.region.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "apiKey": api_key,
                "region": region,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        api_key = d.pop("apiKey")

        region = OpsgenieIntegrationEndpointDtoRegion(d.pop("region"))

        opsgenie_integration_endpoint_dto = cls(
            api_key=api_key,
            region=region,
        )

        opsgenie_integration_endpoint_dto.additional_properties = d
        return opsgenie_integration_endpoint_dto

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
