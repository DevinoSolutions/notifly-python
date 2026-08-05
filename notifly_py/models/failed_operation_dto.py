from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="FailedOperationDto")


@_attrs_define
class FailedOperationDto:
    """
    Attributes:
        message (str | Unset): The error message associated with the failed operation.
        subscriber_id (str | Unset): The subscriber ID associated with the failed operation. This field is optional.
    """

    message: str | Unset = UNSET
    subscriber_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        subscriber_id = self.subscriber_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if message is not UNSET:
            field_dict["message"] = message
        if subscriber_id is not UNSET:
            field_dict["subscriberId"] = subscriber_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        message = d.pop("message", UNSET)

        subscriber_id = d.pop("subscriberId", UNSET)

        failed_operation_dto = cls(
            message=message,
            subscriber_id=subscriber_id,
        )

        failed_operation_dto.additional_properties = d
        return failed_operation_dto

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
