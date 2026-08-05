from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.email_controls_dto import EmailControlsDto


T = TypeVar("T", bound="LayoutControlValuesDto")


@_attrs_define
class LayoutControlValuesDto:
    """
    Attributes:
        email (EmailControlsDto | Unset):
    """

    email: EmailControlsDto | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email: dict[str, Any] | Unset = UNSET
        if not isinstance(self.email, Unset):
            email = self.email.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if email is not UNSET:
            field_dict["email"] = email

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.email_controls_dto import EmailControlsDto

        d = dict(src_dict)
        _email = d.pop("email", UNSET)
        email: EmailControlsDto | Unset
        if isinstance(_email, Unset):
            email = UNSET
        else:
            email = EmailControlsDto.from_dict(_email)

        layout_control_values_dto = cls(
            email=email,
        )

        layout_control_values_dto.additional_properties = d
        return layout_control_values_dto

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
