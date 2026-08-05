from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_workflow_run_response_dto_delivery_lifecycle_status import (
    GetWorkflowRunResponseDtoDeliveryLifecycleStatus,
)
from ..models.get_workflow_run_response_dto_severity import GetWorkflowRunResponseDtoSeverity
from ..models.get_workflow_run_response_dto_status import GetWorkflowRunResponseDtoStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_workflow_run_response_dto_overrides import GetWorkflowRunResponseDtoOverrides
    from ..models.get_workflow_run_response_dto_payload import GetWorkflowRunResponseDtoPayload
    from ..models.step_run_dto import StepRunDto
    from ..models.topic_response_dto import TopicResponseDto


T = TypeVar("T", bound="GetWorkflowRunResponseDto")


@_attrs_define
class GetWorkflowRunResponseDto:
    """
    Attributes:
        id (str): Workflow run id
        workflow_id (str): Workflow identifier
        workflow_name (str): Workflow name
        organization_id (str): Organization identifier
        environment_id (str): Environment identifier
        internal_subscriber_id (str): Internal subscriber identifier
        status (GetWorkflowRunResponseDtoStatus): Workflow run status
        delivery_lifecycle_status (GetWorkflowRunResponseDtoDeliveryLifecycleStatus): Workflow run delivery lifecycle
            status
        trigger_identifier (str): Trigger identifier
        transaction_id (str): Transaction identifier
        created_at (str): Creation timestamp
        updated_at (str): Update timestamp
        severity (GetWorkflowRunResponseDtoSeverity): Severity
        critical (bool): Critical flag
        steps (list[StepRunDto]): Step runs
        payload (GetWorkflowRunResponseDtoPayload): Trigger payload
        subscriber_id (str | Unset): External subscriber identifier
        context_keys (list[str] | Unset): Context (single or multi) in which the workflow run was executed
        topics (list[TopicResponseDto] | Unset): Topics
        overrides (GetWorkflowRunResponseDtoOverrides | Unset): Trigger overrides passed to the original workflow
            trigger
    """

    id: str
    workflow_id: str
    workflow_name: str
    organization_id: str
    environment_id: str
    internal_subscriber_id: str
    status: GetWorkflowRunResponseDtoStatus
    delivery_lifecycle_status: GetWorkflowRunResponseDtoDeliveryLifecycleStatus
    trigger_identifier: str
    transaction_id: str
    created_at: str
    updated_at: str
    severity: GetWorkflowRunResponseDtoSeverity
    critical: bool
    steps: list[StepRunDto]
    payload: GetWorkflowRunResponseDtoPayload
    subscriber_id: str | Unset = UNSET
    context_keys: list[str] | Unset = UNSET
    topics: list[TopicResponseDto] | Unset = UNSET
    overrides: GetWorkflowRunResponseDtoOverrides | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        workflow_id = self.workflow_id

        workflow_name = self.workflow_name

        organization_id = self.organization_id

        environment_id = self.environment_id

        internal_subscriber_id = self.internal_subscriber_id

        status = self.status.value

        delivery_lifecycle_status = self.delivery_lifecycle_status.value

        trigger_identifier = self.trigger_identifier

        transaction_id = self.transaction_id

        created_at = self.created_at

        updated_at = self.updated_at

        severity = self.severity.value

        critical = self.critical

        steps = []
        for steps_item_data in self.steps:
            steps_item = steps_item_data.to_dict()
            steps.append(steps_item)

        payload = self.payload.to_dict()

        subscriber_id = self.subscriber_id

        context_keys: list[str] | Unset = UNSET
        if not isinstance(self.context_keys, Unset):
            context_keys = self.context_keys

        topics: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.topics, Unset):
            topics = []
            for topics_item_data in self.topics:
                topics_item = topics_item_data.to_dict()
                topics.append(topics_item)

        overrides: dict[str, Any] | Unset = UNSET
        if not isinstance(self.overrides, Unset):
            overrides = self.overrides.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "workflowId": workflow_id,
                "workflowName": workflow_name,
                "organizationId": organization_id,
                "environmentId": environment_id,
                "internalSubscriberId": internal_subscriber_id,
                "status": status,
                "deliveryLifecycleStatus": delivery_lifecycle_status,
                "triggerIdentifier": trigger_identifier,
                "transactionId": transaction_id,
                "createdAt": created_at,
                "updatedAt": updated_at,
                "severity": severity,
                "critical": critical,
                "steps": steps,
                "payload": payload,
            }
        )
        if subscriber_id is not UNSET:
            field_dict["subscriberId"] = subscriber_id
        if context_keys is not UNSET:
            field_dict["contextKeys"] = context_keys
        if topics is not UNSET:
            field_dict["topics"] = topics
        if overrides is not UNSET:
            field_dict["overrides"] = overrides

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_workflow_run_response_dto_overrides import GetWorkflowRunResponseDtoOverrides
        from ..models.get_workflow_run_response_dto_payload import GetWorkflowRunResponseDtoPayload
        from ..models.step_run_dto import StepRunDto
        from ..models.topic_response_dto import TopicResponseDto

        d = dict(src_dict)
        id = d.pop("id")

        workflow_id = d.pop("workflowId")

        workflow_name = d.pop("workflowName")

        organization_id = d.pop("organizationId")

        environment_id = d.pop("environmentId")

        internal_subscriber_id = d.pop("internalSubscriberId")

        status = GetWorkflowRunResponseDtoStatus(d.pop("status"))

        delivery_lifecycle_status = GetWorkflowRunResponseDtoDeliveryLifecycleStatus(d.pop("deliveryLifecycleStatus"))

        trigger_identifier = d.pop("triggerIdentifier")

        transaction_id = d.pop("transactionId")

        created_at = d.pop("createdAt")

        updated_at = d.pop("updatedAt")

        severity = GetWorkflowRunResponseDtoSeverity(d.pop("severity"))

        critical = d.pop("critical")

        steps = []
        _steps = d.pop("steps")
        for steps_item_data in _steps:
            steps_item = StepRunDto.from_dict(steps_item_data)

            steps.append(steps_item)

        payload = GetWorkflowRunResponseDtoPayload.from_dict(d.pop("payload"))

        subscriber_id = d.pop("subscriberId", UNSET)

        context_keys = cast(list[str], d.pop("contextKeys", UNSET))

        _topics = d.pop("topics", UNSET)
        topics: list[TopicResponseDto] | Unset = UNSET
        if _topics is not UNSET:
            topics = []
            for topics_item_data in _topics:
                topics_item = TopicResponseDto.from_dict(topics_item_data)

                topics.append(topics_item)

        _overrides = d.pop("overrides", UNSET)
        overrides: GetWorkflowRunResponseDtoOverrides | Unset
        if isinstance(_overrides, Unset):
            overrides = UNSET
        else:
            overrides = GetWorkflowRunResponseDtoOverrides.from_dict(_overrides)

        get_workflow_run_response_dto = cls(
            id=id,
            workflow_id=workflow_id,
            workflow_name=workflow_name,
            organization_id=organization_id,
            environment_id=environment_id,
            internal_subscriber_id=internal_subscriber_id,
            status=status,
            delivery_lifecycle_status=delivery_lifecycle_status,
            trigger_identifier=trigger_identifier,
            transaction_id=transaction_id,
            created_at=created_at,
            updated_at=updated_at,
            severity=severity,
            critical=critical,
            steps=steps,
            payload=payload,
            subscriber_id=subscriber_id,
            context_keys=context_keys,
            topics=topics,
            overrides=overrides,
        )

        get_workflow_run_response_dto.additional_properties = d
        return get_workflow_run_response_dto

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
