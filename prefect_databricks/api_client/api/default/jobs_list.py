"""
This is a module containing functions, auto-generated from the 
REST schema, but note these are **not** Prefect tasks.

Example usage shown below; be sure to replace `endpoint_fn` with the desired endpoint function.

```python
from prefect_databricks.credentials import DatabricksCredentials
from prefect_databricks.api_client.api.default import endpoint_fn

credentials = DatabricksCredentials(token="my-service-token")
client = credentials.get_client()
result = endpoint_fn.sync(client=client)
```

The functions are described below:

- `asyncio`: Non-blocking request that returns parsed data (if successful) or None. Any calls must be awaited.
- `asyncio_detailed`: Non-blocking request that always returns a Request, optionally with parsed set if the request was successful. Any calls must be awaited.
- `sync`: Blocking request that returns parsed data (if successful) or None.
- `sync_detailed`: Blocking request that always returns a Request, optionally with parsed set if the request was successful.
"""

from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.jobs_list_response_200 import JobsListResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    client: AuthenticatedClient,
    limit: Union[Unset, None, int] = 20,
    offset: Union[Unset, None, int] = 0,
    name: Union[Unset, None, str] = UNSET,
    expand_tasks: Union[Unset, None, bool] = False,
) -> Dict[str, Any]:
    url = "{}/2.1/jobs/list".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["limit"] = limit

    params["offset"] = offset

    params["name"] = name

    params["expand_tasks"] = expand_tasks

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    kwargs = {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }

    if "json" in kwargs:
        kwargs["json"] = {k: v for k, v in kwargs["json"].items() if v != UNSET}
    return kwargs


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[Any, JobsListResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = JobsListResponse200.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = cast(Any, None)
        return response_500
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[Any, JobsListResponse200]]:
    response.raise_for_status()

    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    client: AuthenticatedClient,
    limit: Union[Unset, None, int] = 20,
    offset: Union[Unset, None, int] = 0,
    name: Union[Unset, None, str] = UNSET,
    expand_tasks: Union[Unset, None, bool] = False,
) -> Response[Union[Any, JobsListResponse200]]:
    """List all jobs

     Retrieves a list of jobs.

    Args:
        client: An authenticated client.
        limit (Union[Unset, None, int]):  Default: 20. Example: 25.
        offset (Union[Unset, None, int]):
        name (Union[Unset, None, str]):  Example: A%20multitask%20job.
        expand_tasks (Union[Unset, None, bool]):

    Returns:
        The response.
    """

    kwargs = _get_kwargs(
        client=client,
        limit=limit,
        offset=offset,
        name=name,
        expand_tasks=expand_tasks,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    client: AuthenticatedClient,
    limit: Union[Unset, None, int] = 20,
    offset: Union[Unset, None, int] = 0,
    name: Union[Unset, None, str] = UNSET,
    expand_tasks: Union[Unset, None, bool] = False,
) -> Optional[Union[Any, JobsListResponse200]]:
    """List all jobs

     Retrieves a list of jobs.

    Args:
        client: An authenticated client.
        limit (Union[Unset, None, int]):  Default: 20. Example: 25.
        offset (Union[Unset, None, int]):
        name (Union[Unset, None, str]):  Example: A%20multitask%20job.
        expand_tasks (Union[Unset, None, bool]):

    Returns:
        The parsed response.
    """

    return sync_detailed(
        client=client,
        limit=limit,
        offset=offset,
        name=name,
        expand_tasks=expand_tasks,
    ).parsed


async def asyncio_detailed(
    client: AuthenticatedClient,
    limit: Union[Unset, None, int] = 20,
    offset: Union[Unset, None, int] = 0,
    name: Union[Unset, None, str] = UNSET,
    expand_tasks: Union[Unset, None, bool] = False,
) -> Response[Union[Any, JobsListResponse200]]:
    """List all jobs

     Retrieves a list of jobs.

    Args:
        client: An authenticated client.
        limit (Union[Unset, None, int]):  Default: 20. Example: 25.
        offset (Union[Unset, None, int]):
        name (Union[Unset, None, str]):  Example: A%20multitask%20job.
        expand_tasks (Union[Unset, None, bool]):

    Returns:
        The response.
    """

    kwargs = _get_kwargs(
        client=client,
        limit=limit,
        offset=offset,
        name=name,
        expand_tasks=expand_tasks,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    client: AuthenticatedClient,
    limit: Union[Unset, None, int] = 20,
    offset: Union[Unset, None, int] = 0,
    name: Union[Unset, None, str] = UNSET,
    expand_tasks: Union[Unset, None, bool] = False,
) -> Optional[Union[Any, JobsListResponse200]]:
    """List all jobs

     Retrieves a list of jobs.

    Args:
        client: An authenticated client.
        limit (Union[Unset, None, int]):  Default: 20. Example: 25.
        offset (Union[Unset, None, int]):
        name (Union[Unset, None, str]):  Example: A%20multitask%20job.
        expand_tasks (Union[Unset, None, bool]):

    Returns:
        The parsed response.
    """

    return (
        await asyncio_detailed(
            client=client,
            limit=limit,
            offset=offset,
            name=name,
            expand_tasks=expand_tasks,
        )
    ).parsed
