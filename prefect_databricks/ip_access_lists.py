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
async def post_ip_access_lists(
    databricks_instance: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Add an IP access list for this workspace. A list can be an allow list or a block
    list. See the top of this file for a description of how the server treats
    allow lists and block lists at run time.  When creating/updating an IP
    access list:  * For all allow lists and block lists combined, the API
    supports a maximum of 1000 IP/CIDR values, where one CIDR counts as a single
    value. Attempts to exceed that number return error 400 with `error_code`
    value `QUOTA_EXCEEDED`.  * If the new list would block the calling user’s
    current IP, error 400 is returned with `error_code` value `INVALID_STATE`.
    It can take a few minutes for the changes to take effect.  Note that your
    new IP access list has no effect until you enable the feature. See
    [`/workspace-conf`](
    operation/set-status).

    Args:
        databricks_instance: Databricks instance used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/ip-access-lists?](
    https://{databricks_instance}/api/2.0/ip-access-lists?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | An IP access list was successfully created. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/ip-access-lists"  # noqa
    responses = {
        200: "An IP access list was successfully created.",  # noqa
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.POST,
        responses=responses,
    )
    return result


@task
async def get_ip_access_lists(
    databricks_instance: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Get all IP access lists.

    Args:
        databricks_instance: Databricks instance used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/ip-access-lists?](
    https://{databricks_instance}/api/2.0/ip-access-lists?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | IP access lists were successfully returned. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/ip-access-lists"  # noqa
    responses = {
        200: "IP access lists were successfully returned.",  # noqa
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result


@task
async def get_ip_access_lists_ip_access_list_id(
    databricks_instance: str,
    ip_access_list_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Get an IP access list, specified by its list ID.

    Args:
        databricks_instance: Databricks instance used in formatting the endpoint URL.
        ip_access_list_id: Ip access list id used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/ip-access-lists/{ip_access_list_id}?](
    https://{databricks_instance}/api/2.0/ip-access-lists/{ip_access_list_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | An IP access list was successfully returned. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/ip-access-lists/{ip_access_list_id}"  # noqa
    responses = {
        200: "An IP access list was successfully returned.",  # noqa
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result


@task
async def put_ip_access_lists_ip_access_list_id(
    databricks_instance: str,
    ip_access_list_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Replace an IP access list, specified by its ID. A list can include allow lists
    and block lists. See the top of this file for a description of how the
    server treats allow lists and block lists at run time.  When replacing an IP
    access list:  * For all allow lists and block lists combined, the API
    supports a maximum of 1000 IP/CIDR values, where one CIDR counts as a single
    value. Attempts to exceed that number return error 400 with `error_code`
    value `QUOTA_EXCEEDED`.  * If the resulting list would block the calling
    user’s current IP, error 400 is returned with `error_code` value
    `INVALID_STATE`.  It can take a few minutes for the changes to take effect.
    Note that your resulting IP access list has no effect until you enable the
    feature. See [`/workspace-conf`](
    operation/set-status).

    Args:
        databricks_instance: Databricks instance used in formatting the endpoint URL.
        ip_access_list_id: Ip access list id used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/ip-access-lists/{ip_access_list_id}?](
    https://{databricks_instance}/api/2.0/ip-access-lists/{ip_access_list_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The IP access list was successfully replaced. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/ip-access-lists/{ip_access_list_id}"  # noqa
    responses = {
        200: "The IP access list was successfully replaced.",  # noqa
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.PUT,
        responses=responses,
    )
    return result


@task
async def delete_ip_access_lists_ip_access_list_id(
    databricks_instance: str,
    ip_access_list_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Delete an IP access list, specified by its list ID.

    Args:
        databricks_instance: Databricks instance used in formatting the endpoint URL.
        ip_access_list_id: Ip access list id used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/ip-access-lists/{ip_access_list_id}?](
    https://{databricks_instance}/api/2.0/ip-access-lists/{ip_access_list_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The IP access list was successfully deleted. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/ip-access-lists/{ip_access_list_id}"  # noqa
    responses = {
        200: "The IP access list was successfully deleted.",  # noqa
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.DELETE,
        responses=responses,
    )
    return result


@task
async def patch_ip_access_lists_ip_access_list_id(
    databricks_instance: str,
    ip_access_list_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Modify an existing IP access list, specified by its ID. A list can include allow
    lists and block lists. See the top of this file for a description of how the
    server treats allow lists and block lists at run time.  When updating an IP
    access list:  * For all allow lists and block lists combined, the API
    supports a maximum of 1000 IP/CIDR values, where one CIDR counts as a single
    value. Attempts to exceed that number return error 400 with `error_code`
    value `QUOTA_EXCEEDED`.  * If the updated list would block the calling
    user’s current IP, error 400 is returned with `error_code` value
    `INVALID_STATE`.  It can take a few minutes for the changes to take effect.
    Note that your resulting IP access list has no effect until you enable the
    feature. See [`/workspace-conf`](
    operation/set-status).

    Args:
        databricks_instance: Databricks instance used in formatting the endpoint URL.
        ip_access_list_id: Ip access list id used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/ip-access-lists/{ip_access_list_id}?](
    https://{databricks_instance}/api/2.0/ip-access-lists/{ip_access_list_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The IP access list was successfully updated. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/ip-access-lists/{ip_access_list_id}"  # noqa
    responses = {
        200: "The IP access list was successfully updated.",  # noqa
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.PATCH,
        responses=responses,
    )
    return result
