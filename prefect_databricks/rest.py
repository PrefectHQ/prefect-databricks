"""
This is a module containing:
generic REST tasks

It was auto-generated using prefect-collection-generator so
manually editing this file is not recommended.
"""

from enum import Enum
from typing import TYPE_CHECKING, Any, Dict

from prefect import task

if TYPE_CHECKING:
    from prefect_databricks import DatabricksCredentials


class HTTPMethod(Enum):
    GET = "get"
    POST = "post"
    PUT = "put"
    DELETE = "delete"
    PATCH = "patch"


def strip_kwargs(**kwargs: Dict) -> Dict:
    """
    Drops keyword arguments if value is None.

    Args:
        **kwargs: Input keyword arguments.

    Returns:
        Stripped version of kwargs.
    """
    stripped_dict = {}
    for k, v in kwargs.items():
        if isinstance(v, dict):
            v = strip_kwargs(**v)
        if v is not None:
            stripped_dict[k] = v
    return stripped_dict or {}


@task
async def execute_endpoint(
    url: str,
    databricks_credentials: "DatabricksCredentials",
    http_method: HTTPMethod = HTTPMethod.GET,
    params: Dict[str, Any] = None,
    json: Dict[str, Any] = None,
    **kwargs: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Generic function for executing GraphQL operations.

    Args:
        url: The endpoint url.
        databricks_credentials: Credentials to use for authentication with Databricks.
        http_method: Either GET, POST, PUT, DELETE, or PATCH.
        params: URL query parameters in the request.
        json: JSON serializable object to include in the body of the request.
        **kwargs: Additional keyword arguments to pass.

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
            response = execute_endpoint(url, aviationapi_credentials, params=params)
            return response.json()

        example_execute_endpoint_flow()
        ```
    """
    if isinstance(http_method, HTTPMethod):
        http_method = http_method.value

    if params is not None:
        stripped_params = strip_kwargs(**params)
    else:
        stripped_params = None

    async with databricks_credentials.get_client() as client:
        response = await getattr(client, http_method)(
            url, params=stripped_params, json=json, **kwargs
        )

    return response
