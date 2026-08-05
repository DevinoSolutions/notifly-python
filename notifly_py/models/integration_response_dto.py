from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.integration_response_dto_channel import IntegrationResponseDtoChannel
from ..models.integration_response_dto_kind import IntegrationResponseDtoKind
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.configurations_dto import ConfigurationsDto
    from ..models.credentials_dto import CredentialsDto
    from ..models.step_filter_dto import StepFilterDto


T = TypeVar("T", bound="IntegrationResponseDto")


@_attrs_define
class IntegrationResponseDto:
    """
    Attributes:
        field_environment_id (str): The unique identifier for the environment associated with this integration. This
            links to the Environment collection.
        field_organization_id (str): The unique identifier for the organization that owns this integration. This links
            to the Organization collection.
        name (str): The name of the integration, which is used to identify it in the user interface.
        identifier (str): A unique string identifier for the integration, often used for API calls or internal
            references.
        provider_id (str): The identifier for the provider of the integration (e.g., "mailgun", "twilio").
        active (bool): Indicates whether the integration is currently active. An active integration will process events
            and messages.
        deleted (bool): Indicates whether the integration has been marked as deleted (soft delete).
        primary (bool): Indicates whether this integration is marked as primary. A primary integration is often the
            default choice for processing.
        field_id (str | Unset): The unique identifier of the integration record in the database. This is automatically
            generated.
        channel (IntegrationResponseDtoChannel | Unset): The channel type for the integration, which defines how it
            communicates (e.g., email, SMS). Not set for agent-kind integrations.
        kind (IntegrationResponseDtoKind | Unset): Distinguishes delivery integrations from agent-runtime integrations.
            Defaults to "delivery". Agent integrations do not have a channel.
        credentials (CredentialsDto | Unset):
        configurations (ConfigurationsDto | Unset):
        deleted_at (str | Unset): The timestamp indicating when the integration was deleted. This is set when the
            integration is soft deleted.
        deleted_by (str | Unset): The identifier of the user who performed the deletion of this integration. Useful for
            audit trails.
        conditions (list[StepFilterDto] | Unset): An array of conditions associated with the integration that may
            influence its behavior or processing logic.
    """

    field_environment_id: str
    field_organization_id: str
    name: str
    identifier: str
    provider_id: str
    active: bool
    deleted: bool
    primary: bool
    field_id: str | Unset = UNSET
    channel: IntegrationResponseDtoChannel | Unset = UNSET
    kind: IntegrationResponseDtoKind | Unset = UNSET
    credentials: CredentialsDto | Unset = UNSET
    configurations: ConfigurationsDto | Unset = UNSET
    deleted_at: str | Unset = UNSET
    deleted_by: str | Unset = UNSET
    conditions: list[StepFilterDto] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_environment_id = self.field_environment_id

        field_organization_id = self.field_organization_id

        name = self.name

        identifier = self.identifier

        provider_id = self.provider_id

        active = self.active

        deleted = self.deleted

        primary = self.primary

        field_id = self.field_id

        channel: str | Unset = UNSET
        if not isinstance(self.channel, Unset):
            channel = self.channel.value

        kind: str | Unset = UNSET
        if not isinstance(self.kind, Unset):
            kind = self.kind.value

        credentials: dict[str, Any] | Unset = UNSET
        if not isinstance(self.credentials, Unset):
            credentials = self.credentials.to_dict()

        configurations: dict[str, Any] | Unset = UNSET
        if not isinstance(self.configurations, Unset):
            configurations = self.configurations.to_dict()

        deleted_at = self.deleted_at

        deleted_by = self.deleted_by

        conditions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.conditions, Unset):
            conditions = []
            for conditions_item_data in self.conditions:
                conditions_item = conditions_item_data.to_dict()
                conditions.append(conditions_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "_environmentId": field_environment_id,
                "_organizationId": field_organization_id,
                "name": name,
                "identifier": identifier,
                "providerId": provider_id,
                "active": active,
                "deleted": deleted,
                "primary": primary,
            }
        )
        if field_id is not UNSET:
            field_dict["_id"] = field_id
        if channel is not UNSET:
            field_dict["channel"] = channel
        if kind is not UNSET:
            field_dict["kind"] = kind
        if credentials is not UNSET:
            field_dict["credentials"] = credentials
        if configurations is not UNSET:
            field_dict["configurations"] = configurations
        if deleted_at is not UNSET:
            field_dict["deletedAt"] = deleted_at
        if deleted_by is not UNSET:
            field_dict["deletedBy"] = deleted_by
        if conditions is not UNSET:
            field_dict["conditions"] = conditions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.configurations_dto import ConfigurationsDto
        from ..models.credentials_dto import CredentialsDto
        from ..models.step_filter_dto import StepFilterDto

        d = dict(src_dict)
        field_environment_id = d.pop("_environmentId")

        field_organization_id = d.pop("_organizationId")

        name = d.pop("name")

        identifier = d.pop("identifier")

        provider_id = d.pop("providerId")

        active = d.pop("active")

        deleted = d.pop("deleted")

        primary = d.pop("primary")

        field_id = d.pop("_id", UNSET)

        _channel = d.pop("channel", UNSET)
        channel: IntegrationResponseDtoChannel | Unset
        if isinstance(_channel, Unset):
            channel = UNSET
        else:
            channel = IntegrationResponseDtoChannel(_channel)

        _kind = d.pop("kind", UNSET)
        kind: IntegrationResponseDtoKind | Unset
        if isinstance(_kind, Unset):
            kind = UNSET
        else:
            kind = IntegrationResponseDtoKind(_kind)

        _credentials = d.pop("credentials", UNSET)
        credentials: CredentialsDto | Unset
        if isinstance(_credentials, Unset):
            credentials = UNSET
        else:
            credentials = CredentialsDto.from_dict(_credentials)

        _configurations = d.pop("configurations", UNSET)
        configurations: ConfigurationsDto | Unset
        if isinstance(_configurations, Unset):
            configurations = UNSET
        else:
            configurations = ConfigurationsDto.from_dict(_configurations)

        deleted_at = d.pop("deletedAt", UNSET)

        deleted_by = d.pop("deletedBy", UNSET)

        _conditions = d.pop("conditions", UNSET)
        conditions: list[StepFilterDto] | Unset = UNSET
        if _conditions is not UNSET:
            conditions = []
            for conditions_item_data in _conditions:
                conditions_item = StepFilterDto.from_dict(conditions_item_data)

                conditions.append(conditions_item)

        integration_response_dto = cls(
            field_environment_id=field_environment_id,
            field_organization_id=field_organization_id,
            name=name,
            identifier=identifier,
            provider_id=provider_id,
            active=active,
            deleted=deleted,
            primary=primary,
            field_id=field_id,
            channel=channel,
            kind=kind,
            credentials=credentials,
            configurations=configurations,
            deleted_at=deleted_at,
            deleted_by=deleted_by,
            conditions=conditions,
        )

        integration_response_dto.additional_properties = d
        return integration_response_dto

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
