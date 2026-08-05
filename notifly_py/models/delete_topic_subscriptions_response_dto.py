from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.meta_dto import MetaDto
    from ..models.subscription_dto import SubscriptionDto
    from ..models.subscriptions_delete_error_dto import SubscriptionsDeleteErrorDto


T = TypeVar("T", bound="DeleteTopicSubscriptionsResponseDto")


@_attrs_define
class DeleteTopicSubscriptionsResponseDto:
    """
    Attributes:
        data (list[SubscriptionDto]): The list of successfully deleted subscriptions
        meta (MetaDto):
        errors (list[SubscriptionsDeleteErrorDto] | Unset): The list of errors for failed deletion attempts
    """

    data: list[SubscriptionDto]
    meta: MetaDto
    errors: list[SubscriptionsDeleteErrorDto] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)

        meta = self.meta.to_dict()

        errors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "meta": meta,
            }
        )
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.meta_dto import MetaDto
        from ..models.subscription_dto import SubscriptionDto
        from ..models.subscriptions_delete_error_dto import SubscriptionsDeleteErrorDto

        d = dict(src_dict)
        data = []
        _data = d.pop("data")
        for data_item_data in _data:
            data_item = SubscriptionDto.from_dict(data_item_data)

            data.append(data_item)

        meta = MetaDto.from_dict(d.pop("meta"))

        _errors = d.pop("errors", UNSET)
        errors: list[SubscriptionsDeleteErrorDto] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = SubscriptionsDeleteErrorDto.from_dict(errors_item_data)

                errors.append(errors_item)

        delete_topic_subscriptions_response_dto = cls(
            data=data,
            meta=meta,
            errors=errors,
        )

        delete_topic_subscriptions_response_dto.additional_properties = d
        return delete_topic_subscriptions_response_dto

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
