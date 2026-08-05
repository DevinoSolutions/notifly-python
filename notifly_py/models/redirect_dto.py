from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.redirect_dto_target import RedirectDtoTarget
from ..types import UNSET, Unset

T = TypeVar("T", bound="RedirectDto")


@_attrs_define
class RedirectDto:
    """
    Attributes:
        url (str): URL to redirect to
        target (RedirectDtoTarget | Unset): Target attribute for the redirect link
    """

    url: str
    target: RedirectDtoTarget | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        target: str | Unset = UNSET
        if not isinstance(self.target, Unset):
            target = self.target.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "url": url,
            }
        )
        if target is not UNSET:
            field_dict["target"] = target

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url")

        _target = d.pop("target", UNSET)
        target: RedirectDtoTarget | Unset
        if isinstance(_target, Unset):
            target = UNSET
        else:
            target = RedirectDtoTarget(_target)

        redirect_dto = cls(
            url=url,
            target=target,
        )

        redirect_dto.additional_properties = d
        return redirect_dto

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
