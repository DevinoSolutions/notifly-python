from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.notification_trigger_type import NotificationTriggerType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.notification_trigger_variable import NotificationTriggerVariable


T = TypeVar("T", bound="NotificationTrigger")


@_attrs_define
class NotificationTrigger:
    """
    Attributes:
        type_ (NotificationTriggerType):
        identifier (str):
        variables (list[NotificationTriggerVariable]):
        subscriber_variables (list[NotificationTriggerVariable] | Unset):
    """

    type_: NotificationTriggerType
    identifier: str
    variables: list[NotificationTriggerVariable]
    subscriber_variables: list[NotificationTriggerVariable] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value

        identifier = self.identifier

        variables = []
        for variables_item_data in self.variables:
            variables_item = variables_item_data.to_dict()
            variables.append(variables_item)

        subscriber_variables: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.subscriber_variables, Unset):
            subscriber_variables = []
            for subscriber_variables_item_data in self.subscriber_variables:
                subscriber_variables_item = subscriber_variables_item_data.to_dict()
                subscriber_variables.append(subscriber_variables_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "identifier": identifier,
                "variables": variables,
            }
        )
        if subscriber_variables is not UNSET:
            field_dict["subscriberVariables"] = subscriber_variables

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.notification_trigger_variable import NotificationTriggerVariable

        d = dict(src_dict)
        type_ = NotificationTriggerType(d.pop("type"))

        identifier = d.pop("identifier")

        variables = []
        _variables = d.pop("variables")
        for variables_item_data in _variables:
            variables_item = NotificationTriggerVariable.from_dict(variables_item_data)

            variables.append(variables_item)

        _subscriber_variables = d.pop("subscriberVariables", UNSET)
        subscriber_variables: list[NotificationTriggerVariable] | Unset = UNSET
        if _subscriber_variables is not UNSET:
            subscriber_variables = []
            for subscriber_variables_item_data in _subscriber_variables:
                subscriber_variables_item = NotificationTriggerVariable.from_dict(subscriber_variables_item_data)

                subscriber_variables.append(subscriber_variables_item)

        notification_trigger = cls(
            type_=type_,
            identifier=identifier,
            variables=variables,
            subscriber_variables=subscriber_variables,
        )

        notification_trigger.additional_properties = d
        return notification_trigger

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
