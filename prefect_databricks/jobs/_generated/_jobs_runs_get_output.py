"""
This is a module containing tasks for interacting with:
Databricks jobs
"""

# This module was auto-generated using prefect-collection-generator so
# manually editing this file is not recommended. If this module
# is outdated, rerun scripts/generate.py.

# OpenAPI spec: jobs-2.1-aws.yaml
# Updated at: 2022-10-06T01:20:50.406717

from typing import Any, Dict, List, Optional, Union  # noqa

from prefect import task

from prefect_databricks import DatabricksCredentials
from prefect_databricks.models import jobs as models  # noqa
from prefect_databricks.rest._generated import (
    HTTPMethod,
    _unpack_contents,
    execute_endpoint,
)


@task
async def jobs_runs_get_output(
    run_id: int,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Retrieve the output and metadata of a single task run. When a notebook task
    returns a value through the dbutils.notebook.exit() call, you can use this
    endpoint to retrieve that value. Databricks restricts this API to return the
    first 5 MB of the output. To return a larger result, you can store job
    results in a cloud storage service. This endpoint validates that the run_id
    parameter is valid and returns an HTTP status code 400 if the run_id
    parameter is invalid. Runs are automatically removed after 60 days. If you
    to want to reference them beyond 60 days, you must save old run results
    before they expire. To export using the UI, see Export job run results. To
    export using the Jobs API, see Runs export.

    Args:
        run_id:
            The canonical identifier for the run. This field is required.
        databricks_credentials:
            Credentials to use for authentication with Databricks.

    Returns:
        Upon success, a dict of the response. </br>- `notebook_output: "models.NotebookOutput"`</br>- `sql_output: "models.SqlOutput"`</br>- `dbt_output: "models.DbtOutput"`</br>- `logs: Optional[str]`</br>- `logs_truncated: Optional[bool]`</br>- `error: Optional[str]`</br>- `error_trace: Optional[str]`</br>- `metadata: "models.Run"`</br>

    <h4>API Endpoint:</h4>
    `/2.1/jobs/runs/get-output`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Run output was retrieved successfully. |
    | 400 | A job run with multiple tasks was provided. |
    | 401 | The request was unauthorized. |
    | 500 | The request was not handled correctly due to a server error. |
    """  # noqa
    endpoint = "/2.1/jobs/runs/get-output"  # noqa

    responses = {
        200: "Run output was retrieved successfully.",  # noqa
        400: "A job run with multiple tasks was provided.",  # noqa
        401: "The request was unauthorized.",  # noqa
        500: "The request was not handled correctly due to a server error.",  # noqa
    }

    params = {
        "run_id": run_id,
    }

    response = await execute_endpoint.fn(
        endpoint,
        databricks_credentials,
        http_method=HTTPMethod.GET,
        params=params,
    )

    contents = _unpack_contents(response, responses)
    return contents
