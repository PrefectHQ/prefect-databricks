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
async def get_accounts_account_id_credentials(
    account_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Get all Databricks credential configurations associated with an account
    specified by ID.

    Args:
        account_id: Account id used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/credentials?](
    https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/credentials?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Credential configurations were returned successfully. |
    """  # noqa
    url = f"https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/credentials"  # noqa
    responses = {
        200: "Credential configurations were returned successfully.",
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result


@task
async def post_accounts_account_id_credentials(
    account_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Create a Databricks credential configuration that represents cloud cross-account
    credentials for a specified account. Databricks uses this to set up network
    infrastructure properly to host Databricks clusters. For your AWS IAM role,
    you need to trust the External ID (the Databricks Account API account ID)
    in the returned credential object, and configure the required access policy.
    Save the response's `credentials_id` field, which is the ID for your new
    credential configuration object.  For detailed instructions of creating a
    new workspace with this API, see [Create a new workspace using the Account
    API](http://docs.databricks.com/administration-guide/account-api/new-
    workspace.html).

    Args:
        account_id: Account id used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/credentials?](
    https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/credentials?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | The credential configuration creation request succeeded. |
    """  # noqa
    url = f"https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/credentials"  # noqa
    responses = {
        201: "The credential configuration creation request succeeded.",
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.POST,
        responses=responses,
    )
    return result


@task
async def get_accounts_account_id_credentials_credentials_id(
    account_id: str,
    credentials_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Get a Databricks credential configuration object for an account, both specified
    by ID.

    Args:
        account_id: Account id used in formatting the endpoint URL.
        credentials_id: Credentials id used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/credentials/{credentials_id}?](
    https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/credentials/{credentials_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The credential configuration was successfully returned. |
    """  # noqa
    url = f"https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/credentials/{credentials_id}"  # noqa
    responses = {
        200: "The credential configuration was successfully returned.",
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result


@task
async def delete_accounts_account_id_credentials_credentials_id(
    account_id: str,
    credentials_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Delete a Databricks credential configuration object for an account, both
    specified by ID. You cannot delete a credential that is associated with any
    workspace.

    Args:
        account_id: Account id used in formatting the endpoint URL.
        credentials_id: Credentials id used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/credentials/{credentials_id}?](
    https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/credentials/{credentials_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The credential configuration was successfully deleted. |
    """  # noqa
    url = f"https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/credentials/{credentials_id}"  # noqa
    responses = {
        200: "The credential configuration was successfully deleted.",
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.DELETE,
        responses=responses,
    )
    return result


@task
async def get_accounts_account_id_storage_configurations(
    account_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Get a list of all Databricks storage configurations for your account, specified
    by ID.

    Args:
        account_id: Account id used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/storage-configurations?](
    https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/storage-configurations?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The storage configurations were successfully returned. |
    """  # noqa
    url = f"https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/storage-configurations"  # noqa
    responses = {
        200: "The storage configurations were successfully returned.",
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result


@task
async def post_accounts_account_id_storage_configurations(
    account_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Create new storage configuration for an account, specified by ID. Uploads a
    storage configuration object that represents the root AWS S3 bucket in your
    account. Databricks stores related workspace assets including DBFS, cluster
    logs, and job results. For AWS S3 bucket, you need to configure the required
    bucket policy.  For detailed instructions of creating a new workspace with
    this API, see [Create a new workspace using the Account
    API](http://docs.databricks.com/administration-guide/account-api/new-
    workspace.html).

    Args:
        account_id: Account id used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/storage-configurations?](
    https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/storage-configurations?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | The storage configuration was successfully created. |
    """  # noqa
    url = f"https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/storage-configurations"  # noqa
    responses = {
        201: "The storage configuration was successfully created.",
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.POST,
        responses=responses,
    )
    return result


@task
async def get_accounts_account_id_storage_configurations_storage_configuration_id(
    account_id: str,
    storage_configuration_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Get a Databricks storage configuration for an account, both specified by ID.

    Args:
        account_id: Account id used in formatting the endpoint URL.
        storage_configuration_id: Storage configuration id used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/storage-configurations/{storage_configuration_id}?](
    https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/storage-configurations/{storage_configuration_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The storage configuration was successfully returned. |
    """  # noqa
    url = f"https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/storage-configurations/{storage_configuration_id}"  # noqa
    responses = {
        200: "The storage configuration was successfully returned.",
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result


@task
async def delete_accounts_account_id_storage_configurations_storage_configuration_id(
    account_id: str,
    storage_configuration_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Delete a Databricks storage configuration. You cannot delete a storage
    configuration that is currently being associated to any workspace.

    Args:
        account_id: Account id used in formatting the endpoint URL.
        storage_configuration_id: Storage configuration id used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/storage-configurations/{storage_configuration_id}?](
    https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/storage-configurations/{storage_configuration_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The storage configuration was successfully deleted. |
    """  # noqa
    url = f"https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/storage-configurations/{storage_configuration_id}"  # noqa
    responses = {
        200: "The storage configuration was successfully deleted.",
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.DELETE,
        responses=responses,
    )
    return result


@task
async def get_accounts_account_id_networks(
    account_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Get a list of all Databricks network configurations for an account, specified by
    ID.  This operation is available only if your account is on the E2 version
    of the platform.

    Args:
        account_id: Account id used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/networks?](
    https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/networks?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The network configurations were successfully returned. |
    """  # noqa
    url = f"https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/networks"  # noqa
    responses = {
        200: "The network configurations were successfully returned.",
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result


@task
async def post_accounts_account_id_networks(
    account_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Create a Databricks network configuration that represents an AWS VPC and its
    resources. The VPC will be used for new Databricks clusters. This requires a
    pre-created VPC and subnets. For VPC requirements, see [Customer-managed
    VPC](http://docs.databricks.com/administration-guide/cloud-
    configurations/aws/customer-managed-vpc.html).  **Important**: You can share
    one customer-managed VPC with multiple workspaces in a single account.
    Therefore, you can share one VPC across multiple Account API network
    configurations. However, you **cannot** reuse subnets or Security Groups
    between workspaces.  Because a Databricks Account API network configuration
    encapsulates this information, you cannot reuse a Databricks Account API
    network configuration across workspaces. If you plan to share one VPC with
    multiple workspaces, be sure to size your VPC and subnets accordingly. For
    detailed instructions of creating a new workspace with this API, see [Create
    a new workspace using the Account
    API](http://docs.databricks.com/administration-guide/account-api/new-
    workspace.html).  This operation is available only if your account is on the
    E2 version of the platform.

    Args:
        account_id: Account id used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/networks?](
    https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/networks?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | The network configuration was successfully created. |
    """  # noqa
    url = f"https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/networks"  # noqa
    responses = {
        201: "The network configuration was successfully created.",
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.POST,
        responses=responses,
    )
    return result


@task
async def get_accounts_account_id_networks_network_id(
    account_id: str,
    network_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Get a Databricks network configuration, which represents an AWS VPC and its
    resources.  This requires a pre-created VPC and subnets. For VPC
    requirements, see [Customer-managed
    VPC](http://docs.databricks.com/administration-guide/cloud-
    configurations/aws/customer-managed-vpc.html).  This operation is available
    only if your account is on the E2 version of the platform.

    Args:
        account_id: Account id used in formatting the endpoint URL.
        network_id: Network id used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/networks/{network_id}?](
    https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/networks/{network_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The network configuration was successfully returned. |
    """  # noqa
    url = f"https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/networks/{network_id}"  # noqa
    responses = {
        200: "The network configuration was successfully returned.",
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result


@task
async def delete_accounts_account_id_networks_network_id(
    account_id: str,
    network_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Delete a Databricks network configuration, which represents an AWS VPC and its
    resources. You cannot delete a network that is associated with a workspace.
    This operation is available only if your account is on the E2 version of the
    platform.

    Args:
        account_id: Account id used in formatting the endpoint URL.
        network_id: Network id used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/networks/{network_id}?](
    https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/networks/{network_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The network configuration was successfully deleted. |
    """  # noqa
    url = f"https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/networks/{network_id}"  # noqa
    responses = {
        200: "The network configuration was successfully deleted.",
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.DELETE,
        responses=responses,
    )
    return result


@task
async def get_accounts_account_id_customer_managed_keys(
    account_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Get all customer-managed key configuration objects for an account. If the key is
    specified as a workspace's managed services customer-managed key, Databricks
    will use the key to encrypt the workspace's notebooks and secrets in the
    control plane, as well as Databricks SQL queries and query history. If the
    key is specified as a workspace's storage customer-managed key, the key is
    used to encrypt the workspace's root S3 bucket and optionally can encrypt
    cluster EBS volumes data in the data plane.  **Important**: Customer-managed
    keys are supported only for some deployment types, subscription types, and
    AWS regions.  This operation is available only if your account is on the E2
    version of the platform.

    Args:
        account_id: Account id used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/customer-managed-keys?](
    https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/customer-managed-keys?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The encryption key configurations were successfully returned. |
    """  # noqa
    url = f"https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/customer-managed-keys"  # noqa
    responses = {
        200: "The encryption key configurations were successfully returned.",
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result


@task
async def post_accounts_account_id_customer_managed_keys(
    account_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Create a customer-managed key configuration object for an account, specified by
    ID. This operation uploads a reference to a customer-managed key to
    Databricks. If the key is assigned as a workspace's customer-managed key for
    managed services, Databricks uses the key to encrypt the workspaces
    notebooks and secrets in the control plane, as well as Databricks SQL
    queries and query history. If it is specified as a workspace's customer-
    managed key for workspace storage, the key encrypts the workspace's root S3
    bucket (which contains the workspace's root DBFS and system data) and
    optionally cluster EBS volume data.  **Important**: Customer-managed keys
    are supported only for some deployment types, subscription types, and AWS
    regions.  This operation is available only if your account is on the E2
    version of the platform or on a select custom plan that allows multiple
    workspaces per account.

    Args:
        account_id: Account id used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/customer-managed-keys?](
    https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/customer-managed-keys?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | The encryption key configuration was successfully created. |
    """  # noqa
    url = f"https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/customer-managed-keys"  # noqa
    responses = {
        201: "The encryption key configuration was successfully created.",
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.POST,
        responses=responses,
    )
    return result


@task
async def get_accounts_account_id_customer_managed_keys_customer_managed_key_id(
    account_id: str,
    customer_managed_key_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Get a customer-managed key configuration object for an account, specified by ID.
    This operation uploads a reference to a customer-managed key to Databricks.
    If assigned as a workspace's customer-managed key for managed services,
    Databricks uses the key to encrypt the workspaces notebooks and secrets in
    the control plane, as well as Databricks SQL queries and query history. If
    it is specified as a workspace's customer-managed key for storage, the key
    encrypts the workspace's root S3 bucket (which contains the workspace's root
    DBFS and system data) and optionally cluster EBS volume data.
    **Important**: Customer-managed keys are supported only for some deployment
    types, subscription types, and AWS regions.  This operation is available
    only if your account is on the E2 version of the platform.

    Args:
        account_id: Account id used in formatting the endpoint URL.
        customer_managed_key_id: Customer managed key id used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/customer-managed-keys/{customer_managed_key_id}?](
    https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/customer-managed-keys/{customer_managed_key_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The encryption key configuration was successfully returned. |
    """  # noqa
    url = f"https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/customer-managed-keys/{customer_managed_key_id}"  # noqa
    responses = {
        200: "The encryption key configuration was successfully returned.",
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result


@task
async def delete_accounts_account_id_customer_managed_keys_customer_managed_key_id(
    account_id: str,
    customer_managed_key_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Delete a customer-managed key configuration object for an account. You cannot
    delete a configuration that is associated with a running workspace.

    Args:
        account_id: Account id used in formatting the endpoint URL.
        customer_managed_key_id: Customer managed key id used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/customer-managed-keys/{customer_managed_key_id}?](
    https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/customer-managed-keys/{customer_managed_key_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The encryption key configuration was successfully deleted. |
    """  # noqa
    url = f"https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/customer-managed-keys/{customer_managed_key_id}"  # noqa
    responses = {
        200: "The encryption key configuration was successfully deleted.",
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.DELETE,
        responses=responses,
    )
    return result


@task
async def get_accounts_account_id_customer_managed_key_history(
    account_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Get a list of records of how key configurations were associated with workspaces.
    **Important**: Customer-managed keys are supported only for some deployment
    types, subscription types, and AWS regions.  This operation is available
    only if your account is on the E2 version of the platform.

    Args:
        account_id: Account id used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/customer-managed-key-history?](
    https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/customer-managed-key-history?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The key's workspace association history was successfully returned. |
    """  # noqa
    url = f"https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/customer-managed-key-history"  # noqa
    responses = {
        200: "The key's workspace association history was successfully returned.",
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result


@task
async def get_accounts_account_id_workspaces(
    account_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Get a list of all workspaces associated with an account, specified by ID.  This
    operation is available only if your account is on the E2 version of the
    platform or on a select custom plan that allows multiple workspaces per
    account.

    Args:
        account_id: Account id used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/workspaces?](
    https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/workspaces?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The workspaces were returned successfully. |
    """  # noqa
    url = f"https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/workspaces"  # noqa
    responses = {
        200: "The workspaces were returned successfully.",
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result


@task
async def post_accounts_account_id_workspaces(
    account_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Create a new workspace using a credential configuration and a storage
    configuration, an optional network configuration (if using a customer-
    managed VPC), an optional managed services key configuration (if using
    customer-managed keys for managed services), and an optional storage key
    configuration (if using customer-managed keys for storage). The key
    configurations used for managed services and storage encryption may be the
    same or different.  **Important**: This operation is asynchronous. A
    response with HTTP status code 200 means the request has been accepted and
    is in progress, but does not mean that the workspace deployed successfully
    and is running. The initial workspace status is typically  `PROVISIONING`.
    Use the workspace ID (`workspace_id`) field in the response to identify the
    new workspace and make repeated `GET` requests with the workspace ID and
    check its status. The workspace becomes available when the status changes to
    `RUNNING`.  You can share one customer-managed VPC with multiple workspaces
    in a single account. It is not required to create a new VPC for each
    workspace. However, you **cannot** reuse subnets or Security Groups between
    workspaces. If you plan to share one VPC with multiple workspaces, be sure
    to size your VPC and subnets accordingly. Because a Databricks Account API
    network configuration encapsulates this information, you cannot reuse a
    Databricks Account API network configuration across workspaces. For detailed
    instructions of creating a new workspace with this API **including error
    handling** see [Create a new workspace using the Account
    API](http://docs.databricks.com/administration-guide/account-api/new-
    workspace.html).  **Important**: Customer-managed VPCs, PrivateLink, and
    customer-managed keys are supported on a limited set of deployment and
    subscription types. If you have questions about availability, contact your
    Databricks representative.  This operation is available only if your account
    is on the E2 version of the platform or on a select custom plan that allows
    multiple workspaces per account.

    Args:
        account_id: Account id used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/workspaces?](
    https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/workspaces?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Workspace creation request was received. Check workspace status. |
    """  # noqa
    url = f"https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/workspaces"  # noqa
    responses = {
        201: "Workspace creation request was received. Check workspace status.",
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.POST,
        responses=responses,
    )
    return result


@task
async def get_accounts_account_id_workspaces_workspace_id(
    account_id: str,
    workspace_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Get information including status for a Databricks workspace, specified by ID. In
    the response, the `workspace_status` field indicates the current status.
    After initial workspace creation (which is asynchronous), make repeated
    `GET` requests with the workspace ID and check its status. The workspace
    becomes available when the status changes to `RUNNING`.  For detailed
    instructions of creating a new workspace with this API **including error
    handling** see [Create a new workspace using the Account
    API](http://docs.databricks.com/administration-guide/account-api/new-
    workspace.html).  This operation is available only if your account is on the
    E2 version of the platform or on a select custom plan that allows multiple
    workspaces per account.

    Args:
        account_id: Account id used in formatting the endpoint URL.
        workspace_id: Workspace id used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/workspaces/{workspace_id}?](
    https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/workspaces/{workspace_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The workspace configuration was successfully returned. |
    """  # noqa
    url = f"https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/workspaces/{workspace_id}"  # noqa
    responses = {
        200: "The workspace configuration was successfully returned.",
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result


@task
async def patch_accounts_account_id_workspaces_workspace_id(
    account_id: str,
    workspace_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    The `PATCH` operation on this endpoint can update a workspace configuration for
    either a running workspace or a failed workspace. The elements that can be
    updated varies between these two use cases.
    Update a failed workspace You can update a Databricks workspace
    configuration for failed workspace deployment for some but not all fields.
    This request supports updating only the following fields of a failed
    workspace: - Credential configuration ID - Storage configuration ID -
    Network configuration ID. Used only if you use customer-managed VPC. - Key
    configuration ID for managed services (control plane storage, such as
    notebook source and Databricks SQL queries). Used only if you use customer-
    managed keys for managed services. - Key configuration ID for workspace
    storage (root S3 bucket and optionally EBS volumes). Used only if you use
    customer-managed keys for workspace storage. IMPORTANT: If the workspace was
    ever in the running state, even if briefly before becoming a failed
    workspace, you cannot add a new key configuration ID for workspace storage.
    After calling the `PATCH` operation to update the workspace configuration,
    make repeated `GET` requests with the workspace ID and check the workspace
    status. The workspace is successful if the status changes to `RUNNING`.  For
    detailed instructions of creating a new workspace with this API **including
    error handling** see [Create a new workspace using the Account
    API](http://docs.databricks.com/administration-guide/account-api/new-
    workspace.html).
    Update a running workspace You can update a Databricks workspace
    configuration for running workspaces for some but not all fields. This
    request supports updating only the following fields of a running workspace:
    - Credential configuration ID  - Network configuration ID. Used only if you
    already use use customer-managed VPC. This change is supported only if you
    specified a network configuration ID in your original workspace creation. In
    other words, you cannot switch from a Databricks-managed VPC to a customer-
    managed VPC. Note: You cannot use a network configuration update in this API
    to add support for PrivateLink (in Public Preview). To add PrivateLink to an
    existing workspace, contact your Databricks representative.
    - Key configuration ID for managed services (control plane storage, such as
    notebook source and Databricks SQL queries). Databricks does not directly
    encrypt the data with the customer-managed key (CMK). Databricks uses both
    the CMK and the Databricks managed key (DMK) that is unique to your
    workspace to encrypt the Data Encryption Key (DEK). Databricks uses the DEK
    to encrypt your workspace's managed services persisted data. If the
    workspace does not already have a CMK for managed services, adding this ID
    enables managed services encryption for new or updated data. Existing
    managed services data that existed before adding the key remains not
    encrypted with the DEK until modified. If the workspace already has
    customer-managed keys for managed services, this request rotates (changes)
    the CMK keys and the DEK is re-encrypted with the DMK and the new CMK. - Key
    configuration ID for workspace storage (root S3 bucket and optionally EBS
    volumes). You can set this only if the workspace does not already have a
    customer-managed key configuration for workspace storage.
    **Important**: For updating running workspaces, this API is unavailable on
    Mondays, Tuesdays, and Thursdays from 4:30pm-7:30pm PST due to routine
    maintenance. Plan your workspace updates accordingly. For questions about
    this schedule, contact your Databricks representative.  **Important**: To
    update a running workspace, your workspace must have no running cluster
    instances, which includes all-purpose clusters, job clusters, and pools that
    may have running clusters. Terminate all cluster instances in the workspace
    before calling this API.
    Wait until changes take effect After calling the `PATCH` operation to update
    the workspace configuration, make repeated `GET` requests with the workspace
    ID and check the workspace status and the status of the fields. * For
    workspaces with a Databricks-managed VPC, the workspace status becomes
    `PROVISIONING` temporarily (typically under 20 minutes). If the workspace
    update is successful, the workspace status changes to `RUNNING`. Note that
    you can also check the workspace status in the [Account
    Console](https://docs.databricks.com/administration-guide/account-
    settings-e2/account-console-e2.html). However, you cannot use or create
    clusters for another 20 minutes after that status change. This results in a
    total of up to 40 minutes in which you cannot create clusters. If you create
    or use clusters before this time interval elapses, clusters do not launch
    successfully, fail, or could cause other unexpected behavior.
    * For workspaces with a customer-managed VPC, the workspace status stays at
    status `RUNNING` and the VPC change happens immediately. A change to the
    storage customer-managed key configuration ID may take a few minutes to
    update, so continue to check the workspace until you observe it has updated.
    If the update fails, the workspace may revert silently to its original
    configuration. Once the workspace has updated, you cannot use or create
    clusters for another 20 minutes. If you create or use clusters before this
    time interval elapses, clusters do not launch successfully, fail, or could
    cause other unexpected behavior.  If you update the _storage_ customer-
    managed key configurations, it takes 20 minutes for the changes to fully
    take effect. During the 20 minute wait, it is important that you stop all
    REST API calls to the DBFS API. If you are modifying _only the managed
    services key configuration_, you can omit the 20 minute wait.
    **Important**: Customer-managed keys and customer-managed VPCs are supported
    by only some deployment types and subscription types. If you have questions
    about availability, contact your Databricks representative.  This operation
    is available only if your account is on the E2 version of the platform or on
    a select custom plan that allows multiple workspaces per account.

    Args:
        account_id: Account id used in formatting the endpoint URL.
        workspace_id: Workspace id used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/workspaces/{workspace_id}?](
    https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/workspaces/{workspace_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The workspace update request is accepted. |
    """  # noqa
    url = f"https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/workspaces/{workspace_id}"  # noqa
    responses = {
        200: "The workspace update request is accepted.",
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.PATCH,
        responses=responses,
    )
    return result


@task
async def delete_accounts_account_id_workspaces_workspace_id(
    account_id: str,
    workspace_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Terminate and delete a Databricks workspace. From an API perspective, deletion
    is immediate. However, it may take a few minutes for all workspaces
    resources to be deleted, depending on the size and number of workspace
    resources.  This operation is available only if your account is on the E2
    version of the platform or on a select custom plan that allows multiple
    workspaces per account.

    Args:
        account_id: Account id used in formatting the endpoint URL.
        workspace_id: Workspace id used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/workspaces/{workspace_id}?](
    https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/workspaces/{workspace_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The workspace was successfully deleted. |
    """  # noqa
    url = f"https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/workspaces/{workspace_id}"  # noqa
    responses = {
        200: "The workspace was successfully deleted.",
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.DELETE,
        responses=responses,
    )
    return result


@task
async def get_accounts_account_id_workspaces_workspace_id_customer_managed_key_history(
    account_id: str,
    workspace_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Given a workspace specified by ID, this request gets a list of all associations
    with key configuration objects that encapsulate customer-managed keys that
    encrypt managed services, workspace storage, or in some cases both.
    **Important**: In the current implementation, keys cannot be rotated or
    removed from a workspace. It is possible for a workspace to show a storage
    customer-managed key having been attached and then detached if the workspace
    was updated to use the key and the update operation failed.  **Important**:
    Customer-managed keys are supported only for some deployment types and
    subscription types.  This operation is available only if your account is on
    the E2 version of the platform.

    Args:
        account_id: Account id used in formatting the endpoint URL.
        workspace_id: Workspace id used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/workspaces/{workspace_id}/customer-managed-key-history?](
    https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/workspaces/{workspace_id}/customer-managed-key-history?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The workspace's key history was successfully returned. |
    """  # noqa
    url = f"https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/workspaces/{workspace_id}/customer-managed-key-history"  # noqa
    responses = {
        200: "The workspace's key history was successfully returned.",
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result


@task
async def get_accounts_account_id_log_delivery(
    account_id: str,
    status: str,
    credentials_id: str,
    storage_configuration_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Get all Databricks log delivery configurations associated with an account
    specified by ID.

    Args:
        account_id: Account id used in formatting the endpoint URL.
        status: Filter by status `ENABLED` or `DISABLED`.
        credentials_id: Filter by credential configuration ID.
        storage_configuration_id: Filter by storage configuration ID.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/log-delivery?&status=%s&credentials_id=%s&storage_configuration_id=%s](
    https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/log-delivery?&status=%s&credentials_id=%s&storage_configuration_id=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Log delivery configurations were returned successfully. |
    """  # noqa
    url = f"https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/log-delivery"  # noqa
    responses = {
        200: "Log delivery configurations were returned successfully.",
    }

    params = {
        "status": status,
        "credentials_id": credentials_id,
        "storage_configuration_id": storage_configuration_id,
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
async def post_accounts_account_id_log_delivery(
    account_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Create a new Databricks log delivery configuration to enable delivery of the
    specified type of logs to your storage location. This requires that you
    already created a [credential object](
    operation/create-credential-config) (which encapsulates a cross-account
    service IAM role) and a [storage configuration object](
    operation/create-storage-config) (which encapsulates an S3 bucket).  For
    full details, including the required IAM role policies and bucket policies,
    see [Billable usage log
    delivery](https://docs.databricks.com/administration-guide/account-
    settings/billable-usage-delivery.html) or [Audit log
    delivery](https://docs.databricks.com/administration-guide/account-
    settings/audit-logs.html).  Note: There is a limit on the number of log
    delivery configurations available per account (each limit applies separately
    to each log type including billable usage and audit logs). You can create a
    maximum of two enabled account-level delivery configurations (configurations
    without a workspace filter) per type. Additionally, you can create two
    enabled workspace level delivery configurations per workspace for each log
    type, meaning the same workspace ID can occur in the workspace filter for no
    more than two delivery configurations per log type.  You cannot delete a log
    delivery configuration, but you can disable it (see [Enable or disable log
    delivery configuration](
    operation/patch-log-delivery-config-status)).

    Args:
        account_id: Account id used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/log-delivery?](
    https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/log-delivery?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The log delivery configuration creation request succeeded. |
    """  # noqa
    url = f"https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/log-delivery"  # noqa
    responses = {
        200: "The log delivery configuration creation request succeeded.",
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.POST,
        responses=responses,
    )
    return result


@task
async def get_accounts_account_id_log_delivery_log_delivery_configuration_id(
    account_id: str,
    log_delivery_configuration_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Get a Databricks log delivery configuration object for an account, both
    specified by ID.

    Args:
        account_id: Account id used in formatting the endpoint URL.
        log_delivery_configuration_id: Log delivery configuration id used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/log-delivery/{log_delivery_configuration_id}?](
    https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/log-delivery/{log_delivery_configuration_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The log delivery configuration was successfully returned. |
    """  # noqa
    url = f"https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/log-delivery/{log_delivery_configuration_id}"  # noqa
    responses = {
        200: "The log delivery configuration was successfully returned.",
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result


@task
async def patch_accounts_account_id_log_delivery_log_delivery_configuration_id(
    account_id: str,
    log_delivery_configuration_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Enable or disable a log delivery configuration. Deletion of delivery
    configurations is not supported, so disable log delivery configurations that
    are no longer needed. Note that you can't re-enable a delivery configuration
    if this would violate the delivery configuration limits described under
    [Create log delivery](
    operation/create-log-delivery-config).

    Args:
        account_id: Account id used in formatting the endpoint URL.
        log_delivery_configuration_id: Log delivery configuration id used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/log-delivery/{log_delivery_configuration_id}?](
    https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/log-delivery/{log_delivery_configuration_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The log delivery configuration was successfully updated. |
    """  # noqa
    url = f"https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/log-delivery/{log_delivery_configuration_id}"  # noqa
    responses = {
        200: "The log delivery configuration was successfully updated.",
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.PATCH,
        responses=responses,
    )
    return result


@task
async def get_accounts_account_id_usage_download(
    account_id: str,
    start_month: str,
    end_month: str,
    personal_data: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Return billable usage logs in CSV format for the specified account and date
    range. See [CSV file schema](https://docs.databricks.com/administration-
    guide/account-settings/billable-usage-delivery.html
    csv-file-schema) for the data schema. Note that this method may take
    multiple seconds to complete.

    Args:
        account_id: Account id used in formatting the endpoint URL.
        start_month: Format: `YYYY-MM`. First month to return billable usage logs for. This
            field is required.
        end_month: Format: `YYYY-MM`. Last month to return billable usage logs for. This
            field is required.
        personal_data: Specify whether to include personally identifiable information in the
            billable usage logs, for example the email addresses of
            cluster creators. Handle this information with care.
            Defaults to false.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/usage/download?&start_month=%s&end_month=%s&personal_data=%s](
    https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/usage/download?&start_month=%s&end_month=%s&personal_data=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Billable usage data was returned successfully. |
    """  # noqa
    url = f"https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/usage/download"  # noqa
    responses = {
        200: "Billable usage data was returned successfully.",
    }

    params = {
        "start_month": start_month,
        "end_month": end_month,
        "personal_data": personal_data,
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
async def post_accounts_account_id_budget(
    account_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Create a new budget in this account.

    Args:
        account_id: Account id used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/budget?](
    https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/budget?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The budget was successfully created. |
    """  # noqa
    url = f"https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/budget"  # noqa
    responses = {
        200: "The budget was successfully created.",
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.POST,
        responses=responses,
    )
    return result


@task
async def get_accounts_account_id_budget(
    account_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Get all budgets associated with this account, including non-cumulative status
    for each day the budget is configured for.

    Args:
        account_id: Account id used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/budget?](
    https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/budget?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The list of budgets was successfully returned. |
    """  # noqa
    url = f"https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/budget"  # noqa
    responses = {
        200: "The list of budgets was successfully returned.",
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result


@task
async def get_accounts_account_id_budget_budget_id(
    account_id: str,
    budget_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Get budget specified by its UUID, including non-cumulative status for each day
    the budget is configured for.

    Args:
        account_id: Account id used in formatting the endpoint URL.
        budget_id: Budget id used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/budget/{budget_id}?](
    https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/budget/{budget_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The budget was successfully returned. |
    """  # noqa
    url = f"https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/budget/{budget_id}"  # noqa
    responses = {
        200: "The budget was successfully returned.",
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result


@task
async def delete_accounts_account_id_budget_budget_id(
    account_id: str,
    budget_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Delete budget specified by its UUID.

    Args:
        account_id: Account id used in formatting the endpoint URL.
        budget_id: Budget id used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/budget/{budget_id}?](
    https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/budget/{budget_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The budget that was successfully deleted. |
    """  # noqa
    url = f"https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/budget/{budget_id}"  # noqa
    responses = {
        200: "The budget that was successfully deleted.",
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.DELETE,
        responses=responses,
    )
    return result


@task
async def patch_accounts_account_id_budget_budget_id(
    account_id: str,
    budget_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Modify a budget in this account. Budget properties will be fully overwritten.

    Args:
        account_id: Account id used in formatting the endpoint URL.
        budget_id: Budget id used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/budget/{budget_id}?](
    https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/budget/{budget_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/budget/{budget_id}"  # noqa
    responses = {}

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.PATCH,
        responses=responses,
    )
    return result


@task
async def get_accounts_account_id_private_access_settings(
    account_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Get a list of all private access settings objects for an account, specified by
    ID.  This operation is available only if your account is on the E2 version
    of the platform and your Databricks account is enabled for PrivateLink
    (Public Preview). Contact your Databricks representative to enable your
    account for PrivateLink.

    Args:
        account_id: Account id used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/private-access-settings?](
    https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/private-access-settings?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The private access settings object was successfully returned. |
    """  # noqa
    url = f"https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/private-access-settings"  # noqa
    responses = {
        200: "The private access settings object was successfully returned.",
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result


@task
async def post_accounts_account_id_private_access_settings(
    account_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Create a private access settings object, which specifies how your workspace is
    accessed over [AWS PrivateLink](https://aws.amazon.com/privatelink). To use
    AWS PrivateLink, a workspace must have a private access settings object
    referenced by ID in the workspace's `private_access_settings_id` property.
    You can share one private access settings with multiple workspaces in a
    single account.However, private access settings are region specific, so only
    workspaces in the same region may use a given private access settings
    object.  Before configuring PrivateLink, it is important to read the
    [Databricks article about
    PrivateLink](https://docs.databricks.com/administration-guide/cloud-
    configurations/aws/privatelink.html).  This operation is available only if
    your account is on the E2 version of the platform and your Databricks
    account is enabled for PrivateLink (Public Preview). Contact your Databricks
    representative to enable your account for PrivateLink.

    Args:
        account_id: Account id used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/private-access-settings?](
    https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/private-access-settings?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The private access settings object was successfully created. |
    """  # noqa
    url = f"https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/private-access-settings"  # noqa
    responses = {
        200: "The private access settings object was successfully created.",
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.POST,
        responses=responses,
    )
    return result


@task
async def get_accounts_account_id_private_access_settings_private_access_settings_id(
    account_id: str,
    private_access_settings_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Get a private access settings object, which specifies how your workspace is
    accessed over [AWS PrivateLink](https://aws.amazon.com/privatelink).  Before
    configuring PrivateLink, it is important to read the [Databricks article
    about PrivateLink](https://docs.databricks.com/administration-guide/cloud-
    configurations/aws/privatelink.html).  This operation is available only if
    your account is on the E2 version of the platform and your Databricks
    account is enabled for PrivateLink (Public Preview). Contact your Databricks
    representative to enable your account for PrivateLink.

    Args:
        account_id: Account id used in formatting the endpoint URL.
        private_access_settings_id: Private access settings id used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/private-access-settings/{private_access_settings_id}?](
    https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/private-access-settings/{private_access_settings_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The private access settings object was successfully returned. |
    """  # noqa
    url = f"https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/private-access-settings/{private_access_settings_id}"  # noqa
    responses = {
        200: "The private access settings object was successfully returned.",
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result


@task
async def delete_accounts_account_id_private_access_settings_private_access_settings_id(
    account_id: str,
    private_access_settings_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Delete a private access settings object, which determines how your workspace is
    accessed over [AWS PrivateLink](https://aws.amazon.com/privatelink).  Before
    configuring PrivateLink, it is important to read the [Databricks article
    about PrivateLink](https://docs.databricks.com/administration-guide/cloud-
    configurations/aws/privatelink.html).  This operation is available only if
    your account is on the E2 version of the platform and your Databricks
    account is enabled for PrivateLink (Public Preview). Contact your Databricks
    representative to enable your account for PrivateLink.

    Args:
        account_id: Account id used in formatting the endpoint URL.
        private_access_settings_id: Private access settings id used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/private-access-settings/{private_access_settings_id}?](
    https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/private-access-settings/{private_access_settings_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The private access settings was successfully deleted. |
    """  # noqa
    url = f"https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/private-access-settings/{private_access_settings_id}"  # noqa
    responses = {
        200: "The private access settings was successfully deleted.",
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.DELETE,
        responses=responses,
    )
    return result


@task
async def put_accounts_account_id_private_access_settings_private_access_settings_id(
    account_id: str,
    private_access_settings_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Update an existing private access settings object, which specifies how your
    workspace is accessed over [AWS
    PrivateLink](https://aws.amazon.com/privatelink). To use AWS PrivateLink, a
    workspace must have a private access settings object referenced by ID in the
    workspace's `private_access_settings_id` property.  This operation fully
    overwrites your existing private access settings object attached to your
    workspaces. All workspaces attached to the private access settings will see
    the effects of any change. If updating `public_access_enabled`,
    `private_access_level`, or `allowed_vpc_endpoint_ids`, effects of the change
    may take a couple minutes to propagate to the workspace API. You can share
    one private access settings with multiple workspaces in a single account.
    However, private access settings are region specific, so only workspaces in
    the same region may use a given private access settings object.  Before
    configuring PrivateLink, it is important to read the [Databricks article
    about PrivateLink](https://docs.databricks.com/administration-guide/cloud-
    configurations/aws/privatelink.html).  This operation is available only if
    your account is on the E2 version of the platform and your Databricks
    account is enabled for PrivateLink (Public Preview). Contact your Databricks
    representative to enable your account for PrivateLink.

    Args:
        account_id: Account id used in formatting the endpoint URL.
        private_access_settings_id: Private access settings id used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/private-access-settings/{private_access_settings_id}?](
    https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/private-access-settings/{private_access_settings_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The private access settings object was successfully updated. |
    """  # noqa
    url = f"https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/private-access-settings/{private_access_settings_id}"  # noqa
    responses = {
        200: "The private access settings object was successfully updated.",
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.PUT,
        responses=responses,
    )
    return result


@task
async def get_accounts_account_id_vpc_endpoints(
    account_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Get a list of all VPC endpoints for an account, specified by ID.  Before
    configuring PrivateLink, it is important to read the [Databricks article
    about PrivateLink](https://docs.databricks.com/administration-guide/cloud-
    configurations/aws/privatelink.html).  This operation is available only if
    your account is on the E2 version of the platform and your Databricks
    account is enabled for PrivateLink (Public Preview). Contact your Databricks
    representative to enable your account for PrivateLink.

    Args:
        account_id: Account id used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/vpc-endpoints?](
    https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/vpc-endpoints?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The VPC endpoints were successfully returned. |
    """  # noqa
    url = f"https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/vpc-endpoints"  # noqa
    responses = {
        200: "The VPC endpoints were successfully returned.",
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result


@task
async def post_accounts_account_id_vpc_endpoints(
    account_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Create a VPC endpoint configuration, which represents a [VPC
    endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-
    endpoints.html) object in AWS used to communicate privately with Databricks
    over [AWS PrivateLink](https://aws.amazon.com/privatelink).  **IMPORTANT**:
    When you register a VPC endpoint to the Databricks workspace VPC endpoint
    service for any workspace, **in this release <Databricks> enables front-end
    (web application and REST API) access from the source network of the VPC
    endpoint to all workspaces in that AWS region in your <Databricks> account
    if the workspaces have any PrivateLink connections in their workspace
    configuration**. If you have questions about this behavior, contact your
    Databricks representative.  Within AWS, your VPC endpoint stays in
    `pendingAcceptance` state until you register it in a VPC endpoint
    configuration through the Account API. Upon doing so, the Databricks
    [endpoint
    service](https://docs.aws.amazon.com/vpc/latest/privatelink/endpoint-
    service.html) automatically accepts the VPC endpoint and it eventually
    transitions to the `available` state.  Before configuring PrivateLink, it is
    important to read the [Databricks article about
    PrivateLink](https://docs.databricks.com/administration-guide/cloud-
    configurations/aws/privatelink.html).  This operation is available only if
    your account is on the E2 version of the platform and your Databricks
    account is enabled for PrivateLink (Public Preview). Contact your Databricks
    representative to enable your account for PrivateLink.

    Args:
        account_id: Account id used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/vpc-endpoints?](
    https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/vpc-endpoints?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The VPC endpoint configuration was successfully created. |
    """  # noqa
    url = f"https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/vpc-endpoints"  # noqa
    responses = {
        200: "The VPC endpoint configuration was successfully created.",
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.POST,
        responses=responses,
    )
    return result


@task
async def get_accounts_account_id_vpc_endpoints_vpc_endpoint_id(
    account_id: str,
    vpc_endpoint_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Get a VPC endpoint configuration, which represents a [VPC
    endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-
    endpoints.html) object in AWS used to communicate privately with Databricks
    over [AWS PrivateLink](https://aws.amazon.com/privatelink).  This operation
    is available only if your account is on the E2 version of the platform and
    your Databricks account is enabled for PrivateLink (Public Preview). Contact
    your Databricks representative to enable your account for PrivateLink.

    Args:
        account_id: Account id used in formatting the endpoint URL.
        vpc_endpoint_id: Vpc endpoint id used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/vpc-endpoints/{vpc_endpoint_id}?](
    https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/vpc-endpoints/{vpc_endpoint_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The VPC endpoint was successfully returned. |
    """  # noqa
    url = f"https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/vpc-endpoints/{vpc_endpoint_id}"  # noqa
    responses = {
        200: "The VPC endpoint was successfully returned.",
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result


@task
async def delete_accounts_account_id_vpc_endpoints_vpc_endpoint_id(
    account_id: str,
    vpc_endpoint_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Delete a VPC endpoint configuration, which represents an [AWS VPC
    endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-
    endpoints.html) that can communicate privately with Databricks over [AWS
    PrivateLink](https://aws.amazon.com/privatelink).  Upon deleting a VPC
    endpoint configuration, the VPC endpoint in AWS changes its state from
    `accepted` to `rejected`, meaning it will no longer be usable from your VPC.
    Before configuring PrivateLink, it is important to read the [Databricks
    article about PrivateLink](https://docs.databricks.com/administration-
    guide/cloud-configurations/aws/privatelink.html).  This operation is
    available only if your account is on the E2 version of the platform and your
    Databricks account is enabled for PrivateLink (Public Preview). Contact your
    Databricks representative to enable your account for PrivateLink.

    Args:
        account_id: Account id used in formatting the endpoint URL.
        vpc_endpoint_id: Vpc endpoint id used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/vpc-endpoints/{vpc_endpoint_id}?](
    https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/vpc-endpoints/{vpc_endpoint_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The VPC endpoint configuration was successfully deleted. |
    """  # noqa
    url = f"https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/vpc-endpoints/{vpc_endpoint_id}"  # noqa
    responses = {
        200: "The VPC endpoint configuration was successfully deleted.",
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.DELETE,
        responses=responses,
    )
    return result
