from typing import Any, Dict, List, Type, TypeVar, Union, cast

from pydantic import BaseModel, Field

from ..models.cron_schedule import CronSchedule
from ..models.job_cluster import JobCluster
from ..models.job_email_notifications import JobEmailNotifications
from ..models.job_settings_format import JobSettingsFormat
from ..models.job_settings_tags import JobSettingsTags
from ..models.job_task_settings import JobTaskSettings
from ..types import UNSET, Unset

T = TypeVar("T", bound="JobSettings")


class JobSettings(BaseModel):
    """
    Attributes:
        email_notifications (Union[Unset, JobEmailNotifications]):
        format_ (Union[Unset, JobSettingsFormat]): Used to tell what is the format of the job. This field is ignored in
            Create/Update/Reset calls. When using the Jobs API 2.1 this value is always set to `"MULTI_TASK"`. Example:
            MULTI_TASK.
        git_source (Union[Any, Unset]): This functionality is in Public Preview.

            An optional specification for a remote repository containing the notebooks used by this job's notebook tasks.
            Example: {'git_branch': 'main', 'git_provider': 'gitHub', 'git_url': 'https://github.com/databricks/databricks-
            cli'}.
        job_clusters (Union[Unset, List[JobCluster]]): A list of job cluster specifications that can be shared and
            reused by tasks of this job. Libraries cannot be declared in a shared job cluster. You must declare dependent
            libraries in task settings. Example: [{'job_cluster_key': 'auto_scaling_cluster', 'new_cluster': {'autoscale':
            {'max_workers': 16, 'min_workers': 2}, 'aws_attributes': {'availability': 'SPOT', 'zone_id': 'us-west-2a'},
            'node_type_id': 'i3.xlarge', 'spark_conf': {'spark.speculation': True}, 'spark_version': '7.3.x-scala2.12'}}].
        max_concurrent_runs (Union[Unset, int]): An optional maximum allowed number of concurrent runs of the job.

            Set this value if you want to be able to execute multiple runs of the same job concurrently. This is useful for
            example if you trigger your job on a frequent schedule and want to allow consecutive runs to overlap with each
            other, or if you want to trigger multiple runs which differ by their input parameters.

            This setting affects only new runs. For example, suppose the job’s concurrency is 4 and there are 4 concurrent
            active runs. Then setting the concurrency to 3 won’t kill any of the active runs. However, from then on, new
            runs are skipped unless there are fewer than 3 active runs.

            This value cannot exceed 1000\. Setting this value to 0 causes all new runs to be skipped. The default behavior
            is to allow only 1 concurrent run. Example: 10.
        name (Union[Unset, str]): An optional name for the job. Default: 'Untitled'. Example: A multitask job.
        schedule (Union[Unset, CronSchedule]):
        tags (Union[Unset, JobSettingsTags]): A map of tags associated with the job. These are forwarded to the cluster
            as cluster tags for jobs clusters, and are subject to the same limitations as cluster tags. A maximum of 25 tags
            can be added to the job. Example: {'cost-center': 'engineering', 'team': 'jobs'}.
        tasks (Union[Unset, List[JobTaskSettings]]): A list of task specifications to be executed by this job. Example:
            [{'depends_on': [], 'description': 'Extracts session data from events', 'existing_cluster_id':
            '0923-164208-meows279', 'libraries': [{'jar': 'dbfs:/mnt/databricks/Sessionize.jar'}], 'max_retries': 3,
            'min_retry_interval_millis': 2000, 'retry_on_timeout': False, 'spark_jar_task': {'main_class_name':
            'com.databricks.Sessionize', 'parameters': ['--data', 'dbfs:/path/to/data.json']}, 'task_key': 'Sessionize',
            'timeout_seconds': 86400}, {'depends_on': [], 'description': 'Ingests order data', 'job_cluster_key':
            'auto_scaling_cluster', 'libraries': [{'jar': 'dbfs:/mnt/databricks/OrderIngest.jar'}], 'max_retries': 3,
            'min_retry_interval_millis': 2000, 'retry_on_timeout': False, 'spark_jar_task': {'main_class_name':
            'com.databricks.OrdersIngest', 'parameters': ['--data', 'dbfs:/path/to/order-data.json']}, 'task_key':
            'Orders_Ingest', 'timeout_seconds': 86400}, {'depends_on': [{'task_key': 'Orders_Ingest'}, {'task_key':
            'Sessionize'}], 'description': 'Matches orders with user sessions', 'max_retries': 3,
            'min_retry_interval_millis': 2000, 'new_cluster': {'autoscale': {'max_workers': 16, 'min_workers': 2},
            'aws_attributes': {'availability': 'SPOT', 'zone_id': 'us-west-2a'}, 'node_type_id': 'i3.xlarge', 'spark_conf':
            {'spark.speculation': True}, 'spark_version': '7.3.x-scala2.12'}, 'notebook_task': {'base_parameters': {'age':
            '35', 'name': 'John Doe'}, 'notebook_path': '/Users/user.name@databricks.com/Match', 'source': 'WORKSPACE'},
            'retry_on_timeout': False, 'task_key': 'Match', 'timeout_seconds': 86400}].
        timeout_seconds (Union[Unset, int]): An optional timeout applied to each run of this job. The default behavior
            is to have no timeout. Example: 86400.
    """

    email_notifications: Union[Unset, JobEmailNotifications] = UNSET
    format_: Union[Unset, JobSettingsFormat] = UNSET
    git_source: Union[Any, Unset] = UNSET
    job_clusters: Union[Unset, List[JobCluster]] = UNSET
    max_concurrent_runs: Union[Unset, int] = UNSET
    name: Union[Unset, str] = "Untitled"
    schedule: Union[Unset, CronSchedule] = UNSET
    tags: Union[Unset, JobSettingsTags] = UNSET
    tasks: Union[Unset, List[JobTaskSettings]] = UNSET
    timeout_seconds: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = Field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        email_notifications: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.email_notifications, Unset):
            email_notifications = self.email_notifications.to_dict()

        format_: Union[Unset, str] = UNSET
        if not isinstance(self.format_, Unset):
            format_ = self.format_.value

        git_source: Union[Any, Unset]
        if isinstance(self.git_source, Unset):
            git_source = UNSET

        else:
            git_source = self.git_source

        job_clusters: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.job_clusters, Unset):
            job_clusters = []
            for job_clusters_item_data in self.job_clusters:
                job_clusters_item = job_clusters_item_data.to_dict()

                job_clusters.append(job_clusters_item)

        max_concurrent_runs = self.max_concurrent_runs
        name = self.name
        schedule: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.schedule, Unset):
            schedule = self.schedule.to_dict()

        tags: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags.to_dict()

        tasks: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tasks, Unset):
            tasks = []
            for tasks_item_data in self.tasks:
                tasks_item = tasks_item_data.to_dict()

                tasks.append(tasks_item)

        timeout_seconds = self.timeout_seconds

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if email_notifications is not UNSET:
            field_dict["email_notifications"] = email_notifications
        if format_ is not UNSET:
            field_dict["format"] = format_
        if git_source is not UNSET:
            field_dict["git_source"] = git_source
        if job_clusters is not UNSET:
            field_dict["job_clusters"] = job_clusters
        if max_concurrent_runs is not UNSET:
            field_dict["max_concurrent_runs"] = max_concurrent_runs
        if name is not UNSET:
            field_dict["name"] = name
        if schedule is not UNSET:
            field_dict["schedule"] = schedule
        if tags is not UNSET:
            field_dict["tags"] = tags
        if tasks is not UNSET:
            field_dict["tasks"] = tasks
        if timeout_seconds is not UNSET:
            field_dict["timeout_seconds"] = timeout_seconds

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        if src_dict is None or src_dict is UNSET:
            return {}
        d = {k: v if v is not None else UNSET for k, v in src_dict.items()}
        _email_notifications = d.pop("email_notifications", UNSET)
        email_notifications: Union[Unset, JobEmailNotifications]
        if isinstance(_email_notifications, Unset):
            email_notifications = UNSET
        else:
            email_notifications = JobEmailNotifications.from_dict(_email_notifications)

        _format_ = d.pop("format", UNSET)
        format_: Union[Unset, JobSettingsFormat]
        if isinstance(_format_, Unset):
            format_ = UNSET
        else:
            format_ = JobSettingsFormat(_format_)

        def _parse_git_source(data: object) -> Union[Any, Unset]:
            if isinstance(data, Unset):
                return data
            return cast(Union[Any, Unset], data)

        git_source = _parse_git_source(d.pop("git_source", UNSET))

        job_clusters = []
        _job_clusters = d.pop("job_clusters", UNSET)
        for job_clusters_item_data in _job_clusters or []:
            job_clusters_item = JobCluster.from_dict(job_clusters_item_data)

            job_clusters.append(job_clusters_item)

        max_concurrent_runs = d.pop("max_concurrent_runs", UNSET)

        name = d.pop("name", UNSET)

        _schedule = d.pop("schedule", UNSET)
        schedule: Union[Unset, CronSchedule]
        if isinstance(_schedule, Unset):
            schedule = UNSET
        else:
            schedule = CronSchedule.from_dict(_schedule)

        _tags = d.pop("tags", UNSET)
        tags: Union[Unset, JobSettingsTags]
        if isinstance(_tags, Unset):
            tags = UNSET
        else:
            tags = JobSettingsTags.from_dict(_tags)

        tasks = []
        _tasks = d.pop("tasks", UNSET)
        for tasks_item_data in _tasks or []:
            tasks_item = JobTaskSettings.from_dict(tasks_item_data)

            tasks.append(tasks_item)

        timeout_seconds = d.pop("timeout_seconds", UNSET)

        job_settings = cls(
            email_notifications=email_notifications,
            format_=format_,
            git_source=git_source,
            job_clusters=job_clusters,
            max_concurrent_runs=max_concurrent_runs,
            name=name,
            schedule=schedule,
            tags=tags,
            tasks=tasks,
            timeout_seconds=timeout_seconds,
        )

        job_settings.additional_properties = d
        return job_settings

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
