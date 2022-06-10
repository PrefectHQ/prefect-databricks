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
async def get_git_credentials(
    databricks_instance: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Returns the calling user's Git credentials. One credential per user is
    supported.

    Args:
        databricks_instance: Databricks instance used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://{databricks_instance}/api/2.0/git-credentials?](
    https://{databricks_instance}/api/2.0/git-credentials?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Git credentials were successfully returned. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/git-credentials"  # noqa
    responses = {
        200: "Git credentials were successfully returned.",
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result


@task
async def post_git_credentials(
    databricks_instance: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Creates a Git credential entry for the user. Only one Git credential per user is
    supported, so any attempts to create credentials if an entry already exists
    will fail. Use the PATCH endpoint to update existing credentials, or the
    DELETE endpoint to delete existing credentials.

    Args:
        databricks_instance: Databricks instance used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://{databricks_instance}/api/2.0/git-credentials?](
    https://{databricks_instance}/api/2.0/git-credentials?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The credential was successfully configured. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/git-credentials"  # noqa
    responses = {
        200: "The credential was successfully configured.",
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.POST,
        responses=responses,
    )
    return result


@task
async def get_git_credentials_credential_id(
    databricks_instance: str,
    credential_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Returns the credential with the given credential ID.

    Args:
        databricks_instance: Databricks instance used in formatting the endpoint URL.
        credential_id: Credential id used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://{databricks_instance}/api/2.0/git-credentials/{credential_id}?](
    https://{databricks_instance}/api/2.0/git-credentials/{credential_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The credential was successfully returned. |
    """  # noqa
    url = (
        f"https://{databricks_instance}/api/2.0/git-credentials/{credential_id}"  # noqa
    )
    responses = {
        200: "The credential was successfully returned.",
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result


@task
async def patch_git_credentials_credential_id(
    databricks_instance: str,
    credential_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Updates the credential.

    Args:
        databricks_instance: Databricks instance used in formatting the endpoint URL.
        credential_id: Credential id used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://{databricks_instance}/api/2.0/git-credentials/{credential_id}?](
    https://{databricks_instance}/api/2.0/git-credentials/{credential_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The credential was successfully updated. |
    """  # noqa
    url = (
        f"https://{databricks_instance}/api/2.0/git-credentials/{credential_id}"  # noqa
    )
    responses = {
        200: "The credential was successfully updated.",
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.PATCH,
        responses=responses,
    )
    return result


@task
async def delete_git_credentials_credential_id(
    databricks_instance: str,
    credential_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Deletes the specified credential.

    Args:
        databricks_instance: Databricks instance used in formatting the endpoint URL.
        credential_id: Credential id used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://{databricks_instance}/api/2.0/git-credentials/{credential_id}?](
    https://{databricks_instance}/api/2.0/git-credentials/{credential_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The credential was successfully deleted. |
    """  # noqa
    url = (
        f"https://{databricks_instance}/api/2.0/git-credentials/{credential_id}"  # noqa
    )
    responses = {
        200: "The credential was successfully deleted.",
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.DELETE,
        responses=responses,
    )
    return result
