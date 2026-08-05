from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_context_request_dto_data import CreateContextRequestDtoData


T = TypeVar("T", bound="CreateContextRequestDto")


@_attrs_define
class CreateContextRequestDto:
    """
    Attributes:
        type_ (str): Context type (e.g., tenant, app, workspace). Must be lowercase alphanumeric with optional
            separators. Example: tenant.
        id (str): Unique identifier for this context. Must be lowercase alphanumeric with optional separators. Example:
            org-acme.
        data (CreateContextRequestDtoData | Unset): Optional custom data to associate with this context. Example:
            {'tenantName': 'Acme Corp', 'region': 'us-east-1', 'settings': {'theme': 'dark'}}.
    """

    type_: str
    id: str
    data: CreateContextRequestDtoData | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        id = self.id

        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "id": id,
            }
        )
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_context_request_dto_data import CreateContextRequestDtoData

        d = dict(src_dict)
        type_ = d.pop("type")

        id = d.pop("id")

        _data = d.pop("data", UNSET)
        data: CreateContextRequestDtoData | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = CreateContextRequestDtoData.from_dict(_data)

        create_context_request_dto = cls(
            type_=type_,
            id=id,
            data=data,
        )

        create_context_request_dto.additional_properties = d
        return create_context_request_dto

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
