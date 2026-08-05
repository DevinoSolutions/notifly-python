from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.step_issues_dto_controls import StepIssuesDtoControls
    from ..models.step_issues_dto_integration import StepIssuesDtoIntegration


T = TypeVar("T", bound="StepIssuesDto")


@_attrs_define
class StepIssuesDto:
    """
    Attributes:
        controls (StepIssuesDtoControls | Unset): Controls-related issues
        integration (StepIssuesDtoIntegration | Unset): Integration-related issues
    """

    controls: StepIssuesDtoControls | Unset = UNSET
    integration: StepIssuesDtoIntegration | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        controls: dict[str, Any] | Unset = UNSET
        if not isinstance(self.controls, Unset):
            controls = self.controls.to_dict()

        integration: dict[str, Any] | Unset = UNSET
        if not isinstance(self.integration, Unset):
            integration = self.integration.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if controls is not UNSET:
            field_dict["controls"] = controls
        if integration is not UNSET:
            field_dict["integration"] = integration

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.step_issues_dto_controls import StepIssuesDtoControls
        from ..models.step_issues_dto_integration import StepIssuesDtoIntegration

        d = dict(src_dict)
        _controls = d.pop("controls", UNSET)
        controls: StepIssuesDtoControls | Unset
        if isinstance(_controls, Unset):
            controls = UNSET
        else:
            controls = StepIssuesDtoControls.from_dict(_controls)

        _integration = d.pop("integration", UNSET)
        integration: StepIssuesDtoIntegration | Unset
        if isinstance(_integration, Unset):
            integration = UNSET
        else:
            integration = StepIssuesDtoIntegration.from_dict(_integration)

        step_issues_dto = cls(
            controls=controls,
            integration=integration,
        )

        step_issues_dto.additional_properties = d
        return step_issues_dto

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
