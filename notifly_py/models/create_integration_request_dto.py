from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_integration_request_dto_channel import CreateIntegrationRequestDtoChannel
from ..models.create_integration_request_dto_kind import CreateIntegrationRequestDtoKind
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_integration_request_dto_configurations import CreateIntegrationRequestDtoConfigurations
    from ..models.credentials_dto import CredentialsDto
    from ..models.step_filter_dto import StepFilterDto


T = TypeVar("T", bound="CreateIntegrationRequestDto")


@_attrs_define
class CreateIntegrationRequestDto:
    """
    Attributes:
        name (str | Unset): The name of the integration
        identifier (str | Unset): The unique identifier for the integration
        field_environment_id (UUID | Unset): The ID of the associated environment
        provider_id (str | Unset): The provider ID for the integration
        channel (CreateIntegrationRequestDtoChannel | Unset): The channel type for the integration. Not required for
            agent-kind integrations.
        kind (CreateIntegrationRequestDtoKind | Unset): Distinguishes delivery integrations from agent-runtime
            integrations. Defaults to "delivery". Agent integrations do not require a channel.
        credentials (CredentialsDto | Unset):
        active (bool | Unset): If the integration is active, the validation on the credentials field will run
        check (bool | Unset): Flag to check the integration status
        conditions (list[StepFilterDto] | Unset): Conditions for the integration
        configurations (CreateIntegrationRequestDtoConfigurations | Unset): Configurations for the integration
    """

    name: str | Unset = UNSET
    identifier: str | Unset = UNSET
    field_environment_id: UUID | Unset = UNSET
    provider_id: str | Unset = UNSET
    channel: CreateIntegrationRequestDtoChannel | Unset = UNSET
    kind: CreateIntegrationRequestDtoKind | Unset = UNSET
    credentials: CredentialsDto | Unset = UNSET
    active: bool | Unset = UNSET
    check: bool | Unset = UNSET
    conditions: list[StepFilterDto] | Unset = UNSET
    configurations: CreateIntegrationRequestDtoConfigurations | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        identifier = self.identifier

        field_environment_id: str | Unset = UNSET
        if not isinstance(self.field_environment_id, Unset):
            field_environment_id = str(self.field_environment_id)

        provider_id = self.provider_id

        channel: str | Unset = UNSET
        if not isinstance(self.channel, Unset):
            channel = self.channel.value

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value

        credentials: dict[str, Any] | Unset = UNSET
        if not isinstance(self.credentials, Unset):
            credentials = self.credentials.to_dict()

        active = self.active

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
        if provider_id is not UNSET:
            field_dict["providerId"] = provider_id
        if channel is not UNSET:
            field_dict["channel"] = channel
        if kind is not UNSET:
            field_dict["kind"] = kind
        if credentials is not UNSET:
            field_dict["credentials"] = credentials
        if active is not UNSET:
            field_dict["active"] = active
        if check is not UNSET:
            field_dict["check"] = check
        if conditions is not UNSET:
            field_dict["conditions"] = conditions
        if configurations is not UNSET:
            field_dict["configurations"] = configurations

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_integration_request_dto_configurations import CreateIntegrationRequestDtoConfigurations
        from ..models.credentials_dto import CredentialsDto
        from ..models.step_filter_dto import StepFilterDto

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        identifier = d.pop("identifier", UNSET)

        _field_environment_id = d.pop("_environmentId", UNSET)
        field_environment_id: UUID | Unset
        if isinstance(_field_environment_id, Unset):
            field_environment_id = UNSET
        else:
            field_environment_id = UUID(_field_environment_id)

        provider_id = d.pop("providerId", UNSET)

        _channel = d.pop("channel", UNSET)
        channel: CreateIntegrationRequestDtoChannel | Unset
        if isinstance(_channel, Unset):
            channel = UNSET
        else:
            channel = CreateIntegrationRequestDtoChannel(_channel)

        _kind = d.pop("kind", UNSET)
        kind: CreateIntegrationRequestDtoKind | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = CreateIntegrationRequestDtoKind(_kind)

        _credentials = d.pop("credentials", UNSET)
        credentials: CredentialsDto | Unset
        if isinstance(_credentials, Unset):
            credentials = UNSET
        else:
            credentials = CredentialsDto.from_dict(_credentials)

        active = d.pop("active", UNSET)

        check = d.pop("check", UNSET)

        _conditions = d.pop("conditions", UNSET)
        conditions: list[StepFilterDto] | Unset = UNSET
        if _conditions is not UNSET:
            conditions = []
            for conditions_item_data in _conditions:
                conditions_item = StepFilterDto.from_dict(conditions_item_data)

                conditions.append(conditions_item)

        _configurations = d.pop("configurations", UNSET)
        configurations: CreateIntegrationRequestDtoConfigurations | Unset
        if isinstance(_configurations, Unset):
            configurations = UNSET
        else:
            configurations = CreateIntegrationRequestDtoConfigurations.from_dict(_configurations)

        create_integration_request_dto = cls(
            name=name,
            identifier=identifier,
            field_environment_id=field_environment_id,
            provider_id=provider_id,
            channel=channel,
            kind=kind,
            credentials=credentials,
            active=active,
            check=check,
            conditions=conditions,
            configurations=configurations,
        )

        create_integration_request_dto.additional_properties = d
        return create_integration_request_dto

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
