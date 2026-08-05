from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.workflow_response_dto import WorkflowResponseDto


T = TypeVar("T", bound="WebhookCreatedWorkflowDto")


@_attrs_define
class WebhookCreatedWorkflowDto:
    """
    Attributes:
        object_ (WorkflowResponseDto):
    """

    object_: WorkflowResponseDto
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        object_ = self.object_.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "object": object_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.workflow_response_dto import WorkflowResponseDto

        d = dict(src_dict)
        object_ = WorkflowResponseDto.from_dict(d.pop("object"))

        webhook_created_workflow_dto = cls(
            object_=object_,
        )

        webhook_created_workflow_dto.additional_properties = d
        return webhook_created_workflow_dto

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
