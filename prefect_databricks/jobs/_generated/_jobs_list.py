"""
This is a module containing tasks for interacting with:
Databricks jobs
"""

# This module was auto-generated using prefect-collection-generator so
# manually editing this file is not recommended. If this module
# is outdated, rerun scripts/generate.py.

# OpenAPI spec: jobs-2.1-aws.yaml
# Updated at: 2022-10-06T00:34:55.823214

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
async def jobs_list(
    databricks_credentials: "DatabricksCredentials",
    limit: int = 20,
    offset: int = 0,
    expand_tasks: bool = False,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Retrieves a list of jobs.

    Args:
        databricks_credentials:
            Credentials to use for authentication with Databricks.
        limit:
            The number of jobs to return. This value must be greater than 0 and less
            or equal to 25. The default value is 20.
        offset:
            The offset of the first job to return, relative to the most recently
            created job.
        expand_tasks:
            Whether to include task and cluster details in the response.

    Returns:
        Upon success, a dict of the response. </br>- `jobs: Optional[List["models.Job"]]`</br>- `has_more: Optional[bool]`</br>

    <h4>API Endpoint:</h4>
    `/2.1/jobs/list`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | List of jobs was retrieved successfully. |
    | 400 | The request was malformed. See JSON response for error details. |
    | 401 | The request was unauthorized. |
    | 500 | The request was not handled correctly due to a server error. |
    """  # noqa
    endpoint = "/2.1/jobs/list"  # noqa

    responses = {
        200: "List of jobs was retrieved successfully.",  # noqa
        400: "The request was malformed. See JSON response for error details.",  # noqa
        401: "The request was unauthorized.",  # noqa
        500: "The request was not handled correctly due to a server error.",  # noqa
    }

    params = {
        "limit": limit,
        "offset": offset,
        "expand_tasks": expand_tasks,
    }

    response = await execute_endpoint.fn(
        endpoint,
        databricks_credentials,
        http_method=HTTPMethod.GET,
        params=params,
    )

    contents = _unpack_contents(response, responses)
    return contents
