from typing import Any, Dict, List, Type, TypeVar, Union, cast

from pydantic import BaseModel, Field

from ..models.run_parameters_notebook_params import RunParametersNotebookParams
from ..models.run_parameters_pipeline_params import RunParametersPipelineParams
from ..models.run_parameters_python_named_params import RunParametersPythonNamedParams
from ..models.run_parameters_sql_params import RunParametersSqlParams
from ..types import UNSET, Unset

T = TypeVar("T", bound="JobsRunNowJsonBody")


class JobsRunNowJsonBody(BaseModel):
    """
    Attributes:
        idempotency_token (Union[Unset, str]): An optional token to guarantee the idempotency of job run requests. If a
            run with the provided token already exists, the request does not create a new run but returns the ID of the
            existing run instead. If a run with the provided token is deleted, an error is returned.

            If you specify the idempotency token, upon failure you can retry until the request succeeds. Databricks
            guarantees that exactly one run is launched with that idempotency token.

            This token must have at most 64 characters.

            For more information, see [How to ensure idempotency for jobs](https://kb.databricks.com/jobs/jobs-
            idempotency.html). Example: 8f018174-4792-40d5-bcbc-3e6a527352c8.
        job_id (Union[Unset, int]): The ID of the job to be executed Example: 11223344.
        dbt_commands (Union[Unset, List[str]]): An array of commands to execute for jobs with the dbt task, for example
            `"dbt_commands": ["dbt deps", "dbt seed", "dbt run"]` Example: ['dbt deps', 'dbt seed', 'dbt run'].
        jar_params (Union[Unset, List[str]]): A list of parameters for jobs with Spark JAR tasks, for example
            `"jar_params": ["john doe", "35"]`. The parameters are used to invoke the main function of the main class
            specified in the Spark JAR task. If not specified upon `run-now`, it defaults to an empty list. jar_params
            cannot be specified in conjunction with notebook_params. The JSON representation of this field (for example
            `{"jar_params":["john doe","35"]}`) cannot exceed 10,000 bytes.

            Use [Task parameter variables](https://docs.databricks.com/jobs.html#parameter-variables) to set parameters
            containing information about job runs. Example: ['john', 'doe', '35'].
        notebook_params (Union[Unset, RunParametersNotebookParams]): A map from keys to values for jobs with notebook
            task, for example `"notebook_params": {"name": "john doe", "age": "35"}`. The map is passed to the notebook and
            is accessible through the [dbutils.widgets.get](https://docs.databricks.com/dev-tools/databricks-
            utils.html#dbutils-widgets) function.

            If not specified upon `run-now`, the triggered run uses the job’s base parameters.

            notebook_params cannot be specified in conjunction with jar_params.

            Use [Task parameter variables](https://docs.databricks.com/jobs.html#parameter-variables) to set parameters
            containing information about job runs.

            The JSON representation of this field (for example `{"notebook_params":{"name":"john doe","age":"35"}}`) cannot
            exceed 10,000 bytes. Example: {'age': '35', 'name': 'john doe'}.
        pipeline_params (Union[Unset, RunParametersPipelineParams]):
        python_named_params (Union[Unset, RunParametersPythonNamedParams]): A map from keys to values for jobs with
            Python wheel task, for example `"python_named_params": {"name": "task", "data": "dbfs:/path/to/data.json"}`.
            Example: {'data': 'dbfs:/path/to/data.json', 'name': 'task'}.
        python_params (Union[Unset, List[str]]): A list of parameters for jobs with Python tasks, for example
            `"python_params": ["john doe", "35"]`. The parameters are passed to Python file as command-line parameters. If
            specified upon `run-now`, it would overwrite the parameters specified in job setting. The JSON representation of
            this field (for example `{"python_params":["john doe","35"]}`) cannot exceed 10,000 bytes.

            Use [Task parameter variables](https://docs.databricks.com/jobs.html#parameter-variables) to set parameters
            containing information about job runs.

            Important

            These parameters accept only Latin characters (ASCII character set). Using non-ASCII characters returns an
            error. Examples of invalid, non-ASCII characters are Chinese, Japanese kanjis, and emojis. Example: ['john doe',
            '35'].
        spark_submit_params (Union[Unset, List[str]]): A list of parameters for jobs with spark submit task, for example
            `"spark_submit_params": ["--class", "org.apache.spark.examples.SparkPi"]`. The parameters are passed to spark-
            submit script as command-line parameters. If specified upon `run-now`, it would overwrite the parameters
            specified in job setting. The JSON representation of this field (for example `{"python_params":["john
            doe","35"]}`) cannot exceed 10,000 bytes.

            Use [Task parameter variables](https://docs.databricks.com/jobs.html#parameter-variables) to set parameters
            containing information about job runs.

            Important

            These parameters accept only Latin characters (ASCII character set). Using non-ASCII characters returns an
            error. Examples of invalid, non-ASCII characters are Chinese, Japanese kanjis, and emojis. Example: ['--class',
            'org.apache.spark.examples.SparkPi'].
        sql_params (Union[Unset, RunParametersSqlParams]): A map from keys to values for SQL tasks, for example
            `"sql_params": {"name": "john doe", "age": "35"}`. The SQL alert task does not support custom parameters.
            Example: {'age': '35', 'name': 'john doe'}.
    """

    idempotency_token: Union[Unset, str] = UNSET
    job_id: Union[Unset, int] = UNSET
    dbt_commands: Union[Unset, List[str]] = UNSET
    jar_params: Union[Unset, List[str]] = UNSET
    notebook_params: Union[Unset, RunParametersNotebookParams] = UNSET
    pipeline_params: Union[Unset, RunParametersPipelineParams] = UNSET
    python_named_params: Union[Unset, RunParametersPythonNamedParams] = UNSET
    python_params: Union[Unset, List[str]] = UNSET
    spark_submit_params: Union[Unset, List[str]] = UNSET
    sql_params: Union[Unset, RunParametersSqlParams] = UNSET
    additional_properties: Dict[str, Any] = Field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        idempotency_token = self.idempotency_token
        job_id = self.job_id
        dbt_commands: Union[Unset, List[str]] = UNSET
        if not isinstance(self.dbt_commands, Unset):
            dbt_commands = self.dbt_commands

        jar_params: Union[Unset, List[str]] = UNSET
        if not isinstance(self.jar_params, Unset):
            jar_params = self.jar_params

        notebook_params: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.notebook_params, Unset):
            notebook_params = self.notebook_params.to_dict()

        pipeline_params: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pipeline_params, Unset):
            pipeline_params = self.pipeline_params.to_dict()

        python_named_params: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.python_named_params, Unset):
            python_named_params = self.python_named_params.to_dict()

        python_params: Union[Unset, List[str]] = UNSET
        if not isinstance(self.python_params, Unset):
            python_params = self.python_params

        spark_submit_params: Union[Unset, List[str]] = UNSET
        if not isinstance(self.spark_submit_params, Unset):
            spark_submit_params = self.spark_submit_params

        sql_params: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sql_params, Unset):
            sql_params = self.sql_params.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if idempotency_token is not UNSET:
            field_dict["idempotency_token"] = idempotency_token
        if job_id is not UNSET:
            field_dict["job_id"] = job_id
        if dbt_commands is not UNSET:
            field_dict["dbt_commands"] = dbt_commands
        if jar_params is not UNSET:
            field_dict["jar_params"] = jar_params
        if notebook_params is not UNSET:
            field_dict["notebook_params"] = notebook_params
        if pipeline_params is not UNSET:
            field_dict["pipeline_params"] = pipeline_params
        if python_named_params is not UNSET:
            field_dict["python_named_params"] = python_named_params
        if python_params is not UNSET:
            field_dict["python_params"] = python_params
        if spark_submit_params is not UNSET:
            field_dict["spark_submit_params"] = spark_submit_params
        if sql_params is not UNSET:
            field_dict["sql_params"] = sql_params

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        if src_dict is None or src_dict is UNSET:
            return {}
        d = {k: v if v is not None else UNSET for k, v in src_dict.items()}
        idempotency_token = d.pop("idempotency_token", UNSET)

        job_id = d.pop("job_id", UNSET)

        dbt_commands = cast(List[str], d.pop("dbt_commands", UNSET))

        jar_params = cast(List[str], d.pop("jar_params", UNSET))

        _notebook_params = d.pop("notebook_params", UNSET)
        notebook_params: Union[Unset, RunParametersNotebookParams]
        if isinstance(_notebook_params, Unset):
            notebook_params = UNSET
        else:
            notebook_params = RunParametersNotebookParams.from_dict(_notebook_params)

        _pipeline_params = d.pop("pipeline_params", UNSET)
        pipeline_params: Union[Unset, RunParametersPipelineParams]
        if isinstance(_pipeline_params, Unset):
            pipeline_params = UNSET
        else:
            pipeline_params = RunParametersPipelineParams.from_dict(_pipeline_params)

        _python_named_params = d.pop("python_named_params", UNSET)
        python_named_params: Union[Unset, RunParametersPythonNamedParams]
        if isinstance(_python_named_params, Unset):
            python_named_params = UNSET
        else:
            python_named_params = RunParametersPythonNamedParams.from_dict(
                _python_named_params
            )

        python_params = cast(List[str], d.pop("python_params", UNSET))

        spark_submit_params = cast(List[str], d.pop("spark_submit_params", UNSET))

        _sql_params = d.pop("sql_params", UNSET)
        sql_params: Union[Unset, RunParametersSqlParams]
        if isinstance(_sql_params, Unset):
            sql_params = UNSET
        else:
            sql_params = RunParametersSqlParams.from_dict(_sql_params)

        jobs_run_now_json_body = cls(
            idempotency_token=idempotency_token,
            job_id=job_id,
            dbt_commands=dbt_commands,
            jar_params=jar_params,
            notebook_params=notebook_params,
            pipeline_params=pipeline_params,
            python_named_params=python_named_params,
            python_params=python_params,
            spark_submit_params=spark_submit_params,
            sql_params=sql_params,
        )

        jobs_run_now_json_body.additional_properties = d
        return jobs_run_now_json_body

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
