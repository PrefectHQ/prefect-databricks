"""
This is a module for interacting with Databricks REST tasks.
It was auto-generated using prefect-collection-generator so
manually editing this file is not recommended.

OpenAPI spec: token-management-2.0-aws.yaml
Updated at: 2022-06-29T19:47:40.356066
"""

from typing import TYPE_CHECKING, Any, Dict, List, Union  # noqa

from prefect import task

from prefect_databricks.rest import HTTPMethod, execute_endpoint

if TYPE_CHECKING:
    from prefect_databricks import DatabricksCredentials
    from prefect_databricks.models import token_management as models


@task
async def create_obo_token(
    databricks_instance: str,
    databricks_credentials: "DatabricksCredentials",
    application_id: str = None,
    comment: Union["models.comment_input", Dict] = None,
    lifetime_seconds: str = None,
) -> Dict[str, Any]:
    """
    Create a token on behalf of a service principal.

    Args:
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.
        application_id:
            Application ID of the service principal, e.g.
            `6f5ccf28-d83a-4957-9bfb-5bbfac551410`.
        comment:
            Comment that describes the purpose of the token, e.g. `This is for the
            ABC department automation scripts.`.
        lifetime_seconds:
            The number of seconds before the token expires, e.g. `3600`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/token-management/on-behalf-of/tokens?](
    https://{databricks_instance}/api/2.0/token-management/on-behalf-of/tokens?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | A on-behalf token was successfully created for the service principal. |
    | 400 | The request is malformed. |
    | 500 | The request is not handled correctly due to a server error. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/token-management/on-behalf-of/tokens"  # noqa
    responses = {
        200: "A on-behalf token was successfully created for the service principal.",  # noqa
        400: "The request is malformed.",  # noqa
        500: "The request is not handled correctly due to a server error.",  # noqa
    }

    data = {
        "application_id": application_id,
        "comment": comment,
        "lifetime_seconds": lifetime_seconds,
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.POST,
        responses=responses,
        data=data,
    )
    return result


@task
async def get_tokens(
    databricks_instance: str,
    databricks_credentials: "DatabricksCredentials",
    created_by_id: str = None,
    created_by_username: str = None,
) -> Dict[str, Any]:
    """
    List all tokens belonging to a workspace or a user.

    Args:
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.
        created_by_id:
            User ID of the user that created the token.
        created_by_username:
            Username of the user that created the token.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/token-management/tokens?&created_by_id=%s&created_by_username=%s](
    https://{databricks_instance}/api/2.0/token-management/tokens?&created_by_id=%s&created_by_username=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Tokens were successfully returned. |
    | 401 | The request is unauthorized. |
    | 404 | The requested feature is not available. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/token-management/tokens"  # noqa
    responses = {
        200: "Tokens were successfully returned.",  # noqa
        401: "The request is unauthorized.",  # noqa
        404: "The requested feature is not available.",  # noqa
    }

    params = {
        "created_by_id": created_by_id,
        "created_by_username": created_by_username,
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
async def delete_token(
    databricks_instance: str,
    token_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Delete a token, specified by its ID.

    Args:
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        token_id:
            Token id used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/token-management/tokens/{token_id}?](
    https://{databricks_instance}/api/2.0/token-management/tokens/{token_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The token was successfully deleted. |
    | 401 | The request is unauthorized. |
    | 404 | The requested resource does not exist. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/token-management/tokens/{token_id}"  # noqa
    responses = {
        200: "The token was successfully deleted.",  # noqa
        401: "The request is unauthorized.",  # noqa
        404: "The requested resource does not exist.",  # noqa
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.DELETE,
        responses=responses,
    )
    return result


@task
async def get_token(
    databricks_instance: str,
    token_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Get a token, specified by its ID.

    Args:
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        token_id:
            Token id used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/token-management/tokens/{token_id}?](
    https://{databricks_instance}/api/2.0/token-management/tokens/{token_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Token with specified Token ID was successfully returned. |
    | 401 | The request is unauthorized. |
    | 404 | The requested resource does not exist. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/token-management/tokens/{token_id}"  # noqa
    responses = {
        200: "Token with specified Token ID was successfully returned.",  # noqa
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
