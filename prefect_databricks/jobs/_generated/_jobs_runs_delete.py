"""
This is a module containing tasks for interacting with:
Databricks jobs
"""

# This module was auto-generated using prefect-collection-generator so
# manually editing this file is not recommended. If this module
# is outdated, rerun scripts/generate.py.

# OpenAPI spec: jobs-2.1-aws.yaml
# Updated at: 2022-10-06T01:13:18.942076

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
async def jobs_runs_delete(
    databricks_credentials: "DatabricksCredentials",
    run_id: Optional[int] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Deletes a non-active run. Returns an error if the run is active.

    Args:
        databricks_credentials:
            Credentials to use for authentication with Databricks.
        run_id:
            The canonical identifier of the run for which to retrieve the metadata,
            e.g. `455644833`.

    Returns:
        Upon success, an empty dict.

    <h4>API Endpoint:</h4>
    `/2.1/jobs/runs/delete`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Run was deleted successfully. |
    | 400 | The request was malformed. See JSON response for error details. |
    | 401 | The request was unauthorized. |
    | 500 | The request was not handled correctly due to a server error. |
    """  # noqa
    endpoint = "/2.1/jobs/runs/delete"  # noqa

    responses = {
        200: "Run was deleted successfully.",  # noqa
        400: "The request was malformed. See JSON response for error details.",  # noqa
        401: "The request was unauthorized.",  # noqa
        500: "The request was not handled correctly due to a server error.",  # noqa
    }

    json_payload = {
        "run_id": run_id,
    }

    response = await execute_endpoint.fn(
        endpoint,
        databricks_credentials,
        http_method=HTTPMethod.POST,
        json=json_payload,
    )

    contents = _unpack_contents(response, responses)
    return contents
