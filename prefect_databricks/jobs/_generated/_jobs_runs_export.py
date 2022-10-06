"""
This is a module containing tasks for interacting with:
Databricks jobs
"""

# This module was auto-generated using prefect-collection-generator so
# manually editing this file is not recommended. If this module
# is outdated, rerun scripts/generate.py.

# OpenAPI spec: jobs-2.1-aws.yaml
# Updated at: 2022-10-06T00:18:43.707671

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
async def jobs_runs_export(
    run_id: int,
    databricks_credentials: "DatabricksCredentials",
    views_to_export: Optional["models.ViewsToExport"] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Export and retrieve the job run task.

    Args:
        run_id:
            The canonical identifier for the run. This field is required.
        databricks_credentials:
            Credentials to use for authentication with Databricks.
        views_to_export:
            Which views to export (CODE, DASHBOARDS, or ALL). Defaults to CODE.

    Returns:
        Upon success, a dict of the response. </br>- `views: Optional[List["models.ViewItem"]]`</br>

    <h4>API Endpoint:</h4>
    `/2.0/jobs/runs/export`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Run was exported successfully. |
    | 400 | The request was malformed. See JSON response for error details. |
    | 401 | The request was unauthorized. |
    | 500 | The request was not handled correctly due to a server error. |
    """  # noqa
    endpoint = "/2.0/jobs/runs/export"  # noqa

    responses = {
        200: "Run was exported successfully.",  # noqa
        400: "The request was malformed. See JSON response for error details.",  # noqa
        401: "The request was unauthorized.",  # noqa
        500: "The request was not handled correctly due to a server error.",  # noqa
    }

    params = {
        "run_id": run_id,
        "views_to_export": views_to_export,
    }

    response = await execute_endpoint.fn(
        endpoint,
        databricks_credentials,
        http_method=HTTPMethod.GET,
        params=params,
    )

    contents = _unpack_contents(response, responses)
    return contents
