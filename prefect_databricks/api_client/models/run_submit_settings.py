from typing import Any, Dict, List, Type, TypeVar, Union, cast

from pydantic import BaseModel, Field

from ..models.run_submit_task_settings import RunSubmitTaskSettings
from ..types import UNSET, Unset

T = TypeVar("T", bound="RunSubmitSettings")


class RunSubmitSettings(BaseModel):
    """
    Attributes:
        git_source (Union[Any, Unset]): This functionality is in Public Preview.

            An optional specification for a remote repository containing the notebooks used by this job's notebook tasks.
            Example: {'git_branch': 'main', 'git_provider': 'gitHub', 'git_url': 'https://github.com/databricks/databricks-
            cli'}.
        idempotency_token (Union[Unset, str]): An optional token that can be used to guarantee the idempotency of job
            run requests. If a run with the provided token already exists, the request does not create a new run but returns
            the ID of the existing run instead. If a run with the provided token is deleted, an error is returned.

            If you specify the idempotency token, upon failure you can retry until the request succeeds. Databricks
            guarantees that exactly one run is launched with that idempotency token.

            This token must have at most 64 characters.

            For more information, see [How to ensure idempotency for jobs](https://kb.databricks.com/jobs/jobs-
            idempotency.html). Example: 8f018174-4792-40d5-bcbc-3e6a527352c8.
        run_name (Union[Unset, str]): An optional name for the run. The default value is `Untitled`. Example: A
            multitask job run.
        tasks (Union[Unset, List[RunSubmitTaskSettings]]):  Example: [{'depends_on': [], 'description': 'Extracts
            session data from events', 'existing_cluster_id': '0923-164208-meows279', 'libraries': [{'jar':
            'dbfs:/mnt/databricks/Sessionize.jar'}], 'spark_jar_task': {'main_class_name': 'com.databricks.Sessionize',
            'parameters': ['--data', 'dbfs:/path/to/data.json']}, 'task_key': 'Sessionize', 'timeout_seconds': 86400},
            {'depends_on': [], 'description': 'Ingests order data', 'existing_cluster_id': '0923-164208-meows279',
            'libraries': [{'jar': 'dbfs:/mnt/databricks/OrderIngest.jar'}], 'spark_jar_task': {'main_class_name':
            'com.databricks.OrdersIngest', 'parameters': ['--data', 'dbfs:/path/to/order-data.json']}, 'task_key':
            'Orders_Ingest', 'timeout_seconds': 86400}, {'depends_on': [{'task_key': 'Orders_Ingest'}, {'task_key':
            'Sessionize'}], 'description': 'Matches orders with user sessions', 'new_cluster': {'autoscale': {'max_workers':
            16, 'min_workers': 2}, 'aws_attributes': {'availability': 'SPOT', 'zone_id': 'us-west-2a'}, 'node_type_id':
            'i3.xlarge', 'spark_conf': {'spark.speculation': True}, 'spark_version': '7.3.x-scala2.12'}, 'notebook_task':
            {'base_parameters': {'age': '35', 'name': 'John Doe'}, 'notebook_path': '/Users/user.name@databricks.com/Match',
            'source': 'WORKSPACE'}, 'task_key': 'Match', 'timeout_seconds': 86400}].
        timeout_seconds (Union[Unset, int]): An optional timeout applied to each run of this job. The default behavior
            is to have no timeout. Example: 86400.
    """

    git_source: Union[Any, Unset] = UNSET
    idempotency_token: Union[Unset, str] = UNSET
    run_name: Union[Unset, str] = UNSET
    tasks: Union[Unset, List[RunSubmitTaskSettings]] = UNSET
    timeout_seconds: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = Field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        git_source: Union[Any, Unset]
        if isinstance(self.git_source, Unset):
            git_source = UNSET

        else:
            git_source = self.git_source

        idempotency_token = self.idempotency_token
        run_name = self.run_name
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
        if git_source is not UNSET:
            field_dict["git_source"] = git_source
        if idempotency_token is not UNSET:
            field_dict["idempotency_token"] = idempotency_token
        if run_name is not UNSET:
            field_dict["run_name"] = run_name
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

        def _parse_git_source(data: object) -> Union[Any, Unset]:
            if isinstance(data, Unset):
                return data
            return cast(Union[Any, Unset], data)

        git_source = _parse_git_source(d.pop("git_source", UNSET))

        idempotency_token = d.pop("idempotency_token", UNSET)

        run_name = d.pop("run_name", UNSET)

        tasks = []
        _tasks = d.pop("tasks", UNSET)
        for tasks_item_data in _tasks or []:
            tasks_item = RunSubmitTaskSettings.from_dict(tasks_item_data)

            tasks.append(tasks_item)

        timeout_seconds = d.pop("timeout_seconds", UNSET)

        run_submit_settings = cls(
            git_source=git_source,
            idempotency_token=idempotency_token,
            run_name=run_name,
            tasks=tasks,
            timeout_seconds=timeout_seconds,
        )

        run_submit_settings.additional_properties = d
        return run_submit_settings

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
