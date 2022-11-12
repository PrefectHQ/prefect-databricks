from typing import Any, Dict, List, Type, TypeVar

from pydantic import BaseModel, Field

from ..types import UNSET

T = TypeVar("T", bound="NotebookTaskBaseParameters")


class NotebookTaskBaseParameters(BaseModel):
    """Base parameters to be used for each run of this job. If the run is initiated by a call to [`run-
    now`](https://docs.databricks.com/dev-tools/api/latest/jobs.html#operation/JobsRunNow) with parameters specified,
    the two parameters maps are merged. If the same key is specified in `base_parameters` and in `run-now`, the value
    from `run-now` is used.

    Use [Task parameter variables](https://docs.databricks.com/jobs.html#parameter-variables) to set parameters
    containing information about job runs.

    If the notebook takes a parameter that is not specified in the job’s `base_parameters` or the `run-now` override
    parameters, the default value from the notebook is used.

    Retrieve these parameters in a notebook using [dbutils.widgets.get](https://docs.databricks.com/dev-
    tools/databricks-utils.html#dbutils-widgets).

        Example:
            {'age': 35, 'name': 'John Doe'}

    """

    additional_properties: Dict[str, Any] = Field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        if src_dict is None or src_dict is UNSET:
            return {}
        d = {k: v if v is not None else UNSET for k, v in src_dict.items()}
        notebook_task_base_parameters = cls()

        notebook_task_base_parameters.additional_properties = d
        return notebook_task_base_parameters

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
