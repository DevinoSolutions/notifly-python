from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.chat_render_output_card import ChatRenderOutputCard


T = TypeVar("T", bound="ChatRenderOutput")


@_attrs_define
class ChatRenderOutput:
    """
    Attributes:
        body (str | Unset): Body of the chat message. Mutually exclusive with `card`.
        card (ChatRenderOutputCard | Unset): Rich Chat: compiled provider-agnostic card DSL. Mutually exclusive with
            `body`.
    """

    body: str | Unset = UNSET
    card: ChatRenderOutputCard | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        body = self.body

        card: dict[str, Any] | Unset = UNSET
        if not isinstance(self.card, Unset):
            card = self.card.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if body is not UNSET:
            field_dict["body"] = body
        if card is not UNSET:
            field_dict["card"] = card

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chat_render_output_card import ChatRenderOutputCard

        d = dict(src_dict)
        body = d.pop("body", UNSET)

        _card = d.pop("card", UNSET)
        card: ChatRenderOutputCard | Unset
        if isinstance(_card, Unset):
            card = UNSET
        else:
            card = ChatRenderOutputCard.from_dict(_card)

        chat_render_output = cls(
            body=body,
            card=card,
        )

        chat_render_output.additional_properties = d
        return chat_render_output

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
