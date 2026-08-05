from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.redirect_dto import RedirectDto


T = TypeVar("T", bound="ActionDto")


@_attrs_define
class ActionDto:
    """
    Attributes:
        label (str | Unset): Label for the action button.
        redirect (RedirectDto | Unset):
    """

    label: str | Unset = UNSET
    redirect: RedirectDto | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        label = self.label

        redirect: dict[str, Any] | Unset = UNSET
        if not isinstance(self.redirect, Unset):
            redirect = self.redirect.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if label is not UNSET:
            field_dict["label"] = label
        if redirect is not UNSET:
            field_dict["redirect"] = redirect

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.redirect_dto import RedirectDto

        d = dict(src_dict)
        label = d.pop("label", UNSET)

        _redirect = d.pop("redirect", UNSET)
        redirect: RedirectDto | Unset
        if isinstance(_redirect, Unset):
            redirect = UNSET
        else:
            redirect = RedirectDto.from_dict(_redirect)

        action_dto = cls(
            label=label,
            redirect=redirect,
        )

        action_dto.additional_properties = d
        return action_dto

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
