from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.resource_origin_enum import ResourceOriginEnum
from ..models.step_type_enum import StepTypeEnum
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.http_request_control_dto import HttpRequestControlDto
    from ..models.http_request_controls_metadata_response_dto import HttpRequestControlsMetadataResponseDto
    from ..models.http_request_step_response_dto_provider_overrides_type_0 import (
        HttpRequestStepResponseDtoProviderOverridesType0,
    )
    from ..models.http_request_step_response_dto_variables import HttpRequestStepResponseDtoVariables
    from ..models.step_issues_dto import StepIssuesDto


T = TypeVar("T", bound="HttpRequestStepResponseDto")


@_attrs_define
class HttpRequestStepResponseDto:
    """
    Attributes:
        controls (HttpRequestControlsMetadataResponseDto):
        variables (HttpRequestStepResponseDtoVariables): JSON Schema for variables, follows the JSON Schema standard
        step_id (str): Unique identifier of the step
        field_id (str): Database identifier of the step
        name (str): Name of the step
        slug (str): Slug of the step
        type_ (StepTypeEnum): Type of the step
        origin (ResourceOriginEnum): Origin of the layout
        workflow_id (str): Workflow identifier
        workflow_database_id (str): Workflow database identifier
        control_values (HttpRequestControlDto | Unset):
        provider_overrides (HttpRequestStepResponseDtoProviderOverridesType0 | None | Unset): Per-provider content
            overrides keyed by providerId. Stored separately from controlValues and merged over the default body at send
            time. Keys are ChatProviderIdEnum / ToolProviderIdEnum values (e.g. `slack`, `whatsapp-business`, `pagerduty`).
            Example: {'slack': {'text': '{{payload.title}}', 'blocks': [{'type': 'divider'}]}, 'whatsapp-business': {'type':
            'text', 'text': {'body': '{{payload.title}}'}}, 'pagerduty': {'severity': 'warning', 'source': 'novu',
            'summary': '{{payload.title}}'}}.
        issues (StepIssuesDto | Unset):
        step_resolver_hash (str | Unset): Hash identifying the deployed Cloudflare Worker for this step
    """

    controls: HttpRequestControlsMetadataResponseDto
    variables: HttpRequestStepResponseDtoVariables
    step_id: str
    field_id: str
    name: str
    slug: str
    type_: StepTypeEnum
    origin: ResourceOriginEnum
    workflow_id: str
    workflow_database_id: str
    control_values: HttpRequestControlDto | Unset = UNSET
    provider_overrides: HttpRequestStepResponseDtoProviderOverridesType0 | None | Unset = UNSET
    issues: StepIssuesDto | Unset = UNSET
    step_resolver_hash: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.http_request_step_response_dto_provider_overrides_type_0 import (
            HttpRequestStepResponseDtoProviderOverridesType0,
        )

        controls = self.controls.to_dict()

        variables = self.variables.to_dict()

        step_id = self.step_id

        field_id = self.field_id

        name = self.name

        slug = self.slug

        type_ = self.type_.value

        origin = self.origin.value

        workflow_id = self.workflow_id

        workflow_database_id = self.workflow_database_id

        control_values: dict[str, Any] | Unset = UNSET
        if not isinstance(self.control_values, Unset):
            control_values = self.control_values.to_dict()

        provider_overrides: dict[str, Any] | None | Unset
        if isinstance(self.provider_overrides, Unset):
            provider_overrides = UNSET
        elif isinstance(self.provider_overrides, HttpRequestStepResponseDtoProviderOverridesType0):
            provider_overrides = self.provider_overrides.to_dict()
        else:
            provider_overrides = self.provider_overrides

        issues: dict[str, Any] | Unset = UNSET
        if not isinstance(self.issues, Unset):
            issues = self.issues.to_dict()

        step_resolver_hash = self.step_resolver_hash

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "controls": controls,
                "variables": variables,
                "stepId": step_id,
                "_id": field_id,
                "name": name,
                "slug": slug,
                "type": type_,
                "origin": origin,
                "workflowId": workflow_id,
                "workflowDatabaseId": workflow_database_id,
            }
        )
        if control_values is not UNSET:
            field_dict["controlValues"] = control_values
        if provider_overrides is not UNSET:
            field_dict["providerOverrides"] = provider_overrides
        if issues is not UNSET:
            field_dict["issues"] = issues
        if step_resolver_hash is not UNSET:
            field_dict["stepResolverHash"] = step_resolver_hash

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.http_request_control_dto import HttpRequestControlDto
        from ..models.http_request_controls_metadata_response_dto import HttpRequestControlsMetadataResponseDto
        from ..models.http_request_step_response_dto_provider_overrides_type_0 import (
            HttpRequestStepResponseDtoProviderOverridesType0,
        )
        from ..models.http_request_step_response_dto_variables import HttpRequestStepResponseDtoVariables
        from ..models.step_issues_dto import StepIssuesDto

        d = dict(src_dict)
        controls = HttpRequestControlsMetadataResponseDto.from_dict(d.pop("controls"))

        variables = HttpRequestStepResponseDtoVariables.from_dict(d.pop("variables"))

        step_id = d.pop("stepId")

        field_id = d.pop("_id")

        name = d.pop("name")

        slug = d.pop("slug")

        type_ = StepTypeEnum(d.pop("type"))

        origin = ResourceOriginEnum(d.pop("origin"))

        workflow_id = d.pop("workflowId")

        workflow_database_id = d.pop("workflowDatabaseId")

        _control_values = d.pop("controlValues", UNSET)
        control_values: HttpRequestControlDto | Unset
        if isinstance(_control_values, Unset):
            control_values = UNSET
        else:
            control_values = HttpRequestControlDto.from_dict(_control_values)

        def _parse_provider_overrides(data: object) -> HttpRequestStepResponseDtoProviderOverridesType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                provider_overrides_type_0 = HttpRequestStepResponseDtoProviderOverridesType0.from_dict(data)

                return provider_overrides_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(HttpRequestStepResponseDtoProviderOverridesType0 | None | Unset, data)

        provider_overrides = _parse_provider_overrides(d.pop("providerOverrides", UNSET))

        _issues = d.pop("issues", UNSET)
        issues: StepIssuesDto | Unset
        if isinstance(_issues, Unset):
            issues = UNSET
        else:
            issues = StepIssuesDto.from_dict(_issues)

        step_resolver_hash = d.pop("stepResolverHash", UNSET)

        http_request_step_response_dto = cls(
            controls=controls,
            variables=variables,
            step_id=step_id,
            field_id=field_id,
            name=name,
            slug=slug,
            type_=type_,
            origin=origin,
            workflow_id=workflow_id,
            workflow_database_id=workflow_database_id,
            control_values=control_values,
            provider_overrides=provider_overrides,
            issues=issues,
            step_resolver_hash=step_resolver_hash,
        )

        http_request_step_response_dto.additional_properties = d
        return http_request_step_response_dto

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
