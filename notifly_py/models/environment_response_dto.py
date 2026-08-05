from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.environment_response_dto_type import EnvironmentResponseDtoType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.api_key_dto import ApiKeyDto


T = TypeVar("T", bound="EnvironmentResponseDto")


@_attrs_define
class EnvironmentResponseDto:
    """
    Attributes:
        field_id (str): Unique identifier of the environment Example: 60d5ecb8b3b3a30015f3e1a1.
        name (str): Name of the environment Example: Production Environment.
        field_organization_id (str): Organization ID associated with the environment Example: 60d5ecb8b3b3a30015f3e1a2.
        identifier (str): Unique identifier for the environment Example: prod-env-01.
        type_ (EnvironmentResponseDtoType | Unset): Type of the environment Example: prod.
        api_keys (list[ApiKeyDto] | Unset): List of API keys associated with the environment
        field_parent_id (str | Unset): Parent environment ID Example: 60d5ecb8b3b3a30015f3e1a3.
        slug (str | Unset): URL-friendly slug for the environment Example: production.
    """

    field_id: str
    name: str
    field_organization_id: str
    identifier: str
    type_: EnvironmentResponseDtoType | Unset = UNSET
    api_keys: list[ApiKeyDto] | Unset = UNSET
    field_parent_id: str | Unset = UNSET
    slug: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_id = self.field_id

        name = self.name

        field_organization_id = self.field_organization_id

        identifier = self.identifier

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        api_keys: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.api_keys, Unset):
            api_keys = []
            for api_keys_item_data in self.api_keys:
                api_keys_item = api_keys_item_data.to_dict()
                api_keys.append(api_keys_item)

        field_parent_id = self.field_parent_id

        slug = self.slug

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "_id": field_id,
                "name": name,
                "_organizationId": field_organization_id,
                "identifier": identifier,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_
        if api_keys is not UNSET:
            field_dict["apiKeys"] = api_keys
        if field_parent_id is not UNSET:
            field_dict["_parentId"] = field_parent_id
        if slug is not UNSET:
            field_dict["slug"] = slug

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_key_dto import ApiKeyDto

        d = dict(src_dict)
        field_id = d.pop("_id")

        name = d.pop("name")

        field_organization_id = d.pop("_organizationId")

        identifier = d.pop("identifier")

        _type_ = d.pop("type", UNSET)
        type_: EnvironmentResponseDtoType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = EnvironmentResponseDtoType(_type_)

        _api_keys = d.pop("apiKeys", UNSET)
        api_keys: list[ApiKeyDto] | Unset = UNSET
        if _api_keys is not UNSET:
            api_keys = []
            for api_keys_item_data in _api_keys:
                api_keys_item = ApiKeyDto.from_dict(api_keys_item_data)

                api_keys.append(api_keys_item)

        field_parent_id = d.pop("_parentId", UNSET)

        slug = d.pop("slug", UNSET)

        environment_response_dto = cls(
            field_id=field_id,
            name=name,
            field_organization_id=field_organization_id,
            identifier=identifier,
            type_=type_,
            api_keys=api_keys,
            field_parent_id=field_parent_id,
            slug=slug,
        )

        environment_response_dto.additional_properties = d
        return environment_response_dto

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
