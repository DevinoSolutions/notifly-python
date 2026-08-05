from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.credentials_dto import CredentialsDto
    from ..models.step_filter_dto import StepFilterDto
    from ..models.update_integration_request_dto_configurations import UpdateIntegrationRequestDtoConfigurations


T = TypeVar("T", bound="UpdateIntegrationRequestDto")


@_attrs_define
class UpdateIntegrationRequestDto:
    """
    Attributes:
        name (str | Unset):
        identifier (str | Unset):
        field_environment_id (str | Unset):
        active (bool | Unset): If the integration is active the validation on the credentials field will run
        credentials (CredentialsDto | Unset):
        check (bool | Unset):
        conditions (list[StepFilterDto] | Unset):
        configurations (UpdateIntegrationRequestDtoConfigurations | Unset): Configurations for the integration
    """

    name: str | Unset = UNSET
    identifier: str | Unset = UNSET
    field_environment_id: str | Unset = UNSET
    active: bool | Unset = UNSET
    credentials: CredentialsDto | Unset = UNSET
    check: bool | Unset = UNSET
    conditions: list[StepFilterDto] | Unset = UNSET
    configurations: UpdateIntegrationRequestDtoConfigurations | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        identifier = self.identifier

        field_environment_id = self.field_environment_id

        active = self.active

        credentials: dict[str, Any] | Unset = UNSET
        if not isinstance(self.credentials, Unset):
            credentials = self.credentials.to_dict()

        check = self.check

        conditions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.conditions, Unset):
            conditions = []
            for conditions_item_data in self.conditions:
                conditions_item = conditions_item_data.to_dict()
                conditions.append(conditions_item)

        configurations: dict[str, Any] | Unset = UNSET
        if not isinstance(self.configurations, Unset):
            configurations = self.configurations.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if field_environment_id is not UNSET:
            field_dict["_environmentId"] = field_environment_id
        if active is not UNSET:
            field_dict["active"] = active
        if credentials is not UNSET:
            field_dict["credentials"] = credentials
        if check is not UNSET:
            field_dict["check"] = check
        if conditions is not UNSET:
            field_dict["conditions"] = conditions
        if configurations is not UNSET:
            field_dict["configurations"] = configurations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.credentials_dto import CredentialsDto
        from ..models.step_filter_dto import StepFilterDto
        from ..models.update_integration_request_dto_configurations import UpdateIntegrationRequestDtoConfigurations

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        identifier = d.pop("identifier", UNSET)

        field_environment_id = d.pop("_environmentId", UNSET)

        active = d.pop("active", UNSET)

        _credentials = d.pop("credentials", UNSET)
        credentials: CredentialsDto | Unset
        if isinstance(_credentials, Unset):
            credentials = UNSET
        else:
            credentials = CredentialsDto.from_dict(_credentials)

        check = d.pop("check", UNSET)

        _conditions = d.pop("conditions", UNSET)
        conditions: list[StepFilterDto] | Unset = UNSET
        if _conditions is not UNSET:
            conditions = []
            for conditions_item_data in _conditions:
                conditions_item = StepFilterDto.from_dict(conditions_item_data)

                conditions.append(conditions_item)

        _configurations = d.pop("configurations", UNSET)
        configurations: UpdateIntegrationRequestDtoConfigurations | Unset
        if isinstance(_configurations, Unset):
            configurations = UNSET
        else:
            configurations = UpdateIntegrationRequestDtoConfigurations.from_dict(_configurations)

        update_integration_request_dto = cls(
            name=name,
            identifier=identifier,
            field_environment_id=field_environment_id,
            active=active,
            credentials=credentials,
            check=check,
            conditions=conditions,
            configurations=configurations,
        )

        update_integration_request_dto.additional_properties = d
        return update_integration_request_dto

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
