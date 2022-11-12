from typing import Any, Dict, List, Type, TypeVar, Union

from pydantic import BaseModel, Field

from ..models.repair_history_item import RepairHistoryItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="RepairHistory")


class RepairHistory(BaseModel):
    """
    Attributes:
        repair_history (Union[Unset, List[RepairHistoryItem]]): The repair history of the run.
    """

    repair_history: Union[Unset, List[RepairHistoryItem]] = UNSET
    additional_properties: Dict[str, Any] = Field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        repair_history: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.repair_history, Unset):
            repair_history = []
            for repair_history_item_data in self.repair_history:
                repair_history_item = repair_history_item_data.to_dict()

                repair_history.append(repair_history_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if repair_history is not UNSET:
            field_dict["repair_history"] = repair_history

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        if src_dict is None or src_dict is UNSET:
            return {}
        d = {k: v if v is not None else UNSET for k, v in src_dict.items()}
        repair_history = []
        _repair_history = d.pop("repair_history", UNSET)
        for repair_history_item_data in _repair_history or []:
            repair_history_item = RepairHistoryItem.from_dict(repair_history_item_data)

            repair_history.append(repair_history_item)

        repair_history = cls(
            repair_history=repair_history,
        )

        repair_history.additional_properties = d
        return repair_history

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties.get(key)

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
