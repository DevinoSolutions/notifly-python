from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.resource_type import ResourceType

if TYPE_CHECKING:
    from ..models.create_translation_request_dto_content import CreateTranslationRequestDtoContent


T = TypeVar("T", bound="CreateTranslationRequestDto")


@_attrs_define
class CreateTranslationRequestDto:
    """
    Attributes:
        resource_id (str): The resource ID to associate translation with. Accepts identifier or slug format
        resource_type (ResourceType): The resource type to associate translation with
        locale (str): Locale code (e.g., en_US, es_ES)
        content (CreateTranslationRequestDtoContent): Translation content as JSON object
    """

    resource_id: str
    resource_type: ResourceType
    locale: str
    content: CreateTranslationRequestDtoContent
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resource_id = self.resource_id

        resource_type = self.resource_type.value

        locale = self.locale

        content = self.content.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resourceId": resource_id,
                "resourceType": resource_type,
                "locale": locale,
                "content": content,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_translation_request_dto_content import CreateTranslationRequestDtoContent

        d = dict(src_dict)
        resource_id = d.pop("resourceId")

        resource_type = ResourceType(d.pop("resourceType"))

        locale = d.pop("locale")

        content = CreateTranslationRequestDtoContent.from_dict(d.pop("content"))

        create_translation_request_dto = cls(
            resource_id=resource_id,
            resource_type=resource_type,
            locale=locale,
            content=content,
        )

        create_translation_request_dto.additional_properties = d
        return create_translation_request_dto

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
