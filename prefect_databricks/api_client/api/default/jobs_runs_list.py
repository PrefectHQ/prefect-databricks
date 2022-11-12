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
from ...models.jobs_runs_list_response_200 import JobsRunsListResponse200
from ...models.jobs_runs_list_run_type import JobsRunsListRunType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    client: AuthenticatedClient,
    active_only: Union[Unset, None, bool] = False,
    completed_only: Union[Unset, None, bool] = False,
    job_id: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = 0,
    limit: Union[Unset, None, int] = 25,
    run_type: Union[Unset, None, JobsRunsListRunType] = UNSET,
    expand_tasks: Union[Unset, None, bool] = False,
    start_time_from: Union[Unset, None, int] = UNSET,
    start_time_to: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/2.1/jobs/runs/list".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["active_only"] = active_only

    params["completed_only"] = completed_only

    params["job_id"] = job_id

    params["offset"] = offset

    params["limit"] = limit

    json_run_type: Union[Unset, None, str] = UNSET
    if not isinstance(run_type, Unset):
        json_run_type = run_type.value if run_type else None

    params["run_type"] = json_run_type

    params["expand_tasks"] = expand_tasks

    params["start_time_from"] = start_time_from

    params["start_time_to"] = start_time_to

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
) -> Optional[Union[Any, JobsRunsListResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = JobsRunsListResponse200.from_dict(response.json())

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
) -> Response[Union[Any, JobsRunsListResponse200]]:
    response.raise_for_status()

    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    client: AuthenticatedClient,
    active_only: Union[Unset, None, bool] = False,
    completed_only: Union[Unset, None, bool] = False,
    job_id: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = 0,
    limit: Union[Unset, None, int] = 25,
    run_type: Union[Unset, None, JobsRunsListRunType] = UNSET,
    expand_tasks: Union[Unset, None, bool] = False,
    start_time_from: Union[Unset, None, int] = UNSET,
    start_time_to: Union[Unset, None, int] = UNSET,
) -> Response[Union[Any, JobsRunsListResponse200]]:
    """List runs for a job

     List runs in descending order by start time.

    Args:
        client: An authenticated client.
        active_only (Union[Unset, None, bool]):
        completed_only (Union[Unset, None, bool]):
        job_id (Union[Unset, None, int]):  Example: 11223344.
        offset (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):  Default: 25. Example: 25.
        run_type (Union[Unset, None, JobsRunsListRunType]):  Example: JOB_RUN.
        expand_tasks (Union[Unset, None, bool]):
        start_time_from (Union[Unset, None, int]):  Example: 1642521600000.
        start_time_to (Union[Unset, None, int]):  Example: 1642608000000.

    Returns:
        The response.
    """

    kwargs = _get_kwargs(
        client=client,
        active_only=active_only,
        completed_only=completed_only,
        job_id=job_id,
        offset=offset,
        limit=limit,
        run_type=run_type,
        expand_tasks=expand_tasks,
        start_time_from=start_time_from,
        start_time_to=start_time_to,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    client: AuthenticatedClient,
    active_only: Union[Unset, None, bool] = False,
    completed_only: Union[Unset, None, bool] = False,
    job_id: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = 0,
    limit: Union[Unset, None, int] = 25,
    run_type: Union[Unset, None, JobsRunsListRunType] = UNSET,
    expand_tasks: Union[Unset, None, bool] = False,
    start_time_from: Union[Unset, None, int] = UNSET,
    start_time_to: Union[Unset, None, int] = UNSET,
) -> Optional[Union[Any, JobsRunsListResponse200]]:
    """List runs for a job

     List runs in descending order by start time.

    Args:
        client: An authenticated client.
        active_only (Union[Unset, None, bool]):
        completed_only (Union[Unset, None, bool]):
        job_id (Union[Unset, None, int]):  Example: 11223344.
        offset (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):  Default: 25. Example: 25.
        run_type (Union[Unset, None, JobsRunsListRunType]):  Example: JOB_RUN.
        expand_tasks (Union[Unset, None, bool]):
        start_time_from (Union[Unset, None, int]):  Example: 1642521600000.
        start_time_to (Union[Unset, None, int]):  Example: 1642608000000.

    Returns:
        The parsed response.
    """

    return sync_detailed(
        client=client,
        active_only=active_only,
        completed_only=completed_only,
        job_id=job_id,
        offset=offset,
        limit=limit,
        run_type=run_type,
        expand_tasks=expand_tasks,
        start_time_from=start_time_from,
        start_time_to=start_time_to,
    ).parsed


async def asyncio_detailed(
    client: AuthenticatedClient,
    active_only: Union[Unset, None, bool] = False,
    completed_only: Union[Unset, None, bool] = False,
    job_id: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = 0,
    limit: Union[Unset, None, int] = 25,
    run_type: Union[Unset, None, JobsRunsListRunType] = UNSET,
    expand_tasks: Union[Unset, None, bool] = False,
    start_time_from: Union[Unset, None, int] = UNSET,
    start_time_to: Union[Unset, None, int] = UNSET,
) -> Response[Union[Any, JobsRunsListResponse200]]:
    """List runs for a job

     List runs in descending order by start time.

    Args:
        client: An authenticated client.
        active_only (Union[Unset, None, bool]):
        completed_only (Union[Unset, None, bool]):
        job_id (Union[Unset, None, int]):  Example: 11223344.
        offset (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):  Default: 25. Example: 25.
        run_type (Union[Unset, None, JobsRunsListRunType]):  Example: JOB_RUN.
        expand_tasks (Union[Unset, None, bool]):
        start_time_from (Union[Unset, None, int]):  Example: 1642521600000.
        start_time_to (Union[Unset, None, int]):  Example: 1642608000000.

    Returns:
        The response.
    """

    kwargs = _get_kwargs(
        client=client,
        active_only=active_only,
        completed_only=completed_only,
        job_id=job_id,
        offset=offset,
        limit=limit,
        run_type=run_type,
        expand_tasks=expand_tasks,
        start_time_from=start_time_from,
        start_time_to=start_time_to,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    client: AuthenticatedClient,
    active_only: Union[Unset, None, bool] = False,
    completed_only: Union[Unset, None, bool] = False,
    job_id: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = 0,
    limit: Union[Unset, None, int] = 25,
    run_type: Union[Unset, None, JobsRunsListRunType] = UNSET,
    expand_tasks: Union[Unset, None, bool] = False,
    start_time_from: Union[Unset, None, int] = UNSET,
    start_time_to: Union[Unset, None, int] = UNSET,
) -> Optional[Union[Any, JobsRunsListResponse200]]:
    """List runs for a job

     List runs in descending order by start time.

    Args:
        client: An authenticated client.
        active_only (Union[Unset, None, bool]):
        completed_only (Union[Unset, None, bool]):
        job_id (Union[Unset, None, int]):  Example: 11223344.
        offset (Union[Unset, None, int]):
        limit (Union[Unset, None, int]):  Default: 25. Example: 25.
        run_type (Union[Unset, None, JobsRunsListRunType]):  Example: JOB_RUN.
        expand_tasks (Union[Unset, None, bool]):
        start_time_from (Union[Unset, None, int]):  Example: 1642521600000.
        start_time_to (Union[Unset, None, int]):  Example: 1642608000000.

    Returns:
        The parsed response.
    """

    return (
        await asyncio_detailed(
            client=client,
            active_only=active_only,
            completed_only=completed_only,
            job_id=job_id,
            offset=offset,
            limit=limit,
            run_type=run_type,
            expand_tasks=expand_tasks,
            start_time_from=start_time_from,
            start_time_to=start_time_to,
        )
    ).parsed
