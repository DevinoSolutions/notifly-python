from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TriggerEventRequestDtoPayload")


@_attrs_define
class TriggerEventRequestDtoPayload:
    """The payload object is used to pass additional custom information that could be
        used to render the workflow, or perform routing rules based on it.
          This data will also be available when fetching the notifications feed from the API to display certain parts of
    the UI.

        Example:
            {'comment_id': 'string', 'post': {'text': 'string'}}

    """

    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        trigger_event_request_dto_payload = cls()

        trigger_event_request_dto_payload.additional_properties = d
        return trigger_event_request_dto_payload

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
