from typing import Any, Dict, List, Type, TypeVar, Union

from pydantic import BaseModel, Field

from ..models.dbt_task import DbtTask
from ..models.job_email_notifications import JobEmailNotifications
from ..models.library import Library
from ..models.new_cluster import NewCluster
from ..models.notebook_task import NotebookTask
from ..models.pipeline_task import PipelineTask
from ..models.python_wheel_task import PythonWheelTask
from ..models.spark_jar_task import SparkJarTask
from ..models.spark_python_task import SparkPythonTask
from ..models.spark_submit_task import SparkSubmitTask
from ..models.sql_task import SqlTask
from ..models.task_dependencies_item import TaskDependenciesItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="JobTaskSettings")


class JobTaskSettings(BaseModel):
    """
    Attributes:
        task_key (str): A unique name for the task. This field is used to refer to this task from other tasks.
            This field is required and must be unique within its parent job.
            On Update or Reset, this field is used to reference the tasks to be updated or reset.
            The maximum length is 100 characters. Example: Task_Key.
        dbt_task (Union[Unset, DbtTask]):
        depends_on (Union[Unset, List[TaskDependenciesItem]]): An optional array of objects specifying the dependency
            graph of the task. All tasks specified in this field must complete successfully before executing this task.
            The key is `task_key`, and the value is the name assigned to the dependent task.
            This field is required when a job consists of more than one task. Example: [{'task_key': 'Previous_Task_Key'},
            {'task_key': 'Other_Task_Key'}].
        description (Union[Unset, str]): An optional description for this task.
            The maximum length is 4096 bytes. Example: This is the description for this task..
        email_notifications (Union[Unset, JobEmailNotifications]):
        existing_cluster_id (Union[Unset, str]): If existing_cluster_id, the ID of an existing cluster that is used for
            all runs of this task. When running tasks on an existing cluster, you may need to manually restart the cluster
            if it stops responding. We suggest running jobs on new clusters for greater reliability. Example:
            0923-164208-meows279.
        job_cluster_key (Union[Unset, str]): If job_cluster_key, this task is executed reusing the cluster specified in
            `job.settings.job_clusters`.
        libraries (Union[Unset, List[Library]]): An optional list of libraries to be installed on the cluster that
            executes the task. The default value is an empty list.
        max_retries (Union[Unset, int]): An optional maximum number of times to retry an unsuccessful run. A run is
            considered to be unsuccessful if it completes with the `FAILED` result_state or `INTERNAL_ERROR`
            `life_cycle_state`. The value -1 means to retry indefinitely and the value 0 means to never retry. The default
            behavior is to never retry. Example: 10.
        min_retry_interval_millis (Union[Unset, int]): An optional minimal interval in milliseconds between the start of
            the failed run and the subsequent retry run. The default behavior is that unsuccessful runs are immediately
            retried. Example: 2000.
        new_cluster (Union[Unset, NewCluster]):
        notebook_task (Union[Unset, NotebookTask]):
        pipeline_task (Union[Unset, PipelineTask]):
        python_wheel_task (Union[Unset, PythonWheelTask]):
        retry_on_timeout (Union[Unset, bool]): An optional policy to specify whether to retry a task when it times out.
            The default behavior is to not retry on timeout. Example: True.
        spark_jar_task (Union[Unset, SparkJarTask]):
        spark_python_task (Union[Unset, SparkPythonTask]):
        spark_submit_task (Union[Unset, SparkSubmitTask]):
        sql_task (Union[Unset, SqlTask]):
        timeout_seconds (Union[Unset, int]): An optional timeout applied to each run of this job task. The default
            behavior is to have no timeout. Example: 86400.
    """

    task_key: str = None
    dbt_task: Union[Unset, DbtTask] = UNSET
    depends_on: Union[Unset, List[TaskDependenciesItem]] = UNSET
    description: Union[Unset, str] = UNSET
    email_notifications: Union[Unset, JobEmailNotifications] = UNSET
    existing_cluster_id: Union[Unset, str] = UNSET
    job_cluster_key: Union[Unset, str] = UNSET
    libraries: Union[Unset, List[Library]] = UNSET
    max_retries: Union[Unset, int] = UNSET
    min_retry_interval_millis: Union[Unset, int] = UNSET
    new_cluster: Union[Unset, NewCluster] = UNSET
    notebook_task: Union[Unset, NotebookTask] = UNSET
    pipeline_task: Union[Unset, PipelineTask] = UNSET
    python_wheel_task: Union[Unset, PythonWheelTask] = UNSET
    retry_on_timeout: Union[Unset, bool] = UNSET
    spark_jar_task: Union[Unset, SparkJarTask] = UNSET
    spark_python_task: Union[Unset, SparkPythonTask] = UNSET
    spark_submit_task: Union[Unset, SparkSubmitTask] = UNSET
    sql_task: Union[Unset, SqlTask] = UNSET
    timeout_seconds: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = Field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        task_key = self.task_key
        dbt_task: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.dbt_task, Unset):
            dbt_task = self.dbt_task.to_dict()

        depends_on: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.depends_on, Unset):
            depends_on = []
            for componentsschemas_task_dependencies_item_data in self.depends_on:
                componentsschemas_task_dependencies_item = (
                    componentsschemas_task_dependencies_item_data.to_dict()
                )

                depends_on.append(componentsschemas_task_dependencies_item)

        description = self.description
        email_notifications: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.email_notifications, Unset):
            email_notifications = self.email_notifications.to_dict()

        existing_cluster_id = self.existing_cluster_id
        job_cluster_key = self.job_cluster_key
        libraries: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.libraries, Unset):
            libraries = []
            for libraries_item_data in self.libraries:
                libraries_item = libraries_item_data.to_dict()

                libraries.append(libraries_item)

        max_retries = self.max_retries
        min_retry_interval_millis = self.min_retry_interval_millis
        new_cluster: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.new_cluster, Unset):
            new_cluster = self.new_cluster.to_dict()

        notebook_task: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.notebook_task, Unset):
            notebook_task = self.notebook_task.to_dict()

        pipeline_task: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pipeline_task, Unset):
            pipeline_task = self.pipeline_task.to_dict()

        python_wheel_task: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.python_wheel_task, Unset):
            python_wheel_task = self.python_wheel_task.to_dict()

        retry_on_timeout = self.retry_on_timeout
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

        timeout_seconds = self.timeout_seconds

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "task_key": task_key,
            }
        )
        if dbt_task is not UNSET:
            field_dict["dbt_task"] = dbt_task
        if depends_on is not UNSET:
            field_dict["depends_on"] = depends_on
        if description is not UNSET:
            field_dict["description"] = description
        if email_notifications is not UNSET:
            field_dict["email_notifications"] = email_notifications
        if existing_cluster_id is not UNSET:
            field_dict["existing_cluster_id"] = existing_cluster_id
        if job_cluster_key is not UNSET:
            field_dict["job_cluster_key"] = job_cluster_key
        if libraries is not UNSET:
            field_dict["libraries"] = libraries
        if max_retries is not UNSET:
            field_dict["max_retries"] = max_retries
        if min_retry_interval_millis is not UNSET:
            field_dict["min_retry_interval_millis"] = min_retry_interval_millis
        if new_cluster is not UNSET:
            field_dict["new_cluster"] = new_cluster
        if notebook_task is not UNSET:
            field_dict["notebook_task"] = notebook_task
        if pipeline_task is not UNSET:
            field_dict["pipeline_task"] = pipeline_task
        if python_wheel_task is not UNSET:
            field_dict["python_wheel_task"] = python_wheel_task
        if retry_on_timeout is not UNSET:
            field_dict["retry_on_timeout"] = retry_on_timeout
        if spark_jar_task is not UNSET:
            field_dict["spark_jar_task"] = spark_jar_task
        if spark_python_task is not UNSET:
            field_dict["spark_python_task"] = spark_python_task
        if spark_submit_task is not UNSET:
            field_dict["spark_submit_task"] = spark_submit_task
        if sql_task is not UNSET:
            field_dict["sql_task"] = sql_task
        if timeout_seconds is not UNSET:
            field_dict["timeout_seconds"] = timeout_seconds

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        if src_dict is None or src_dict is UNSET:
            return {}
        d = {k: v if v is not None else UNSET for k, v in src_dict.items()}
        task_key = d.pop("task_key")

        _dbt_task = d.pop("dbt_task", UNSET)
        dbt_task: Union[Unset, DbtTask]
        if isinstance(_dbt_task, Unset):
            dbt_task = UNSET
        else:
            dbt_task = DbtTask.from_dict(_dbt_task)

        depends_on = []
        _depends_on = d.pop("depends_on", UNSET)
        for componentsschemas_task_dependencies_item_data in _depends_on or []:
            componentsschemas_task_dependencies_item = TaskDependenciesItem.from_dict(
                componentsschemas_task_dependencies_item_data
            )

            depends_on.append(componentsschemas_task_dependencies_item)

        description = d.pop("description", UNSET)

        _email_notifications = d.pop("email_notifications", UNSET)
        email_notifications: Union[Unset, JobEmailNotifications]
        if isinstance(_email_notifications, Unset):
            email_notifications = UNSET
        else:
            email_notifications = JobEmailNotifications.from_dict(_email_notifications)

        existing_cluster_id = d.pop("existing_cluster_id", UNSET)

        job_cluster_key = d.pop("job_cluster_key", UNSET)

        libraries = []
        _libraries = d.pop("libraries", UNSET)
        for libraries_item_data in _libraries or []:
            libraries_item = Library.from_dict(libraries_item_data)

            libraries.append(libraries_item)

        max_retries = d.pop("max_retries", UNSET)

        min_retry_interval_millis = d.pop("min_retry_interval_millis", UNSET)

        _new_cluster = d.pop("new_cluster", UNSET)
        new_cluster: Union[Unset, NewCluster]
        if isinstance(_new_cluster, Unset):
            new_cluster = UNSET
        else:
            new_cluster = NewCluster.from_dict(_new_cluster)

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

        retry_on_timeout = d.pop("retry_on_timeout", UNSET)

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

        timeout_seconds = d.pop("timeout_seconds", UNSET)

        job_task_settings = cls(
            task_key=task_key,
            dbt_task=dbt_task,
            depends_on=depends_on,
            description=description,
            email_notifications=email_notifications,
            existing_cluster_id=existing_cluster_id,
            job_cluster_key=job_cluster_key,
            libraries=libraries,
            max_retries=max_retries,
            min_retry_interval_millis=min_retry_interval_millis,
            new_cluster=new_cluster,
            notebook_task=notebook_task,
            pipeline_task=pipeline_task,
            python_wheel_task=python_wheel_task,
            retry_on_timeout=retry_on_timeout,
            spark_jar_task=spark_jar_task,
            spark_python_task=spark_python_task,
            spark_submit_task=spark_submit_task,
            sql_task=sql_task,
            timeout_seconds=timeout_seconds,
        )

        job_task_settings.additional_properties = d
        return job_task_settings

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
