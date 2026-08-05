from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.integration_issue_enum import IntegrationIssueEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="StepIntegrationIssue")


@_attrs_define
class StepIntegrationIssue:
    """
    Attributes:
        issue_type (IntegrationIssueEnum): Type of integration issue
        message (str): Detailed message describing the issue
        variable_name (str | Unset): Name of the variable related to the issue
    """

    issue_type: IntegrationIssueEnum
    message: str
    variable_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        issue_type = self.issue_type.value

        message = self.message

        variable_name = self.variable_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "issueType": issue_type,
                "message": message,
            }
        )
        if variable_name is not UNSET:
            field_dict["variableName"] = variable_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        issue_type = IntegrationIssueEnum(d.pop("issueType"))

        message = d.pop("message")

        variable_name = d.pop("variableName", UNSET)

        step_integration_issue = cls(
            issue_type=issue_type,
            message=message,
            variable_name=variable_name,
        )

        step_integration_issue.additional_properties = d
        return step_integration_issue

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
