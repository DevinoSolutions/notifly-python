from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.severity_level_enum import SeverityLevelEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.notification_workflow_dto_data import NotificationWorkflowDtoData


T = TypeVar("T", bound="NotificationWorkflowDto")


@_attrs_define
class NotificationWorkflowDto:
    """
    Attributes:
        id (str): Unique identifier of the workflow
        identifier (str): Workflow identifier used for triggering
        name (str): Human-readable name of the workflow
        critical (bool): Whether this workflow is marked as critical
        severity (SeverityLevelEnum): Severity of the workflow
        tags (list[str] | Unset): Tags associated with the workflow
        data (NotificationWorkflowDtoData | Unset): Custom data associated with the workflow
    """

    id: str
    identifier: str
    name: str
    critical: bool
    severity: SeverityLevelEnum
    tags: list[str] | Unset = UNSET
    data: NotificationWorkflowDtoData | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        identifier = self.identifier

        name = self.name

        critical = self.critical

        severity = self.severity.value

        tags: list[str] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags

        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "identifier": identifier,
                "name": name,
                "critical": critical,
                "severity": severity,
            }
        )
        if tags is not UNSET:
            field_dict["tags"] = tags
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.notification_workflow_dto_data import NotificationWorkflowDtoData

        d = dict(src_dict)
        id = d.pop("id")

        identifier = d.pop("identifier")

        name = d.pop("name")

        critical = d.pop("critical")

        severity = SeverityLevelEnum(d.pop("severity"))

        tags = cast(list[str], d.pop("tags", UNSET))

        _data = d.pop("data", UNSET)
        data: NotificationWorkflowDtoData | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = NotificationWorkflowDtoData.from_dict(_data)

        notification_workflow_dto = cls(
            id=id,
            identifier=identifier,
            name=name,
            critical=critical,
            severity=severity,
            tags=tags,
            data=data,
        )

        notification_workflow_dto.additional_properties = d
        return notification_workflow_dto

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
