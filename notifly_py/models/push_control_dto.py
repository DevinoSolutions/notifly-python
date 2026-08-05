from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.push_control_dto_skip import PushControlDtoSkip


T = TypeVar("T", bound="PushControlDto")


@_attrs_define
class PushControlDto:
    """
    Attributes:
        skip (PushControlDtoSkip | Unset): JSONLogic filter conditions for conditionally skipping the step execution.
            Supports complex logical operations with AND, OR, and comparison operators. See https://jsonlogic.com/ for full
            typing reference. Example: {'and': [{'==': [{'var': 'payload.tier'}, 'pro']}, {'==': [{'var':
            'subscriber.data.role'}, 'admin']}, {'>': [{'var': 'payload.amount'}, '4']}]}.
        subject (str | Unset): Subject/title of the push notification.
        body (str | Unset): Body content of the push notification.
    """

    skip: PushControlDtoSkip | Unset = UNSET
    subject: str | Unset = UNSET
    body: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        skip: dict[str, Any] | Unset = UNSET
        if not isinstance(self.skip, Unset):
            skip = self.skip.to_dict()

        subject = self.subject

        body = self.body

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if skip is not UNSET:
            field_dict["skip"] = skip
        if subject is not UNSET:
            field_dict["subject"] = subject
        if body is not UNSET:
            field_dict["body"] = body

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.push_control_dto_skip import PushControlDtoSkip

        d = dict(src_dict)
        _skip = d.pop("skip", UNSET)
        skip: PushControlDtoSkip | Unset
        if isinstance(_skip, Unset):
            skip = UNSET
        else:
            skip = PushControlDtoSkip.from_dict(_skip)

        subject = d.pop("subject", UNSET)

        body = d.pop("body", UNSET)

        push_control_dto = cls(
            skip=skip,
            subject=subject,
            body=body,
        )

        push_control_dto.additional_properties = d
        return push_control_dto

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
