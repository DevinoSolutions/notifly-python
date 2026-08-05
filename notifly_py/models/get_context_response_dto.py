from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.get_context_response_dto_data import GetContextResponseDtoData


T = TypeVar("T", bound="GetContextResponseDto")


@_attrs_define
class GetContextResponseDto:
    """
    Attributes:
        type_ (str): Context type (e.g., tenant, app, workspace)
        id (str): Unique identifier for this context
        data (GetContextResponseDtoData): Custom data associated with this context
        created_at (str): Creation timestamp
        updated_at (str): Last update timestamp
    """

    type_: str
    id: str
    data: GetContextResponseDtoData
    created_at: str
    updated_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        id = self.id

        data = self.data.to_dict()

        created_at = self.created_at

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "id": id,
                "data": data,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_context_response_dto_data import GetContextResponseDtoData

        d = dict(src_dict)
        type_ = d.pop("type")

        id = d.pop("id")

        data = GetContextResponseDtoData.from_dict(d.pop("data"))

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        get_context_response_dto = cls(
            type_=type_,
            id=id,
            data=data,
            created_at=created_at,
            updated_at=updated_at,
        )

        get_context_response_dto.additional_properties = d
        return get_context_response_dto

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
