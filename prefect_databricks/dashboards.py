"""
This is a module for interacting with Databricks REST tasks.
It was auto-generated using prefect-collection-generator so
manually editing this file is not recommended.

OpenAPI spec: queries-dashboards-2.0-aws.yaml
Updated at: 2022-06-29T19:47:27.559492
"""

from typing import TYPE_CHECKING, Any, Dict, List, Union  # noqa

from prefect import task

from prefect_databricks.rest import HTTPMethod, execute_endpoint

if TYPE_CHECKING:
    from prefect_databricks import DatabricksCredentials
    from prefect_databricks.models import dashboards as models


@task
async def get_sql_analytics_dashboards(
    databricks_instance: str,
    databricks_credentials: "DatabricksCredentials",
    page_size: int = None,
    page: int = None,
    order: str = None,
    q: str = None,
) -> Dict[str, Any]:
    """


    Args:
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.
        page_size:
            Number of dashboards to return per page.
        page:
            Page number to retrieve.
        order:
            Name of dashboard attribute to order by.
        q:
            Full text search term.

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
        params=params,
        responses=responses,
    )
    return result


@task
async def sql_analytics_create_dashboard(
    dashboard_filters_enabled: bool,
    is_draft: bool,
    is_trashed: bool,
    layout: List,
    name: str,
    tags: List,
    widgets: List,
    databricks_instance: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Create a new dashboard object.

    Args:
        dashboard_filters_enabled:
            In the web application, query filters that share a name are coupled to a
            single selection box if this value is true.
        is_draft:
            Draft dashboards only appear in list views for their owners.
        is_trashed:
            Whether the dashboard is trashed. Trashed dashboards won't appear in
            list views.
        layout:
            Currently unused. In a previous version of this API `layout` contained
            information for arranging widgets on the grid.
        name:
            The title of this dashboard which appears in list views and at the top
            of the dashboard page, e.g. `Sales Dashboard`.
        tags:

        widgets:
            An array of widget objects. A complete description of widget objects can
            be found in the response to [Retrieve A Dashboard
            Definition](
            operation/sql-analytics-fetch-dashboard). Databricks does
            not recommend creating new widgets via this API.
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.

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

    data = {
        "dashboard_filters_enabled": dashboard_filters_enabled,
        "is_draft": is_draft,
        "is_trashed": is_trashed,
        "layout": layout,
        "name": name,
        "tags": tags,
        "widgets": widgets,
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.POST,
        responses=responses,
        data=data,
    )
    return result


@task
async def sql_analytics_restore_trashed_dashboard(
    databricks_instance: str,
    dashboard_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    A restored dashboard appears in list views and searches and can be shared.

    Args:
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        dashboard_id:
            Dashboard id used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.

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
async def sql_analytics_trash_dashboard(
    databricks_instance: str,
    dashboard_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Trashed dashboards do not appear in list views or searches and cannot be shared.

    Args:
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        dashboard_id:
            Dashboard id used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.

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
async def sql_analytics_fetch_dashboard(
    databricks_instance: str,
    dashboard_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Returns a JSON representation of a dashboard object, including its visualization
    and query objects.

    Args:
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        dashboard_id:
            Dashboard id used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.

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
