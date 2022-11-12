""" Contains methods for accessing the API """

import functools
from typing import Callable, TypeVar

from typing_extensions import Concatenate, ParamSpec

from prefect_databricks.api_client.client import AuthenticatedClient
from prefect_databricks.credentials import DatabricksCredentials

C = ParamSpec("C")  # client function
T = ParamSpec("T")  # task function
R = TypeVar("R")  # The return type of the API function


def _update_kwargs_and_execute(
    endpoint_fn: Callable[Concatenate[AuthenticatedClient, C], R]
) -> Callable[[Callable[C, R]], Callable[Concatenate[DatabricksCredentials, C], R]]:
    """
    This decorator:
    1. replaces the AuthenticatedClient with DatabricksCredentials type annotation
    2. uses the databricks_credentials to get the client and execute endpoint_fn.
    """

    def wrap(task_fn: Callable[T, R]) -> Callable[C, R]:
        @functools.wraps(task_fn)
        async def run(*args: C.args, **kwargs: C.kwargs) -> R:
            if "databricks_credentials" in kwargs:
                kwargs.pop("databricks_credentials")
                input_args = (hightouch_credentials.get_client(), *args)
            else:
                args[0]
                input_args = (hightouch_credentials.get_client(), *args[1:])
            parsed_response = await endpoint_fn(*input_args, **kwargs)
            if hasattr(parsed_response, "data"):
                parsed_response = parsed_response.data
            return parsed_response

        return run

    return wrap
