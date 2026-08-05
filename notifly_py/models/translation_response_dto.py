from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.resource_type import ResourceType

if TYPE_CHECKING:
    from ..models.translation_response_dto_content import TranslationResponseDtoContent


T = TypeVar("T", bound="TranslationResponseDto")


@_attrs_define
class TranslationResponseDto:
    """
    Attributes:
        resource_id (str): Resource identifier
        resource_type (ResourceType): The resource type to associate translation with
        locale (str): Locale code
        content (TranslationResponseDtoContent): Translation content as JSON object
        created_at (str): Creation timestamp
        updated_at (str): Last update timestamp
    """

    resource_id: str
    resource_type: ResourceType
    locale: str
    content: TranslationResponseDtoContent
    created_at: str
    updated_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        resource_id = self.resource_id

        resource_type = self.resource_type.value

        locale = self.locale

        content = self.content.to_dict()

        created_at = self.created_at

        updated_at = self.updated_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "resourceId": resource_id,
                "resourceType": resource_type,
                "locale": locale,
                "content": content,
                "createdAt": created_at,
                "updatedAt": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.translation_response_dto_content import TranslationResponseDtoContent

        d = dict(src_dict)
        resource_id = d.pop("resourceId")

        resource_type = ResourceType(d.pop("resourceType"))

        locale = d.pop("locale")

        content = TranslationResponseDtoContent.from_dict(d.pop("content"))

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        translation_response_dto = cls(
            resource_id=resource_id,
            resource_type=resource_type,
            locale=locale,
            content=content,
            created_at=created_at,
            updated_at=updated_at,
        )

        translation_response_dto.additional_properties = d
        return translation_response_dto

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
