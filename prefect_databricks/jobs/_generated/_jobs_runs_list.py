"""
This is a module containing tasks for interacting with:
Databricks jobs
"""

# This module was auto-generated using prefect-collection-generator so
# manually editing this file is not recommended. If this module
# is outdated, rerun scripts/generate.py.

# OpenAPI spec: jobs-2.1-aws.yaml
# Updated at: 2022-10-06T01:20:50.407495

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
async def jobs_runs_list(
    databricks_credentials: "DatabricksCredentials",
    active_only: bool = False,
    completed_only: bool = False,
    job_id: Optional[int] = None,
    offset: int = 0,
    limit: int = 25,
    run_type: Optional[str] = None,
    expand_tasks: bool = False,
    start_time_from: Optional[int] = None,
    start_time_to: Optional[int] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    List runs in descending order by start time.

    Args:
        databricks_credentials:
            Credentials to use for authentication with Databricks.
        active_only:
            If active_only is `true`, only active runs are included in the results;
            otherwise, lists both active and completed runs. An active
            run is a run in the `PENDING`, `RUNNING`, or `TERMINATING`.
            This field cannot be `true` when completed_only is `true`.
        completed_only:
            If completed_only is `true`, only completed runs are included in the
            results; otherwise, lists both active and completed runs.
            This field cannot be `true` when active_only is `true`.
        job_id:
            The job for which to list runs. If omitted, the Jobs service lists runs
            from all jobs.
        offset:
            The offset of the first run to return, relative to the most recent run.
        limit:
            The number of runs to return. This value must be greater than 0 and less
            than 25\. The default value is 25\. If a request specifies a
            limit of 0, the service instead uses the maximum limit.
        run_type:
            The type of runs to return. For a description of run types, see
            [Run](https://docs.databricks.com/dev-
            tools/api/latest/jobs.html
            operation/JobsRunsGet).
        expand_tasks:
            Whether to include task and cluster details in the response.
        start_time_from:
            Show runs that started _at or after_ this value. The value must be a UTC
            timestamp in milliseconds. Can be combined with
            _start_time_to_ to filter by a time range.
        start_time_to:
            Show runs that started _at or before_ this value. The value must be a
            UTC timestamp in milliseconds. Can be combined with
            _start_time_from_ to filter by a time range.

    Returns:
        Upon success, a dict of the response. </br>- `runs: Optional[List["models.Run"]]`</br>- `has_more: Optional[bool]`</br>

    <h4>API Endpoint:</h4>
    `/2.1/jobs/runs/list`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | List of runs was retrieved successfully. |
    | 400 | The request was malformed. See JSON response for error details. |
    | 401 | The request was unauthorized. |
    | 500 | The request was not handled correctly due to a server error. |
    """  # noqa
    endpoint = "/2.1/jobs/runs/list"  # noqa

    responses = {
        200: "List of runs was retrieved successfully.",  # noqa
        400: "The request was malformed. See JSON response for error details.",  # noqa
        401: "The request was unauthorized.",  # noqa
        500: "The request was not handled correctly due to a server error.",  # noqa
    }

    params = {
        "active_only": active_only,
        "completed_only": completed_only,
        "job_id": job_id,
        "offset": offset,
        "limit": limit,
        "run_type": run_type,
        "expand_tasks": expand_tasks,
        "start_time_from": start_time_from,
        "start_time_to": start_time_to,
    }

    response = await execute_endpoint.fn(
        endpoint,
        databricks_credentials,
        http_method=HTTPMethod.GET,
        params=params,
    )

    contents = _unpack_contents(response, responses)
    return contents
