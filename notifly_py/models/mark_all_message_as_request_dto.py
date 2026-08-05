from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.mark_all_message_as_request_dto_mark_as import MarkAllMessageAsRequestDtoMarkAs
from ..types import UNSET, Unset

T = TypeVar("T", bound="MarkAllMessageAsRequestDto")


@_attrs_define
class MarkAllMessageAsRequestDto:
    """
    Attributes:
        mark_as (MarkAllMessageAsRequestDtoMarkAs): Mark all subscriber messages as read, unread, seen or unseen
        feed_identifier (list[str] | str | Unset): Optional feed identifier or array of feed identifiers
    """

    mark_as: MarkAllMessageAsRequestDtoMarkAs
    feed_identifier: list[str] | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mark_as = self.mark_as.value

        feed_identifier: list[str] | str | Unset
        if isinstance(self.feed_identifier, Unset):
            feed_identifier = UNSET
        elif isinstance(self.feed_identifier, list):
            feed_identifier = self.feed_identifier

        else:
            feed_identifier = self.feed_identifier

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "markAs": mark_as,
            }
        )
        if feed_identifier is not UNSET:
            field_dict["feedIdentifier"] = feed_identifier

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        mark_as = MarkAllMessageAsRequestDtoMarkAs(d.pop("markAs"))

        def _parse_feed_identifier(data: object) -> list[str] | str | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                feed_identifier_type_1 = cast(list[str], data)

                return feed_identifier_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | str | Unset, data)

        feed_identifier = _parse_feed_identifier(d.pop("feedIdentifier", UNSET))

        mark_all_message_as_request_dto = cls(
            mark_as=mark_as,
            feed_identifier=feed_identifier,
        )

        mark_all_message_as_request_dto.additional_properties = d
        return mark_all_message_as_request_dto

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
