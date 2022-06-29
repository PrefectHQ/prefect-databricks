"""
This is a module for interacting with Databricks REST tasks.
It was auto-generated using prefect-collection-generator so
manually editing this file is not recommended.

OpenAPI spec: ip-access-list-aws.yaml
Updated at: 2022-06-29T19:47:30.865451
"""

from typing import TYPE_CHECKING, Any, Dict, List, Union  # noqa

from prefect import task

from prefect_databricks.rest import HTTPMethod, execute_endpoint

if TYPE_CHECKING:
    from prefect_databricks import DatabricksCredentials
    from prefect_databricks.models import workspace_conf as models


@task
async def get_status(
    keys: str,
    databricks_instance: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Get the IP access list feature status for this Databricks workspace. If the
    feature is disabled for a workspace, access is allowed for this workspace
    for all IP addresses for the web application and REST APIs.  Use the
    separate `/ip-access-lists` endpoint to add a allow list or block list.

    Args:
        keys:
            Always set the value `enableIpAccessLists`, e.g. `enableIpAccessLists`.
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/workspace-conf?&keys=%s](
    https://{databricks_instance}/api/2.0/workspace-conf?&keys=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Status was returned successfully. |
    | 400 | The request is malformed. See the error code and message for details. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/workspace-conf"  # noqa
    responses = {
        200: "Status was returned successfully.",  # noqa
        400: "The request is malformed. See the error code and message for details.",  # noqa
    }

    params = {
        "keys": keys,
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
async def set_status(
    databricks_instance: str,
    databricks_credentials: "DatabricksCredentials",
    enable_ip_access_lists: str = None,
) -> Dict[str, Any]:
    """
    Enable or disable the IP access list feature for this workspace. IP access lists
    affect both web application access and REST API access. If the feature is
    disabled for a workspace, all access is allowed for this workspace.  To add
    an allow list or block list, see [`/ip-access-lists`](
    operation/add-list). It can take a few minutes for the changes to take
    effect.

    Args:
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.
        enable_ip_access_lists:
            The IP access list feature is enabled for the workspace if `true` and it
            is disabled if `false`. Note that these are String values,
            not booleans, e.g. `false`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/workspace-conf?](
    https://{databricks_instance}/api/2.0/workspace-conf?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 204 | Enabling or disabling IP access list was successful. |
    | 400 | The request is malformed. See the error code and message for details. |
    | 401 | The request is unauthorized. |
    | 500 | The request is not handled correctly due to a server error. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/workspace-conf"  # noqa
    responses = {
        204: "Enabling or disabling IP access list was successful.",  # noqa
        400: "The request is malformed. See the error code and message for details.",  # noqa
        401: "The request is unauthorized.",  # noqa
        500: "The request is not handled correctly due to a server error.",  # noqa
    }

    data = {
        "enable_ip_access_lists": enable_ip_access_lists,
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
async def get_configuration(
    keys: str,
    databricks_instance: str,
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
        keys:
            Pass one of the following:  * `enableTokensConfig` — Enable or disable
            personal access tokens for this workspace.  *
            `maxTokenLifetimeDays` — Get the maximum token lifetime in
            days that a new token can have in a workspace. If set, users
            cannot create new tokens with a lifetime greater than this
            value. **WARNING:** This limit only applies to new tokens,
            so there may be tokens with lifetimes longer than this
            value, including unlimited lifetime. Such tokens may have
            been created before the current maximum token lifetime was
            set. To review existing tokens, see the [get tokens API](
            operation/get-tokens), e.g. `maxTokenLifetimeDays`.
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.

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
    | 400 | The request is malformed. See the error code and message for details. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/workspace-conf"  # noqa
    responses = {
        200: "Getting token lifetime status was returned successfully.",  # noqa
        400: "The request is malformed. See the error code and message for details.",  # noqa
    }

    params = {
        "keys": keys,
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
async def set_configuration(
    databricks_instance: str,
    databricks_credentials: "DatabricksCredentials",
    enable_tokens_config: bool = None,
    max_token_lifetime_days: str = None,
) -> Dict[str, Any]:
    """
    This request sets different workspace settings based on the parameters that you
    set. For example, enable or disable personal access tokens, or set maximum
    token lifetime for new tokens. See parameters for details.

    Args:
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.
        enable_tokens_config:
            Enable or disable personal access tokens for this workspace.
        max_token_lifetime_days:
            Maximum token lifetime of new tokens in days, as an integer. If zero,
            new tokens are permitted to have no lifetime limit. Negative
            numbers are unsupported. **WARNING:** This limit only
            applies to new tokens, so there may be tokens with lifetimes
            longer than this value, including unlimited lifetime. Such
            tokens may have been created before the current maximum
            token lifetime was set. To review existing tokens, see the
            [get tokens API](             operation/get-tokens), e.g.
            `90`.

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
    | 400 | The request is malformed. See the error code and message for details. |
    | 401 | The request is unauthorized. |
    | 500 | The request is not handled correctly due to a server error. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/workspace-conf"  # noqa
    responses = {
        204: "Configuring maximum token lifetime was successful.",  # noqa
        400: "The request is malformed. See the error code and message for details.",  # noqa
        401: "The request is unauthorized.",  # noqa
        500: "The request is not handled correctly due to a server error.",  # noqa
    }

    data = {
        "enable_tokens_config": enable_tokens_config,
        "max_token_lifetime_days": max_token_lifetime_days,
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.PATCH,
        responses=responses,
        data=data,
    )
    return result
