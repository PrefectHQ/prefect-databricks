from typing import Any, Dict, List, Type, TypeVar, Union

from pydantic import BaseModel, Field

from ..models.notebook_task_base_parameters import NotebookTaskBaseParameters
from ..models.notebook_task_source import NotebookTaskSource
from ..types import UNSET, Unset

T = TypeVar("T", bound="NotebookTask")


class NotebookTask(BaseModel):
    """
    Attributes:
        notebook_path (str): The path of the notebook to be run in the Databricks workspace or remote repository. For
            notebooks stored in the Databricks workspace, the path must be absolute and begin with a slash. For notebooks
            stored in a remote repository, the path must be relative. This field is required. Example:
            /Users/user.name@databricks.com/notebook_to_run.
        base_parameters (Union[Unset, NotebookTaskBaseParameters]): Base parameters to be used for each run of this job.
            If the run is initiated by a call to [`run-now`](https://docs.databricks.com/dev-
            tools/api/latest/jobs.html#operation/JobsRunNow) with parameters specified, the two parameters maps are merged.
            If the same key is specified in `base_parameters` and in `run-now`, the value from `run-now` is used.

            Use [Task parameter variables](https://docs.databricks.com/jobs.html#parameter-variables) to set parameters
            containing information about job runs.

            If the notebook takes a parameter that is not specified in the job’s `base_parameters` or the `run-now` override
            parameters, the default value from the notebook is used.

            Retrieve these parameters in a notebook using [dbutils.widgets.get](https://docs.databricks.com/dev-
            tools/databricks-utils.html#dbutils-widgets). Example: {'age': 35, 'name': 'John Doe'}.
        source (Union[Unset, NotebookTaskSource]): Optional location type of the notebook. When set to `WORKSPACE`, the
            notebook will be retrieved from the local Databricks workspace. When set to `GIT`, the notebook will be
            retrieved from a Git repository defined in `git_source`. If the value is empty, the task will use `GIT` if
            `git_source` is defined and `WORKSPACE` otherwise. Example: WORKSPACE.
    """

    notebook_path: str = None
    base_parameters: Union[Unset, NotebookTaskBaseParameters] = UNSET
    source: Union[Unset, NotebookTaskSource] = UNSET
    additional_properties: Dict[str, Any] = Field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        notebook_path = self.notebook_path
        base_parameters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.base_parameters, Unset):
            base_parameters = self.base_parameters.to_dict()

        source: Union[Unset, str] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "notebook_path": notebook_path,
            }
        )
        if base_parameters is not UNSET:
            field_dict["base_parameters"] = base_parameters
        if source is not UNSET:
            field_dict["source"] = source

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        if src_dict is None or src_dict is UNSET:
            return {}
        d = {k: v if v is not None else UNSET for k, v in src_dict.items()}
        notebook_path = d.pop("notebook_path")

        _base_parameters = d.pop("base_parameters", UNSET)
        base_parameters: Union[Unset, NotebookTaskBaseParameters]
        if isinstance(_base_parameters, Unset):
            base_parameters = UNSET
        else:
            base_parameters = NotebookTaskBaseParameters.from_dict(_base_parameters)

        _source = d.pop("source", UNSET)
        source: Union[Unset, NotebookTaskSource]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = NotebookTaskSource(_source)

        notebook_task = cls(
            notebook_path=notebook_path,
            base_parameters=base_parameters,
            source=source,
        )

        notebook_task.additional_properties = d
        return notebook_task

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
