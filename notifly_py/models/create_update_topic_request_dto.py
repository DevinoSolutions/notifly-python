from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_update_topic_request_dto_data_type_0 import CreateUpdateTopicRequestDtoDataType0


T = TypeVar("T", bound="CreateUpdateTopicRequestDto")


@_attrs_define
class CreateUpdateTopicRequestDto:
    """
    Attributes:
        key (str): The unique key identifier for the topic. The key must contain only alphanumeric characters (a-z, A-Z,
            0-9), hyphens (-), underscores (_), colons (:), or be a valid email address. Example: task:12345.
        name (str | Unset): The display name for the topic Example: Task Title.
        data (CreateUpdateTopicRequestDtoDataType0 | None | Unset): Additional custom data associated with the topic.
            Flat key-value pairs of scalars (string, number, boolean, string[]). Maximum size: 64KB. Example: {'category':
            'product', 'priority': 1}.
    """

    key: str
    name: str | Unset = UNSET
    data: CreateUpdateTopicRequestDtoDataType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.create_update_topic_request_dto_data_type_0 import CreateUpdateTopicRequestDtoDataType0

        key = self.key

        name = self.name

        data: dict[str, Any] | None | Unset
        if isinstance(self.data, Unset):
            data = UNSET
        elif isinstance(self.data, CreateUpdateTopicRequestDtoDataType0):
            data = self.data.to_dict()
        else:
            data = self.data

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_update_topic_request_dto_data_type_0 import CreateUpdateTopicRequestDtoDataType0

        d = dict(src_dict)
        key = d.pop("key")

        name = d.pop("name", UNSET)

        def _parse_data(data: object) -> CreateUpdateTopicRequestDtoDataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = CreateUpdateTopicRequestDtoDataType0.from_dict(data)

                return data_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CreateUpdateTopicRequestDtoDataType0 | None | Unset, data)

        data = _parse_data(d.pop("data", UNSET))

        create_update_topic_request_dto = cls(
            key=key,
            name=name,
            data=data,
        )

        create_update_topic_request_dto.additional_properties = d
        return create_update_topic_request_dto

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
