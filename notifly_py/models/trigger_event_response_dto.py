from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.trigger_event_response_dto_status import TriggerEventResponseDtoStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.trigger_event_response_dto_job_data import TriggerEventResponseDtoJobData


T = TypeVar("T", bound="TriggerEventResponseDto")


@_attrs_define
class TriggerEventResponseDto:
    """
    Attributes:
        acknowledged (bool): Indicates whether the trigger was acknowledged or not
        status (TriggerEventResponseDtoStatus): Status of the trigger
        error (list[str] | Unset): In case of an error, this field will contain the error message(s)
        transaction_id (str | Unset): The returned transaction ID of the trigger
        activity_feed_link (str | Unset): Link to the activity feed for this trigger event
        job_data (TriggerEventResponseDtoJobData | Unset):
    """

    acknowledged: bool
    status: TriggerEventResponseDtoStatus
    error: list[str] | Unset = UNSET
    transaction_id: str | Unset = UNSET
    activity_feed_link: str | Unset = UNSET
    job_data: TriggerEventResponseDtoJobData | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        acknowledged = self.acknowledged

        status = self.status.value

        error: list[str] | Unset = UNSET
        if not isinstance(self.error, Unset):
            error = self.error

        transaction_id = self.transaction_id

        activity_feed_link = self.activity_feed_link

        job_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.job_data, Unset):
            job_data = self.job_data.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "acknowledged": acknowledged,
                "status": status,
            }
        )
        if error is not UNSET:
            field_dict["error"] = error
        if transaction_id is not UNSET:
            field_dict["transactionId"] = transaction_id
        if activity_feed_link is not UNSET:
            field_dict["activityFeedLink"] = activity_feed_link
        if job_data is not UNSET:
            field_dict["jobData"] = job_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.trigger_event_response_dto_job_data import TriggerEventResponseDtoJobData

        d = dict(src_dict)
        acknowledged = d.pop("acknowledged")

        status = TriggerEventResponseDtoStatus(d.pop("status"))

        error = cast(list[str], d.pop("error", UNSET))

        transaction_id = d.pop("transactionId", UNSET)

        activity_feed_link = d.pop("activityFeedLink", UNSET)

        _job_data = d.pop("jobData", UNSET)
        job_data: TriggerEventResponseDtoJobData | Unset
        if isinstance(_job_data, Unset):
            job_data = UNSET
        else:
            job_data = TriggerEventResponseDtoJobData.from_dict(_job_data)

        trigger_event_response_dto = cls(
            acknowledged=acknowledged,
            status=status,
            error=error,
            transaction_id=transaction_id,
            activity_feed_link=activity_feed_link,
            job_data=job_data,
        )

        trigger_event_response_dto.additional_properties = d
        return trigger_event_response_dto

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
