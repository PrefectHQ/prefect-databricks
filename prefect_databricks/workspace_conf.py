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
async def get_workspace_conf(
    databricks_instance: str,
    keys: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    This request gets different information based on what you pass to `keys`
    parameter:  * `enableTokensConfig` — Enable or disable personal access
    tokens for this workspace.  * `maxTokenLifetimeDays` — Get the maximum token
    lifetime in days that a new token can have in a workspace. If set, users
    cannot create new tokens with a lifetime greater than this value.
    **WARNING:** This limit only applies to new tokens, so there may be tokens
    with lifetimes longer than this value, including unlimited lifetime. Such
    tokens may have been created before the current maximum token lifetime was
    set. To review existing tokens, see the [get tokens API](
    operation/get-tokens).

    Args:
        databricks_instance: Databricks instance used in formatting the endpoint URL.
        keys: Pass one of the following:  * `enableTokensConfig` — Enable or disable
            personal access tokens for this workspace.  *
            `maxTokenLifetimeDays` — Get the maximum token lifetime in
            days that a new token can have in a workspace. If set, users
            cannot create new tokens with a lifetime greater than this
            value. **WARNING:** This limit only applies to new tokens,
            so there may be tokens with lifetimes longer than this
            value, including unlimited lifetime. Such tokens may have
            been created before the current maximum token lifetime was
            set. To review existing tokens, see the [get tokens API](
            operation/get-tokens).
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/workspace-conf?&keys=%s](
    https://{databricks_instance}/api/2.0/workspace-conf?&keys=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Getting token lifetime status was returned successfully. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/workspace-conf"  # noqa
    responses = {
        200: "Getting token lifetime status was returned successfully.",  # noqa
    }

    params = {
        "keys": keys,
    }
    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
        **params,
    )
    return result


@task
async def patch_workspace_conf(
    databricks_instance: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    This request sets different workspace settings based on the parameters that you
    set. For example, enable or disable personal access tokens, or set maximum
    token lifetime for new tokens. See parameters for details.

    Args:
        databricks_instance: Databricks instance used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/workspace-conf?](
    https://{databricks_instance}/api/2.0/workspace-conf?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | Configuring maximum token lifetime was successful. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/workspace-conf"  # noqa
    responses = {
        204: "Configuring maximum token lifetime was successful.",  # noqa
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.PATCH,
        responses=responses,
    )
    return result
