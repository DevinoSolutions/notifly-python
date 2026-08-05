from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.resource_origin_enum import ResourceOriginEnum
from ..models.resource_type_enum import ResourceTypeEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.layout_controls_dto import LayoutControlsDto
    from ..models.layout_response_dto_variables_type_0 import LayoutResponseDtoVariablesType0
    from ..models.user_response_dto import UserResponseDto


T = TypeVar("T", bound="LayoutResponseDto")


@_attrs_define
class LayoutResponseDto:
    """
    Attributes:
        field_id (str): Unique internal identifier of the layout
        layout_id (str): Unique identifier for the layout
        slug (str): Slug of the layout
        name (str): Name of the layout
        is_default (bool): Whether the layout is the default layout
        is_translation_enabled (bool): Whether the layout translations are enabled
        updated_at (str): Last updated timestamp
        created_at (str): Creation timestamp
        origin (ResourceOriginEnum): Origin of the layout
        type_ (ResourceTypeEnum): Type of the layout
        controls (LayoutControlsDto):
        updated_by (None | Unset | UserResponseDto): User who last updated the layout
        variables (LayoutResponseDtoVariablesType0 | None | Unset): The variables JSON Schema for the layout
    """

    field_id: str
    layout_id: str
    slug: str
    name: str
    is_default: bool
    is_translation_enabled: bool
    updated_at: str
    created_at: str
    origin: ResourceOriginEnum
    type_: ResourceTypeEnum
    controls: LayoutControlsDto
    updated_by: None | Unset | UserResponseDto = UNSET
    variables: LayoutResponseDtoVariablesType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.layout_response_dto_variables_type_0 import LayoutResponseDtoVariablesType0
        from ..models.user_response_dto import UserResponseDto

        field_id = self.field_id

        layout_id = self.layout_id

        slug = self.slug

        name = self.name

        is_default = self.is_default

        is_translation_enabled = self.is_translation_enabled

        updated_at = self.updated_at

        created_at = self.created_at

        origin = self.origin.value

        type_ = self.type_.value

        controls = self.controls.to_dict()

        updated_by: dict[str, Any] | None | Unset
        if isinstance(self.updated_by, Unset):
            updated_by = UNSET
        elif isinstance(self.updated_by, UserResponseDto):
            updated_by = self.updated_by.to_dict()
        else:
            updated_by = self.updated_by

        variables: dict[str, Any] | None | Unset
        if isinstance(self.variables, Unset):
            variables = UNSET
        elif isinstance(self.variables, LayoutResponseDtoVariablesType0):
            variables = self.variables.to_dict()
        else:
            variables = self.variables

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "_id": field_id,
                "layoutId": layout_id,
                "slug": slug,
                "name": name,
                "isDefault": is_default,
                "isTranslationEnabled": is_translation_enabled,
                "updatedAt": updated_at,
                "createdAt": created_at,
                "origin": origin,
                "type": type_,
                "controls": controls,
            }
        )
        if updated_by is not UNSET:
            field_dict["updatedBy"] = updated_by
        if variables is not UNSET:
            field_dict["variables"] = variables

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.layout_controls_dto import LayoutControlsDto
        from ..models.layout_response_dto_variables_type_0 import LayoutResponseDtoVariablesType0
        from ..models.user_response_dto import UserResponseDto

        d = dict(src_dict)
        field_id = d.pop("_id")

        layout_id = d.pop("layoutId")

        slug = d.pop("slug")

        name = d.pop("name")

        is_default = d.pop("isDefault")

        is_translation_enabled = d.pop("isTranslationEnabled")

        updated_at = d.pop("updatedAt")

        created_at = d.pop("createdAt")

        origin = ResourceOriginEnum(d.pop("origin"))

        type_ = ResourceTypeEnum(d.pop("type"))

        controls = LayoutControlsDto.from_dict(d.pop("controls"))

        def _parse_updated_by(data: object) -> None | Unset | UserResponseDto:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                updated_by_type_1 = UserResponseDto.from_dict(data)

                return updated_by_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UserResponseDto, data)

        updated_by = _parse_updated_by(d.pop("updatedBy", UNSET))

        def _parse_variables(data: object) -> LayoutResponseDtoVariablesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                variables_type_0 = LayoutResponseDtoVariablesType0.from_dict(data)

                return variables_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(LayoutResponseDtoVariablesType0 | None | Unset, data)

        variables = _parse_variables(d.pop("variables", UNSET))

        layout_response_dto = cls(
            field_id=field_id,
            layout_id=layout_id,
            slug=slug,
            name=name,
            is_default=is_default,
            is_translation_enabled=is_translation_enabled,
            updated_at=updated_at,
            created_at=created_at,
            origin=origin,
            type_=type_,
            controls=controls,
            updated_by=updated_by,
            variables=variables,
        )

        layout_response_dto.additional_properties = d
        return layout_response_dto

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
