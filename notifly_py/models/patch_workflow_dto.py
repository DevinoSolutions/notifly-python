from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.patch_workflow_dto_payload_schema_type_0 import PatchWorkflowDtoPayloadSchemaType0


T = TypeVar("T", bound="PatchWorkflowDto")


@_attrs_define
class PatchWorkflowDto:
    """
    Attributes:
        active (bool | Unset): Activate or deactivate the workflow
        name (str | Unset): New name for the workflow
        description (str | Unset): Updated description of the workflow
        tags (list[str] | Unset): Tags associated with the workflow
        payload_schema (None | PatchWorkflowDtoPayloadSchemaType0 | Unset): The payload JSON Schema for the workflow
        validate_payload (bool | Unset): Enable or disable payload schema validation
        is_translation_enabled (bool | Unset): Enable or disable translations for this workflow
    """

    active: bool | Unset = UNSET
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    tags: list[str] | Unset = UNSET
    payload_schema: None | PatchWorkflowDtoPayloadSchemaType0 | Unset = UNSET
    validate_payload: bool | Unset = UNSET
    is_translation_enabled: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.patch_workflow_dto_payload_schema_type_0 import PatchWorkflowDtoPayloadSchemaType0

        active = self.active

        name = self.name

        description = self.description

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        payload_schema: dict[str, Any] | None | Unset
        if isinstance(self.payload_schema, Unset):
            payload_schema = UNSET
        elif isinstance(self.payload_schema, PatchWorkflowDtoPayloadSchemaType0):
            payload_schema = self.payload_schema.to_dict()
        else:
            payload_schema = self.payload_schema

        validate_payload = self.validate_payload

        is_translation_enabled = self.is_translation_enabled

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if active is not UNSET:
            field_dict["active"] = active
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if tags is not UNSET:
            field_dict["tags"] = tags
        if payload_schema is not UNSET:
            field_dict["payloadSchema"] = payload_schema
        if validate_payload is not UNSET:
            field_dict["validatePayload"] = validate_payload
        if is_translation_enabled is not UNSET:
            field_dict["isTranslationEnabled"] = is_translation_enabled

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.patch_workflow_dto_payload_schema_type_0 import PatchWorkflowDtoPayloadSchemaType0

        d = dict(src_dict)
        active = d.pop("active", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        tags = cast(list[str], d.pop("tags", UNSET))

        def _parse_payload_schema(data: object) -> None | PatchWorkflowDtoPayloadSchemaType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                payload_schema_type_0 = PatchWorkflowDtoPayloadSchemaType0.from_dict(data)

                return payload_schema_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PatchWorkflowDtoPayloadSchemaType0 | Unset, data)

        payload_schema = _parse_payload_schema(d.pop("payloadSchema", UNSET))

        validate_payload = d.pop("validatePayload", UNSET)

        is_translation_enabled = d.pop("isTranslationEnabled", UNSET)

        patch_workflow_dto = cls(
            active=active,
            name=name,
            description=description,
            tags=tags,
            payload_schema=payload_schema,
            validate_payload=validate_payload,
            is_translation_enabled=is_translation_enabled,
        )

        patch_workflow_dto.additional_properties = d
        return patch_workflow_dto

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
