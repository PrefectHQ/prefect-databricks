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
async def get_repos(
    databricks_instance: str,
    path_prefix: str,
    next_page_token: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Returns repos that the calling user has Manage permissions on. Results are
    paginated with each page containing twenty repos.

    Args:
        databricks_instance: Databricks instance used in formatting the endpoint URL.
        path_prefix: Filters repos that have paths starting with the given path prefix.
        next_page_token: Token used to get the next page of results. If not specified, returns
            the first page of results as well as a next page token if
            there are more results.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/repos?&path_prefix=%s&next_page_token=%s](
    https://{databricks_instance}/api/2.0/repos?&path_prefix=%s&next_page_token=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Repos were successfully returned. |
    | 404 | Repos is not enabled for the workspace. |
    | 500 | The request is not handled correctly due to a server error. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/repos"  # noqa
    responses = {
        200: "Repos were successfully returned.",  # noqa
        404: "Repos is not enabled for the workspace.",  # noqa
        500: "The request is not handled correctly due to a server error.",  # noqa
    }

    params = {
        "path_prefix": path_prefix,
        "next_page_token": next_page_token,
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
async def post_repos(
    databricks_instance: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Creates a repo in the workspace and links it to the remote Git repo specified.
    Note that repos created programmatically must be linked to a remote Git
    repo, unlike repos created in the browser.

    Args:
        databricks_instance: Databricks instance used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/repos?](
    https://{databricks_instance}/api/2.0/repos?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The repo was successfully created. |
    | 400 | The request is invalid. |
    | 404 | The specified directory does not exist. |
    | 500 | The request is not handled correctly due to a server error. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/repos"  # noqa
    responses = {
        200: "The repo was successfully created.",  # noqa
        400: "The request is invalid.",  # noqa
        404: "The specified directory does not exist.",  # noqa
        500: "The request is not handled correctly due to a server error.",  # noqa
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.POST,
        responses=responses,
    )
    return result


@task
async def get_repos_repo_id(
    databricks_instance: str,
    repo_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Returns the repo with the given repo ID.

    Args:
        databricks_instance: Databricks instance used in formatting the endpoint URL.
        repo_id: Repo id used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/repos/{repo_id}?](
    https://{databricks_instance}/api/2.0/repos/{repo_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The repo was successfully returned. |
    | 403 | The user does not have access to the requested resource. |
    | 404 | The specified repo does not exist. |
    | 500 | The request is not handled correctly due to a server error. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/repos/{repo_id}"  # noqa
    responses = {
        200: "The repo was successfully returned.",  # noqa
        403: "The user does not have access to the requested resource.",  # noqa
        404: "The specified repo does not exist.",  # noqa
        500: "The request is not handled correctly due to a server error.",  # noqa
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result


@task
async def patch_repos_repo_id(
    databricks_instance: str,
    repo_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Updates the repo to a different branch or tag, or updates the repo to the latest
    commit on the same branch.

    Args:
        databricks_instance: Databricks instance used in formatting the endpoint URL.
        repo_id: Repo id used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/repos/{repo_id}?](
    https://{databricks_instance}/api/2.0/repos/{repo_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The repo was successfully updated. |
    | 400 | The specified ref is invalid. |
    | 403 | The user does not have access to the requested resource. |
    | 404 | The specified repo does not exist. |
    | 500 | The request is not handled correctly due to a server error. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/repos/{repo_id}"  # noqa
    responses = {
        200: "The repo was successfully updated.",  # noqa
        400: "The specified ref is invalid.",  # noqa
        403: "The user does not have access to the requested resource.",  # noqa
        404: "The specified repo does not exist.",  # noqa
        500: "The request is not handled correctly due to a server error.",  # noqa
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.PATCH,
        responses=responses,
    )
    return result


@task
async def delete_repos_repo_id(
    databricks_instance: str,
    repo_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Deletes the specified repo.

    Args:
        databricks_instance: Databricks instance used in formatting the endpoint URL.
        repo_id: Repo id used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/repos/{repo_id}?](
    https://{databricks_instance}/api/2.0/repos/{repo_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The repo was successfully deleted. |
    | 403 | The user does not have access to the requested resource. |
    | 404 | The specified repo does not exist. |
    | 500 | The request is not handled correctly due to a server error. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/repos/{repo_id}"  # noqa
    responses = {
        200: "The repo was successfully deleted.",  # noqa
        403: "The user does not have access to the requested resource.",  # noqa
        404: "The specified repo does not exist.",  # noqa
        500: "The request is not handled correctly due to a server error.",  # noqa
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.DELETE,
        responses=responses,
    )
    return result
