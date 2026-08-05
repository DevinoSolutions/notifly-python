from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.severity_level_enum import SeverityLevelEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.workflow_dto_data import WorkflowDtoData


T = TypeVar("T", bound="WorkflowDto")


@_attrs_define
class WorkflowDto:
    """
    Attributes:
        id (str): Unique identifier of the workflow Example: 64a1b2c3d4e5f6g7h8i9j0k1.
        identifier (str): Workflow identifier used for triggering Example: welcome-email.
        name (str): Human-readable name of the workflow Example: Welcome Email Workflow.
        critical (bool): Whether this workflow is marked as critical
        severity (SeverityLevelEnum): Severity of the workflow
        tags (list[str] | Unset): Tags associated with the workflow Example: ['user-onboarding', 'email'].
        data (WorkflowDtoData | Unset): Custom data associated with the workflow Example: {'category': 'onboarding',
            'priority': 'high'}.
    """

    id: str
    identifier: str
    name: str
    critical: bool
    severity: SeverityLevelEnum
    tags: list[str] | Unset = UNSET
    data: WorkflowDtoData | Unset = UNSET
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
        from ..models.workflow_dto_data import WorkflowDtoData

        d = dict(src_dict)
        id = d.pop("id")

        identifier = d.pop("identifier")

        name = d.pop("name")

        critical = d.pop("critical")

        severity = SeverityLevelEnum(d.pop("severity"))

        tags = cast(list[str], d.pop("tags", UNSET))

        _data = d.pop("data", UNSET)
        data: WorkflowDtoData | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = WorkflowDtoData.from_dict(_data)

        workflow_dto = cls(
            id=id,
            identifier=identifier,
            name=name,
            critical=critical,
            severity=severity,
            tags=tags,
            data=data,
        )

        workflow_dto.additional_properties = d
        return workflow_dto

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
