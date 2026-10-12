from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WebexPersonEndpointDto")


@_attrs_define
class WebexPersonEndpointDto:
    """
    Attributes:
        person_id (str | Unset): Webex person ID. Provide exactly one of personId or personEmail. Example:
            Y2lzY29zcGFyazovL3VzL1BFT1BMRS8....
        person_email (str | Unset): Webex person email. Provide exactly one of personId or personEmail. Example:
            user@example.com.
    """

    person_id: str | Unset = UNSET
    person_email: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        person_id = self.person_id

        person_email = self.person_email

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if person_id is not UNSET:
            field_dict["personId"] = person_id
        if person_email is not UNSET:
            field_dict["personEmail"] = person_email

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        person_id = d.pop("personId", UNSET)

        person_email = d.pop("personEmail", UNSET)

        webex_person_endpoint_dto = cls(
            person_id=person_id,
            person_email=person_email,
        )

        webex_person_endpoint_dto.additional_properties = d
        return webex_person_endpoint_dto

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
