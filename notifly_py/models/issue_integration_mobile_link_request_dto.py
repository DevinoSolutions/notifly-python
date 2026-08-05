from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="IssueIntegrationMobileLinkRequestDto")


@_attrs_define
class IssueIntegrationMobileLinkRequestDto:
    """
    Attributes:
        subscriber_id (str | Unset): Optional subscriber to link via `/start` deep link after mobile setup completes.
            When provided, the consume response may include a ready-to-open Telegram deep link. Example: subscriber-123.
    """

    subscriber_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        subscriber_id = self.subscriber_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if subscriber_id is not UNSET:
            field_dict["subscriberId"] = subscriber_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        subscriber_id = d.pop("subscriberId", UNSET)

        issue_integration_mobile_link_request_dto = cls(
            subscriber_id=subscriber_id,
        )

        issue_integration_mobile_link_request_dto.additional_properties = d
        return issue_integration_mobile_link_request_dto

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
