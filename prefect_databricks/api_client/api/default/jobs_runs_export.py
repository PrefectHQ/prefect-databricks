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
from ...models.jobs_runs_export_response_200 import JobsRunsExportResponse200
from ...models.views_to_export import ViewsToExport
from ...types import UNSET, Response, Unset


def _get_kwargs(
    client: AuthenticatedClient,
    run_id: int,
    views_to_export: Union[Unset, None, ViewsToExport] = ViewsToExport.CODE,
) -> Dict[str, Any]:
    url = "{}/2.0/jobs/runs/export".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["run_id"] = run_id

    json_views_to_export: Union[Unset, None, str] = UNSET
    if not isinstance(views_to_export, Unset):
        json_views_to_export = views_to_export.value if views_to_export else None

    params["views_to_export"] = json_views_to_export

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
) -> Optional[Union[Any, JobsRunsExportResponse200]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = JobsRunsExportResponse200.from_dict(response.json())

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
) -> Response[Union[Any, JobsRunsExportResponse200]]:
    response.raise_for_status()

    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    client: AuthenticatedClient,
    run_id: int,
    views_to_export: Union[Unset, None, ViewsToExport] = ViewsToExport.CODE,
) -> Response[Union[Any, JobsRunsExportResponse200]]:
    """Export and retrieve a job run

     Export and retrieve the job run task.

    Args:
        client: An authenticated client.
        run_id (int):  Example: 455644833.
        views_to_export (Union[Unset, None, ViewsToExport]): * `CODE`: Code view of the notebook.
            * `DASHBOARDS`: All dashboard views of the notebook.
            * `ALL`: All views of the notebook. Default: ViewsToExport.CODE.

    Returns:
        The response.
    """

    kwargs = _get_kwargs(
        client=client,
        run_id=run_id,
        views_to_export=views_to_export,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    client: AuthenticatedClient,
    run_id: int,
    views_to_export: Union[Unset, None, ViewsToExport] = ViewsToExport.CODE,
) -> Optional[Union[Any, JobsRunsExportResponse200]]:
    """Export and retrieve a job run

     Export and retrieve the job run task.

    Args:
        client: An authenticated client.
        run_id (int):  Example: 455644833.
        views_to_export (Union[Unset, None, ViewsToExport]): * `CODE`: Code view of the notebook.
            * `DASHBOARDS`: All dashboard views of the notebook.
            * `ALL`: All views of the notebook. Default: ViewsToExport.CODE.

    Returns:
        The parsed response.
    """

    return sync_detailed(
        client=client,
        run_id=run_id,
        views_to_export=views_to_export,
    ).parsed


async def asyncio_detailed(
    client: AuthenticatedClient,
    run_id: int,
    views_to_export: Union[Unset, None, ViewsToExport] = ViewsToExport.CODE,
) -> Response[Union[Any, JobsRunsExportResponse200]]:
    """Export and retrieve a job run

     Export and retrieve the job run task.

    Args:
        client: An authenticated client.
        run_id (int):  Example: 455644833.
        views_to_export (Union[Unset, None, ViewsToExport]): * `CODE`: Code view of the notebook.
            * `DASHBOARDS`: All dashboard views of the notebook.
            * `ALL`: All views of the notebook. Default: ViewsToExport.CODE.

    Returns:
        The response.
    """

    kwargs = _get_kwargs(
        client=client,
        run_id=run_id,
        views_to_export=views_to_export,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    client: AuthenticatedClient,
    run_id: int,
    views_to_export: Union[Unset, None, ViewsToExport] = ViewsToExport.CODE,
) -> Optional[Union[Any, JobsRunsExportResponse200]]:
    """Export and retrieve a job run

     Export and retrieve the job run task.

    Args:
        client: An authenticated client.
        run_id (int):  Example: 455644833.
        views_to_export (Union[Unset, None, ViewsToExport]): * `CODE`: Code view of the notebook.
            * `DASHBOARDS`: All dashboard views of the notebook.
            * `ALL`: All views of the notebook. Default: ViewsToExport.CODE.

    Returns:
        The parsed response.
    """

    return (
        await asyncio_detailed(
            client=client,
            run_id=run_id,
            views_to_export=views_to_export,
        )
    ).parsed
