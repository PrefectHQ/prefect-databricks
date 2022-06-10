"""
This is a module for interacting with Databricks REST tasks.
It was auto-generated using prefect-collection-generator so
manually editing this file is not recommended.
"""

from typing import TYPE_CHECKING, Any, Dict

from prefect import task

from prefect_databricks.rest import HTTPMethod, execute_endpoint

if TYPE_CHECKING:
    from prefect_databricks import DatabricksCredentials


@task
async def get_2dot0_jobs_runs_export(
    databricks_instance: str,
    run_id: str,
    views_to_export: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Export and retrieve the job run task.

    Args:
        databricks_instance: Databricks instance used in formatting the endpoint URL.
        run_id: The canonical identifier for the run. This field is required.
        views_to_export: Which views to export (CODE, DASHBOARDS, or ALL). Defaults to CODE.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://{databricks_instance}/api//2.0/jobs/runs/export?&run_id=%s&views_to_export=%s](
    https://{databricks_instance}/api//2.0/jobs/runs/export?&run_id=%s&views_to_export=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Run was exported successfully. |
    """  # noqa
    url = f"https://{databricks_instance}/api//2.0/jobs/runs/export"  # noqa
    responses = {
        200: "Run was exported successfully.",
    }

    params = {
        "run_id": run_id,
        "views_to_export": views_to_export,
    }
    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
        **params,
    )
    return result
