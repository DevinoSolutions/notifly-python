from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_context_request_dto_data import UpdateContextRequestDtoData


T = TypeVar("T", bound="UpdateContextRequestDto")


@_attrs_define
class UpdateContextRequestDto:
    """
    Attributes:
        data (UpdateContextRequestDtoData): Custom data to associate with this context. Replaces existing data. Example:
            {'tenantName': 'Acme Corp', 'region': 'us-east-1', 'settings': {'theme': 'dark'}}.
        bridge_url (None | str | Unset): Optional bridge URL override for agent connect. When an inbound agent turn
            resolves this context, its bridge call is routed here instead of the agent default bridge URL. Must be a
            publicly reachable URL. Pass null to clear an existing override. Example: https://tenant-
            acme.example.com/api/novu.
    """

    data: UpdateContextRequestDtoData
    bridge_url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_dict()

        bridge_url: None | str | Unset
        if isinstance(self.bridge_url, Unset):
            bridge_url = UNSET
        else:
            bridge_url = self.bridge_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
            }
        )
        if bridge_url is not UNSET:
            field_dict["bridgeUrl"] = bridge_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_context_request_dto_data import UpdateContextRequestDtoData

        d = dict(src_dict)
        data = UpdateContextRequestDtoData.from_dict(d.pop("data"))

        def _parse_bridge_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bridge_url = _parse_bridge_url(d.pop("bridgeUrl", UNSET))

        update_context_request_dto = cls(
            data=data,
            bridge_url=bridge_url,
        )

        update_context_request_dto.additional_properties = d
        return update_context_request_dto

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
