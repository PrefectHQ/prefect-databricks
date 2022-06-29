"""
This is a module for interacting with Databricks REST tasks.
It was auto-generated using prefect-collection-generator so
manually editing this file is not recommended.

OpenAPI spec: queries-dashboards-2.0-aws.yaml
Updated at: 2022-06-29T19:47:27.566878
"""

from typing import TYPE_CHECKING, Any, Dict, List, Union  # noqa

from prefect import task

from prefect_databricks.rest import HTTPMethod, execute_endpoint

if TYPE_CHECKING:
    from prefect_databricks import DatabricksCredentials
    from prefect_databricks.models import permissions as models


@task
async def get_sql_analytics_object_permissions(
    object_type: str,
    object_id: str,
    databricks_instance: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Returns a JSON representation of the access control list (ACL) for a specified
    object.

    Args:
        object_type:
            Object type used in formatting the endpoint URL.
        object_id:
            Object id used in formatting the endpoint URL.
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/preview/sql/permissions/{object_type}/{object_id}?&object_type=%s&object_id=%s](
    https://{databricks_instance}/api/2.0/preview/sql/permissions/{object_type}/{object_id}?&object_type=%s&object_id=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | A JSON representation of the access control list (ACL) for an object. |
    | 400 | Bad request. |
    | 403 | Forbidden request. |
    | 404 | Path not found. |
    | 500 | Server error. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/preview/sql/permissions/{object_type}/{object_id}"  # noqa
    responses = {
        200: "A JSON representation of the access control list (ACL) for an object.",  # noqa
        400: "Bad request.",  # noqa
        403: "Forbidden request.",  # noqa
        404: "Path not found.",  # noqa
        500: "Server error.",  # noqa
    }

    params = {
        "object_type": object_type,
        "object_id": object_id,
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.GET,
        params=params,
        responses=responses,
    )
    return result


@task
async def set_sql_analytics_object_permissions(
    object_type: str,
    object_id: str,
    databricks_instance: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Completely rewrite the access control list for a specified object.

    Args:
        object_type:
            Object type used in formatting the endpoint URL.
        object_id:
            Object id used in formatting the endpoint URL.
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/preview/sql/permissions/{object_type}/{object_id}?&object_type=%s&object_id=%s](
    https://{databricks_instance}/api/2.0/preview/sql/permissions/{object_type}/{object_id}?&object_type=%s&object_id=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | A JSON representation of the access control list (ACL) for an object. |
    | 400 | Bad request. |
    | 403 | Forbidden request. |
    | 404 | Path not found. |
    | 500 | Server error. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/preview/sql/permissions/{object_type}/{object_id}"  # noqa
    responses = {
        200: "A JSON representation of the access control list (ACL) for an object.",  # noqa
        400: "Bad request.",  # noqa
        403: "Forbidden request.",  # noqa
        404: "Path not found.",  # noqa
        500: "Server error.",  # noqa
    }

    params = {
        "object_type": object_type,
        "object_id": object_id,
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.POST,
        params=params,
        responses=responses,
    )
    return result


@task
async def set_sql_analytics_object_owner(
    object_type: str,
    object_id: str,
    databricks_instance: str,
    databricks_credentials: "DatabricksCredentials",
    new_owner: str = None,
) -> Dict[str, Any]:
    """
    Transfer ownership of a dashboard, query, or alert to an active user. Requires
    an admin API key.

    Args:
        object_type:
            Object type used in formatting the endpoint URL.
        object_id:
            Object id used in formatting the endpoint URL.
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.
        new_owner:
            Email address for the new owner, who must exist in the workspace, e.g.
            `user@example.com`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/preview/sql/permissions/{object_type}/{object_id}/transfer?&object_type=%s&object_id=%s](
    https://{databricks_instance}/api/2.0/preview/sql/permissions/{object_type}/{object_id}/transfer?&object_type=%s&object_id=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Generic success message. |
    | 400 | Bad request. |
    | 403 | Forbidden request. |
    | 404 | Path not found. |
    | 500 | Server error. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/preview/sql/permissions/{object_type}/{object_id}/transfer"  # noqa
    responses = {
        200: "Generic success message.",  # noqa
        400: "Bad request.",  # noqa
        403: "Forbidden request.",  # noqa
        404: "Path not found.",  # noqa
        500: "Server error.",  # noqa
    }

    params = {
        "object_type": object_type,
        "object_id": object_id,
    }

    data = {
        "new_owner": new_owner,
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.POST,
        params=params,
        responses=responses,
        data=data,
    )
    return result


@task
async def get_tokens_permission_levels(
    databricks_instance: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Returns a JSON representation of the possible permissions levels for tokens. For
    details, see the [required token permission levels for various actions](
    tag/Token-permissions). The results of this request do **not** change based
    on the state of the workspace or the permissions of the calling user. This
    request is published for consistency with other permissions APIs.

    Args:
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/preview/permissions/authorization/tokens/permissionLevels?](
    https://{databricks_instance}/api/2.0/preview/permissions/authorization/tokens/permissionLevels?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Token permission levels were successfully returned. |
    | 400 | The request is malformed. |
    | 401 | The request is unauthorized. |
    | 404 | The requested resource does not exist. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/preview/permissions/authorization/tokens/permissionLevels"  # noqa
    responses = {
        200: "Token permission levels were successfully returned.",  # noqa
        400: "The request is malformed.",  # noqa
        401: "The request is unauthorized.",  # noqa
        404: "The requested resource does not exist.",  # noqa
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result


@task
async def get_password_permission_levels(
    databricks_instance: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Returns a JSON representation of the possible permissions levels for passwords.

    Args:
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/preview/permissions/authorization/passwords/permissionLevels?](
    https://{databricks_instance}/api/2.0/preview/permissions/authorization/passwords/permissionLevels?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Password permission levels were successfully returned. |
    | 400 | The request is malformed. |
    | 401 | The request is unauthorized. |
    | 404 | The requested resource does not exist. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/preview/permissions/authorization/passwords/permissionLevels"  # noqa
    responses = {
        200: "Password permission levels were successfully returned.",  # noqa
        400: "The request is malformed.",  # noqa
        401: "The request is unauthorized.",  # noqa
        404: "The requested resource does not exist.",  # noqa
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result


@task
async def get_clusters_permission_levels(
    databricks_instance: str,
    cluster_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Returns a JSON representation of the possible permissions levels for clusters.

    Args:
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        cluster_id:
            Cluster id used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/preview/permissions/clusters/{cluster_id}/permissionLevels?](
    https://{databricks_instance}/api/2.0/preview/permissions/clusters/{cluster_id}/permissionLevels?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Cluster permission levels were successfully returned. |
    | 400 | The request is malformed. |
    | 401 | The request is unauthorized. |
    | 404 | The requested resource does not exist. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/preview/permissions/clusters/{cluster_id}/permissionLevels"  # noqa
    responses = {
        200: "Cluster permission levels were successfully returned.",  # noqa
        400: "The request is malformed.",  # noqa
        401: "The request is unauthorized.",  # noqa
        404: "The requested resource does not exist.",  # noqa
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result


@task
async def get_instance_pools_permission_levels(
    databricks_instance: str,
    instance_pool_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Returns a JSON representation of the possible permissions levels for pools.

    Args:
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        instance_pool_id:
            Instance pool id used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/preview/permissions/instance-pools/{instance_pool_id}/permissionLevels?](
    https://{databricks_instance}/api/2.0/preview/permissions/instance-pools/{instance_pool_id}/permissionLevels?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Pool permission levels were successfully returned. |
    | 400 | The request is malformed. |
    | 401 | The request is unauthorized. |
    | 404 | The requested resource does not exist. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/preview/permissions/instance-pools/{instance_pool_id}/permissionLevels"  # noqa
    responses = {
        200: "Pool permission levels were successfully returned.",  # noqa
        400: "The request is malformed.",  # noqa
        401: "The request is unauthorized.",  # noqa
        404: "The requested resource does not exist.",  # noqa
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result


@task
async def get_jobs_permission_levels(
    databricks_instance: str,
    job_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Returns a JSON representation of the possible permissions levels for jobs.

    Args:
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        job_id:
            Job id used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/preview/permissions/jobs/{job_id}/permissionLevels?](
    https://{databricks_instance}/api/2.0/preview/permissions/jobs/{job_id}/permissionLevels?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Job permission levels were successfully returned. |
    | 400 | The request is malformed. |
    | 401 | The request is unauthorized. |
    | 404 | The requested resource does not exist. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/preview/permissions/jobs/{job_id}/permissionLevels"  # noqa
    responses = {
        200: "Job permission levels were successfully returned.",  # noqa
        400: "The request is malformed.",  # noqa
        401: "The request is unauthorized.",  # noqa
        404: "The requested resource does not exist.",  # noqa
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result


@task
async def get_pipelines_permission_levels(
    databricks_instance: str,
    pipeline_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Returns a JSON representation of the possible permissions levels for pipelines.

    Args:
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        pipeline_id:
            Pipeline id used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/preview/permissions/pipelines/{pipeline_id}/permissionLevels?](
    https://{databricks_instance}/api/2.0/preview/permissions/pipelines/{pipeline_id}/permissionLevels?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Pipeline permission levels were successfully returned. |
    | 400 | The request is malformed. |
    | 401 | The request is unauthorized. |
    | 404 | The requested resource does not exist. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/preview/permissions/pipelines/{pipeline_id}/permissionLevels"  # noqa
    responses = {
        200: "Pipeline permission levels were successfully returned.",  # noqa
        400: "The request is malformed.",  # noqa
        401: "The request is unauthorized.",  # noqa
        404: "The requested resource does not exist.",  # noqa
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result


@task
async def get_notebooks_permission_levels(
    databricks_instance: str,
    notebook_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Returns a JSON representation of the possible permissions levels for notebooks.

    Args:
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        notebook_id:
            Notebook id used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/preview/permissions/notebooks/{notebook_id}/permissionLevels?](
    https://{databricks_instance}/api/2.0/preview/permissions/notebooks/{notebook_id}/permissionLevels?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Notebook permission levels were successfully returned. |
    | 400 | The request is malformed. |
    | 401 | The request is unauthorized. |
    | 404 | The requested resource does not exist. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/preview/permissions/notebooks/{notebook_id}/permissionLevels"  # noqa
    responses = {
        200: "Notebook permission levels were successfully returned.",  # noqa
        400: "The request is malformed.",  # noqa
        401: "The request is unauthorized.",  # noqa
        404: "The requested resource does not exist.",  # noqa
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result


@task
async def get_directories_permission_levels(
    databricks_instance: str,
    directory_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Returns a JSON representation of the possible permissions levels for
    directories.

    Args:
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        directory_id:
            Directory id used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/preview/permissions/directories/{directory_id}/permissionLevels?](
    https://{databricks_instance}/api/2.0/preview/permissions/directories/{directory_id}/permissionLevels?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Directory permission levels were successfully returned. |
    | 400 | The request is malformed. |
    | 401 | The request is unauthorized. |
    | 404 | The requested resource does not exist. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/preview/permissions/directories/{directory_id}/permissionLevels"  # noqa
    responses = {
        200: "Directory permission levels were successfully returned.",  # noqa
        400: "The request is malformed.",  # noqa
        401: "The request is unauthorized.",  # noqa
        404: "The requested resource does not exist.",  # noqa
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result


@task
async def get_experiment_permission_levels(
    databricks_instance: str,
    experiment_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Returns a JSON representation of the possible permission levels for experiments.

    Args:
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        experiment_id:
            Experiment id used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/preview/permissions/experiments/{experiment_id}/permissionLevels?](
    https://{databricks_instance}/api/2.0/preview/permissions/experiments/{experiment_id}/permissionLevels?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Experiment permission levels were successfully returned. |
    | 400 | The request is malformed. |
    | 401 | The request is unauthorized. |
    | 404 | The requested resource does not exist. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/preview/permissions/experiments/{experiment_id}/permissionLevels"  # noqa
    responses = {
        200: "Experiment permission levels were successfully returned.",  # noqa
        400: "The request is malformed.",  # noqa
        401: "The request is unauthorized.",  # noqa
        404: "The requested resource does not exist.",  # noqa
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result


@task
async def get_registered_models_permission_levels(
    databricks_instance: str,
    registered_model_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Returns a JSON representation of the possible permissions levels for MLflow
    registered models.

    Args:
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        registered_model_id:
            Registered model id used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/preview/permissions/registered-models/{registered_model_id}/permissionLevels?](
    https://{databricks_instance}/api/2.0/preview/permissions/registered-models/{registered_model_id}/permissionLevels?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Registered model permission levels were successfully returned. |
    | 400 | The request is malformed. |
    | 401 | The request is unauthorized. |
    | 404 | The requested resource does not exist. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/preview/permissions/registered-models/{registered_model_id}/permissionLevels"  # noqa
    responses = {
        200: "Registered model permission levels were successfully returned.",  # noqa
        400: "The request is malformed.",  # noqa
        401: "The request is unauthorized.",  # noqa
        404: "The requested resource does not exist.",  # noqa
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result


@task
async def get_sqlwarehouse_permission_levels(
    databricks_instance: str,
    warehouse_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Returns a JSON representation of the possible permissions levels for SQL
    warehouses.

    Args:
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        warehouse_id:
            Warehouse id used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/preview/permissions/sql/warehouses/{warehouse_id}/permissionLevels?](
    https://{databricks_instance}/api/2.0/preview/permissions/sql/warehouses/{warehouse_id}/permissionLevels?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | SQL warehouse permission levels were successfully returned. |
    | 400 | The request is malformed. |
    | 401 | The request is unauthorized. |
    | 404 | The requested resource does not exist. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/preview/permissions/sql/warehouses/{warehouse_id}/permissionLevels"  # noqa
    responses = {
        200: "SQL warehouse permission levels were successfully returned.",  # noqa
        400: "The request is malformed.",  # noqa
        401: "The request is unauthorized.",  # noqa
        404: "The requested resource does not exist.",  # noqa
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result


@task
async def get_repos_permission_levels(
    databricks_instance: str,
    repo_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Returns a JSON representation of the possible permissions levels for repos.

    Args:
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        repo_id:
            Repo id used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/preview/permissions/repos/{repo_id}/permissionLevels?](
    https://{databricks_instance}/api/2.0/preview/permissions/repos/{repo_id}/permissionLevels?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Repo permission levels were successfully returned. |
    | 400 | The request is malformed. |
    | 401 | The request is unauthorized. |
    | 404 | The requested resource does not exist. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/preview/permissions/repos/{repo_id}/permissionLevels"  # noqa
    responses = {
        200: "Repo permission levels were successfully returned.",  # noqa
        400: "The request is malformed.",  # noqa
        401: "The request is unauthorized.",  # noqa
        404: "The requested resource does not exist.",  # noqa
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result


@task
async def get_tokens_permissions(
    databricks_instance: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Get the set of all token permissions for the workspace. For an overview, see the
    [introduction to token permissions](
    tag/Token-permissions).

    Args:
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/preview/permissions/authorization/tokens?](
    https://{databricks_instance}/api/2.0/preview/permissions/authorization/tokens?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Tokens were successfully returned. |
    | 400 | The request is malformed. |
    | 401 | The request is unauthorized. |
    | 404 | The requested resource does not exist. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/preview/permissions/authorization/tokens"  # noqa
    responses = {
        200: "Tokens were successfully returned.",  # noqa
        400: "The request is malformed.",  # noqa
        401: "The request is unauthorized.",  # noqa
        404: "The requested resource does not exist.",  # noqa
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result


@task
async def set_tokens_permissions(
    databricks_instance: str,
    databricks_credentials: "DatabricksCredentials",
    access_control_list: List[
        Union["models.TokensAccessControlListsObjectForPatch", Dict]
    ] = None,
) -> Dict[str, Any]:
    """
    Grant token permissions for one or more users, groups, or service principals.
    You can only grant the Can Use (`CAN_USE`) permission. The Can Manage
    (`CAN_MANAGE`) permission level cannot be granted with this API because it
    is tied automatically to membership in the `admins` group.  **IMPORTANT:**
    You cannot use this request to revoke (remove) any permissions. The only way
    to remove permissions is with the [replace token permissions for entire
    workspace API](
    operation/update-tokens-permissions), which requires you specify the
    complete set of permissions for all objects that are granted permissions.
    To grant Can Use permission, in the `access_control_list` array in the
    request body, create an array element for the target object and set its name
    property (varies by object type) and `permission_level` property to
    `CAN_USE`.  To update and replace permissions for all entities for the
    entire workspace, see [replace token permissions for entire workspace](
    operation/update-tokens-permissions).  For an overview, see the
    [introduction to token permissions](
    tag/Token-permissions).

    Args:
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.
        access_control_list:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/preview/permissions/authorization/tokens?](
    https://{databricks_instance}/api/2.0/preview/permissions/authorization/tokens?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The token permissions for specified entities were successfully updated. |
    | 400 | The request is malformed. |
    | 401 | The request is unauthorized. |
    | 404 | The requested resource does not exist. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/preview/permissions/authorization/tokens"  # noqa
    responses = {
        200: "The token permissions for specified entities were successfully updated.",  # noqa
        400: "The request is malformed.",  # noqa
        401: "The request is unauthorized.",  # noqa
        404: "The requested resource does not exist.",  # noqa
    }

    data = {
        "access_control_list": access_control_list,
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.PATCH,
        responses=responses,
        data=data,
    )
    return result


@task
async def update_tokens_permissions(
    databricks_instance: str,
    databricks_credentials: "DatabricksCredentials",
    access_control_list: List[
        Union["models.TokensAccessControlListsObjectForPut", Dict]
    ] = None,
) -> Dict[str, Any]:
    """
    Update all token permissions for all users, groups, and service principals for
    the entire workspace. The permissions that you specify in this request
    overwrite the existing permissions entirely. You must provide a complete set
    of all permissions for all objects in one request.  At the end of processing
    your request, all users and service principals that do not have either
    `CAN_USE` or `CAN_MANAGE` permission either explicitly or implicitly due to
    group assignment no longer have any tokens permissions. Affected users or
    service principals immediately have all their tokens deleted.  Notes about
    the special two built-in groups:  * For workspaces created after the release
    of <Databricks> platform version 3.28 (Sept 9-15, 2020) the default is for
    no users to have the Can Use permission. Admins must explicitly grant those
    permissions, whether to the entire `users` group or on a user-by-user or
    group-by-group basis. **Important:** Workspaces created before 3.28 was
    released will maintain the permissions that were already in place. The
    default was for all users to have the Can Use permission. Admins can revoke
    that group permission assignment and add it to other groups or to individual
    non-admin users. * You are required to grant the administrators group (group
    `admins`) the `CAN_MANAGE` permission. It is unsupported to grant this
    permission to any other entities. **WARNING:** This request has powerful
    effects for workspace security configuration and on a workspace's users if
    they already use tokens. Use with caution. This request overwrites all
    existing token permissions with the data in the request body. By omitting
    reference to an entity that previously had permissions, access is stripped
    and existing tokens are permanently deleted.  To grant token permissions for
    one specific entity rather than the entire workspace, instead see [update
    tokens permissions for a specific object](
    operation/set-tokens-permissions). That API can only add permissions, not
    revoke permissions.  For an overview, see the [introduction to token
    permissions](
    tag/Token-permissions).

    Args:
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.
        access_control_list:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/preview/permissions/authorization/tokens?](
    https://{databricks_instance}/api/2.0/preview/permissions/authorization/tokens?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The permissions for the workspace were successfully updated. |
    | 400 | The request is malformed. |
    | 401 | The request is unauthorized. |
    | 404 | The requested resource does not exist. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/preview/permissions/authorization/tokens"  # noqa
    responses = {
        200: "The permissions for the workspace were successfully updated.",  # noqa
        400: "The request is malformed.",  # noqa
        401: "The request is unauthorized.",  # noqa
        404: "The requested resource does not exist.",  # noqa
    }

    data = {
        "access_control_list": access_control_list,
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.PUT,
        responses=responses,
        data=data,
    )
    return result


@task
async def get_passwords_permissions(
    databricks_instance: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Get all passwords permissions for the workspace.

    Args:
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/preview/permissions/authorization/passwords?](
    https://{databricks_instance}/api/2.0/preview/permissions/authorization/passwords?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Permissions for passwords were successfully returned. |
    | 400 | The request is malformed. |
    | 401 | The request is unauthorized. |
    | 404 | The requested resource does not exist. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/preview/permissions/authorization/passwords"  # noqa
    responses = {
        200: "Permissions for passwords were successfully returned.",  # noqa
        400: "The request is malformed.",  # noqa
        401: "The request is unauthorized.",  # noqa
        404: "The requested resource does not exist.",  # noqa
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result


@task
async def set_password_permissions(
    databricks_instance: str,
    databricks_credentials: "DatabricksCredentials",
    access_control_list: List[
        Union["models.PasswordsAccessControlListsObjectForPatch", Dict]
    ] = None,
) -> Dict[str, Any]:
    """
    Grant password permissions for one or more users or groups. You can only grant
    the Can Use (`CAN_USE`) permission. The CAN_USE permission if granted allows
    user to use passwords to login via UI and also authenticate via API when SSO
    is enabled.  This request only grants (adds) permissions. To revoke, use the
    [replace all password permissions](
    operation/update-all-password-permissions) operation.

    Args:
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.
        access_control_list:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/preview/permissions/authorization/passwords?](
    https://{databricks_instance}/api/2.0/preview/permissions/authorization/passwords?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The token permissions for specified items were updated successfully. |
    | 400 | The request is malformed. |
    | 401 | The request is unauthorized. |
    | 404 | The requested resource does not exist. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/preview/permissions/authorization/passwords"  # noqa
    responses = {
        200: "The token permissions for specified items were updated successfully.",  # noqa
        400: "The request is malformed.",  # noqa
        401: "The request is unauthorized.",  # noqa
        404: "The requested resource does not exist.",  # noqa
    }

    data = {
        "access_control_list": access_control_list,
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.PATCH,
        responses=responses,
        data=data,
    )
    return result


@task
async def update_all_password_permissions(
    databricks_instance: str,
    databricks_credentials: "DatabricksCredentials",
    access_control_list: List[
        Union["models.PasswordsAccessControlListsObjectForPut", Dict]
    ] = None,
) -> Dict[str, Any]:
    """
    Update all passwords permissions for all users, groups, for the entire
    workspace. **WARNING:** This request overwrites all existing permissions for
    the workspace and replaces it with the new permissions specified in the
    request body.

    Args:
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.
        access_control_list:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/preview/permissions/authorization/passwords?](
    https://{databricks_instance}/api/2.0/preview/permissions/authorization/passwords?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The permissions for the workspace were successfully updated. |
    | 400 | The request is malformed. |
    | 401 | The request is unauthorized. |
    | 404 | The requested resource does not exist. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/preview/permissions/authorization/passwords"  # noqa
    responses = {
        200: "The permissions for the workspace were successfully updated.",  # noqa
        400: "The request is malformed.",  # noqa
        401: "The request is unauthorized.",  # noqa
        404: "The requested resource does not exist.",  # noqa
    }

    data = {
        "access_control_list": access_control_list,
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.PUT,
        responses=responses,
        data=data,
    )
    return result


@task
async def get_cluster_permissions(
    databricks_instance: str,
    cluster_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Get cluster permissions.

    Args:
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        cluster_id:
            Cluster id used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/preview/permissions/clusters/{cluster_id}?](
    https://{databricks_instance}/api/2.0/preview/permissions/clusters/{cluster_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Permissions for the cluster were successfully returned. |
    | 400 | The request is malformed. |
    | 401 | The request is unauthorized. |
    | 404 | The requested resource does not exist. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/preview/permissions/clusters/{cluster_id}"  # noqa
    responses = {
        200: "Permissions for the cluster were successfully returned.",  # noqa
        400: "The request is malformed.",  # noqa
        401: "The request is unauthorized.",  # noqa
        404: "The requested resource does not exist.",  # noqa
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result


@task
async def set_cluster_permissions(
    databricks_instance: str,
    cluster_id: str,
    databricks_credentials: "DatabricksCredentials",
    access_control_list: List[
        Union["models.ClustersAccessControlListsObjectForPatch", Dict]
    ] = None,
) -> Dict[str, Any]:
    """
    Grant cluster permissions for one or more users, groups, or service principals.
    This request only grants (adds) permissions. To revoke, use the [replace all
    cluster permissions](
    operation/update-all-cluster-permissions) operation.

    Args:
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        cluster_id:
            Cluster id used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.
        access_control_list:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/preview/permissions/clusters/{cluster_id}?](
    https://{databricks_instance}/api/2.0/preview/permissions/clusters/{cluster_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The cluster permissions for specified items were successfully updated. |
    | 400 | The request is malformed. |
    | 401 | The request is unauthorized. |
    | 404 | The requested resource does not exist. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/preview/permissions/clusters/{cluster_id}"  # noqa
    responses = {
        200: "The cluster permissions for specified items were successfully updated.",  # noqa
        400: "The request is malformed.",  # noqa
        401: "The request is unauthorized.",  # noqa
        404: "The requested resource does not exist.",  # noqa
    }

    data = {
        "access_control_list": access_control_list,
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.PATCH,
        responses=responses,
        data=data,
    )
    return result


@task
async def update_all_cluster_permissions(
    databricks_instance: str,
    cluster_id: str,
    databricks_credentials: "DatabricksCredentials",
    access_control_list: List[
        Union["models.ClustersAccessControlListsObjectForPut", Dict]
    ] = None,
) -> Dict[str, Any]:
    """
    Update all clusters permissions for a specific cluster, specifying all users,
    groups, or service principal.  **WARNING:** This request overwrites all
    existing direct (non-inherited) permissions on the cluster and replaces it
    with the new permissions specified in the request body.

    Args:
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        cluster_id:
            Cluster id used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.
        access_control_list:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/preview/permissions/clusters/{cluster_id}?](
    https://{databricks_instance}/api/2.0/preview/permissions/clusters/{cluster_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The permissions for the cluster were successfully updated. |
    | 400 | The request is malformed. |
    | 401 | The request is unauthorized. |
    | 404 | The requested resource does not exist. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/preview/permissions/clusters/{cluster_id}"  # noqa
    responses = {
        200: "The permissions for the cluster were successfully updated.",  # noqa
        400: "The request is malformed.",  # noqa
        401: "The request is unauthorized.",  # noqa
        404: "The requested resource does not exist.",  # noqa
    }

    data = {
        "access_control_list": access_control_list,
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.PUT,
        responses=responses,
        data=data,
    )
    return result


@task
async def get_instance_pool_permissions(
    databricks_instance: str,
    instance_pool_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Get permissions for a specific pool.

    Args:
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        instance_pool_id:
            Instance pool id used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/preview/permissions/instance-pools/{instance_pool_id}?](
    https://{databricks_instance}/api/2.0/preview/permissions/instance-pools/{instance_pool_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Permissions for the pool were successfully returned. |
    | 400 | The request is malformed. |
    | 401 | The request is unauthorized. |
    | 404 | The requested resource does not exist. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/preview/permissions/instance-pools/{instance_pool_id}"  # noqa
    responses = {
        200: "Permissions for the pool were successfully returned.",  # noqa
        400: "The request is malformed.",  # noqa
        401: "The request is unauthorized.",  # noqa
        404: "The requested resource does not exist.",  # noqa
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result


@task
async def set_instance_pool_permissions(
    databricks_instance: str,
    instance_pool_id: str,
    databricks_credentials: "DatabricksCredentials",
    access_control_list: List[
        Union["models.InstancePoolsAccessControlListsObjectForPatch", Dict]
    ] = None,
) -> Dict[str, Any]:
    """
    Grant pool permissions for one or more users, groups, or service principal.
    This request only grants (adds) permissions. To revoke, use the [replace all
    pool permissions](
    operation/update-all-instance-pool-permissions) operation.

    Args:
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        instance_pool_id:
            Instance pool id used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.
        access_control_list:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/preview/permissions/instance-pools/{instance_pool_id}?](
    https://{databricks_instance}/api/2.0/preview/permissions/instance-pools/{instance_pool_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The pool permissions were updated successfully. |
    | 400 | The request is malformed. |
    | 401 | The request is unauthorized. |
    | 404 | The requested resource does not exist. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/preview/permissions/instance-pools/{instance_pool_id}"  # noqa
    responses = {
        200: "The pool permissions were updated successfully.",  # noqa
        400: "The request is malformed.",  # noqa
        401: "The request is unauthorized.",  # noqa
        404: "The requested resource does not exist.",  # noqa
    }

    data = {
        "access_control_list": access_control_list,
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.PATCH,
        responses=responses,
        data=data,
    )
    return result


@task
async def update_all_instance_pool_permissions(
    databricks_instance: str,
    instance_pool_id: str,
    databricks_credentials: "DatabricksCredentials",
    access_control_list: List[
        Union["models.InstancePoolsAccessControlListsObjectForPut", Dict]
    ] = None,
) -> Dict[str, Any]:
    """
    Update all pool permissions for all users, groups, or service principal for a
    specific pool.  **WARNING:** This request overwrites all existing
    permissions on the pool and replaces it with the new permissions specified
    in the request body.

    Args:
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        instance_pool_id:
            Instance pool id used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.
        access_control_list:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/preview/permissions/instance-pools/{instance_pool_id}?](
    https://{databricks_instance}/api/2.0/preview/permissions/instance-pools/{instance_pool_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The permissions for the workspace were successfully updated. |
    | 400 | The request is malformed. |
    | 401 | The request is unauthorized. |
    | 404 | The requested resource does not exist. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/preview/permissions/instance-pools/{instance_pool_id}"  # noqa
    responses = {
        200: "The permissions for the workspace were successfully updated.",  # noqa
        400: "The request is malformed.",  # noqa
        401: "The request is unauthorized.",  # noqa
        404: "The requested resource does not exist.",  # noqa
    }

    data = {
        "access_control_list": access_control_list,
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.PUT,
        responses=responses,
        data=data,
    )
    return result


@task
async def get_job_permissions(
    databricks_instance: str,
    job_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Get job permissions.

    Args:
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        job_id:
            Job id used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/preview/permissions/jobs/{job_id}?](
    https://{databricks_instance}/api/2.0/preview/permissions/jobs/{job_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Permissions for the job were successfully returned. |
    | 400 | The request is malformed. |
    | 401 | The request is unauthorized. |
    | 404 | The requested resource does not exist. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/preview/permissions/jobs/{job_id}"  # noqa
    responses = {
        200: "Permissions for the job were successfully returned.",  # noqa
        400: "The request is malformed.",  # noqa
        401: "The request is unauthorized.",  # noqa
        404: "The requested resource does not exist.",  # noqa
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result


@task
async def set_job_permissions(
    databricks_instance: str,
    job_id: str,
    databricks_credentials: "DatabricksCredentials",
    access_control_list: List[
        Union["models.JobsAccessControlListsObjectForPatch", Dict]
    ] = None,
) -> Dict[str, Any]:
    """
    Grant jobs permissions for one or more users, groups, or service principals.
    This request only grants (adds) permissions. To revoke, use the [replace all
    job permissions](
    operation/update-all-job-permissions) operation.

    Args:
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        job_id:
            Job id used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.
        access_control_list:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/preview/permissions/jobs/{job_id}?](
    https://{databricks_instance}/api/2.0/preview/permissions/jobs/{job_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The job permissions for specified items were successfully updated. |
    | 400 | The request is malformed. |
    | 401 | The request is unauthorized. |
    | 404 | The requested resource does not exist. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/preview/permissions/jobs/{job_id}"  # noqa
    responses = {
        200: "The job permissions for specified items were successfully updated.",  # noqa
        400: "The request is malformed.",  # noqa
        401: "The request is unauthorized.",  # noqa
        404: "The requested resource does not exist.",  # noqa
    }

    data = {
        "access_control_list": access_control_list,
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.PATCH,
        responses=responses,
        data=data,
    )
    return result


@task
async def update_all_job_permissions(
    databricks_instance: str,
    job_id: str,
    databricks_credentials: "DatabricksCredentials",
    access_control_list: List[
        Union["models.JobsAccessControlListsObjectForPut", Dict]
    ] = None,
) -> Dict[str, Any]:
    """
    Update all jobs permissions for all users, groups, or service principal for a
    specific job.  **WARNING:** This request overwrites all existing direct
    permissions on the job and replaces it with the new permissions specified in
    the request body.

    Args:
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        job_id:
            Job id used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.
        access_control_list:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/preview/permissions/jobs/{job_id}?](
    https://{databricks_instance}/api/2.0/preview/permissions/jobs/{job_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The permissions for the workspace were updated successfully. |
    | 400 | The request is malformed. |
    | 401 | The request is unauthorized. |
    | 404 | The requested resource does not exist. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/preview/permissions/jobs/{job_id}"  # noqa
    responses = {
        200: "The permissions for the workspace were updated successfully.",  # noqa
        400: "The request is malformed.",  # noqa
        401: "The request is unauthorized.",  # noqa
        404: "The requested resource does not exist.",  # noqa
    }

    data = {
        "access_control_list": access_control_list,
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.PUT,
        responses=responses,
        data=data,
    )
    return result


@task
async def get_pipeline_permissions(
    pipeline_id: str,
    databricks_instance: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Get the set of all permissions granted to users, groups, and service principals
    on a pipeline.

    Args:
        pipeline_id:
            Pipeline id used in formatting the endpoint URL.
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/preview/permissions/pipelines/{pipeline_id}?&pipeline_id=%s](
    https://{databricks_instance}/api/2.0/preview/permissions/pipelines/{pipeline_id}?&pipeline_id=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Permissions for the pipeline were successfully returned. |
    | 400 | The request is malformed. |
    | 401 | The request is unauthorized. |
    | 404 | The requested resource does not exist. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/preview/permissions/pipelines/{pipeline_id}"  # noqa
    responses = {
        200: "Permissions for the pipeline were successfully returned.",  # noqa
        400: "The request is malformed.",  # noqa
        401: "The request is unauthorized.",  # noqa
        404: "The requested resource does not exist.",  # noqa
    }

    params = {
        "pipeline_id": pipeline_id,
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.GET,
        params=params,
        responses=responses,
    )
    return result


@task
async def set_pipeline_permissions(
    pipeline_id: str,
    databricks_instance: str,
    databricks_credentials: "DatabricksCredentials",
    access_control_list: List[
        Union["models.PipelinesAccessControlListsObjectForPatch", Dict]
    ] = None,
) -> Dict[str, Any]:
    """
    Grant permissions on a pipeline for one or more users, groups, or service
    principals.  This request only grants (adds) permissions. To revoke, use the
    [replace all pipeline permissions](
    operation/update-all-pipeline-permissions) operation.

    Args:
        pipeline_id:
            Pipeline id used in formatting the endpoint URL.
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.
        access_control_list:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/preview/permissions/pipelines/{pipeline_id}?&pipeline_id=%s](
    https://{databricks_instance}/api/2.0/preview/permissions/pipelines/{pipeline_id}?&pipeline_id=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The permissions for specified pipelines were successfully updated. |
    | 400 | The request is malformed. |
    | 401 | The request is unauthorized. |
    | 404 | The requested resource does not exist. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/preview/permissions/pipelines/{pipeline_id}"  # noqa
    responses = {
        200: "The permissions for specified pipelines were successfully updated.",  # noqa
        400: "The request is malformed.",  # noqa
        401: "The request is unauthorized.",  # noqa
        404: "The requested resource does not exist.",  # noqa
    }

    params = {
        "pipeline_id": pipeline_id,
    }

    data = {
        "access_control_list": access_control_list,
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.PATCH,
        params=params,
        responses=responses,
        data=data,
    )
    return result


@task
async def update_all_pipeline_permissions(
    pipeline_id: str,
    databricks_instance: str,
    databricks_credentials: "DatabricksCredentials",
    access_control_list: List[
        Union["models.PipelinesAccessControlListsObjectForPut", Dict]
    ] = None,
) -> Dict[str, Any]:
    """
    Update permissions granted to users, groups and service principals on the
    specified pipeline.  **WARNING:** This request overwrites all existing
    direct (non-inherited) permissions on the pipeline and replaces it with the
    new permissions specified in the request body.

    Args:
        pipeline_id:
            Pipeline id used in formatting the endpoint URL.
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.
        access_control_list:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/preview/permissions/pipelines/{pipeline_id}?&pipeline_id=%s](
    https://{databricks_instance}/api/2.0/preview/permissions/pipelines/{pipeline_id}?&pipeline_id=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The permissions for the pipeline were updated successfully. |
    | 400 | The request is malformed. |
    | 401 | The request is unauthorized. |
    | 404 | The requested resource does not exist. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/preview/permissions/pipelines/{pipeline_id}"  # noqa
    responses = {
        200: "The permissions for the pipeline were updated successfully.",  # noqa
        400: "The request is malformed.",  # noqa
        401: "The request is unauthorized.",  # noqa
        404: "The requested resource does not exist.",  # noqa
    }

    params = {
        "pipeline_id": pipeline_id,
    }

    data = {
        "access_control_list": access_control_list,
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.PUT,
        params=params,
        responses=responses,
        data=data,
    )
    return result


@task
async def get_notebook_permissions(
    databricks_instance: str,
    notebook_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Get notebook permissions.

    Args:
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        notebook_id:
            Notebook id used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/preview/permissions/notebooks/{notebook_id}?](
    https://{databricks_instance}/api/2.0/preview/permissions/notebooks/{notebook_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Permissions for the notebook were successfully returned. |
    | 400 | The request is malformed. |
    | 401 | The request is unauthorized. |
    | 404 | The requested resource does not exist. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/preview/permissions/notebooks/{notebook_id}"  # noqa
    responses = {
        200: "Permissions for the notebook were successfully returned.",  # noqa
        400: "The request is malformed.",  # noqa
        401: "The request is unauthorized.",  # noqa
        404: "The requested resource does not exist.",  # noqa
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result


@task
async def set_notebook_permissions(
    databricks_instance: str,
    notebook_id: str,
    databricks_credentials: "DatabricksCredentials",
    access_control_list: List[
        Union["models.NotebooksAccessControlListsObjectForPatch", Dict]
    ] = None,
) -> Dict[str, Any]:
    """
    Grant a notebook new permissions for one or more users, groups, or service
    principals.  This request only grants (adds) permissions. To revoke, use the
    [replace all notebook permissions](
    operation/update-all-notebook-permissions) operation.

    Args:
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        notebook_id:
            Notebook id used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.
        access_control_list:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/preview/permissions/notebooks/{notebook_id}?](
    https://{databricks_instance}/api/2.0/preview/permissions/notebooks/{notebook_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The notebook permissions for specified items were updated successfully. |
    | 400 | The request is malformed. |
    | 401 | The request is unauthorized. |
    | 404 | The requested resource does not exist. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/preview/permissions/notebooks/{notebook_id}"  # noqa
    responses = {
        200: "The notebook permissions for specified items were updated successfully.",  # noqa
        400: "The request is malformed.",  # noqa
        401: "The request is unauthorized.",  # noqa
        404: "The requested resource does not exist.",  # noqa
    }

    data = {
        "access_control_list": access_control_list,
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.PATCH,
        responses=responses,
        data=data,
    )
    return result


@task
async def update_all_notebook_permissions(
    databricks_instance: str,
    notebook_id: str,
    databricks_credentials: "DatabricksCredentials",
    access_control_list: List[
        Union["models.NotebooksAccessControlListsObjectForPut", Dict]
    ] = None,
) -> Dict[str, Any]:
    """
    Update all notebooks permissions for all users, groups, or service principal for
    a specific notebook.  **WARNING:** This request overwrites all existing
    direct permissions on the notebook and replaces it with the new permissions
    specified in the request body.

    Args:
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        notebook_id:
            Notebook id used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.
        access_control_list:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/preview/permissions/notebooks/{notebook_id}?](
    https://{databricks_instance}/api/2.0/preview/permissions/notebooks/{notebook_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The permissions for the notebook were successfully updated. |
    | 400 | The request is malformed. |
    | 401 | The request is unauthorized. |
    | 404 | The requested resource does not exist. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/preview/permissions/notebooks/{notebook_id}"  # noqa
    responses = {
        200: "The permissions for the notebook were successfully updated.",  # noqa
        400: "The request is malformed.",  # noqa
        401: "The request is unauthorized.",  # noqa
        404: "The requested resource does not exist.",  # noqa
    }

    data = {
        "access_control_list": access_control_list,
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.PUT,
        responses=responses,
        data=data,
    )
    return result


@task
async def get_directory_permissions(
    databricks_instance: str,
    directory_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Get directory permissions for a specific directory.

    Args:
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        directory_id:
            Directory id used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/preview/permissions/directories/{directory_id}?](
    https://{databricks_instance}/api/2.0/preview/permissions/directories/{directory_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Permissions for the directory were successfully returned. |
    | 400 | The request is malformed. |
    | 401 | The request is unauthorized. |
    | 404 | The requested resource does not exist. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/preview/permissions/directories/{directory_id}"  # noqa
    responses = {
        200: "Permissions for the directory were successfully returned.",  # noqa
        400: "The request is malformed.",  # noqa
        401: "The request is unauthorized.",  # noqa
        404: "The requested resource does not exist.",  # noqa
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result


@task
async def set_directory_permissions(
    databricks_instance: str,
    directory_id: str,
    databricks_credentials: "DatabricksCredentials",
    access_control_list: List[
        Union["models.DirectoriesAccessControlListsObjectForPatch", Dict]
    ] = None,
) -> Dict[str, Any]:
    """
    Grant a directory new permissions for one or more users, groups, or service
    principals.  This request only grants (adds) permissions. To revoke, use the
    [replace all directory permissions](
    operation/update-all-directory-permissions) operation.

    Args:
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        directory_id:
            Directory id used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.
        access_control_list:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/preview/permissions/directories/{directory_id}?](
    https://{databricks_instance}/api/2.0/preview/permissions/directories/{directory_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The directory permissions for specified items were successfully updated. |
    | 400 | The request is malformed. |
    | 401 | The request is unauthorized. |
    | 404 | The requested resource does not exist. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/preview/permissions/directories/{directory_id}"  # noqa
    responses = {
        200: "The directory permissions for specified items were successfully updated.",  # noqa
        400: "The request is malformed.",  # noqa
        401: "The request is unauthorized.",  # noqa
        404: "The requested resource does not exist.",  # noqa
    }

    data = {
        "access_control_list": access_control_list,
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.PATCH,
        responses=responses,
        data=data,
    )
    return result


@task
async def update_all_directory_permissions(
    databricks_instance: str,
    directory_id: str,
    databricks_credentials: "DatabricksCredentials",
    access_control_list: List[
        Union["models.DirectoriesAccessControlListsObjectForPut", Dict]
    ] = None,
) -> Dict[str, Any]:
    """
    Update all directory permissions for all users, groups, or service principal for
    a specific directory.  **WARNING:** This request overwrites all existing
    direct permissions on the directory and replaces it with the new permissions
    specified in the request body.

    Args:
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        directory_id:
            Directory id used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.
        access_control_list:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/preview/permissions/directories/{directory_id}?](
    https://{databricks_instance}/api/2.0/preview/permissions/directories/{directory_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The permissions for the directory were successfully updated. |
    | 400 | The request is malformed. |
    | 401 | The request is unauthorized. |
    | 404 | The requested resource does not exist. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/preview/permissions/directories/{directory_id}"  # noqa
    responses = {
        200: "The permissions for the directory were successfully updated.",  # noqa
        400: "The request is malformed.",  # noqa
        401: "The request is unauthorized.",  # noqa
        404: "The requested resource does not exist.",  # noqa
    }

    data = {
        "access_control_list": access_control_list,
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.PUT,
        responses=responses,
        data=data,
    )
    return result


@task
async def get_experiment_permissions(
    databricks_instance: str,
    experiment_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Get experiment permissions.

    Args:
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        experiment_id:
            Experiment id used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/preview/permissions/experiments/{experiment_id}?](
    https://{databricks_instance}/api/2.0/preview/permissions/experiments/{experiment_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Permissions for the experiment were successfully returned. |
    | 400 | The request is malformed. |
    | 401 | The request is unauthorized. |
    | 404 | The requested resource does not exist. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/preview/permissions/experiments/{experiment_id}"  # noqa
    responses = {
        200: "Permissions for the experiment were successfully returned.",  # noqa
        400: "The request is malformed.",  # noqa
        401: "The request is unauthorized.",  # noqa
        404: "The requested resource does not exist.",  # noqa
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result


@task
async def set_experiment_permissions(
    databricks_instance: str,
    experiment_id: str,
    databricks_credentials: "DatabricksCredentials",
    access_control_list: List[
        Union["models.ExperimentsAccessControlListsObjectForPatch", Dict]
    ] = None,
) -> Dict[str, Any]:
    """
    Grant an experiment new permissions for one or more users, groups, or service
    principals.  This request only grants (adds) permissions. To revoke, use the
    [replace all experiment permissions](
    operation/update-all-experiment-permissions) operation.

    Args:
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        experiment_id:
            Experiment id used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.
        access_control_list:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/preview/permissions/experiments/{experiment_id}?](
    https://{databricks_instance}/api/2.0/preview/permissions/experiments/{experiment_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The experiment permissions for specified items were updated successfully. |
    | 400 | The request is malformed. |
    | 401 | The request is unauthorized. |
    | 404 | The requested resource does not exist. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/preview/permissions/experiments/{experiment_id}"  # noqa
    responses = {
        200: (  # noqa
            "The experiment permissions for specified items were updated successfully."
        ),
        400: "The request is malformed.",  # noqa
        401: "The request is unauthorized.",  # noqa
        404: "The requested resource does not exist.",  # noqa
    }

    data = {
        "access_control_list": access_control_list,
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.PATCH,
        responses=responses,
        data=data,
    )
    return result


@task
async def update_all_experiment_permissions(
    databricks_instance: str,
    experiment_id: str,
    databricks_credentials: "DatabricksCredentials",
    access_control_list: List[
        Union["models.ExperimentsAccessControlListsObjectForPut", Dict]
    ] = None,
) -> Dict[str, Any]:
    """
    Update all experiment permissions for all users, groups or service principal for
    a specific experiment.  **WARNING:** This request overwrites all existing
    direct permissions on the experiment and replaces it with the new
    permissions specified in the request body.

    Args:
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        experiment_id:
            Experiment id used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.
        access_control_list:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/preview/permissions/experiments/{experiment_id}?](
    https://{databricks_instance}/api/2.0/preview/permissions/experiments/{experiment_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The permissions for the experiment were successfully updated. |
    | 400 | The request is malformed. |
    | 401 | The request is unauthorized. |
    | 404 | The requested resource does not exist. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/preview/permissions/experiments/{experiment_id}"  # noqa
    responses = {
        200: "The permissions for the experiment were successfully updated.",  # noqa
        400: "The request is malformed.",  # noqa
        401: "The request is unauthorized.",  # noqa
        404: "The requested resource does not exist.",  # noqa
    }

    data = {
        "access_control_list": access_control_list,
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.PUT,
        responses=responses,
        data=data,
    )
    return result


@task
async def get_registered_model_permissions(
    databricks_instance: str,
    registered_model_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Get permissions for a specific MLflow registered model.

    Args:
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        registered_model_id:
            Registered model id used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/preview/permissions/registered-models/{registered_model_id}?](
    https://{databricks_instance}/api/2.0/preview/permissions/registered-models/{registered_model_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Permissions for the registered model were successfully returned. |
    | 400 | The request is malformed. |
    | 401 | The request is unauthorized. |
    | 404 | The requested resource does not exist. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/preview/permissions/registered-models/{registered_model_id}"  # noqa
    responses = {
        200: "Permissions for the registered model were successfully returned.",  # noqa
        400: "The request is malformed.",  # noqa
        401: "The request is unauthorized.",  # noqa
        404: "The requested resource does not exist.",  # noqa
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result


@task
async def set_registered_model_permissions(
    databricks_instance: str,
    registered_model_id: str,
    databricks_credentials: "DatabricksCredentials",
    access_control_list: List[
        Union["models.RegisteredModelsAccessControlListsObjectForPatch", Dict]
    ] = None,
) -> Dict[str, Any]:
    """
    Grant MLflow registered model permissions for one or more users, groups, or
    service principals.

    Args:
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        registered_model_id:
            Registered model id used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.
        access_control_list:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/preview/permissions/registered-models/{registered_model_id}?](
    https://{databricks_instance}/api/2.0/preview/permissions/registered-models/{registered_model_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The registered model permissions for specified items were updated successfully. |
    | 400 | The request is malformed. |
    | 401 | The request is unauthorized. |
    | 404 | The requested resource does not exist. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/preview/permissions/registered-models/{registered_model_id}"  # noqa
    responses = {
        200: (  # noqa
            "The registered model permissions for specified items were updated"
            " successfully."
        ),
        400: "The request is malformed.",  # noqa
        401: "The request is unauthorized.",  # noqa
        404: "The requested resource does not exist.",  # noqa
    }

    data = {
        "access_control_list": access_control_list,
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.PATCH,
        responses=responses,
        data=data,
    )
    return result


@task
async def update_registered_model_permissions(
    databricks_instance: str,
    registered_model_id: str,
    databricks_credentials: "DatabricksCredentials",
    access_control_list: List[
        Union["models.RegisteredModelsAccessControlListsObjectForPut", Dict]
    ] = None,
) -> Dict[str, Any]:
    """
    Update all MLflow registered model permissions for all users, groups, or service
    principal for a specific registered model.  **WARNING:** This request
    overwrites all existing direct permissions on the registered model and
    replaces it with the new permissions specified in the request body.

    Args:
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        registered_model_id:
            Registered model id used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.
        access_control_list:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/preview/permissions/registered-models/{registered_model_id}?](
    https://{databricks_instance}/api/2.0/preview/permissions/registered-models/{registered_model_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The permissions for the registered model were successfully updated. |
    | 400 | The request is malformed. |
    | 401 | The request is unauthorized. |
    | 404 | The requested resource does not exist. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/preview/permissions/registered-models/{registered_model_id}"  # noqa
    responses = {
        200: "The permissions for the registered model were successfully updated.",  # noqa
        400: "The request is malformed.",  # noqa
        401: "The request is unauthorized.",  # noqa
        404: "The requested resource does not exist.",  # noqa
    }

    data = {
        "access_control_list": access_control_list,
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.PUT,
        responses=responses,
        data=data,
    )
    return result


@task
async def get_sqlwarehouse_permissions(
    databricks_instance: str,
    warehouse_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Get SQL warehouse permissions.

    Args:
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        warehouse_id:
            Warehouse id used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/preview/permissions/sql/warehouses/{warehouse_id}?](
    https://{databricks_instance}/api/2.0/preview/permissions/sql/warehouses/{warehouse_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Permissions for the SQL warehouses were successfully returned. |
    | 400 | The request is malformed. |
    | 401 | The request is unauthorized. |
    | 404 | The requested resource does not exist. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/preview/permissions/sql/warehouses/{warehouse_id}"  # noqa
    responses = {
        200: "Permissions for the SQL warehouses were successfully returned.",  # noqa
        400: "The request is malformed.",  # noqa
        401: "The request is unauthorized.",  # noqa
        404: "The requested resource does not exist.",  # noqa
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result


@task
async def set_sqlwarehouse_permissions(
    databricks_instance: str,
    warehouse_id: str,
    databricks_credentials: "DatabricksCredentials",
    access_control_list: List[
        Union["models.SqlWarehousesAccessControlListsObjectForPatch", Dict]
    ] = None,
) -> Dict[str, Any]:
    """
    Grant SQL warehouse permissions for one or more users, groups, or service
    principals.  This request only grants (adds) permissions. To revoke, use the
    [replace all SQL warehouse permissions](
    operation/update-all-sqlwarehouse-permissions) operation.

    Args:
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        warehouse_id:
            Warehouse id used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.
        access_control_list:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/preview/permissions/sql/warehouses/{warehouse_id}?](
    https://{databricks_instance}/api/2.0/preview/permissions/sql/warehouses/{warehouse_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The SQL warehouse permissions for specified items were successfully updated. |
    | 400 | The request is malformed. |
    | 401 | The request is unauthorized. |
    | 404 | The requested resource does not exist. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/preview/permissions/sql/warehouses/{warehouse_id}"  # noqa
    responses = {
        200: (  # noqa
            "The SQL warehouse permissions for specified items were successfully"
            " updated."
        ),
        400: "The request is malformed.",  # noqa
        401: "The request is unauthorized.",  # noqa
        404: "The requested resource does not exist.",  # noqa
    }

    data = {
        "access_control_list": access_control_list,
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.PATCH,
        responses=responses,
        data=data,
    )
    return result


@task
async def update_all_sqlwarehouse_permissions(
    databricks_instance: str,
    warehouse_id: str,
    databricks_credentials: "DatabricksCredentials",
    access_control_list: List[
        Union["models.SqlWarehousesAccessControlListsObjectForPut", Dict]
    ] = None,
) -> Dict[str, Any]:
    """
    Update all permissions for a specific SQL warehouse, specifying all users,
    groups or service principal.  **WARNING:** This request overwrites all
    existing direct (non-inherited) permissions on the SQL warehouse and
    replaces it with the new permissions specified in the request body.

    Args:
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        warehouse_id:
            Warehouse id used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.
        access_control_list:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/preview/permissions/sql/warehouses/{warehouse_id}?](
    https://{databricks_instance}/api/2.0/preview/permissions/sql/warehouses/{warehouse_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The permissions for the SQL warehouse were successfully updated. |
    | 400 | The request is malformed. |
    | 401 | The request is unauthorized. |
    | 404 | The requested resource does not exist. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/preview/permissions/sql/warehouses/{warehouse_id}"  # noqa
    responses = {
        200: "The permissions for the SQL warehouse were successfully updated.",  # noqa
        400: "The request is malformed.",  # noqa
        401: "The request is unauthorized.",  # noqa
        404: "The requested resource does not exist.",  # noqa
    }

    data = {
        "access_control_list": access_control_list,
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.PUT,
        responses=responses,
        data=data,
    )
    return result


@task
async def get_repo_permissions(
    databricks_instance: str,
    repo_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Get repo permissions.

    Args:
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        repo_id:
            Repo id used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/preview/permissions/repos/{repo_id}?](
    https://{databricks_instance}/api/2.0/preview/permissions/repos/{repo_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Permissions for the repo were successfully returned. |
    | 400 | The request is malformed. |
    | 401 | The request is unauthorized. |
    | 404 | The requested resource does not exist. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/preview/permissions/repos/{repo_id}"  # noqa
    responses = {
        200: "Permissions for the repo were successfully returned.",  # noqa
        400: "The request is malformed.",  # noqa
        401: "The request is unauthorized.",  # noqa
        404: "The requested resource does not exist.",  # noqa
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result


@task
async def set_repo_permissions(
    databricks_instance: str,
    repo_id: str,
    databricks_credentials: "DatabricksCredentials",
    access_control_list: List[
        Union["models.ReposAccessControlListsObjectForPatch", Dict]
    ] = None,
) -> Dict[str, Any]:
    """
    Grant a repo new permissions for one or more users, groups, or service
    principals.  This request only grants (adds) permissions. To revoke, use the
    [replace all repo permissions](
    operation/update-all-repo-permissions) operation.

    Args:
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        repo_id:
            Repo id used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.
        access_control_list:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/preview/permissions/repos/{repo_id}?](
    https://{databricks_instance}/api/2.0/preview/permissions/repos/{repo_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The repo permissions for specified items were updated successfully. |
    | 400 | The request is malformed. |
    | 401 | The request is unauthorized. |
    | 404 | The requested resource does not exist. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/preview/permissions/repos/{repo_id}"  # noqa
    responses = {
        200: "The repo permissions for specified items were updated successfully.",  # noqa
        400: "The request is malformed.",  # noqa
        401: "The request is unauthorized.",  # noqa
        404: "The requested resource does not exist.",  # noqa
    }

    data = {
        "access_control_list": access_control_list,
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.PATCH,
        responses=responses,
        data=data,
    )
    return result


@task
async def update_all_repo_permissions(
    databricks_instance: str,
    repo_id: str,
    databricks_credentials: "DatabricksCredentials",
    access_control_list: List[
        Union["models.ReposAccessControlListsObjectForPut", Dict]
    ] = None,
) -> Dict[str, Any]:
    """
    Update all repos permissions for all users, groups or service principal for a
    specific repo.  **WARNING:** This request overwrites all existing direct
    permissions on the repo and replaces it with the new permissions specified
    in the request body.

    Args:
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        repo_id:
            Repo id used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.
        access_control_list:


    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/preview/permissions/repos/{repo_id}?](
    https://{databricks_instance}/api/2.0/preview/permissions/repos/{repo_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The permissions for the repo were successfully updated. |
    | 400 | The request is malformed. |
    | 401 | The request is unauthorized. |
    | 404 | The requested resource does not exist. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/preview/permissions/repos/{repo_id}"  # noqa
    responses = {
        200: "The permissions for the repo were successfully updated.",  # noqa
        400: "The request is malformed.",  # noqa
        401: "The request is unauthorized.",  # noqa
        404: "The requested resource does not exist.",  # noqa
    }

    data = {
        "access_control_list": access_control_list,
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.PUT,
        responses=responses,
        data=data,
    )
    return result
