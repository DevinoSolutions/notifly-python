from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.resource_to_publish_dto import ResourceToPublishDto


T = TypeVar("T", bound="PublishEnvironmentRequestDto")


@_attrs_define
class PublishEnvironmentRequestDto:
    """
    Attributes:
        source_environment_id (str | Unset): Source environment ID to sync from. Defaults to the Development environment
            if not provided. Example: 507f1f77bcf86cd799439011.
        dry_run (bool | Unset): Perform a dry run without making actual changes Default: False.
        resources (list[ResourceToPublishDto] | Unset): Array of specific resources to publish. If not provided, all
            resources will be published.
    """

    source_environment_id: str | Unset = UNSET
    dry_run: bool | Unset = False
    resources: list[ResourceToPublishDto] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        source_environment_id = self.source_environment_id

        dry_run = self.dry_run

        resources: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.resources, Unset):
            resources = []
            for resources_item_data in self.resources:
                resources_item = resources_item_data.to_dict()
                resources.append(resources_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if source_environment_id is not UNSET:
            field_dict["sourceEnvironmentId"] = source_environment_id
        if dry_run is not UNSET:
            field_dict["dryRun"] = dry_run
        if resources is not UNSET:
            field_dict["resources"] = resources

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.resource_to_publish_dto import ResourceToPublishDto

        d = dict(src_dict)
        source_environment_id = d.pop("sourceEnvironmentId", UNSET)

        dry_run = d.pop("dryRun", UNSET)

        _resources = d.pop("resources", UNSET)
        resources: list[ResourceToPublishDto] | Unset = UNSET
        if _resources is not UNSET:
            resources = []
            for resources_item_data in _resources:
                resources_item = ResourceToPublishDto.from_dict(resources_item_data)

                resources.append(resources_item)

        publish_environment_request_dto = cls(
            source_environment_id=source_environment_id,
            dry_run=dry_run,
            resources=resources,
        )

        publish_environment_request_dto.additional_properties = d
        return publish_environment_request_dto

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
