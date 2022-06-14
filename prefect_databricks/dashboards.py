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
async def get_dashboards(
    databricks_instance: str,
    databricks_credentials: "DatabricksCredentials",
    page_size: str = None,
    page: str = None,
    order: str = None,
    q: str = None,
) -> Dict[str, Any]:
    """


    Args:
        databricks_instance: Databricks instance used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.
        page_size: Number of dashboards to return per page.
        page: Page number to retrieve.
        order: Name of dashboard attribute to order by.
        q: Full text search term.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/preview/sql/dashboards?&page_size=%s&page=%s&order=%s&q=%s](
    https://{databricks_instance}/api/2.0/preview/sql/dashboards?&page_size=%s&page=%s&order=%s&q=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/preview/sql/dashboards"  # noqa
    responses = {}

    params = {
        "page_size": page_size,
        "page": page,
        "order": order,
        "q": q,
    }
    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
        **params,
    )
    return result


@task
async def post_dashboards(
    databricks_instance: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Create a new dashboard object.

    Args:
        databricks_instance: Databricks instance used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/preview/sql/dashboards?](
    https://{databricks_instance}/api/2.0/preview/sql/dashboards?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | A dashboard object was successfully created. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/preview/sql/dashboards"  # noqa
    responses = {
        200: "A dashboard object was successfully created.",  # noqa
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.POST,
        responses=responses,
    )
    return result


@task
async def post_dashboards_trash_dashboard_id(
    databricks_instance: str,
    dashboard_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    A restored dashboard appears in list views and searches and can be shared.

    Args:
        databricks_instance: Databricks instance used in formatting the endpoint URL.
        dashboard_id: Dashboard id used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/preview/sql/dashboards/trash/{dashboard_id}?](
    https://{databricks_instance}/api/2.0/preview/sql/dashboards/trash/{dashboard_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Dashboard restored successfully. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/preview/sql/dashboards/trash/{dashboard_id}"  # noqa
    responses = {
        200: "Dashboard restored successfully.",  # noqa
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.POST,
        responses=responses,
    )
    return result


@task
async def delete_dashboards_dashboard_id(
    databricks_instance: str,
    dashboard_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Trashed dashboards do not appear in list views or searches and cannot be shared.

    Args:
        databricks_instance: Databricks instance used in formatting the endpoint URL.
        dashboard_id: Dashboard id used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/preview/sql/dashboards/{dashboard_id}?](
    https://{databricks_instance}/api/2.0/preview/sql/dashboards/{dashboard_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Dashboard successfully moved to trash. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/preview/sql/dashboards/{dashboard_id}"  # noqa
    responses = {
        200: "Dashboard successfully moved to trash.",  # noqa
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.DELETE,
        responses=responses,
    )
    return result


@task
async def get_dashboards_dashboard_id(
    databricks_instance: str,
    dashboard_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Returns a JSON representation of a dashboard object, including its visualization
    and query objects.

    Args:
        databricks_instance: Databricks instance used in formatting the endpoint URL.
        dashboard_id: Dashboard id used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/preview/sql/dashboards/{dashboard_id}?](
    https://{databricks_instance}/api/2.0/preview/sql/dashboards/{dashboard_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Dashboard fetched successfully. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/preview/sql/dashboards/{dashboard_id}"  # noqa
    responses = {
        200: "Dashboard fetched successfully.",  # noqa
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result
