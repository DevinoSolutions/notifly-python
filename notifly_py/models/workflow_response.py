from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.notification_group import NotificationGroup
    from ..models.notification_step_dto import NotificationStepDto
    from ..models.notification_trigger import NotificationTrigger
    from ..models.subscriber_preference_channels import SubscriberPreferenceChannels
    from ..models.workflow_response_data import WorkflowResponseData
    from ..models.workflow_response_workflow_integration_status import WorkflowResponseWorkflowIntegrationStatus


T = TypeVar("T", bound="WorkflowResponse")


@_attrs_define
class WorkflowResponse:
    """
    Attributes:
        name (str):
        description (str):
        active (bool):
        draft (bool):
        preference_settings (SubscriberPreferenceChannels):
        critical (bool):
        tags (list[str]):
        steps (list[NotificationStepDto]):
        field_organization_id (str):
        field_creator_id (str):
        field_environment_id (str):
        triggers (list[NotificationTrigger]):
        field_notification_group_id (str):
        deleted (bool):
        deleted_at (str):
        deleted_by (str):
        field_id (str | Unset):
        field_parent_id (str | Unset):
        notification_group (NotificationGroup | Unset):
        data (WorkflowResponseData | Unset):
        workflow_integration_status (WorkflowResponseWorkflowIntegrationStatus | Unset):
    """

    name: str
    description: str
    active: bool
    draft: bool
    preference_settings: SubscriberPreferenceChannels
    critical: bool
    tags: list[str]
    steps: list[NotificationStepDto]
    field_organization_id: str
    field_creator_id: str
    field_environment_id: str
    triggers: list[NotificationTrigger]
    field_notification_group_id: str
    deleted: bool
    deleted_at: str
    deleted_by: str
    field_id: str | Unset = UNSET
    field_parent_id: str | Unset = UNSET
    notification_group: NotificationGroup | Unset = UNSET
    data: WorkflowResponseData | Unset = UNSET
    workflow_integration_status: WorkflowResponseWorkflowIntegrationStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        description = self.description

        active = self.active

        draft = self.draft

        preference_settings = self.preference_settings.to_dict()

        critical = self.critical

        tags = self.tags

        steps = []
        for steps_item_data in self.steps:
            steps_item = steps_item_data.to_dict()
            steps.append(steps_item)

        field_organization_id = self.field_organization_id

        field_creator_id = self.field_creator_id

        field_environment_id = self.field_environment_id

        triggers = []
        for triggers_item_data in self.triggers:
            triggers_item = triggers_item_data.to_dict()
            triggers.append(triggers_item)

        field_notification_group_id = self.field_notification_group_id

        deleted = self.deleted

        deleted_at = self.deleted_at

        deleted_by = self.deleted_by

        field_id = self.field_id

        field_parent_id = self.field_parent_id

        notification_group: dict[str, Any] | Unset = UNSET
        if not isinstance(self.notification_group, Unset):
            notification_group = self.notification_group.to_dict()

        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        workflow_integration_status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.workflow_integration_status, Unset):
            workflow_integration_status = self.workflow_integration_status.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "description": description,
                "active": active,
                "draft": draft,
                "preferenceSettings": preference_settings,
                "critical": critical,
                "tags": tags,
                "steps": steps,
                "_organizationId": field_organization_id,
                "_creatorId": field_creator_id,
                "_environmentId": field_environment_id,
                "triggers": triggers,
                "_notificationGroupId": field_notification_group_id,
                "deleted": deleted,
                "deletedAt": deleted_at,
                "deletedBy": deleted_by,
            }
        )
        if field_id is not UNSET:
            field_dict["_id"] = field_id
        if field_parent_id is not UNSET:
            field_dict["_parentId"] = field_parent_id
        if notification_group is not UNSET:
            field_dict["notificationGroup"] = notification_group
        if data is not UNSET:
            field_dict["data"] = data
        if workflow_integration_status is not UNSET:
            field_dict["workflowIntegrationStatus"] = workflow_integration_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.notification_group import NotificationGroup
        from ..models.notification_step_dto import NotificationStepDto
        from ..models.notification_trigger import NotificationTrigger
        from ..models.subscriber_preference_channels import SubscriberPreferenceChannels
        from ..models.workflow_response_data import WorkflowResponseData
        from ..models.workflow_response_workflow_integration_status import WorkflowResponseWorkflowIntegrationStatus

        d = dict(src_dict)
        name = d.pop("name")

        description = d.pop("description")

        active = d.pop("active")

        draft = d.pop("draft")

        preference_settings = SubscriberPreferenceChannels.from_dict(d.pop("preferenceSettings"))

        critical = d.pop("critical")

        tags = cast(list[str], d.pop("tags"))

        steps = []
        _steps = d.pop("steps")
        for steps_item_data in _steps:
            steps_item = NotificationStepDto.from_dict(steps_item_data)

            steps.append(steps_item)

        field_organization_id = d.pop("_organizationId")

        field_creator_id = d.pop("_creatorId")

        field_environment_id = d.pop("_environmentId")

        triggers = []
        _triggers = d.pop("triggers")
        for triggers_item_data in _triggers:
            triggers_item = NotificationTrigger.from_dict(triggers_item_data)

            triggers.append(triggers_item)

        field_notification_group_id = d.pop("_notificationGroupId")

        deleted = d.pop("deleted")

        deleted_at = d.pop("deletedAt")

        deleted_by = d.pop("deletedBy")

        field_id = d.pop("_id", UNSET)

        field_parent_id = d.pop("_parentId", UNSET)

        _notification_group = d.pop("notificationGroup", UNSET)
        notification_group: NotificationGroup | Unset
        if isinstance(_notification_group, Unset):
            notification_group = UNSET
        else:
            notification_group = NotificationGroup.from_dict(_notification_group)

        _data = d.pop("data", UNSET)
        data: WorkflowResponseData | Unset
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = WorkflowResponseData.from_dict(_data)

        _workflow_integration_status = d.pop("workflowIntegrationStatus", UNSET)
        workflow_integration_status: WorkflowResponseWorkflowIntegrationStatus | Unset
        if isinstance(_workflow_integration_status, Unset):
            workflow_integration_status = UNSET
        else:
            workflow_integration_status = WorkflowResponseWorkflowIntegrationStatus.from_dict(
                _workflow_integration_status
            )

        workflow_response = cls(
            name=name,
            description=description,
            active=active,
            draft=draft,
            preference_settings=preference_settings,
            critical=critical,
            tags=tags,
            steps=steps,
            field_organization_id=field_organization_id,
            field_creator_id=field_creator_id,
            field_environment_id=field_environment_id,
            triggers=triggers,
            field_notification_group_id=field_notification_group_id,
            deleted=deleted,
            deleted_at=deleted_at,
            deleted_by=deleted_by,
            field_id=field_id,
            field_parent_id=field_parent_id,
            notification_group=notification_group,
            data=data,
            workflow_integration_status=workflow_integration_status,
        )

        workflow_response.additional_properties = d
        return workflow_response

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
