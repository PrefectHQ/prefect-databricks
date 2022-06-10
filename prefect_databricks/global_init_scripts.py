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
async def get_global_init_scripts(
    databricks_instance: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Get a list of all global init scripts for this workspace. This returns all
    properties for each script but **not** the script contents. To retrieve the
    contents of a script, use the [get a global init script](
    operation/get-script) operation.

    Args:
        databricks_instance: Databricks instance used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://{databricks_instance}/api/2.0/global-init-scripts?](
    https://{databricks_instance}/api/2.0/global-init-scripts?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/global-init-scripts"  # noqa
    responses = {}

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result


@task
async def post_global_init_scripts(
    databricks_instance: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Create a new global init script in this workspace.

    Args:
        databricks_instance: Databricks instance used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://{databricks_instance}/api/2.0/global-init-scripts?](
    https://{databricks_instance}/api/2.0/global-init-scripts?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/global-init-scripts"  # noqa
    responses = {}

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.POST,
        responses=responses,
    )
    return result


@task
async def delete_global_init_scripts_script_id(
    databricks_instance: str,
    script_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Delete a global init script.

    Args:
        databricks_instance: Databricks instance used in formatting the endpoint URL.
        script_id: Script id used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://{databricks_instance}/api/2.0/global-init-scripts/{script_id}?](
    https://{databricks_instance}/api/2.0/global-init-scripts/{script_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The script was deleted successfully. |
    """  # noqa
    url = (
        f"https://{databricks_instance}/api/2.0/global-init-scripts/{script_id}"  # noqa
    )
    responses = {
        200: "The script was deleted successfully.",
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.DELETE,
        responses=responses,
    )
    return result


@task
async def get_global_init_scripts_script_id(
    databricks_instance: str,
    script_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Get all the details of a script, including its Base64-encoded contents.

    Args:
        databricks_instance: Databricks instance used in formatting the endpoint URL.
        script_id: Script id used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://{databricks_instance}/api/2.0/global-init-scripts/{script_id}?](
    https://{databricks_instance}/api/2.0/global-init-scripts/{script_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = (
        f"https://{databricks_instance}/api/2.0/global-init-scripts/{script_id}"  # noqa
    )
    responses = {}

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result


@task
async def patch_global_init_scripts_script_id(
    databricks_instance: str,
    script_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Update a global init script, specifying only the fields to change. All fields
    are optional. Unspecified fields retain their current value.

    Args:
        databricks_instance: Databricks instance used in formatting the endpoint URL.
        script_id: Script id used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://{databricks_instance}/api/2.0/global-init-scripts/{script_id}?](
    https://{databricks_instance}/api/2.0/global-init-scripts/{script_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The script was updated successfully. |
    """  # noqa
    url = (
        f"https://{databricks_instance}/api/2.0/global-init-scripts/{script_id}"  # noqa
    )
    responses = {
        200: "The script was updated successfully.",
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.PATCH,
        responses=responses,
    )
    return result
