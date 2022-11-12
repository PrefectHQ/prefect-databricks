from typing import Any, Dict, List, Type, TypeVar, Union, cast

from pydantic import BaseModel, Field

from ..models.cluster_instance import ClusterInstance
from ..models.dbt_task import DbtTask
from ..models.library import Library
from ..models.new_cluster import NewCluster
from ..models.notebook_task import NotebookTask
from ..models.pipeline_task import PipelineTask
from ..models.python_wheel_task import PythonWheelTask
from ..models.run_state import RunState
from ..models.spark_jar_task import SparkJarTask
from ..models.spark_python_task import SparkPythonTask
from ..models.spark_submit_task import SparkSubmitTask
from ..models.sql_task import SqlTask
from ..models.task_dependencies_item import TaskDependenciesItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="RunTask")


class RunTask(BaseModel):
    """
    Attributes:
        attempt_number (Union[Unset, int]): The sequence number of this run attempt for a triggered job run. The initial
            attempt of a run has an attempt_number of 0\. If the initial run attempt fails, and the job has a retry policy
            (`max_retries` \> 0), subsequent runs are created with an `original_attempt_run_id` of the original attempt’s ID
            and an incrementing `attempt_number`. Runs are retried only until they succeed, and the maximum `attempt_number`
            is the same as the `max_retries` value for the job.
        cleanup_duration (Union[Unset, int]): The time in milliseconds it took to terminate the cluster and clean up any
            associated artifacts. The total duration of the run is the sum of the setup_duration, the execution_duration,
            and the cleanup_duration.
        cluster_instance (Union[Unset, ClusterInstance]):
        dbt_task (Union[Unset, DbtTask]):
        depends_on (Union[Unset, List[TaskDependenciesItem]]): An optional array of objects specifying the dependency
            graph of the task. All tasks specified in this field must complete successfully before executing this task.
            The key is `task_key`, and the value is the name assigned to the dependent task.
            This field is required when a job consists of more than one task. Example: [{'task_key': 'Previous_Task_Key'},
            {'task_key': 'Other_Task_Key'}].
        description (Union[Unset, str]): An optional description for this task.
            The maximum length is 4096 bytes. Example: This is the description for this task..
        end_time (Union[Unset, int]): The time at which this run ended in epoch milliseconds (milliseconds since
            1/1/1970 UTC). This field is set to 0 if the job is still running. Example: 1625060863413.
        execution_duration (Union[Unset, int]): The time in milliseconds it took to execute the commands in the JAR or
            notebook until they completed, failed, timed out, were cancelled, or encountered an unexpected error.
        existing_cluster_id (Union[Unset, str]): If existing_cluster_id, the ID of an existing cluster that is used for
            all runs of this job. When running jobs on an existing cluster, you may need to manually restart the cluster if
            it stops responding. We suggest running jobs on new clusters for greater reliability.
        git_source (Union[Any, Unset]): This functionality is in Public Preview.

            An optional specification for a remote repository containing the notebooks used by this job's notebook tasks.
            Example: {'git_branch': 'main', 'git_provider': 'gitHub', 'git_url': 'https://github.com/databricks/databricks-
            cli'}.
        libraries (Union[Unset, List[Library]]): An optional list of libraries to be installed on the cluster that
            executes the job. The default value is an empty list.
        new_cluster (Union[Unset, NewCluster]):
        notebook_task (Union[Unset, NotebookTask]):
        pipeline_task (Union[Unset, PipelineTask]):
        python_wheel_task (Union[Unset, PythonWheelTask]):
        run_id (Union[Unset, int]): The ID of the task run. Example: 99887766.
        setup_duration (Union[Unset, int]): The time it took to set up the cluster in milliseconds. For runs that run on
            new clusters this is the cluster creation time, for runs that run on existing clusters this time should be very
            short.
        spark_jar_task (Union[Unset, SparkJarTask]):
        spark_python_task (Union[Unset, SparkPythonTask]):
        spark_submit_task (Union[Unset, SparkSubmitTask]):
        sql_task (Union[Unset, SqlTask]):
        start_time (Union[Unset, int]): The time at which this run was started in epoch milliseconds (milliseconds since
            1/1/1970 UTC). This may not be the time when the job task starts executing, for example, if the job is scheduled
            to run on a new cluster, this is the time the cluster creation call is issued. Example: 1625060460483.
        state (Union[Unset, RunState]): The result and lifecycle state of the run.
        task_key (Union[Unset, str]): A unique name for the task. This field is used to refer to this task from other
            tasks.
            This field is required and must be unique within its parent job.
            On Update or Reset, this field is used to reference the tasks to be updated or reset.
            The maximum length is 100 characters. Example: Task_Key.
    """

    attempt_number: Union[Unset, int] = UNSET
    cleanup_duration: Union[Unset, int] = UNSET
    cluster_instance: Union[Unset, ClusterInstance] = UNSET
    dbt_task: Union[Unset, DbtTask] = UNSET
    depends_on: Union[Unset, List[TaskDependenciesItem]] = UNSET
    description: Union[Unset, str] = UNSET
    end_time: Union[Unset, int] = UNSET
    execution_duration: Union[Unset, int] = UNSET
    existing_cluster_id: Union[Unset, str] = UNSET
    git_source: Union[Any, Unset] = UNSET
    libraries: Union[Unset, List[Library]] = UNSET
    new_cluster: Union[Unset, NewCluster] = UNSET
    notebook_task: Union[Unset, NotebookTask] = UNSET
    pipeline_task: Union[Unset, PipelineTask] = UNSET
    python_wheel_task: Union[Unset, PythonWheelTask] = UNSET
    run_id: Union[Unset, int] = UNSET
    setup_duration: Union[Unset, int] = UNSET
    spark_jar_task: Union[Unset, SparkJarTask] = UNSET
    spark_python_task: Union[Unset, SparkPythonTask] = UNSET
    spark_submit_task: Union[Unset, SparkSubmitTask] = UNSET
    sql_task: Union[Unset, SqlTask] = UNSET
    start_time: Union[Unset, int] = UNSET
    state: Union[Unset, RunState] = UNSET
    task_key: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = Field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        attempt_number = self.attempt_number
        cleanup_duration = self.cleanup_duration
        cluster_instance: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cluster_instance, Unset):
            cluster_instance = self.cluster_instance.to_dict()

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
        end_time = self.end_time
        execution_duration = self.execution_duration
        existing_cluster_id = self.existing_cluster_id
        git_source: Union[Any, Unset]
        if isinstance(self.git_source, Unset):
            git_source = UNSET

        else:
            git_source = self.git_source

        libraries: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.libraries, Unset):
            libraries = []
            for libraries_item_data in self.libraries:
                libraries_item = libraries_item_data.to_dict()

                libraries.append(libraries_item)

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

        run_id = self.run_id
        setup_duration = self.setup_duration
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

        start_time = self.start_time
        state: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.to_dict()

        task_key = self.task_key

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attempt_number is not UNSET:
            field_dict["attempt_number"] = attempt_number
        if cleanup_duration is not UNSET:
            field_dict["cleanup_duration"] = cleanup_duration
        if cluster_instance is not UNSET:
            field_dict["cluster_instance"] = cluster_instance
        if dbt_task is not UNSET:
            field_dict["dbt_task"] = dbt_task
        if depends_on is not UNSET:
            field_dict["depends_on"] = depends_on
        if description is not UNSET:
            field_dict["description"] = description
        if end_time is not UNSET:
            field_dict["end_time"] = end_time
        if execution_duration is not UNSET:
            field_dict["execution_duration"] = execution_duration
        if existing_cluster_id is not UNSET:
            field_dict["existing_cluster_id"] = existing_cluster_id
        if git_source is not UNSET:
            field_dict["git_source"] = git_source
        if libraries is not UNSET:
            field_dict["libraries"] = libraries
        if new_cluster is not UNSET:
            field_dict["new_cluster"] = new_cluster
        if notebook_task is not UNSET:
            field_dict["notebook_task"] = notebook_task
        if pipeline_task is not UNSET:
            field_dict["pipeline_task"] = pipeline_task
        if python_wheel_task is not UNSET:
            field_dict["python_wheel_task"] = python_wheel_task
        if run_id is not UNSET:
            field_dict["run_id"] = run_id
        if setup_duration is not UNSET:
            field_dict["setup_duration"] = setup_duration
        if spark_jar_task is not UNSET:
            field_dict["spark_jar_task"] = spark_jar_task
        if spark_python_task is not UNSET:
            field_dict["spark_python_task"] = spark_python_task
        if spark_submit_task is not UNSET:
            field_dict["spark_submit_task"] = spark_submit_task
        if sql_task is not UNSET:
            field_dict["sql_task"] = sql_task
        if start_time is not UNSET:
            field_dict["start_time"] = start_time
        if state is not UNSET:
            field_dict["state"] = state
        if task_key is not UNSET:
            field_dict["task_key"] = task_key

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        if src_dict is None or src_dict is UNSET:
            return {}
        d = {k: v if v is not None else UNSET for k, v in src_dict.items()}
        attempt_number = d.pop("attempt_number", UNSET)

        cleanup_duration = d.pop("cleanup_duration", UNSET)

        _cluster_instance = d.pop("cluster_instance", UNSET)
        cluster_instance: Union[Unset, ClusterInstance]
        if isinstance(_cluster_instance, Unset):
            cluster_instance = UNSET
        else:
            cluster_instance = ClusterInstance.from_dict(_cluster_instance)

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

        end_time = d.pop("end_time", UNSET)

        execution_duration = d.pop("execution_duration", UNSET)

        existing_cluster_id = d.pop("existing_cluster_id", UNSET)

        def _parse_git_source(data: object) -> Union[Any, Unset]:
            if isinstance(data, Unset):
                return data
            return cast(Union[Any, Unset], data)

        git_source = _parse_git_source(d.pop("git_source", UNSET))

        libraries = []
        _libraries = d.pop("libraries", UNSET)
        for libraries_item_data in _libraries or []:
            libraries_item = Library.from_dict(libraries_item_data)

            libraries.append(libraries_item)

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

        run_id = d.pop("run_id", UNSET)

        setup_duration = d.pop("setup_duration", UNSET)

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

        start_time = d.pop("start_time", UNSET)

        _state = d.pop("state", UNSET)
        state: Union[Unset, RunState]
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = RunState.from_dict(_state)

        task_key = d.pop("task_key", UNSET)

        run_task = cls(
            attempt_number=attempt_number,
            cleanup_duration=cleanup_duration,
            cluster_instance=cluster_instance,
            dbt_task=dbt_task,
            depends_on=depends_on,
            description=description,
            end_time=end_time,
            execution_duration=execution_duration,
            existing_cluster_id=existing_cluster_id,
            git_source=git_source,
            libraries=libraries,
            new_cluster=new_cluster,
            notebook_task=notebook_task,
            pipeline_task=pipeline_task,
            python_wheel_task=python_wheel_task,
            run_id=run_id,
            setup_duration=setup_duration,
            spark_jar_task=spark_jar_task,
            spark_python_task=spark_python_task,
            spark_submit_task=spark_submit_task,
            sql_task=sql_task,
            start_time=start_time,
            state=state,
            task_key=task_key,
        )

        run_task.additional_properties = d
        return run_task

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
