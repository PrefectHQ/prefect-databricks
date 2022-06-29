"""
This is a module for interacting with Databricks REST tasks.
It was auto-generated using prefect-collection-generator so
manually editing this file is not recommended.

OpenAPI spec: ip-access-list-aws.yaml
Updated at: 2022-06-29T19:47:30.868496
"""

from typing import TYPE_CHECKING, Any, Dict, List, Union  # noqa

from prefect import task

from prefect_databricks.rest import HTTPMethod, execute_endpoint

if TYPE_CHECKING:
    from prefect_databricks import DatabricksCredentials
    from prefect_databricks.models import ip_access_lists as models


@task
async def add_list(
    databricks_instance: str,
    databricks_credentials: "DatabricksCredentials",
    label: str = None,
    list_type: str = None,
    ip_addresses: str = None,
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
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.
        label:
            Label for the IP access list. This **cannot** be empty, e.g. `Office
            VPN`.
        list_type:
            Type of IP access list. Valid values are as follows and are case-
            sensitive: * `ALLOW` — An allow list. Include this IP or
            range.  * `BLOCK` — A block list. Exclude this IP or range.
            IP addresses in the block list are excluded even if they are
            included in an allow list, e.g. `ALLOW`.
        ip_addresses:
            Array of IP addresses or CIDR values to be added to the IP access list, e.g.
            ```
            ["32.19.112.0", "192.168.100.0/22"]
            ```

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
    | 400 | The request is malformed. |
    | 401 | The request is unauthorized. |
    | 404 | The requested resource does not exist. |
    | 500 | The request is not handled correctly due to a server error. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/ip-access-lists"  # noqa
    responses = {
        200: "An IP access list was successfully created.",  # noqa
        400: "The request is malformed.",  # noqa
        401: "The request is unauthorized.",  # noqa
        404: "The requested resource does not exist.",  # noqa
        500: "The request is not handled correctly due to a server error.",  # noqa
    }

    data = {
        "label": label,
        "list_type": list_type,
        "ip_addresses": ip_addresses,
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
async def get_lists(
    databricks_instance: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Get all IP access lists.

    Args:
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.

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
    | 401 | The request is unauthorized. |
    | 404 | The requested resource does not exist. |
    | 500 | The request is not handled correctly due to a server error. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/ip-access-lists"  # noqa
    responses = {
        200: "IP access lists were successfully returned.",  # noqa
        401: "The request is unauthorized.",  # noqa
        404: "The requested resource does not exist.",  # noqa
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
async def get_list(
    databricks_instance: str,
    ip_access_list_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Get an IP access list, specified by its list ID.

    Args:
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        ip_access_list_id:
            Ip access list id used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.

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
    | 400 | The request is malformed. |
    | 401 | The request is unauthorized. |
    | 404 | The requested resource does not exist. |
    | 500 | The request is not handled correctly due to a server error. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/ip-access-lists/{ip_access_list_id}"  # noqa
    responses = {
        200: "An IP access list was successfully returned.",  # noqa
        400: "The request is malformed.",  # noqa
        401: "The request is unauthorized.",  # noqa
        404: "The requested resource does not exist.",  # noqa
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
async def replace_list(
    databricks_instance: str,
    ip_access_list_id: str,
    databricks_credentials: "DatabricksCredentials",
    list_id: str = None,
    label: str = None,
    list_type: str = None,
    ip_addresses: str = None,
    enabled: str = None,
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
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        ip_access_list_id:
            Ip access list id used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.
        list_id:
            UUID of the IP access list.
        label:
            Label for the IP access list. This **cannot** be empty, e.g. `Office
            VPN`.
        list_type:
            Type of IP access list. Valid values are as follows and are case-
            sensitive: * `ALLOW` — An allow list. Include this IP or
            range.  * `BLOCK` — A block list. Exclude this IP or range.
            IP addresses in the block list are excluded even if they are
            included in an allow list, e.g. `ALLOW`.
        ip_addresses:
            Array of IP addresses or CIDR values to be added to the IP access list, e.g.
            ```
            ["32.19.112.0", "192.168.100.0/22"]
            ```
        enabled:
            Specifies whether this IP access list is enabled.

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
    | 400 | The request is malformed. |
    | 401 | The request is unauthorized. |
    | 404 | The requested resource does not exist. |
    | 500 | The request is not handled correctly due to a server error. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/ip-access-lists/{ip_access_list_id}"  # noqa
    responses = {
        200: "The IP access list was successfully replaced.",  # noqa
        400: "The request is malformed.",  # noqa
        401: "The request is unauthorized.",  # noqa
        404: "The requested resource does not exist.",  # noqa
        500: "The request is not handled correctly due to a server error.",  # noqa
    }

    data = {
        "list_id": list_id,
        "label": label,
        "list_type": list_type,
        "ip_addresses": ip_addresses,
        "enabled": enabled,
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
async def delete_ip_access_lists_ip_access_list_id(
    databricks_instance: str,
    ip_access_list_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Delete an IP access list, specified by its list ID.

    Args:
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        ip_access_list_id:
            Ip access list id used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.

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
    | 400 | The request is malformed. |
    | 401 | The request is unauthorized. |
    | 404 | The requested resource does not exist. |
    | 500 | The request is not handled correctly due to a server error. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/ip-access-lists/{ip_access_list_id}"  # noqa
    responses = {
        200: "The IP access list was successfully deleted.",  # noqa
        400: "The request is malformed.",  # noqa
        401: "The request is unauthorized.",  # noqa
        404: "The requested resource does not exist.",  # noqa
        500: "The request is not handled correctly due to a server error.",  # noqa
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.DELETE,
        responses=responses,
    )
    return result


@task
async def update_list(
    databricks_instance: str,
    ip_access_list_id: str,
    databricks_credentials: "DatabricksCredentials",
    list_id: str = None,
    label: str = None,
    list_type: str = None,
    ip_addresses: str = None,
    enabled: str = None,
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
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        ip_access_list_id:
            Ip access list id used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.
        list_id:
            UUID of the IP access list.
        label:
            Label for the IP access list. This **cannot** be empty, e.g. `Office
            VPN`.
        list_type:
            Type of IP access list. Valid values are as follows and are case-
            sensitive: * `ALLOW` — An allow list. Include this IP or
            range.  * `BLOCK` — A block list. Exclude this IP or range.
            IP addresses in the block list are excluded even if they are
            included in an allow list, e.g. `ALLOW`.
        ip_addresses:
            Array of IP addresses or CIDR values to be added to the IP access list, e.g.
            ```
            ["32.19.112.0", "192.168.100.0/22"]
            ```
        enabled:
            Specifies whether this IP access list is enabled.

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
    | 400 | The request is malformed. |
    | 401 | The request is unauthorized. |
    | 404 | The requested resource does not exist. |
    | 500 | The request is not handled correctly due to a server error. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/ip-access-lists/{ip_access_list_id}"  # noqa
    responses = {
        200: "The IP access list was successfully updated.",  # noqa
        400: "The request is malformed.",  # noqa
        401: "The request is unauthorized.",  # noqa
        404: "The requested resource does not exist.",  # noqa
        500: "The request is not handled correctly due to a server error.",  # noqa
    }

    data = {
        "list_id": list_id,
        "label": label,
        "list_type": list_type,
        "ip_addresses": ip_addresses,
        "enabled": enabled,
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.PATCH,
        responses=responses,
        data=data,
    )
    return result
