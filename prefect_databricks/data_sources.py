"""
This is a module for interacting with Databricks REST tasks.
It was auto-generated using prefect-collection-generator so
manually editing this file is not recommended.

OpenAPI spec: queries-dashboards-2.0-aws.yaml
Updated at: 2022-06-29T19:47:27.565607
"""

from typing import TYPE_CHECKING, Any, Dict, List, Union  # noqa

from prefect import task

from prefect_databricks.rest import HTTPMethod, execute_endpoint

if TYPE_CHECKING:
    from prefect_databricks import DatabricksCredentials
    from prefect_databricks.models import data_sources as models


@task
async def get_sql_analytics_data_sources(
    databricks_instance: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Retrieve a full list of SQL warehouses available in this workspace. All fields
    that appear in this API response are enumerated for clarity. However, you
    will only need a SQL warehouse's `id` to create new queries against it.

    Args:
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/preview/sql/data_sources?](
    https://{databricks_instance}/api/2.0/preview/sql/data_sources?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/preview/sql/data_sources"  # noqa
    responses = {}

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result
