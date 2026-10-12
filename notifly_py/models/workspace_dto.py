from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="WorkspaceDto")


@_attrs_define
class WorkspaceDto:
    """
    Attributes:
        id (str):  Example: T123456.
        name (str | Unset):  Example: Acme HQ.
        bot_user_id (str | Unset):  Example: U0123456789.
    """

    id: str
    name: str | Unset = UNSET
    bot_user_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        bot_user_id = self.bot_user_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if bot_user_id is not UNSET:
            field_dict["botUserId"] = bot_user_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name", UNSET)

        bot_user_id = d.pop("botUserId", UNSET)

        workspace_dto = cls(
            id=id,
            name=name,
            bot_user_id=bot_user_id,
        )

        workspace_dto.additional_properties = d
        return workspace_dto

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
