from typing import Any, Dict, List, Type, TypeVar, Union, cast

from pydantic import BaseModel, Field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RepairRunInput")


class RepairRunInput(BaseModel):
    """
    Attributes:
        latest_repair_id (Union[Unset, int]): The ID of the latest repair. This parameter is not required when repairing
            a run for the first time, but must be provided on subsequent requests to repair the same run. Example:
            734650698524280.
        rerun_all_failed_tasks (Union[Unset, bool]): If true, repair all failed tasks. Only one of rerun_tasks or
            rerun_all_failed_tasks can be used.
        rerun_tasks (Union[Unset, List[str]]): The task keys of the task runs to repair. Example: ['task0', 'task1'].
        run_id (Union[Unset, int]): The job run ID of the run to repair. The run must not be in progress. Example:
            455644833.
    """

    latest_repair_id: Union[Unset, int] = UNSET
    rerun_all_failed_tasks: Union[Unset, bool] = False
    rerun_tasks: Union[Unset, List[str]] = UNSET
    run_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = Field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        latest_repair_id = self.latest_repair_id
        rerun_all_failed_tasks = self.rerun_all_failed_tasks
        rerun_tasks: Union[Unset, List[str]] = UNSET
        if not isinstance(self.rerun_tasks, Unset):
            rerun_tasks = self.rerun_tasks

        run_id = self.run_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if latest_repair_id is not UNSET:
            field_dict["latest_repair_id"] = latest_repair_id
        if rerun_all_failed_tasks is not UNSET:
            field_dict["rerun_all_failed_tasks"] = rerun_all_failed_tasks
        if rerun_tasks is not UNSET:
            field_dict["rerun_tasks"] = rerun_tasks
        if run_id is not UNSET:
            field_dict["run_id"] = run_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        if src_dict is None or src_dict is UNSET:
            return {}
        d = {k: v if v is not None else UNSET for k, v in src_dict.items()}
        latest_repair_id = d.pop("latest_repair_id", UNSET)

        rerun_all_failed_tasks = d.pop("rerun_all_failed_tasks", UNSET)

        rerun_tasks = cast(List[str], d.pop("rerun_tasks", UNSET))

        run_id = d.pop("run_id", UNSET)

        repair_run_input = cls(
            latest_repair_id=latest_repair_id,
            rerun_all_failed_tasks=rerun_all_failed_tasks,
            rerun_tasks=rerun_tasks,
            run_id=run_id,
        )

        repair_run_input.additional_properties = d
        return repair_run_input

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
