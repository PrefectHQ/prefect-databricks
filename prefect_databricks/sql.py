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
async def get_sql_history_queries(
    databricks_instance: str,
    filter_by: str,
    include_metrics: str,
    max_results: str,
    page_token: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    List the history of queries through SQL endpoints. You can filter by user ID,
    endpoint ID, status, and time range.

    Args:
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        filter_by:
            A filter to limit query history results. This field is optional. Key-values:
            - endpoint_id:
                Endpoint ID, e.g. `098765321fedcba`.
            - query_start_time_range:

            - status:
                Query status with one the following values:            `QUEUED` - Query
                            has been received and queued.           `RUNNING` - Query
                            has started.           `CANCELED` - Query has been cancelled
                            by the user.           `FAILED` - Query has failed.
                            `FINISHED` - Query has completed, e.g. `FINISHED`.
            - user_id:
                The ID of the user who ran the query, e.g. `01234567890123456`.
        include_metrics:
            Whether to include metrics about query, e.g. `True`.
        max_results:
            Limit the number of results returned in one page. The default is 100,
            e.g. `100`.
        page_token:
            A token that can be used to get the next page of results, e.g.
            `Ei0KJDU4NjEwZjY5LTgzNzUtNDdiMS04YTg1LWYxNTU5ODI5MDYyMhDdobu`.
        databricks_credentials:
            Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/sql/history/queries?](
    https://{databricks_instance}/api/2.0/sql/history/queries?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The list of SQL queries. |
    | 500 | The request failed due to a server error. |
    | 503 | Temporarily unavailable due to a server error. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/sql/history/queries"  # noqa
    responses = {
        200: "The list of SQL queries.",  # noqa
        500: "The request failed due to a server error.",  # noqa
        503: "Temporarily unavailable due to a server error.",  # noqa
    }

    data = {
        "filter_by": filter_by,
        "include_metrics": include_metrics,
        "max_results": max_results,
        "page_token": page_token,
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
        data=data,
    )
    return result
