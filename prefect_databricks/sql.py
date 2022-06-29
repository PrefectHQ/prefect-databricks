"""
This is a module for interacting with Databricks REST tasks.
It was auto-generated using prefect-collection-generator so
manually editing this file is not recommended.

OpenAPI spec: history-2.0-aws.yaml
Updated at: 2022-06-29T19:47:28.452474
"""

from typing import TYPE_CHECKING, Any, Dict, List, Union  # noqa

from prefect import task

from prefect_databricks.rest import HTTPMethod, execute_endpoint

if TYPE_CHECKING:
    from prefect_databricks import DatabricksCredentials


@task
async def get_sql_queries(
    databricks_instance: str,
    databricks_credentials: "DatabricksCredentials",
    filter_by: str = None,
    include_metrics: str = None,
    max_results: str = None,
    page_token: str = None,
) -> Dict[str, Any]:
    """
    List the history of queries through SQL warehouses. You can filter by user ID,
    warehouse ID, status, and time range.

    Args:
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.
        filter_by:
            A filter to limit query history results. This field is optional. Key-values:
            - endpoint_id:
                Use `warehouse_ids: [<id>]` instead, e.g. `098765321fedcba`.
            - endpoint_ids:
                Alias for `warehouse_ids`.
            - query_start_time_range:

            - status:
                Use `statuses: [<status>]` instead.
            - statuses:
                Query status with one the following values:  `QUEUED` :
                Query has been received and queued.  `RUNNING` : Query has
                started.  `CANCELED` : Query has been cancelled by the user.
                `FAILED` : Query has failed.  `FINISHED` : Query has
                completed, e.g.
                ```
                ["FINISHED", "FAILED"]
                ```
            - user_id:
                Use `user_ids: [<id>]` instead, e.g. `01234567890123456`.
            - user_ids:
                A list of user IDs who ran the queries, e.g.
                            ```
                            [1234567890123456, 6789012345678901]
                            ```
            - warehouse_ids:
                A list of warehouse IDs, e.g.
                            ```
                            ["098765321fedcba", "1234567890abcdef"]
                            ```
        include_metrics:
            Whether to include metrics about query, e.g. `True`.
        max_results:
            Limit the number of results returned in one page. The default is 100,
            e.g. `100`.
        page_token:
            A token that can be used to get the next page of results, e.g.
            `Ei0KJDU4NjEwZjY5LTgzNzUtNDdiMS04YTg1LWYxNTU5ODI5MDYyMhDdobu`.

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
