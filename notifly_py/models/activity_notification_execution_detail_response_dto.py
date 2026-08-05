from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.execution_details_source_enum import ExecutionDetailsSourceEnum
from ..models.execution_details_status_enum import ExecutionDetailsStatusEnum
from ..models.providers_id_enum import ProvidersIdEnum
from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivityNotificationExecutionDetailResponseDto")


@_attrs_define
class ActivityNotificationExecutionDetailResponseDto:
    """
    Attributes:
        field_id (str): Unique identifier of the execution detail
        status (ExecutionDetailsStatusEnum): Status of the execution detail
        detail (str): Detailed information about the execution
        is_retry (bool): Whether the execution is a retry or not
        is_test (bool): Whether the execution is a test or not
        source (ExecutionDetailsSourceEnum): Source of the execution detail
        created_at (str | Unset): Creation time of the execution detail
        provider_id (ProvidersIdEnum | Unset): Provider ID of the job
        raw (None | str | Unset): Raw data of the execution
    """

    field_id: str
    status: ExecutionDetailsStatusEnum
    detail: str
    is_retry: bool
    is_test: bool
    source: ExecutionDetailsSourceEnum
    created_at: str | Unset = UNSET
    provider_id: ProvidersIdEnum | Unset = UNSET
    raw: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_id = self.field_id

        status = self.status.value

        detail = self.detail

        is_retry = self.is_retry

        is_test = self.is_test

        source = self.source.value

        created_at = self.created_at

        provider_id: str | Unset = UNSET
        if not isinstance(self.provider_id, Unset):
            provider_id = self.provider_id.value

        raw: None | str | Unset
        if isinstance(self.raw, Unset):
            raw = UNSET
        else:
            raw = self.raw

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "_id": field_id,
                "status": status,
                "detail": detail,
                "isRetry": is_retry,
                "isTest": is_test,
                "source": source,
            }
        )
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if provider_id is not UNSET:
            field_dict["providerId"] = provider_id
        if raw is not UNSET:
            field_dict["raw"] = raw

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        field_id = d.pop("_id")

        status = ExecutionDetailsStatusEnum(d.pop("status"))

        detail = d.pop("detail")

        is_retry = d.pop("isRetry")

        is_test = d.pop("isTest")

        source = ExecutionDetailsSourceEnum(d.pop("source"))

        created_at = d.pop("createdAt", UNSET)

        _provider_id = d.pop("providerId", UNSET)
        provider_id: ProvidersIdEnum | Unset
        if isinstance(_provider_id, Unset):
            provider_id = UNSET
        else:
            provider_id = ProvidersIdEnum(_provider_id)

        def _parse_raw(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        raw = _parse_raw(d.pop("raw", UNSET))

        activity_notification_execution_detail_response_dto = cls(
            field_id=field_id,
            status=status,
            detail=detail,
            is_retry=is_retry,
            is_test=is_test,
            source=source,
            created_at=created_at,
            provider_id=provider_id,
            raw=raw,
        )

        activity_notification_execution_detail_response_dto.additional_properties = d
        return activity_notification_execution_detail_response_dto

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
