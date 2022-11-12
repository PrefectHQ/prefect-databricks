from typing import Any, Dict, List, Type, TypeVar, Union

from pydantic import BaseModel, Field

from ..models.dbt_output import DbtOutput
from ..models.notebook_output import NotebookOutput
from ..models.run import Run
from ..models.sql_output import SqlOutput
from ..types import UNSET, Unset

T = TypeVar("T", bound="JobsRunsGetOutputResponse200")


class JobsRunsGetOutputResponse200(BaseModel):
    """
    Attributes:
        dbt_output (Union[Unset, DbtOutput]):
        error (Union[Unset, str]): An error message indicating why a task failed or why output is not available. The
            message is unstructured, and its exact format is subject to change. Example: ZeroDivisionError: integer division
            or modulo by zero.
        error_trace (Union[Unset, str]): If there was an error executing the run, this field contains any available
            stack traces. Example: ---------------------------------------------------------------------------
            Exception                                 Traceback (most recent call last)
                  1 numerator = 42
                  2 denominator = 0
            ----> 3 return numerator / denominator

            ZeroDivisionError: integer division or modulo by zero.
        logs (Union[Unset, str]): The output from tasks that write to standard streams (stdout/stderr) such as
            [SparkJarTask](https://docs.databricks.com/dev-tools/api/latest/jobs.html#/components/schemas/SparkJarTask),
            [SparkPythonTask](https://docs.databricks.com/dev-
            tools/api/latest/jobs.html#/components/schemas/SparkPythonTask,
            [PythonWheelTask](https://docs.databricks.com/dev-
            tools/api/latest/jobs.html#/components/schemas/PythonWheelTask. It's not supported for the
            [NotebookTask](https://docs.databricks.com/dev-tools/api/latest/jobs.html#/components/schemas/NotebookTask,
            [PipelineTask](https://docs.databricks.com/dev-tools/api/latest/jobs.html#/components/schemas/PipelineTask, or
            [SparkSubmitTask](https://docs.databricks.com/dev-
            tools/api/latest/jobs.html#/components/schemas/SparkSubmitTask. Databricks restricts this API to return the last
            5 MB of these logs. Example: Hello World!.
        logs_truncated (Union[Unset, bool]): Whether the logs are truncated. Example: True.
        metadata (Union[Unset, Run]):
        notebook_output (Union[Unset, NotebookOutput]):
        sql_output (Union[Unset, SqlOutput]):
    """

    dbt_output: Union[Unset, DbtOutput] = UNSET
    error: Union[Unset, str] = UNSET
    error_trace: Union[Unset, str] = UNSET
    logs: Union[Unset, str] = UNSET
    logs_truncated: Union[Unset, bool] = UNSET
    metadata: Union[Unset, Run] = UNSET
    notebook_output: Union[Unset, NotebookOutput] = UNSET
    sql_output: Union[Unset, SqlOutput] = UNSET
    additional_properties: Dict[str, Any] = Field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        dbt_output: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.dbt_output, Unset):
            dbt_output = self.dbt_output.to_dict()

        error = self.error
        error_trace = self.error_trace
        logs = self.logs
        logs_truncated = self.logs_truncated
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        notebook_output: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.notebook_output, Unset):
            notebook_output = self.notebook_output.to_dict()

        sql_output: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sql_output, Unset):
            sql_output = self.sql_output.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dbt_output is not UNSET:
            field_dict["dbt_output"] = dbt_output
        if error is not UNSET:
            field_dict["error"] = error
        if error_trace is not UNSET:
            field_dict["error_trace"] = error_trace
        if logs is not UNSET:
            field_dict["logs"] = logs
        if logs_truncated is not UNSET:
            field_dict["logs_truncated"] = logs_truncated
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if notebook_output is not UNSET:
            field_dict["notebook_output"] = notebook_output
        if sql_output is not UNSET:
            field_dict["sql_output"] = sql_output

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        if src_dict is None or src_dict is UNSET:
            return {}
        d = {k: v if v is not None else UNSET for k, v in src_dict.items()}
        _dbt_output = d.pop("dbt_output", UNSET)
        dbt_output: Union[Unset, DbtOutput]
        if isinstance(_dbt_output, Unset):
            dbt_output = UNSET
        else:
            dbt_output = DbtOutput.from_dict(_dbt_output)

        error = d.pop("error", UNSET)

        error_trace = d.pop("error_trace", UNSET)

        logs = d.pop("logs", UNSET)

        logs_truncated = d.pop("logs_truncated", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, Run]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = Run.from_dict(_metadata)

        _notebook_output = d.pop("notebook_output", UNSET)
        notebook_output: Union[Unset, NotebookOutput]
        if isinstance(_notebook_output, Unset):
            notebook_output = UNSET
        else:
            notebook_output = NotebookOutput.from_dict(_notebook_output)

        _sql_output = d.pop("sql_output", UNSET)
        sql_output: Union[Unset, SqlOutput]
        if isinstance(_sql_output, Unset):
            sql_output = UNSET
        else:
            sql_output = SqlOutput.from_dict(_sql_output)

        jobs_runs_get_output_response_200 = cls(
            dbt_output=dbt_output,
            error=error,
            error_trace=error_trace,
            logs=logs,
            logs_truncated=logs_truncated,
            metadata=metadata,
            notebook_output=notebook_output,
            sql_output=sql_output,
        )

        jobs_runs_get_output_response_200.additional_properties = d
        return jobs_runs_get_output_response_200

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
