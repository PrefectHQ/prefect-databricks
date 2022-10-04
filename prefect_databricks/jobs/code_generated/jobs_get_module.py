"""
This is a module containing tasks for interacting with:
Databricks jobs
"""

# This module was auto-generated using prefect-collection-generator so
# manually editing this file is not recommended. If this module
# is outdated, rerun scripts/generate.py.

# OpenAPI spec: jobs-2.1-aws.yaml
# Updated at: 2022-10-04T03:38:50.049139

from typing import Any, Dict, List, Optional, Union  # noqa

from prefect import task

from prefect_databricks import DatabricksCredentials
from prefect_databricks.models import jobs as models  # noqa
from prefect_databricks.rest import HTTPMethod, _unpack_contents, execute_endpoint


@task
async def jobs_get(
    job_id: int,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:  # pragma: no cover
    """
    Retrieves the details for a single job.

    Args:
        job_id:
            The canonical identifier of the job to retrieve information about. This
            field is required.
        databricks_credentials:
            Credentials to use for authentication with Databricks.

    Returns:
        Upon success, a dict of the response. </br>- `job_id: Optional[int]`</br>- `creator_user_name: Optional[str]`</br>- `run_as_user_name: Optional[str]`</br>- `settings: "models.JobSettings"`</br>- `created_time: Optional[int]`</br>

    <h4>API Endpoint:</h4>
    `/2.1/jobs/get`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Job was retrieved successfully. |
    | 400 | The request was malformed. See JSON response for error details. |
    | 401 | The request was unauthorized. |
    | 500 | The request was not handled correctly due to a server error. |
    """  # noqa
    endpoint = "/2.1/jobs/get"  # noqa

    responses = {
        200: "Job was retrieved successfully.",  # noqa
        400: "The request was malformed. See JSON response for error details.",  # noqa
        401: "The request was unauthorized.",  # noqa
        500: "The request was not handled correctly due to a server error.",  # noqa
    }

    params = {
        "job_id": job_id,
    }

    response = await execute_endpoint.fn(
        endpoint,
        databricks_credentials,
        http_method=HTTPMethod.GET,
        params=params,
    )

    contents = _unpack_contents(response, responses)
    return contents
