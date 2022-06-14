"""
This is a module for interacting with generic REST tasks.
It was auto-generated using prefect-collection-generator so
manually editing this file is not recommended.
"""

from enum import Enum
from typing import TYPE_CHECKING, Any, Dict

import httpx
from prefect import task

if TYPE_CHECKING:
    from prefect_databricks import DatabricksCredentials


class HTTPMethod(Enum):
    GET = "get"
    POST = "post"
    PUT = "put"
    DELETE = "delete"
    PATCH = "patch"


@task
async def execute_endpoint(
    url: str,
    databricks_credentials: "DatabricksCredentials",
    http_method: HTTPMethod = HTTPMethod.GET,
    responses: Dict[int, str] = None,
    **params: Dict[str, Any],
) -> Dict[str, Any]:
    """
    Generic function for executing GraphQL operations.

    Args:
        url: The endpoint url.
        databricks_credentials: Credentials to use for authentication with Databricks.
        http_method: Either GET, POST, PUT, DELETE, or PATCH.
        responses: Status codes mapped to the corresponding descriptions.

    Returns:
        A dict of the returned fields.

    Examples:
        Queries the weather at an airport.
        ```python
        from prefect import flow
        from prefect_aviationapi import AviationAPICredentials
        from prefect_aviationapi.rest import execute_endpoint

        @flow()
        def example_execute_endpoint_flow():
            url = "https://api.aviationapi.com/v1/weather/metar"
            aviationapi_credentials = AviationAPICredentials()
            params = dict(apt="KORD,KSEA")
            result = execute_endpoint(url, aviationapi_credentials, **params)
            return result

        example_execute_endpoint_flow()
        ```
    """
    if isinstance(http_method, HTTPMethod):
        http_method = http_method.value

    async with databricks_credentials.get_client() as client:
        response = await getattr(client, http_method)(url, params=params)

    try:
        response.raise_for_status()
    except httpx.HTTPStatusError as exc:
        helpful_error_response = (responses or {}).get(response.status_code, "")
        if helpful_error_response:
            raise httpx.HTTPStatusError(
                helpful_error_response, request=exc.request, response=exc.response
            ) from exc
        else:
            raise

    result = response.json()
    return result
