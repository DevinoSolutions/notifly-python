from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pager_duty_service_endpoint_dto_region import PagerDutyServiceEndpointDtoRegion

T = TypeVar("T", bound="PagerDutyServiceEndpointDto")


@_attrs_define
class PagerDutyServiceEndpointDto:
    """
    Attributes:
        routing_key (str): PagerDuty Events API v2 integration key (32-character alphanumeric string). Encrypted at rest
            on the channel endpoint (`endpoint` field). Example: R0UTINGK3YEXAMPLE000000000000000.
        region (PagerDutyServiceEndpointDtoRegion): PagerDuty account region — determines the events API data-center
            endpoint. Example: us.
    """

    routing_key: str
    region: PagerDutyServiceEndpointDtoRegion
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        routing_key = self.routing_key

        region = self.region.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "routingKey": routing_key,
                "region": region,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        routing_key = d.pop("routingKey")

        region = PagerDutyServiceEndpointDtoRegion(d.pop("region"))

        pager_duty_service_endpoint_dto = cls(
            routing_key=routing_key,
            region=region,
        )

        pager_duty_service_endpoint_dto.additional_properties = d
        return pager_duty_service_endpoint_dto

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
