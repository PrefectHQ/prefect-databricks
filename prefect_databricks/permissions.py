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
async def get_permissions_object_type_object_id(
    databricks_instance: str,
    object_type: str,
    object_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Returns a JSON representation of the access control list (ACL) for a specified
    object.

    Args:
        databricks_instance: Databricks instance used in formatting the endpoint URL.
        object_type: Object type used in formatting the endpoint URL.
        object_id: Object id used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/preview/sql/permissions/{object_type}/{object_id}?](
    https://{databricks_instance}/api/2.0/preview/sql/permissions/{object_type}/{object_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/preview/sql/permissions/{object_type}/{object_id}"  # noqa
    responses = {}

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result


@task
async def post_permissions_object_type_object_id(
    databricks_instance: str,
    object_type: str,
    object_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Completely rewrite the access control list for a specified object.

    Args:
        databricks_instance: Databricks instance used in formatting the endpoint URL.
        object_type: Object type used in formatting the endpoint URL.
        object_id: Object id used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/preview/sql/permissions/{object_type}/{object_id}?](
    https://{databricks_instance}/api/2.0/preview/sql/permissions/{object_type}/{object_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/preview/sql/permissions/{object_type}/{object_id}"  # noqa
    responses = {}

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.POST,
        responses=responses,
    )
    return result


@task
async def post_permissions_object_type_object_id_transfer(
    databricks_instance: str,
    object_type: str,
    object_id: str,
    new_owner: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Transfer ownership of a dashboard, query, or alert to an active user. Requires
    an admin API key.

    Args:
        databricks_instance: Databricks instance used in formatting the endpoint URL.
        object_type: Object type used in formatting the endpoint URL.
        object_id: Object id used in formatting the endpoint URL.
        new_owner: Email address for the new owner, who must exist in the workspace, e.g.
            `user@example.com`.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/preview/sql/permissions/{object_type}/{object_id}/transfer?](
    https://{databricks_instance}/api/2.0/preview/sql/permissions/{object_type}/{object_id}/transfer?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/preview/sql/permissions/{object_type}/{object_id}/transfer"  # noqa
    responses = {}

    data = {
        "new_owner": new_owner,
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.POST,
        responses=responses,
        data=data,
    )
    return result
