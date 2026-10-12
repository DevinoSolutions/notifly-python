from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.trigger_signal_dto_type import TriggerSignalDtoType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.trigger_signal_dto_payload import TriggerSignalDtoPayload
    from ..models.trigger_signal_dto_to_type_1 import TriggerSignalDtoToType1
    from ..models.trigger_signal_dto_to_type_2_item_type_1 import TriggerSignalDtoToType2ItemType1


T = TypeVar("T", bound="TriggerSignalDto")


@_attrs_define
class TriggerSignalDto:
    """
    Attributes:
        type_ (TriggerSignalDtoType):
        workflow_id (str): Workflow identifier (same string used with `events.trigger`). Example: order-shipped.
        to (list[str | TriggerSignalDtoToType2ItemType1] | str | TriggerSignalDtoToType1 | Unset): Recipient(s). Accepts
            a subscriberId string, subscriber object, topic object, or an array of those. When omitted, Novu falls back to
            the conversation subscriber.
        payload (TriggerSignalDtoPayload | Unset): Arbitrary payload forwarded to the workflow. Example: {'orderId':
            'ORD-42'}.
    """

    type_: TriggerSignalDtoType
    workflow_id: str
    to: list[str | TriggerSignalDtoToType2ItemType1] | str | TriggerSignalDtoToType1 | Unset = UNSET
    payload: TriggerSignalDtoPayload | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.trigger_signal_dto_to_type_1 import TriggerSignalDtoToType1
        from ..models.trigger_signal_dto_to_type_2_item_type_1 import TriggerSignalDtoToType2ItemType1

        type_ = self.type_.value

        workflow_id = self.workflow_id

        to: dict[str, Any] | list[dict[str, Any] | str] | str | Unset
        if isinstance(self.to, Unset):
            to = UNSET
        elif isinstance(self.to, TriggerSignalDtoToType1):
            to = self.to.to_dict()
        elif isinstance(self.to, list):
            to = []
            for to_type_2_item_data in self.to:
                to_type_2_item: dict[str, Any] | str
                if isinstance(to_type_2_item_data, TriggerSignalDtoToType2ItemType1):
                    to_type_2_item = to_type_2_item_data.to_dict()
                else:
                    to_type_2_item = to_type_2_item_data
                to.append(to_type_2_item)

        else:
            to = self.to

        payload: dict[str, Any] | Unset = UNSET
        if not isinstance(self.payload, Unset):
            payload = self.payload.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "workflowId": workflow_id,
            }
        )
        if to is not UNSET:
            field_dict["to"] = to
        if payload is not UNSET:
            field_dict["payload"] = payload

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.trigger_signal_dto_payload import TriggerSignalDtoPayload
        from ..models.trigger_signal_dto_to_type_1 import TriggerSignalDtoToType1
        from ..models.trigger_signal_dto_to_type_2_item_type_1 import TriggerSignalDtoToType2ItemType1

        d = dict(src_dict)
        type_ = TriggerSignalDtoType(d.pop("type"))

        workflow_id = d.pop("workflowId")

        def _parse_to(
            data: object,
        ) -> list[str | TriggerSignalDtoToType2ItemType1] | str | TriggerSignalDtoToType1 | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                to_type_1 = TriggerSignalDtoToType1.from_dict(data)

                return to_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                to_type_2 = []
                _to_type_2 = data
                for to_type_2_item_data in _to_type_2:

                    def _parse_to_type_2_item(data: object) -> str | TriggerSignalDtoToType2ItemType1:
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            to_type_2_item_type_1 = TriggerSignalDtoToType2ItemType1.from_dict(data)

                            return to_type_2_item_type_1
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        return cast(str | TriggerSignalDtoToType2ItemType1, data)

                    to_type_2_item = _parse_to_type_2_item(to_type_2_item_data)

                    to_type_2.append(to_type_2_item)

                return to_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str | TriggerSignalDtoToType2ItemType1] | str | TriggerSignalDtoToType1 | Unset, data)

        to = _parse_to(d.pop("to", UNSET))

        _payload = d.pop("payload", UNSET)
        payload: TriggerSignalDtoPayload | Unset
        if isinstance(_payload, Unset):
            payload = UNSET
        else:
            payload = TriggerSignalDtoPayload.from_dict(_payload)

        trigger_signal_dto = cls(
            type_=type_,
            workflow_id=workflow_id,
            to=to,
            payload=payload,
        )

        trigger_signal_dto.additional_properties = d
        return trigger_signal_dto

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
