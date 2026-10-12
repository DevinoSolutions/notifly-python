from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.chat_control_dto_editor_type import ChatControlDtoEditorType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.chat_control_dto_skip import ChatControlDtoSkip


T = TypeVar("T", bound="ChatControlDto")


@_attrs_define
class ChatControlDto:
    """
    Attributes:
        skip (ChatControlDtoSkip | Unset): JSONLogic filter conditions for conditionally skipping the step execution.
            Supports complex logical operations with AND, OR, and comparison operators. See https://jsonlogic.com/ for full
            typing reference. Example: {'and': [{'==': [{'var': 'payload.tier'}, 'pro']}, {'==': [{'var':
            'subscriber.data.role'}, 'admin']}, {'>': [{'var': 'payload.amount'}, '4']}]}.
        body (str | Unset): Content of the chat message.
        editor_type (ChatControlDtoEditorType | Unset): Type of editor to use for the body. When omitted, inferred from
            the body: Maily JSON is "block", otherwise "text".
    """

    skip: ChatControlDtoSkip | Unset = UNSET
    body: str | Unset = UNSET
    editor_type: ChatControlDtoEditorType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        skip: dict[str, Any] | Unset = UNSET
        if not isinstance(self.skip, Unset):
            skip = self.skip.to_dict()

        body = self.body

        editor_type: str | Unset = UNSET
        if not isinstance(self.editor_type, Unset):
            editor_type = self.editor_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if skip is not UNSET:
            field_dict["skip"] = skip
        if body is not UNSET:
            field_dict["body"] = body
        if editor_type is not UNSET:
            field_dict["editorType"] = editor_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chat_control_dto_skip import ChatControlDtoSkip

        d = dict(src_dict)
        _skip = d.pop("skip", UNSET)
        skip: ChatControlDtoSkip | Unset
        if isinstance(_skip, Unset):
            skip = UNSET
        else:
            skip = ChatControlDtoSkip.from_dict(_skip)

        body = d.pop("body", UNSET)

        _editor_type = d.pop("editorType", UNSET)
        editor_type: ChatControlDtoEditorType | Unset
        if isinstance(_editor_type, Unset):
            editor_type = UNSET
        else:
            editor_type = ChatControlDtoEditorType(_editor_type)

        chat_control_dto = cls(
            skip=skip,
            body=body,
            editor_type=editor_type,
        )

        chat_control_dto.additional_properties = d
        return chat_control_dto

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
