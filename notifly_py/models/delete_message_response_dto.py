from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.delete_message_response_dto_status import DeleteMessageResponseDtoStatus

T = TypeVar("T", bound="DeleteMessageResponseDto")


@_attrs_define
class DeleteMessageResponseDto:
    """
    Attributes:
        acknowledged (bool): A boolean stating the success of the action
        status (DeleteMessageResponseDtoStatus): The status enum for the performed action
    """

    acknowledged: bool
    status: DeleteMessageResponseDtoStatus
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        acknowledged = self.acknowledged

        status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "acknowledged": acknowledged,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        acknowledged = d.pop("acknowledged")

        status = DeleteMessageResponseDtoStatus(d.pop("status"))

        delete_message_response_dto = cls(
            acknowledged=acknowledged,
            status=status,
        )

        delete_message_response_dto.additional_properties = d
        return delete_message_response_dto

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
