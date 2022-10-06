"""
This is a module containing tasks for interacting with:
Databricks jobs
"""

# This module was auto-generated using prefect-collection-generator so
# manually editing this file is not recommended. If this module
# is outdated, rerun scripts/generate.py.

# OpenAPI spec: jobs-2.1-aws.yaml
# Updated at: 2022-10-06T00:18:43.812494

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
async def jobs_runs_get(
    run_id: int,
    databricks_credentials: "DatabricksCredentials",
    include_history: Optional[bool] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Retrieve the metadata of a run.

    Args:
        run_id:
            The canonical identifier of the run for which to retrieve the metadata.
            This field is required.
        databricks_credentials:
            Credentials to use for authentication with Databricks.
        include_history:
            Whether to include the repair history in the response.

    Returns:
        Upon success, a dict of the response. </br>- `job_id: Optional[int]`</br>- `run_id: Optional[int]`</br>- `number_in_job: Optional[int]`</br>- `creator_user_name: Optional[str]`</br>- `original_attempt_run_id: Optional[int]`</br>- `state: "models.RunState"`</br>- `schedule: "models.CronSchedule"`</br>- `tasks: Optional[List["models.RunTask"]]`</br>- `job_clusters: Optional[List["models.JobCluster"]]`</br>- `cluster_spec: "models.ClusterSpec"`</br>- `cluster_instance: "models.ClusterInstance"`</br>- `git_source: "models.GitSource"`</br>- `overriding_parameters: "models.RunParameters"`</br>- `start_time: Optional[int]`</br>- `setup_duration: Optional[int]`</br>- `execution_duration: Optional[int]`</br>- `cleanup_duration: Optional[int]`</br>- `end_time: Optional[int]`</br>- `trigger: "models.TriggerType"`</br>- `run_name: str`</br>- `run_page_url: Optional[str]`</br>- `run_type: "models.RunType"`</br>- `attempt_number: Optional[int]`</br>- `repair_history: Optional[List["models.RepairHistoryItem"]]`</br>

    <h4>API Endpoint:</h4>
    `/2.1/jobs/runs/get`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Run was retrieved successfully. |
    | 400 | The request was malformed. See JSON response for error details. |
    | 401 | The request was unauthorized. |
    | 500 | The request was not handled correctly due to a server error. |
    """  # noqa
    endpoint = "/2.1/jobs/runs/get"  # noqa

    responses = {
        200: "Run was retrieved successfully.",  # noqa
        400: "The request was malformed. See JSON response for error details.",  # noqa
        401: "The request was unauthorized.",  # noqa
        500: "The request was not handled correctly due to a server error.",  # noqa
    }

    params = {
        "run_id": run_id,
        "include_history": include_history,
    }

    response = await execute_endpoint.fn(
        endpoint,
        databricks_credentials,
        http_method=HTTPMethod.GET,
        params=params,
    )

    contents = _unpack_contents(response, responses)
    return contents
