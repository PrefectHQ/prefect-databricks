from typing import Any, Dict, List, Type, TypeVar, Union, cast

from pydantic import BaseModel, Field

from ..models.repair_history_item_type import RepairHistoryItemType
from ..models.run_state import RunState
from ..types import UNSET, Unset

T = TypeVar("T", bound="RepairHistoryItem")


class RepairHistoryItem(BaseModel):
    """
    Attributes:
        end_time (Union[Unset, int]): The end time of the (repaired) run. Example: 1625060863413.
        id (Union[Unset, int]): The ID of the repair. Only returned for the items that represent a repair in
            `repair_history`. Example: 734650698524280.
        start_time (Union[Unset, int]): The start time of the (repaired) run. Example: 1625060460483.
        state (Union[Unset, RunState]): The result and lifecycle state of the run.
        task_run_ids (Union[Unset, List[int]]): The run IDs of the task runs that ran as part of this repair history
            item. Example: [1106460542112844, 988297789683452].
        type (Union[Unset, RepairHistoryItemType]): The repair history item type. Indicates whether a run is the
            original run or a repair run.
    """

    end_time: Union[Unset, int] = UNSET
    id: Union[Unset, int] = UNSET
    start_time: Union[Unset, int] = UNSET
    state: Union[Unset, RunState] = UNSET
    task_run_ids: Union[Unset, List[int]] = UNSET
    type: Union[Unset, RepairHistoryItemType] = UNSET
    additional_properties: Dict[str, Any] = Field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        end_time = self.end_time
        id = self.id
        start_time = self.start_time
        state: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.to_dict()

        task_run_ids: Union[Unset, List[int]] = UNSET
        if not isinstance(self.task_run_ids, Unset):
            task_run_ids = self.task_run_ids

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_time is not UNSET:
            field_dict["end_time"] = end_time
        if id is not UNSET:
            field_dict["id"] = id
        if start_time is not UNSET:
            field_dict["start_time"] = start_time
        if state is not UNSET:
            field_dict["state"] = state
        if task_run_ids is not UNSET:
            field_dict["task_run_ids"] = task_run_ids
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        if src_dict is None or src_dict is UNSET:
            return {}
        d = {k: v if v is not None else UNSET for k, v in src_dict.items()}
        end_time = d.pop("end_time", UNSET)

        id = d.pop("id", UNSET)

        start_time = d.pop("start_time", UNSET)

        _state = d.pop("state", UNSET)
        state: Union[Unset, RunState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = RunState.from_dict(_state)

        task_run_ids = cast(List[int], d.pop("task_run_ids", UNSET))

        _type = d.pop("type", UNSET)
        type: Union[Unset, RepairHistoryItemType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = RepairHistoryItemType(_type)

        repair_history_item = cls(
            end_time=end_time,
            id=id,
            start_time=start_time,
            state=state,
            task_run_ids=task_run_ids,
            type=type,
        )

        repair_history_item.additional_properties = d
        return repair_history_item

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
