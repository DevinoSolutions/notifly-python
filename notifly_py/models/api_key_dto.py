from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ApiKeyDto")


@_attrs_define
class ApiKeyDto:
    """
    Attributes:
        key (str): API key Example: sk_test_1234567890abcdef.
        field_user_id (str): User ID associated with the API key Example: 60d5ecb8b3b3a30015f3e1a4.
        hash_ (str | Unset): Hashed representation of the API key Example: hash_value_here.
    """

    key: str
    field_user_id: str
    hash_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        key = self.key

        field_user_id = self.field_user_id

        hash_ = self.hash_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "_userId": field_user_id,
            }
        )
        if hash_ is not UNSET:
            field_dict["hash"] = hash_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        key = d.pop("key")

        field_user_id = d.pop("_userId")

        hash_ = d.pop("hash", UNSET)

        api_key_dto = cls(
            key=key,
            field_user_id=field_user_id,
            hash_=hash_,
        )

        api_key_dto.additional_properties = d
        return api_key_dto

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
