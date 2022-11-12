from typing import Any, Dict, List, Type, TypeVar, Union

from pydantic import BaseModel, Field

from ..models.dbt_task import DbtTask
from ..models.notebook_task import NotebookTask
from ..models.pipeline_task import PipelineTask
from ..models.python_wheel_task import PythonWheelTask
from ..models.spark_jar_task import SparkJarTask
from ..models.spark_python_task import SparkPythonTask
from ..models.spark_submit_task import SparkSubmitTask
from ..models.sql_task import SqlTask
from ..types import UNSET, Unset

T = TypeVar("T", bound="JobTask")


class JobTask(BaseModel):
    """
    Attributes:
        dbt_task (Union[Unset, DbtTask]):
        notebook_task (Union[Unset, NotebookTask]):
        pipeline_task (Union[Unset, PipelineTask]):
        python_wheel_task (Union[Unset, PythonWheelTask]):
        spark_jar_task (Union[Unset, SparkJarTask]):
        spark_python_task (Union[Unset, SparkPythonTask]):
        spark_submit_task (Union[Unset, SparkSubmitTask]):
        sql_task (Union[Unset, SqlTask]):
    """

    dbt_task: Union[Unset, DbtTask] = UNSET
    notebook_task: Union[Unset, NotebookTask] = UNSET
    pipeline_task: Union[Unset, PipelineTask] = UNSET
    python_wheel_task: Union[Unset, PythonWheelTask] = UNSET
    spark_jar_task: Union[Unset, SparkJarTask] = UNSET
    spark_python_task: Union[Unset, SparkPythonTask] = UNSET
    spark_submit_task: Union[Unset, SparkSubmitTask] = UNSET
    sql_task: Union[Unset, SqlTask] = UNSET
    additional_properties: Dict[str, Any] = Field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        dbt_task: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.dbt_task, Unset):
            dbt_task = self.dbt_task.to_dict()

        notebook_task: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.notebook_task, Unset):
            notebook_task = self.notebook_task.to_dict()

        pipeline_task: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pipeline_task, Unset):
            pipeline_task = self.pipeline_task.to_dict()

        python_wheel_task: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.python_wheel_task, Unset):
            python_wheel_task = self.python_wheel_task.to_dict()

        spark_jar_task: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.spark_jar_task, Unset):
            spark_jar_task = self.spark_jar_task.to_dict()

        spark_python_task: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.spark_python_task, Unset):
            spark_python_task = self.spark_python_task.to_dict()

        spark_submit_task: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.spark_submit_task, Unset):
            spark_submit_task = self.spark_submit_task.to_dict()

        sql_task: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sql_task, Unset):
            sql_task = self.sql_task.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dbt_task is not UNSET:
            field_dict["dbt_task"] = dbt_task
        if notebook_task is not UNSET:
            field_dict["notebook_task"] = notebook_task
        if pipeline_task is not UNSET:
            field_dict["pipeline_task"] = pipeline_task
        if python_wheel_task is not UNSET:
            field_dict["python_wheel_task"] = python_wheel_task
        if spark_jar_task is not UNSET:
            field_dict["spark_jar_task"] = spark_jar_task
        if spark_python_task is not UNSET:
            field_dict["spark_python_task"] = spark_python_task
        if spark_submit_task is not UNSET:
            field_dict["spark_submit_task"] = spark_submit_task
        if sql_task is not UNSET:
            field_dict["sql_task"] = sql_task

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        if src_dict is None or src_dict is UNSET:
            return {}
        d = {k: v if v is not None else UNSET for k, v in src_dict.items()}
        _dbt_task = d.pop("dbt_task", UNSET)
        dbt_task: Union[Unset, DbtTask]
        if isinstance(_dbt_task, Unset):
            dbt_task = UNSET
        else:
            dbt_task = DbtTask.from_dict(_dbt_task)

        _notebook_task = d.pop("notebook_task", UNSET)
        notebook_task: Union[Unset, NotebookTask]
        if isinstance(_notebook_task, Unset):
            notebook_task = UNSET
        else:
            notebook_task = NotebookTask.from_dict(_notebook_task)

        _pipeline_task = d.pop("pipeline_task", UNSET)
        pipeline_task: Union[Unset, PipelineTask]
        if isinstance(_pipeline_task, Unset):
            pipeline_task = UNSET
        else:
            pipeline_task = PipelineTask.from_dict(_pipeline_task)

        _python_wheel_task = d.pop("python_wheel_task", UNSET)
        python_wheel_task: Union[Unset, PythonWheelTask]
        if isinstance(_python_wheel_task, Unset):
            python_wheel_task = UNSET
        else:
            python_wheel_task = PythonWheelTask.from_dict(_python_wheel_task)

        _spark_jar_task = d.pop("spark_jar_task", UNSET)
        spark_jar_task: Union[Unset, SparkJarTask]
        if isinstance(_spark_jar_task, Unset):
            spark_jar_task = UNSET
        else:
            spark_jar_task = SparkJarTask.from_dict(_spark_jar_task)

        _spark_python_task = d.pop("spark_python_task", UNSET)
        spark_python_task: Union[Unset, SparkPythonTask]
        if isinstance(_spark_python_task, Unset):
            spark_python_task = UNSET
        else:
            spark_python_task = SparkPythonTask.from_dict(_spark_python_task)

        _spark_submit_task = d.pop("spark_submit_task", UNSET)
        spark_submit_task: Union[Unset, SparkSubmitTask]
        if isinstance(_spark_submit_task, Unset):
            spark_submit_task = UNSET
        else:
            spark_submit_task = SparkSubmitTask.from_dict(_spark_submit_task)

        _sql_task = d.pop("sql_task", UNSET)
        sql_task: Union[Unset, SqlTask]
        if isinstance(_sql_task, Unset):
            sql_task = UNSET
        else:
            sql_task = SqlTask.from_dict(_sql_task)

        job_task = cls(
            dbt_task=dbt_task,
            notebook_task=notebook_task,
            pipeline_task=pipeline_task,
            python_wheel_task=python_wheel_task,
            spark_jar_task=spark_jar_task,
            spark_python_task=spark_python_task,
            spark_submit_task=spark_submit_task,
            sql_task=sql_task,
        )

        job_task.additional_properties = d
        return job_task

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
