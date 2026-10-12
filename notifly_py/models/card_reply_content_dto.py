from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.card_reply_content_dto_card import CardReplyContentDtoCard
    from ..models.file_ref_dto import FileRefDto


T = TypeVar("T", bound="CardReplyContentDto")


@_attrs_define
class CardReplyContentDto:
    """
    Attributes:
        card (CardReplyContentDtoCard): Interactive card as a Chat SDK element tree (`type: "card"`). Prefer building
            with `@notifly/framework` Card helpers when using TypeScript. Example: {'type': 'card', 'title': 'Order #123',
            'children': [{'type': 'text', 'content': 'Your order is ready for pickup.'}, {'type': 'button', 'id': 'confirm',
            'label': 'Confirm', 'style': 'primary'}]}.
        files (list[FileRefDto] | Unset): Optional attachments (max 15). Supported alongside cards on platforms that
            allow it (e.g. WhatsApp).
    """

    card: CardReplyContentDtoCard
    files: list[FileRefDto] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        card = self.card.to_dict()

        files: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.files, Unset):
            files = []
            for files_item_data in self.files:
                files_item = files_item_data.to_dict()
                files.append(files_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "card": card,
            }
        )
        if files is not UNSET:
            field_dict["files"] = files

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.card_reply_content_dto_card import CardReplyContentDtoCard
        from ..models.file_ref_dto import FileRefDto

        d = dict(src_dict)
        card = CardReplyContentDtoCard.from_dict(d.pop("card"))

        _files = d.pop("files", UNSET)
        files: list[FileRefDto] | Unset = UNSET
        if _files is not UNSET:
            files = []
            for files_item_data in _files:
                files_item = FileRefDto.from_dict(files_item_data)

                files.append(files_item)

        card_reply_content_dto = cls(
            card=card,
            files=files,
        )

        card_reply_content_dto.additional_properties = d
        return card_reply_content_dto

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
