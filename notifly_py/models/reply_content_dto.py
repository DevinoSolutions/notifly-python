from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.file_ref_dto import FileRefDto
    from ..models.reply_content_dto_card import ReplyContentDtoCard
    from ..models.reply_content_dto_tool_approval_card import ReplyContentDtoToolApprovalCard


T = TypeVar("T", bound="ReplyContentDto")


@_attrs_define
class ReplyContentDto:
    """
    Attributes:
        markdown (str | Unset): Plain text or markdown body. Mutually exclusive with `card` and `toolApprovalCard`.
            Example: Hello! How can I help?.
        card (ReplyContentDtoCard | Unset): Interactive Chat SDK card JSON. Mutually exclusive with `markdown` and
            `toolApprovalCard`.
        tool_approval_card (ReplyContentDtoToolApprovalCard | Unset): Built-in tool-approval card. Mutually exclusive
            with `markdown` and `card`.
        files (list[FileRefDto] | Unset): Optional file attachments (max 15). Requires markdown, card, or
            toolApprovalCard.
    """

    markdown: str | Unset = UNSET
    card: ReplyContentDtoCard | Unset = UNSET
    tool_approval_card: ReplyContentDtoToolApprovalCard | Unset = UNSET
    files: list[FileRefDto] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        markdown = self.markdown

        card: dict[str, Any] | Unset = UNSET
        if not isinstance(self.card, Unset):
            card = self.card.to_dict()

        tool_approval_card: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tool_approval_card, Unset):
            tool_approval_card = self.tool_approval_card.to_dict()

        files: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.files, Unset):
            files = []
            for files_item_data in self.files:
                files_item = files_item_data.to_dict()
                files.append(files_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if markdown is not UNSET:
            field_dict["markdown"] = markdown
        if card is not UNSET:
            field_dict["card"] = card
        if tool_approval_card is not UNSET:
            field_dict["toolApprovalCard"] = tool_approval_card
        if files is not UNSET:
            field_dict["files"] = files

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.file_ref_dto import FileRefDto
        from ..models.reply_content_dto_card import ReplyContentDtoCard
        from ..models.reply_content_dto_tool_approval_card import ReplyContentDtoToolApprovalCard

        d = dict(src_dict)
        markdown = d.pop("markdown", UNSET)

        _card = d.pop("card", UNSET)
        card: ReplyContentDtoCard | Unset
        if isinstance(_card, Unset):
            card = UNSET
        else:
            card = ReplyContentDtoCard.from_dict(_card)

        _tool_approval_card = d.pop("toolApprovalCard", UNSET)
        tool_approval_card: ReplyContentDtoToolApprovalCard | Unset
        if isinstance(_tool_approval_card, Unset):
            tool_approval_card = UNSET
        else:
            tool_approval_card = ReplyContentDtoToolApprovalCard.from_dict(_tool_approval_card)

        _files = d.pop("files", UNSET)
        files: list[FileRefDto] | Unset = UNSET
        if _files is not UNSET:
            files = []
            for files_item_data in _files:
                files_item = FileRefDto.from_dict(files_item_data)

                files.append(files_item)

        reply_content_dto = cls(
            markdown=markdown,
            card=card,
            tool_approval_card=tool_approval_card,
            files=files,
        )

        reply_content_dto.additional_properties = d
        return reply_content_dto

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
