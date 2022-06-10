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
async def get_queries(
    databricks_instance: str,
    databricks_credentials: "DatabricksCredentials",
    page_size: str = None,
    page: str = None,
    order: str = None,
    q: str = None,
) -> Dict[str, Any]:
    """
    Optionally this list can be filtered by a search term.

    Args:
        databricks_instance: Databricks instance used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.
        page_size: Number of queries to return per page.
        page: Page number to retrieve.
        order: Name of query attribute to order by. Default sort order is ascending.
            Append a dash (`-`) to order descending instead.
            - `name`: The name of the query.
            - `created_at`: The timestamp the query was created.
            - `schedule`: The refresh interval for each query. For
            example: "Every 5 Hours" or "Every 5 Minutes". "Never" is
            treated as the highest value for sorting.
            - `runtime`: The time it took to run this query. This will
            be blank for parameterized queries. A blank value is treated
            as the highest value for sorting.
            - `executed_at`: The timestamp when the query was last run.
            - `created_by`: The user name of the user that created the
            query.
        q: Full text search term.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://{databricks_instance}/api/2.0/preview/sql/queries?&page_size=%s&page=%s&order=%s&q=%s](
    https://{databricks_instance}/api/2.0/preview/sql/queries?&page_size=%s&page=%s&order=%s&q=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/preview/sql/queries"  # noqa
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
async def post_queries(
    databricks_instance: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Queries created with this endpoint belong to the authenticated user making the
    request.
    **Note**: You cannot add a visualization until you create the query.

    Args:
        databricks_instance: Databricks instance used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://{databricks_instance}/api/2.0/preview/sql/queries?](
    https://{databricks_instance}/api/2.0/preview/sql/queries?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Query created successfully. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/preview/sql/queries"  # noqa
    responses = {
        200: "Query created successfully.",
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.POST,
        responses=responses,
    )
    return result


@task
async def post_queries_trash_query_id(
    databricks_instance: str,
    query_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    A restored query appears in list views and searches. You can use restored
    queries for alerts.

    Args:
        databricks_instance: Databricks instance used in formatting the endpoint URL.
        query_id: Query id used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://{databricks_instance}/api/2.0/preview/sql/queries/trash/{query_id}?](
    https://{databricks_instance}/api/2.0/preview/sql/queries/trash/{query_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Query restored successfully. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/preview/sql/queries/trash/{query_id}"  # noqa
    responses = {
        200: "Query restored successfully.",
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.POST,
        responses=responses,
    )
    return result


@task
async def delete_queries_query_id(
    databricks_instance: str,
    query_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Trashed queries immediately disappear from searches and list views and cannot be
    used for alerts. The trash is deleted after 30 days.

    Args:
        databricks_instance: Databricks instance used in formatting the endpoint URL.
        query_id: Query id used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://{databricks_instance}/api/2.0/preview/sql/queries/{query_id}?](
    https://{databricks_instance}/api/2.0/preview/sql/queries/{query_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Query moved to trash. |
    """  # noqa
    url = (
        f"https://{databricks_instance}/api/2.0/preview/sql/queries/{query_id}"  # noqa
    )
    responses = {
        200: "Query moved to trash.",
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.DELETE,
        responses=responses,
    )
    return result


@task
async def get_queries_query_id(
    databricks_instance: str,
    query_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Retrieve a query object definition along with contextual permissions information
    about the currently authenticated user.

    Args:
        databricks_instance: Databricks instance used in formatting the endpoint URL.
        query_id: Query id used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://{databricks_instance}/api/2.0/preview/sql/queries/{query_id}?](
    https://{databricks_instance}/api/2.0/preview/sql/queries/{query_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Query fetched successfully. |
    """  # noqa
    url = (
        f"https://{databricks_instance}/api/2.0/preview/sql/queries/{query_id}"  # noqa
    )
    responses = {
        200: "Query fetched successfully.",
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result


@task
async def post_queries_query_id(
    databricks_instance: str,
    query_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Modify this query definition.  **Note**: You cannot undo this operation.

    Args:
        databricks_instance: Databricks instance used in formatting the endpoint URL.
        query_id: Query id used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://{databricks_instance}/api/2.0/preview/sql/queries/{query_id}?](
    https://{databricks_instance}/api/2.0/preview/sql/queries/{query_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Query changed successfully. |
    """  # noqa
    url = (
        f"https://{databricks_instance}/api/2.0/preview/sql/queries/{query_id}"  # noqa
    )
    responses = {
        200: "Query changed successfully.",
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.POST,
        responses=responses,
    )
    return result
