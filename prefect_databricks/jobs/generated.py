"""
This is a module containing tasks, auto-generated from the Databricks
REST schema, used for interacting with jobs.
"""

# This module was auto-generated using prefect-collection-generator so
# manually editing this file is not recommended. If this module is outdated
# rerun scripts/generate.py. To override the default generated output:
# 1. create a separate module and rewrite the class / function
# 2. import in `__init__.py`, under the `from .generated import *` line
# 3. hide the generated function in `docs/jobs.md` under `options`

# OpenAPI spec: jobs-2.1-aws.yaml
# Updated at: 2022-11-12T01:20:24.231624

from prefect import task

from prefect_databricks.api_client import models as api_models
from prefect_databricks.api_client.api import _update_kwargs_and_execute
from prefect_databricks.api_client.api.default.jobs_create import (
    asyncio as _jobs_create_endpoint,
)
from prefect_databricks.api_client.api.default.jobs_delete import (
    asyncio as _jobs_delete_endpoint,
)
from prefect_databricks.api_client.api.default.jobs_get import (
    asyncio as _jobs_get_endpoint,
)
from prefect_databricks.api_client.api.default.jobs_list import (
    asyncio as _jobs_list_endpoint,
)
from prefect_databricks.api_client.api.default.jobs_reset import (
    asyncio as _jobs_reset_endpoint,
)
from prefect_databricks.api_client.api.default.jobs_run_now import (
    asyncio as _jobs_run_now_endpoint,
)
from prefect_databricks.api_client.api.default.jobs_runs_cancel import (
    asyncio as _jobs_runs_cancel_endpoint,
)
from prefect_databricks.api_client.api.default.jobs_runs_cancel_all import (
    asyncio as _jobs_runs_cancel_all_endpoint,
)
from prefect_databricks.api_client.api.default.jobs_runs_delete import (
    asyncio as _jobs_runs_delete_endpoint,
)
from prefect_databricks.api_client.api.default.jobs_runs_export import (
    asyncio as _jobs_runs_export_endpoint,
)
from prefect_databricks.api_client.api.default.jobs_runs_get import (
    asyncio as _jobs_runs_get_endpoint,
)
from prefect_databricks.api_client.api.default.jobs_runs_get_output import (
    asyncio as _jobs_runs_get_output_endpoint,
)
from prefect_databricks.api_client.api.default.jobs_runs_list import (
    asyncio as _jobs_runs_list_endpoint,
)
from prefect_databricks.api_client.api.default.jobs_runs_repair import (
    asyncio as _jobs_runs_repair_endpoint,
)
from prefect_databricks.api_client.api.default.jobs_runs_submit import (
    asyncio as _jobs_runs_submit_endpoint,
)
from prefect_databricks.api_client.api.default.jobs_update import (
    asyncio as _jobs_update_endpoint,
)


@task
@_update_kwargs_and_execute(_jobs_runs_export_endpoint)
async def jobs_runs_export(
    *args, **kwargs
) -> api_models.jobs_runs_export_response_200.JobsRunsExportResponse200:
    """
    Export and retrieve the job run task.

    Args:
        databricks_credentials (DatabricksCredentials):
            Credentials to use for authentication with Databricks.
        run_id (int):
            The canonical identifier for the run. This field is required.
        views_to_export (Optional[models.views_to_export.ViewsToExport]]):
            Which views to export (CODE, DASHBOARDS, or ALL). Defaults to CODE.


    Returns:
        - `views`: `List`<br>


    <h4>API Endpoint:</h4>
    `/2.0/jobs/runs/export`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Run was exported successfully. |
    | 400 | The request was malformed. See JSON response for error details. |
    | 401 | The request was unauthorized. |
    | 500 | The request was not handled correctly due to a server error. |
    """  # noqa
    ...  # pragma: no cover because only the decorated function gets run


@task
@_update_kwargs_and_execute(_jobs_create_endpoint)
async def jobs_create(
    *args, **kwargs
) -> api_models.jobs_create_response_200.JobsCreateResponse200:
    """
    Create a new job.

    Args:
        databricks_credentials (DatabricksCredentials):
            Credentials to use for authentication with Databricks.
        json_body (models.jobs_create_json_body.JobsCreateJsonBody):



    Returns:
        - `job_id`: `int`<br>


    <h4>API Endpoint:</h4>
    `/2.1/jobs/create`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Job was created successfully. |
    | 400 | The request was malformed. See JSON response for error details. |
    | 401 | The request was unauthorized. |
    | 500 | The request was not handled correctly due to a server error. |
    """  # noqa
    ...  # pragma: no cover because only the decorated function gets run


@task
@_update_kwargs_and_execute(_jobs_delete_endpoint)
async def jobs_delete(
    *args, **kwargs
) -> api_models.jobs_delete_response_200.JobsDeleteResponse200:
    """
    Deletes a job.

    Args:
        databricks_credentials (DatabricksCredentials):
            Credentials to use for authentication with Databricks.
        json_body (models.jobs_delete_json_body.JobsDeleteJsonBody):




    <h4>API Endpoint:</h4>
    `/2.1/jobs/delete`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Job was deleted successfully. |
    | 400 | The request was malformed. See JSON response for error details. |
    | 401 | The request was unauthorized. |
    | 500 | The request was not handled correctly due to a server error. |
    """  # noqa
    ...  # pragma: no cover because only the decorated function gets run


@task
@_update_kwargs_and_execute(_jobs_get_endpoint)
async def jobs_get(
    *args, **kwargs
) -> api_models.jobs_get_response_200.JobsGetResponse200:
    """
    Retrieves the details for a single job.

    Args:
        databricks_credentials (DatabricksCredentials):
            Credentials to use for authentication with Databricks.
        job_id (int):
            The canonical identifier of the job to retrieve information about. This
            field is required.


    Returns:
        - `job_id`: `int`<br>
            - `creator_user_name`: `str`<br>
            - `run_as_user_name`: `str`<br>
            - `settings`: `"models.JobSettings"`<br>
            - `created_time`: `int`<br>


    <h4>API Endpoint:</h4>
    `/2.1/jobs/get`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Job was retrieved successfully. |
    | 400 | The request was malformed. See JSON response for error details. |
    | 401 | The request was unauthorized. |
    | 500 | The request was not handled correctly due to a server error. |
    """  # noqa
    ...  # pragma: no cover because only the decorated function gets run


@task
@_update_kwargs_and_execute(_jobs_list_endpoint)
async def jobs_list(
    *args, **kwargs
) -> api_models.jobs_list_response_200.JobsListResponse200:
    """
    Retrieves a list of jobs.

    Args:
        databricks_credentials (DatabricksCredentials):
            Credentials to use for authentication with Databricks.
        limit (Optional[int]]):
            The number of jobs to return. This value must be greater than 0 and less
            or equal to 25. The default value is 20.
        offset (Optional[int]]):
            The offset of the first job to return, relative to the most recently
            created job.
        name (Optional[str]]):
            A filter on the list based on the exact (case insensitive) job name.
        expand_tasks (Optional[bool]]):
            Whether to include task and cluster details in the response.


    Returns:
        - `jobs`: `List`<br>
            - `has_more`: `bool`<br>


    <h4>API Endpoint:</h4>
    `/2.1/jobs/list`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | List of jobs was retrieved successfully. |
    | 400 | The request was malformed. See JSON response for error details. |
    | 401 | The request was unauthorized. |
    | 500 | The request was not handled correctly due to a server error. |
    """  # noqa
    ...  # pragma: no cover because only the decorated function gets run


@task
@_update_kwargs_and_execute(_jobs_reset_endpoint)
async def jobs_reset(
    *args, **kwargs
) -> api_models.jobs_reset_response_200.JobsResetResponse200:
    """
    Overwrites all the settings for a specific job. Use the Update endpoint to
    update job settings partially.

    Args:
        databricks_credentials (DatabricksCredentials):
            Credentials to use for authentication with Databricks.
        json_body (models.jobs_reset_json_body.JobsResetJsonBody):




    <h4>API Endpoint:</h4>
    `/2.1/jobs/reset`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Job was overwritten successfully. |
    | 400 | The request was malformed. See JSON response for error details. |
    | 401 | The request was unauthorized. |
    | 500 | The request was not handled correctly due to a server error. |
    """  # noqa
    ...  # pragma: no cover because only the decorated function gets run


@task
@_update_kwargs_and_execute(_jobs_run_now_endpoint)
async def jobs_run_now(
    *args, **kwargs
) -> api_models.jobs_run_now_response_200.JobsRunNowResponse200:
    """
    Run a job and return the `run_id` of the triggered run.

    Args:
        databricks_credentials (DatabricksCredentials):
            Credentials to use for authentication with Databricks.
        json_body (models.jobs_run_now_json_body.JobsRunNowJsonBody):



    Returns:
        - `run_id`: `int`<br>
            - `number_in_job`: `int`<br>


    <h4>API Endpoint:</h4>
    `/2.1/jobs/run-now`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Run was started successfully. |
    | 400 | The request was malformed. See JSON response for error details. |
    | 401 | The request was unauthorized. |
    | 500 | The request was not handled correctly due to a server error. |
    """  # noqa
    ...  # pragma: no cover because only the decorated function gets run


@task
@_update_kwargs_and_execute(_jobs_runs_cancel_endpoint)
async def jobs_runs_cancel(
    *args, **kwargs
) -> api_models.jobs_runs_cancel_response_200.JobsRunsCancelResponse200:
    """
    Cancels a job run. The run is canceled asynchronously, so it may still be
    running when this request completes.

    Args:
        databricks_credentials (DatabricksCredentials):
            Credentials to use for authentication with Databricks.
        json_body (models.jobs_runs_cancel_json_body.JobsRunsCancelJsonBody):




    <h4>API Endpoint:</h4>
    `/2.1/jobs/runs/cancel`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Run was cancelled successfully. |
    | 400 | The request was malformed. See JSON response for error details. |
    | 401 | The request was unauthorized. |
    | 500 | The request was not handled correctly due to a server error. |
    """  # noqa
    ...  # pragma: no cover because only the decorated function gets run


@task
@_update_kwargs_and_execute(_jobs_runs_cancel_all_endpoint)
async def jobs_runs_cancel_all(
    *args, **kwargs
) -> api_models.jobs_runs_cancel_all_response_200.JobsRunsCancelAllResponse200:
    """
    Cancels all active runs of a job. The runs are canceled asynchronously, so it
    doesn't prevent new runs from being started.

    Args:
        databricks_credentials (DatabricksCredentials):
            Credentials to use for authentication with Databricks.
        json_body (models.jobs_runs_cancel_all_json_body.JobsRunsCancelAllJsonBody):




    <h4>API Endpoint:</h4>
    `/2.1/jobs/runs/cancel-all`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | All runs were cancelled successfully. |
    | 400 | The request was malformed. See JSON response for error details. |
    | 401 | The request was unauthorized. |
    | 500 | The request was not handled correctly due to a server error. |
    """  # noqa
    ...  # pragma: no cover because only the decorated function gets run


@task
@_update_kwargs_and_execute(_jobs_runs_delete_endpoint)
async def jobs_runs_delete(
    *args, **kwargs
) -> api_models.jobs_runs_delete_response_200.JobsRunsDeleteResponse200:
    """
    Deletes a non-active run. Returns an error if the run is active.

    Args:
        databricks_credentials (DatabricksCredentials):
            Credentials to use for authentication with Databricks.
        json_body (models.jobs_runs_delete_json_body.JobsRunsDeleteJsonBody):




    <h4>API Endpoint:</h4>
    `/2.1/jobs/runs/delete`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Run was deleted successfully. |
    | 400 | The request was malformed. See JSON response for error details. |
    | 401 | The request was unauthorized. |
    | 500 | The request was not handled correctly due to a server error. |
    """  # noqa
    ...  # pragma: no cover because only the decorated function gets run


@task
@_update_kwargs_and_execute(_jobs_runs_get_endpoint)
async def jobs_runs_get(
    *args, **kwargs
) -> api_models.jobs_runs_get_response_200.JobsRunsGetResponse200:
    """
    Retrieve the metadata of a run.

    Args:
        databricks_credentials (DatabricksCredentials):
            Credentials to use for authentication with Databricks.
        run_id (int):
            The canonical identifier of the run for which to retrieve the metadata.
            This field is required.
        include_history (Optional[bool]]):
            Whether to include the repair history in the response.


    Returns:
        - `job_id`: `int`<br>
            - `run_id`: `int`<br>
            - `number_in_job`: `int`<br>
            - `creator_user_name`: `str`<br>
            - `original_attempt_run_id`: `int`<br>
            - `state`: `"models.RunState"`<br>
            - `schedule`: `"models.CronSchedule"`<br>
            - `tasks`: `List`<br>
            - `job_clusters`: `List`<br>
            - `cluster_spec`: `"models.ClusterSpec"`<br>
            - `cluster_instance`: `"models.ClusterInstance"`<br>
            - `git_source`: `"models.GitSource"`<br>
            - `overriding_parameters`: `"models.RunParameters"`<br>
            - `start_time`: `int`<br>
            - `setup_duration`: `int`<br>
            - `execution_duration`: `int`<br>
            - `cleanup_duration`: `int`<br>
            - `end_time`: `int`<br>
            - `trigger`: `"models.TriggerType"`<br>
            - `run_name`: `str`<br>
            - `run_page_url`: `str`<br>
            - `run_type`: `"models.RunType"`<br>
            - `attempt_number`: `int`<br>
            - `repair_history`: `List`<br>


    <h4>API Endpoint:</h4>
    `/2.1/jobs/runs/get`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Run was retrieved successfully. |
    | 400 | The request was malformed. See JSON response for error details. |
    | 401 | The request was unauthorized. |
    | 500 | The request was not handled correctly due to a server error. |
    """  # noqa
    ...  # pragma: no cover because only the decorated function gets run


@task
@_update_kwargs_and_execute(_jobs_runs_get_output_endpoint)
async def jobs_runs_get_output(*args, **kwargs) -> api_models.error.Error:
    """
    Retrieve the output and metadata of a single task run. When a notebook task
    returns a value through the dbutils.notebook.exit() call, you can use this
    endpoint to retrieve that value. Databricks restricts this API to return the
    first 5 MB of the output. To return a larger result, you can store job
    results in a cloud storage service. This endpoint validates that the run_id
    parameter is valid and returns an HTTP status code 400 if the run_id
    parameter is invalid. Runs are automatically removed after 60 days. If you
    to want to reference them beyond 60 days, you must save old run results
    before they expire. To export using the UI, see Export job run results. To
    export using the Jobs API, see Runs export.

    Args:
        databricks_credentials (DatabricksCredentials):
            Credentials to use for authentication with Databricks.
        run_id (int):
            The canonical identifier for the run. This field is required.


    Returns:
        - `notebook_output`: `"models.NotebookOutput"`<br>
            - `sql_output`: `"models.SqlOutput"`<br>
            - `dbt_output`: `"models.DbtOutput"`<br>
            - `logs`: `str`<br>
            - `logs_truncated`: `bool`<br>
            - `error`: `str`<br>
            - `error_trace`: `str`<br>
            - `metadata`: `"models.Run"`<br>


    <h4>API Endpoint:</h4>
    `/2.1/jobs/runs/get-output`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Run output was retrieved successfully. |
    | 400 | A job run with multiple tasks was provided. |
    | 401 | The request was unauthorized. |
    | 500 | The request was not handled correctly due to a server error. |
    """  # noqa
    ...  # pragma: no cover because only the decorated function gets run


@task
@_update_kwargs_and_execute(_jobs_runs_list_endpoint)
async def jobs_runs_list(
    *args, **kwargs
) -> api_models.jobs_runs_list_response_200.JobsRunsListResponse200:
    """
    List runs in descending order by start time.

    Args:
        databricks_credentials (DatabricksCredentials):
            Credentials to use for authentication with Databricks.
        active_only (Optional[bool]]):
            If active_only is `true`, only active runs are included in the results;
            otherwise, lists both active and completed runs. An active
            run is a run in the `PENDING`, `RUNNING`, or `TERMINATING`.
            This field cannot be `true` when completed_only is `true`.
        completed_only (Optional[bool]]):
            If completed_only is `true`, only completed runs are included in the
            results; otherwise, lists both active and completed runs.
            This field cannot be `true` when active_only is `true`.
        job_id (Optional[int]]):
            The job for which to list runs. If omitted, the Jobs service lists runs
            from all jobs.
        offset (Optional[int]]):
            The offset of the first run to return, relative to the most recent run.
        limit (Optional[int]]):
            The number of runs to return. This value must be greater than 0 and less
            than 25\. The default value is 25\. If a request specifies a
            limit of 0, the service instead uses the maximum limit.
        run_type (Optional[models.jobs_runs_list_run_type.JobsRunsListRunType]]):
            The type of runs to return. For a description of run types, see
            [Run](https://docs.databricks.com/dev-
            tools/api/latest/jobs.html
            operation/JobsRunsGet).
        expand_tasks (Optional[bool]]):
            Whether to include task and cluster details in the response.
        start_time_from (Optional[int]]):
            Show runs that started _at or after_ this value. The value must be a UTC
            timestamp in milliseconds. Can be combined with
            _start_time_to_ to filter by a time range.
        start_time_to (Optional[int]]):
            Show runs that started _at or before_ this value. The value must be a
            UTC timestamp in milliseconds. Can be combined with
            _start_time_from_ to filter by a time range.


    Returns:
        - `runs`: `List`<br>
            - `has_more`: `bool`<br>


    <h4>API Endpoint:</h4>
    `/2.1/jobs/runs/list`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | List of runs was retrieved successfully. |
    | 400 | The request was malformed. See JSON response for error details. |
    | 401 | The request was unauthorized. |
    | 500 | The request was not handled correctly due to a server error. |
    """  # noqa
    ...  # pragma: no cover because only the decorated function gets run


@task
@_update_kwargs_and_execute(_jobs_runs_repair_endpoint)
async def jobs_runs_repair(
    *args, **kwargs
) -> api_models.jobs_runs_repair_response_200.JobsRunsRepairResponse200:
    """
    Re-run one or more tasks. Tasks are re-run as part of the original job run, use
    the current job and task settings, and can be viewed in the history for the
    original job run.

    Args:
        databricks_credentials (DatabricksCredentials):
            Credentials to use for authentication with Databricks.
        json_body (models.jobs_runs_repair_json_body.JobsRunsRepairJsonBody):



    Returns:
        - `repair_id`: `int`<br>


    <h4>API Endpoint:</h4>
    `/2.1/jobs/runs/repair`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Run repair was initiated. |
    | 400 | The request was malformed. See JSON response for error details. |
    | 401 | The request was unauthorized. |
    | 500 | The request was not handled correctly due to a server error. |
    """  # noqa
    ...  # pragma: no cover because only the decorated function gets run


@task
@_update_kwargs_and_execute(_jobs_runs_submit_endpoint)
async def jobs_runs_submit(
    *args, **kwargs
) -> api_models.jobs_runs_submit_response_200.JobsRunsSubmitResponse200:
    """
    Submit a one-time run. This endpoint allows you to submit a workload directly
    without creating a job. Use the `jobs/runs/get` API to check the run state
    after the job is submitted.

    Args:
        databricks_credentials (DatabricksCredentials):
            Credentials to use for authentication with Databricks.
        json_body (models.jobs_runs_submit_json_body.JobsRunsSubmitJsonBody):



    Returns:
        - `run_id`: `int`<br>


    <h4>API Endpoint:</h4>
    `/2.1/jobs/runs/submit`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Run was created and started successfully. |
    | 400 | The request was malformed. See JSON response for error details. |
    | 401 | The request was unauthorized. |
    | 500 | The request was not handled correctly due to a server error. |
    """  # noqa
    ...  # pragma: no cover because only the decorated function gets run


@task
@_update_kwargs_and_execute(_jobs_update_endpoint)
async def jobs_update(
    *args, **kwargs
) -> api_models.jobs_update_response_200.JobsUpdateResponse200:
    """
    Add, update, or remove specific settings of an existing job. Use the Reset
    endpoint to overwrite all job settings.

    Args:
        databricks_credentials (DatabricksCredentials):
            Credentials to use for authentication with Databricks.
        json_body (models.jobs_update_json_body.JobsUpdateJsonBody):




    <h4>API Endpoint:</h4>
    `/2.1/jobs/update`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Job was updated successfully. |
    | 400 | The request was malformed. See JSON response for error details. |
    | 401 | The request was unauthorized. |
    | 500 | The request was not handled correctly due to a server error. |
    """  # noqa
    ...  # pragma: no cover because only the decorated function gets run
