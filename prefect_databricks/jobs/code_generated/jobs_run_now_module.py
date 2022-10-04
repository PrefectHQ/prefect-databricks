"""
This is a module containing tasks for interacting with:
Databricks jobs
"""

# This module was auto-generated using prefect-collection-generator so
# manually editing this file is not recommended. If this module
# is outdated, rerun scripts/generate.py.

# OpenAPI spec: jobs-2.1-aws.yaml
# Updated at: 2022-10-04T03:38:50.065231

from typing import Any, Dict, List, Optional, Union  # noqa

from prefect import task

from prefect_databricks import DatabricksCredentials
from prefect_databricks.models import jobs as models  # noqa
from prefect_databricks.rest import HTTPMethod, _unpack_contents, execute_endpoint


@task
async def jobs_run_now(
    databricks_credentials: "DatabricksCredentials",
    job_id: Optional[int] = None,
    idempotency_token: Optional[str] = None,
    jar_params: Optional[List[str]] = None,
    notebook_params: Optional[Dict] = None,
    python_params: Optional[List[str]] = None,
    spark_submit_params: Optional[List[str]] = None,
    python_named_params: Optional[Dict] = None,
    pipeline_params: Optional[str] = None,
    sql_params: Optional[Dict] = None,
    dbt_commands: Optional[List] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Run a job and return the `run_id` of the triggered run.

    Args:
        databricks_credentials:
            Credentials to use for authentication with Databricks.
        job_id:
            The ID of the job to be executed, e.g. `11223344`.
        idempotency_token:
            An optional token to guarantee the idempotency of job run requests. If a
            run with the provided token already exists, the request does
            not create a new run but returns the ID of the existing run
            instead. If a run with the provided token is deleted, an
            error is returned.  If you specify the idempotency token,
            upon failure you can retry until the request succeeds.
            Databricks guarantees that exactly one run is launched with
            that idempotency token.  This token must have at most 64
            characters.  For more information, see [How to ensure
            idempotency for jobs](https://kb.databricks.com/jobs/jobs-
            idempotency.html), e.g.
            `8f018174-4792-40d5-bcbc-3e6a527352c8`.
        jar_params:
            A list of parameters for jobs with Spark JAR tasks, for example
            `'jar_params': ['john doe', '35']`. The parameters are used
            to invoke the main function of the main class specified in
            the Spark JAR task. If not specified upon `run-now`, it
            defaults to an empty list. jar_params cannot be specified in
            conjunction with notebook_params. The JSON representation of
            this field (for example `{'jar_params':['john doe','35']}`)
            cannot exceed 10,000 bytes.  Use [Task parameter
            variables](https://docs.databricks.com/jobs.html
            parameter-variables) to set parameters containing
            information about job runs, e.g.
            ```
            ["john", "doe", "35"]
            ```
        notebook_params:
            A map from keys to values for jobs with notebook task, for example
            `'notebook_params': {'name': 'john doe', 'age': '35'}`. The
            map is passed to the notebook and is accessible through the
            [dbutils.widgets.get](https://docs.databricks.com/dev-
            tools/databricks-utils.html
            dbutils-widgets) function.  If not specified upon `run-now`,
            the triggered run uses the job’s base parameters.
            notebook_params cannot be specified in conjunction with
            jar_params.  Use [Task parameter
            variables](https://docs.databricks.com/jobs.html
            parameter-variables) to set parameters containing
            information about job runs.  The JSON representation of this
            field (for example `{'notebook_params':{'name':'john
            doe','age':'35'}}`) cannot exceed 10,000 bytes, e.g.
            ```
            {"name": "john doe", "age": "35"}
            ```
        python_params:
            A list of parameters for jobs with Python tasks, for example
            `'python_params': ['john doe', '35']`. The parameters are
            passed to Python file as command-line parameters. If
            specified upon `run-now`, it would overwrite the parameters
            specified in job setting. The JSON representation of this
            field (for example `{'python_params':['john doe','35']}`)
            cannot exceed 10,000 bytes.  Use [Task parameter
            variables](https://docs.databricks.com/jobs.html
            parameter-variables) to set parameters containing
            information about job runs.  Important  These parameters
            accept only Latin characters (ASCII character set). Using
            non-ASCII characters returns an error. Examples of invalid,
            non-ASCII characters are Chinese, Japanese kanjis, and
            emojis, e.g.
            ```
            ["john doe", "35"]
            ```
        spark_submit_params:
            A list of parameters for jobs with spark submit task, for example
            `'spark_submit_params': ['--class',
            'org.apache.spark.examples.SparkPi']`. The parameters are
            passed to spark-submit script as command-line parameters. If
            specified upon `run-now`, it would overwrite the parameters
            specified in job setting. The JSON representation of this
            field (for example `{'python_params':['john doe','35']}`)
            cannot exceed 10,000 bytes.  Use [Task parameter
            variables](https://docs.databricks.com/jobs.html
            parameter-variables) to set parameters containing
            information about job runs.  Important  These parameters
            accept only Latin characters (ASCII character set). Using
            non-ASCII characters returns an error. Examples of invalid,
            non-ASCII characters are Chinese, Japanese kanjis, and
            emojis, e.g.
            ```
            ["--class", "org.apache.spark.examples.SparkPi"]
            ```
        python_named_params:
            A map from keys to values for jobs with Python wheel task, for example
            `'python_named_params': {'name': 'task', 'data':
            'dbfs:/path/to/data.json'}`, e.g.
            ```
            {"name": "task", "data": "dbfs:/path/to/data.json"}
            ```
        pipeline_params:

        sql_params:
            A map from keys to values for SQL tasks, for example `'sql_params':
            {'name': 'john doe', 'age': '35'}`. The SQL alert task does
            not support custom parameters, e.g.
            ```
            {"name": "john doe", "age": "35"}
            ```
        dbt_commands:
            An array of commands to execute for jobs with the dbt task, for example
            `'dbt_commands': ['dbt deps', 'dbt seed', 'dbt run']`, e.g.
            ```
            ["dbt deps", "dbt seed", "dbt run"]
            ```

    Returns:
        Upon success, a dict of the response. </br>- `run_id: Optional[int]`</br>- `number_in_job: Optional[int]`</br>

    <h4>API Endpoint:</h4>
    `/2.1/jobs/run-now`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Run was started successfully. |
    | 400 | The request was malformed. See JSON response for error details. |
    | 401 | The request was unauthorized. |
    | 500 | The request was not handled correctly due to a server error. |
    """  # noqa
    endpoint = "/2.1/jobs/run-now"  # noqa

    responses = {
        200: "Run was started successfully.",  # noqa
        400: "The request was malformed. See JSON response for error details.",  # noqa
        401: "The request was unauthorized.",  # noqa
        500: "The request was not handled correctly due to a server error.",  # noqa
    }

    json_payload = {
        "job_id": job_id,
        "idempotency_token": idempotency_token,
        "jar_params": jar_params,
        "notebook_params": notebook_params,
        "python_params": python_params,
        "spark_submit_params": spark_submit_params,
        "python_named_params": python_named_params,
        "pipeline_params": pipeline_params,
        "sql_params": sql_params,
        "dbt_commands": dbt_commands,
    }

    response = await execute_endpoint.fn(
        endpoint,
        databricks_credentials,
        http_method=HTTPMethod.POST,
        json=json_payload,
    )

    contents = _unpack_contents(response, responses)
    return contents
