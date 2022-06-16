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
        account_id:
            Account id used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/credentials?](
    https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/credentials?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Credential configurations were returned successfully. |
    | 401 | The request is unauthenticated. The user's credentials are missing or incorrect. |
    | 404 | The requested resource does not exist. |
    | 500 | The request is not handled correctly due to a server error. |
    """  # noqa
    url = f"https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/credentials"  # noqa
    responses = {
        200: "Credential configurations were returned successfully.",  # noqa
        401: "The request is unauthenticated. The user's credentials are missing or incorrect.",  # noqa
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
async def post_accounts_account_id_credentials(
    account_id: str,
    credentials_name: str,
    aws_credentials: dict,
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
        account_id:
            Account id used in formatting the endpoint URL.
        credentials_name:
            The human-readable name of the credential configuration object, e.g.
            `credential_1`.
        aws_credentials:

        databricks_credentials:
            Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/credentials?](
    https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/credentials?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | The credential configuration creation request succeeded. |
    | 400 | The request is malformed. |
    | 401 | The request is unauthenticated. The user's credentials are missing or incorrect. |
    | 404 | The requested resource does not exist. |
    | 500 | The request is not handled correctly due to a server error. |
    """  # noqa
    url = f"https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/credentials"  # noqa
    responses = {
        201: "The credential configuration creation request succeeded.",  # noqa
        400: "The request is malformed.",  # noqa
        401: "The request is unauthenticated. The user's credentials are missing or incorrect.",  # noqa
        404: "The requested resource does not exist.",  # noqa
        500: "The request is not handled correctly due to a server error.",  # noqa
    }

    data = {
        "credentials_name": credentials_name,
        "aws_credentials": aws_credentials,
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
async def get_accounts_account_id_credentials_credentials_id(
    account_id: str,
    credentials_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Get a Databricks credential configuration object for an account, both specified
    by ID.

    Args:
        account_id:
            Account id used in formatting the endpoint URL.
        credentials_id:
            Credentials id used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/credentials/{credentials_id}?](
    https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/credentials/{credentials_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The credential configuration was successfully returned. |
    | 401 | The request is unauthenticated. The user's credentials are missing or incorrect. |
    | 404 | The requested resource does not exist. |
    | 500 | The request is not handled correctly due to a server error. |
    """  # noqa
    url = f"https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/credentials/{credentials_id}"  # noqa
    responses = {
        200: "The credential configuration was successfully returned.",  # noqa
        401: "The request is unauthenticated. The user's credentials are missing or incorrect.",  # noqa
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
        account_id:
            Account id used in formatting the endpoint URL.
        credentials_id:
            Credentials id used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/credentials/{credentials_id}?](
    https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/credentials/{credentials_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The credential configuration was successfully deleted. |
    | 401 | The request is unauthenticated. The user's credentials are missing or incorrect. |
    | 404 | The requested resource does not exist. |
    | 409 | The request conflicts with the current state of the target resource. |
    | 500 | The request is not handled correctly due to a server error. |
    """  # noqa
    url = f"https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/credentials/{credentials_id}"  # noqa
    responses = {
        200: "The credential configuration was successfully deleted.",  # noqa
        401: "The request is unauthenticated. The user's credentials are missing or incorrect.",  # noqa
        404: "The requested resource does not exist.",  # noqa
        409: "The request conflicts with the current state of the target resource.",  # noqa
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
async def get_accounts_account_id_storage_configurations(
    account_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Get a list of all Databricks storage configurations for your account, specified
    by ID.

    Args:
        account_id:
            Account id used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/storage-configurations?](
    https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/storage-configurations?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The storage configurations were successfully returned. |
    | 401 | The request is unauthenticated. The user's credentials are missing or incorrect. |
    | 404 | The requested resource does not exist. |
    | 500 | The request is not handled correctly due to a server error. |
    """  # noqa
    url = f"https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/storage-configurations"  # noqa
    responses = {
        200: "The storage configurations were successfully returned.",  # noqa
        401: "The request is unauthenticated. The user's credentials are missing or incorrect.",  # noqa
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
async def post_accounts_account_id_storage_configurations(
    account_id: str,
    storage_configuration_name: str,
    root_bucket_info: dict,
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
        account_id:
            Account id used in formatting the endpoint URL.
        storage_configuration_name:
            The human-readable name of the storage configuration, e.g.
            `storage_conf_1`.
        root_bucket_info:
            Root S3 bucket information.
        databricks_credentials:
            Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/storage-configurations?](
    https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/storage-configurations?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | The storage configuration was successfully created. |
    | 400 | The request is malformed. |
    | 401 | The request is unauthenticated. The user's credentials are missing or incorrect. |
    | 404 | The requested resource does not exist. |
    | 500 | The request is not handled correctly due to a server error. |
    """  # noqa
    url = f"https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/storage-configurations"  # noqa
    responses = {
        201: "The storage configuration was successfully created.",  # noqa
        400: "The request is malformed.",  # noqa
        401: "The request is unauthenticated. The user's credentials are missing or incorrect.",  # noqa
        404: "The requested resource does not exist.",  # noqa
        500: "The request is not handled correctly due to a server error.",  # noqa
    }

    data = {
        "storage_configuration_name": storage_configuration_name,
        "root_bucket_info": root_bucket_info,
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
async def get_accounts_account_id_storage_configurations_storage_configuration_id(
    account_id: str,
    storage_configuration_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Get a Databricks storage configuration for an account, both specified by ID.

    Args:
        account_id:
            Account id used in formatting the endpoint URL.
        storage_configuration_id:
            Storage configuration id used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/storage-configurations/{storage_configuration_id}?](
    https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/storage-configurations/{storage_configuration_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The storage configuration was successfully returned. |
    | 401 | The request is unauthenticated. The user's credentials are missing or incorrect. |
    | 404 | The requested resource does not exist. |
    | 500 | The request is not handled correctly due to a server error. |
    """  # noqa
    url = f"https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/storage-configurations/{storage_configuration_id}"  # noqa
    responses = {
        200: "The storage configuration was successfully returned.",  # noqa
        401: "The request is unauthenticated. The user's credentials are missing or incorrect.",  # noqa
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
async def delete_accounts_account_id_storage_configurations_storage_configuration_id(
    account_id: str,
    storage_configuration_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Delete a Databricks storage configuration. You cannot delete a storage
    configuration that is currently being associated to any workspace.

    Args:
        account_id:
            Account id used in formatting the endpoint URL.
        storage_configuration_id:
            Storage configuration id used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/storage-configurations/{storage_configuration_id}?](
    https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/storage-configurations/{storage_configuration_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The storage configuration was successfully deleted. |
    | 401 | The request is unauthenticated. The user's credentials are missing or incorrect. |
    | 404 | The requested resource does not exist. |
    | 409 | The request conflicts with the current state of the target resource. |
    | 500 | The request is not handled correctly due to a server error. |
    """  # noqa
    url = f"https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/storage-configurations/{storage_configuration_id}"  # noqa
    responses = {
        200: "The storage configuration was successfully deleted.",  # noqa
        401: "The request is unauthenticated. The user's credentials are missing or incorrect.",  # noqa
        404: "The requested resource does not exist.",  # noqa
        409: "The request conflicts with the current state of the target resource.",  # noqa
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
async def get_accounts_account_id_networks(
    account_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Get a list of all Databricks network configurations for an account, specified by
    ID.  This operation is available only if your account is on the E2 version
    of the platform.

    Args:
        account_id:
            Account id used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/networks?](
    https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/networks?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The network configurations were successfully returned. |
    | 401 | The request is unauthenticated. The user's credentials are missing or incorrect. |
    | 404 | The requested resource does not exist. |
    | 500 | The request is not handled correctly due to a server error. |
    """  # noqa
    url = f"https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/networks"  # noqa
    responses = {
        200: "The network configurations were successfully returned.",  # noqa
        401: "The request is unauthenticated. The user's credentials are missing or incorrect.",  # noqa
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
async def post_accounts_account_id_networks(
    account_id: str,
    network_name: str,
    vpc_id: str,
    subnet_ids: list,
    security_group_ids: list,
    vpc_endpoints: str,
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
        account_id:
            Account id used in formatting the endpoint URL.
        network_name:
            The human-readable name of the network configuration.
        vpc_id:
            The ID of the VPC associated with this network. VPC IDs can be used in
            multiple network configurations.
        subnet_ids:
            IDs of at least 2 subnets associated with this network. Subnet IDs
            **cannot** be used in multiple network configurations.
        security_group_ids:
            IDs of 1 to 5 security groups associated with this network. Security
            groups IDs **cannot** be used in multiple network
            configurations.
        vpc_endpoints:
            If specified, contains the VPC endpoints used to allow cluster
            communication from this VPC over [AWS
            PrivateLink](https://aws.amazon.com/privatelink/). Key-values:
            - rest_api:
                The VPC endpoint ID used by this Network to access the
                Databricks REST API. Databricks clusters make calls to our
                REST API as part of cluster creation, mlflow tracking, and
                many other features. Thus, this is required even if your
                workspace allows public access to the REST API.  This is a
                list type for future compatibility, but currently only one
                VPC endpoint ID should be supplied.  Note: This is the
                Databricks-specific ID of the VPC endpoint object in the
                Account API, not the AWS VPC endpoint ID that you see for
                your endpoint in the AWS Console.
            - dataplane_relay:
                The VPC endpoint ID used by this Network to access the
                Databricks secure cluster connectivity relay. See [Secure
                Cluster
                Connectivity](https://docs.databricks.com/security/secure-
                cluster-connectivity.html).  This is a list type for future
                compatibility, but currently only one VPC endpoint ID should
                be supplied.  Note: This is the Databricks-specific ID of
                the VPC endpoint object in the Account API, not the AWS VPC
                endpoint ID that you see for your endpoint in the AWS
                Console.
        databricks_credentials:
            Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/networks?](
    https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/networks?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | The network configuration was successfully created. |
    | 400 | The request is malformed. |
    | 401 | The request is unauthenticated. The user's credentials are missing or incorrect. |
    | 404 | The requested resource does not exist. |
    | 500 | The request is not handled correctly due to a server error. |
    """  # noqa
    url = f"https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/networks"  # noqa
    responses = {
        201: "The network configuration was successfully created.",  # noqa
        400: "The request is malformed.",  # noqa
        401: "The request is unauthenticated. The user's credentials are missing or incorrect.",  # noqa
        404: "The requested resource does not exist.",  # noqa
        500: "The request is not handled correctly due to a server error.",  # noqa
    }

    data = {
        "network_name": network_name,
        "vpc_id": vpc_id,
        "subnet_ids": subnet_ids,
        "security_group_ids": security_group_ids,
        "vpc_endpoints": vpc_endpoints,
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
        account_id:
            Account id used in formatting the endpoint URL.
        network_id:
            Network id used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/networks/{network_id}?](
    https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/networks/{network_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The network configuration was successfully returned. |
    | 401 | The request is unauthenticated. The user's credentials are missing or incorrect. |
    | 404 | The requested resource does not exist. |
    | 500 | The request is not handled correctly due to a server error. |
    """  # noqa
    url = f"https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/networks/{network_id}"  # noqa
    responses = {
        200: "The network configuration was successfully returned.",  # noqa
        401: "The request is unauthenticated. The user's credentials are missing or incorrect.",  # noqa
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
        account_id:
            Account id used in formatting the endpoint URL.
        network_id:
            Network id used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/networks/{network_id}?](
    https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/networks/{network_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The network configuration was successfully deleted. |
    | 401 | The request is unauthenticated. The user's credentials are missing or incorrect. |
    | 404 | The requested resource does not exist. |
    | 409 | The request conflicts with the current state of the target resource. |
    | 500 | The request is not handled correctly due to a server error. |
    """  # noqa
    url = f"https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/networks/{network_id}"  # noqa
    responses = {
        200: "The network configuration was successfully deleted.",  # noqa
        401: "The request is unauthenticated. The user's credentials are missing or incorrect.",  # noqa
        404: "The requested resource does not exist.",  # noqa
        409: "The request conflicts with the current state of the target resource.",  # noqa
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
        account_id:
            Account id used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/customer-managed-keys?](
    https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/customer-managed-keys?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The encryption key configurations were successfully returned. |
    | 401 | The request is unauthenticated. The user's credentials are missing or incorrect. |
    | 404 | The requested resource does not exist. |
    | 500 | The request is not handled correctly due to a server error. |
    """  # noqa
    url = f"https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/customer-managed-keys"  # noqa
    responses = {
        200: "The encryption key configurations were successfully returned.",  # noqa
        401: "The request is unauthenticated. The user's credentials are missing or incorrect.",  # noqa
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
async def post_accounts_account_id_customer_managed_keys(
    account_id: str,
    aws_key_info: str,
    use_cases: list,
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
        account_id:
            Account id used in formatting the endpoint URL.
        aws_key_info:
             Key-values:
            - key_arn:
                The AWS KMS key's Amazon Resource Name (ARN). Note that the
                key's AWS region is inferred from the ARN, e.g.
                `arn:aws:kms:us-
                west-2:111122223333:key/0987dcba-09fe-87dc-65ba-
                ab0987654321`.
            - key_alias:
                The AWS KMS key alias, e.g. `alias/projectKey1`.
            - reuse_key_for_cluster_volumes:
                This field applies only if the `use_cases` property includes
                `STORAGE`. If this is set to `true` or omitted, the key is
                also used to encrypt cluster EBS volumes. To not use this
                key also for encrypting EBS volumes, set this to `false`,
                e.g. `True`.
        use_cases:
            The cases that the key can be used for. Include one or both of these
            options:  * `MANAGED_SERVICES`: Encrypts notebook and secret
            data in the control plane  * `STORAGE`: Encrypts the
            workspace's root S3 bucket (root DBFS and system data) and
            optionally cluster EBS volumes, e.g.
            ```
            ["MANAGED_SERVICES", "STORAGE"]
            ```
        databricks_credentials:
            Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/customer-managed-keys?](
    https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/customer-managed-keys?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | The encryption key configuration was successfully created. |
    | 400 | The request is malformed. |
    | 401 | The request is unauthenticated. The user's credentials are missing or incorrect. |
    | 403 | The request is forbidden from being fulfilled. |
    | 404 | The requested resource does not exist. |
    | 500 | The request is not handled correctly due to a server error. |
    """  # noqa
    url = f"https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/customer-managed-keys"  # noqa
    responses = {
        201: "The encryption key configuration was successfully created.",  # noqa
        400: "The request is malformed.",  # noqa
        401: "The request is unauthenticated. The user's credentials are missing or incorrect.",  # noqa
        403: "The request is forbidden from being fulfilled.",  # noqa
        404: "The requested resource does not exist.",  # noqa
        500: "The request is not handled correctly due to a server error.",  # noqa
    }

    data = {
        "aws_key_info": aws_key_info,
        "use_cases": use_cases,
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
        account_id:
            Account id used in formatting the endpoint URL.
        customer_managed_key_id:
            Customer managed key id used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/customer-managed-keys/{customer_managed_key_id}?](
    https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/customer-managed-keys/{customer_managed_key_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The encryption key configuration was successfully returned. |
    | 401 | The request is unauthenticated. The user's credentials are missing or incorrect. |
    | 404 | The requested resource does not exist. |
    | 500 | The request is not handled correctly due to a server error. |
    """  # noqa
    url = f"https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/customer-managed-keys/{customer_managed_key_id}"  # noqa
    responses = {
        200: "The encryption key configuration was successfully returned.",  # noqa
        401: "The request is unauthenticated. The user's credentials are missing or incorrect.",  # noqa
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
async def delete_accounts_account_id_customer_managed_keys_customer_managed_key_id(
    account_id: str,
    customer_managed_key_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Delete a customer-managed key configuration object for an account. You cannot
    delete a configuration that is associated with a running workspace.

    Args:
        account_id:
            Account id used in formatting the endpoint URL.
        customer_managed_key_id:
            Customer managed key id used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/customer-managed-keys/{customer_managed_key_id}?](
    https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/customer-managed-keys/{customer_managed_key_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The encryption key configuration was successfully deleted. |
    | 401 | The request is unauthenticated. The user's credentials are missing or incorrect. |
    | 404 | The requested resource does not exist. |
    | 409 | The request conflicts with the current state of the target resource. |
    | 500 | The request is not handled correctly due to a server error. |
    """  # noqa
    url = f"https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/customer-managed-keys/{customer_managed_key_id}"  # noqa
    responses = {
        200: "The encryption key configuration was successfully deleted.",  # noqa
        401: "The request is unauthenticated. The user's credentials are missing or incorrect.",  # noqa
        404: "The requested resource does not exist.",  # noqa
        409: "The request conflicts with the current state of the target resource.",  # noqa
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
        account_id:
            Account id used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/customer-managed-key-history?](
    https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/customer-managed-key-history?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The key's workspace association history was successfully returned. |
    | 401 | The request is unauthenticated. The user's credentials are missing or incorrect. |
    | 404 | The requested resource does not exist. |
    | 500 | The request is not handled correctly due to a server error. |
    """  # noqa
    url = f"https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/customer-managed-key-history"  # noqa
    responses = {
        200: "The key's workspace association history was successfully returned.",  # noqa
        401: "The request is unauthenticated. The user's credentials are missing or incorrect.",  # noqa
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
        account_id:
            Account id used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/workspaces?](
    https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/workspaces?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The workspaces were returned successfully. |
    | 401 | The request is unauthenticated. The user's credentials are missing or incorrect. |
    | 404 | The requested resource does not exist. |
    | 500 | The request is not handled correctly due to a server error. |
    """  # noqa
    url = f"https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/workspaces"  # noqa
    responses = {
        200: "The workspaces were returned successfully.",  # noqa
        401: "The request is unauthenticated. The user's credentials are missing or incorrect.",  # noqa
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
async def post_accounts_account_id_workspaces(
    account_id: str,
    workspace_name: str,
    deployment_name: str,
    aws_region: str,
    credentials_id: str,
    storage_configuration_id: str,
    network_id: str,
    managed_services_customer_managed_key_id: str,
    private_access_settings_id: str,
    pricing_tier: str,
    storage_customer_managed_key_id: str,
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
        account_id:
            Account id used in formatting the endpoint URL.
        workspace_name:
            The workspace's human-readable name, e.g. `My workspace 1`.
        deployment_name:
            The deployment name defines part of the subdomain for the workspace. The
            workspace URL for web application and REST APIs is
            `<workspace-deployment-name>.cloud.databricks.com`. For
            example, if the deployment name is `abcsales`, your
            workspace URL will be
            `https://abcsales.cloud.databricks.com`. Hyphens are
            allowed.  This property supports only the set of characters
            that are allowed in a subdomain.  If your account has a non-
            empty deployment name prefix at workspace creation time, the
            workspace deployment name changes so that the beginning has
            the account prefix and a hyphen. For example, if your
            account's deployment prefix is `acme` and the workspace
            deployment name is `workspace-1`, the `deployment_name`
            field becomes `acme-workspace-1` and that is the value that
            will be returned in JSON responses for the `deployment_name`
            field. The workspace URL is `acme-
            workspace-1.cloud.databricks.com`.  If your account has a
            non-empty deployment name prefix and you set
            `deployment_name` to the reserved keyword `EMPTY`,
            `deployment_name` is just the account prefix only. For
            example, if your account's deployment prefix is `acme` and
            the workspace deployment name is `EMPTY`, `deployment_name`
            becomes `acme` only and the workspace URL is
            `acme.cloud.databricks.com`.  Contact your Databricks
            representatives to add an account deployment name prefix to
            your account. If you do not have a deployment name prefix,
            the special deployment name value `EMPTY` is invalid.  This
            value must be unique across all non-deleted deployments
            across all AWS regions.  If a new workspace omits this
            property, the server generates a unique deployment name for
            you with the pattern `dbc-xxxxxxxx-xxxx`, e.g. `workspace_1`.
        aws_region:
            The AWS region of the workspace's Data Plane, e.g. `us-west-2`.
        credentials_id:
            ID of the workspace's credential configuration object, e.g.
            `ccc64f28-ebdc-4c89-add9-5dcb6d7727d8`.
        storage_configuration_id:
            The ID of the workspace's storage configuration object, e.g.
            `b43a6064-04c1-4e1c-88b6-d91e5b136b13`.
        network_id:
            The ID of the workspace's network configuration object. To use [AWS
            PrivateLink](https://docs.databricks.com/administration-
            guide/cloud-configurations/aws/privatelink.html) (Public
            Preview), this field is required, e.g.
            `fd0cc5bc-683c-47e9-b15e-144d7744a496`.
        managed_services_customer_managed_key_id:
            The ID of the workspace's managed services encryption key configuration
            object. This is used to encrypt the workspace's notebook and
            secret data in the control plane, as well as Databricks SQL
            queries and query history. The provided key configuration
            object property `use_cases` must contain `MANAGED_SERVICES`,
            e.g. `849b3d6b-e68e-468d-b3e5-deb08b03c56d`.
        private_access_settings_id:
            Only used for PrivateLink, which is in Public Preview. This is the ID of
            the workspace's private access settings object. This ID must
            be specified for customers using [AWS
            PrivateLink](https://aws.amazon.com/privatelink/) for either
            front-end (user-to-workspace connection), back-end (data
            plane to control plane connection), or both connection
            types.  Before configuring PrivateLink, it is important to
            read the [Databricks article about
            PrivateLink](https://docs.databricks.com/administration-
            guide/cloud-configurations/aws/privatelink.html).
        pricing_tier:
            The pricing tier of the workspace. If you do not provide this, the API
            will default to the highest pricing tier available to your
            account. See https://databricks.com/product/aws-pricing for
            available pricing tier information, e.g. `PREMIUM`.
        storage_customer_managed_key_id:
            The ID of the workspace's storage encryption key configuration object.
            This is used to encrypt the workspace's root S3 bucket (root
            DBFS and system data) and optionally cluster EBS volumes.
            The provided key configuration object property `use_cases`
            must contain `STORAGE`.
        databricks_credentials:
            Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/workspaces?](
    https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/workspaces?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 201 | Workspace creation request was received. Check workspace status. |
    | 400 | The request is malformed. |
    | 401 | The request is unauthenticated. The user's credentials are missing or incorrect. |
    | 403 | The request is forbidden from being fulfilled. |
    | 404 | The requested resource does not exist. |
    | 500 | The request is not handled correctly due to a server error. |
    """  # noqa
    url = f"https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/workspaces"  # noqa
    responses = {
        201: "Workspace creation request was received. Check workspace status.",  # noqa
        400: "The request is malformed.",  # noqa
        401: "The request is unauthenticated. The user's credentials are missing or incorrect.",  # noqa
        403: "The request is forbidden from being fulfilled.",  # noqa
        404: "The requested resource does not exist.",  # noqa
        500: "The request is not handled correctly due to a server error.",  # noqa
    }

    data = {
        "workspace_name": workspace_name,
        "deployment_name": deployment_name,
        "aws_region": aws_region,
        "credentials_id": credentials_id,
        "storage_configuration_id": storage_configuration_id,
        "network_id": network_id,
        "managed_services_customer_managed_key_id": managed_services_customer_managed_key_id,  # noqa
        "private_access_settings_id": private_access_settings_id,
        "pricing_tier": pricing_tier,
        "storage_customer_managed_key_id": storage_customer_managed_key_id,
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
        account_id:
            Account id used in formatting the endpoint URL.
        workspace_id:
            Workspace id used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/workspaces/{workspace_id}?](
    https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/workspaces/{workspace_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The workspace configuration was successfully returned. |
    | 401 | The request is unauthenticated. The user's credentials are missing or incorrect. |
    | 404 | The requested resource does not exist. |
    | 500 | The request is not handled correctly due to a server error. |
    """  # noqa
    url = f"https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/workspaces/{workspace_id}"  # noqa
    responses = {
        200: "The workspace configuration was successfully returned.",  # noqa
        401: "The request is unauthenticated. The user's credentials are missing or incorrect.",  # noqa
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
async def patch_accounts_account_id_workspaces_workspace_id(
    account_id: str,
    workspace_id: str,
    aws_region: str,
    credentials_id: str,
    storage_configuration_id: str,
    network_id: str,
    managed_services_customer_managed_key_id: str,
    storage_customer_managed_key_id: str,
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
        account_id:
            Account id used in formatting the endpoint URL.
        workspace_id:
            Workspace id used in formatting the endpoint URL.
        aws_region:
            The AWS region of the workspace's Data Plane. For example, `us-west-2`.
            This parameter is available only for updating failed
            workspaces, e.g. `us-west-2`.
        credentials_id:
            ID of the workspace's credential configuration object. This parameter is
            available for updating both failed and running workspaces.
        storage_configuration_id:
            The ID of the workspace's storage configuration object. This parameter
            is available only for updating failed workspaces.
        network_id:
            The ID of the workspace's network configuration object. Used only if you
            already use a customer-managed VPC. This change is supported
            only if you specified a network configuration ID when the
            workspace was created. In other words, you cannot switch
            from a Databricks-managed VPC to a customer-managed VPC.
            This parameter is available for updating both failed and
            running workspaces. Note: You cannot use a network
            configuration update in this API to add support for
            PrivateLink (in Public Preview). To add PrivateLink to an
            existing workspace, contact your Databricks representative.
        managed_services_customer_managed_key_id:
            The ID of the workspace's managed services encryption key configuration
            object. This parameter is available only for updating failed
            workspaces.
        storage_customer_managed_key_id:
            The ID of the key configuration object for workspace storage. This
            parameter is available for updating both failed and running
            workspaces.
        databricks_credentials:
            Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/workspaces/{workspace_id}?](
    https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/workspaces/{workspace_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The workspace update request is accepted. |
    | 400 | The request is malformed. |
    | 401 | The request is unauthenticated. The user's credentials are missing or incorrect. |
    | 403 | The request is forbidden from being fulfilled. |
    | 404 | The requested resource does not exist. |
    | 409 | The request conflicts with the current state of the target resource. |
    | 500 | The request is not handled correctly due to a server error. |
    | 509 | The service is unavailable. |
    """  # noqa
    url = f"https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/workspaces/{workspace_id}"  # noqa
    responses = {
        200: "The workspace update request is accepted.",  # noqa
        400: "The request is malformed.",  # noqa
        401: "The request is unauthenticated. The user's credentials are missing or incorrect.",  # noqa
        403: "The request is forbidden from being fulfilled.",  # noqa
        404: "The requested resource does not exist.",  # noqa
        409: "The request conflicts with the current state of the target resource.",  # noqa
        500: "The request is not handled correctly due to a server error.",  # noqa
        509: "The service is unavailable.",  # noqa
    }

    data = {
        "aws_region": aws_region,
        "credentials_id": credentials_id,
        "storage_configuration_id": storage_configuration_id,
        "network_id": network_id,
        "managed_services_customer_managed_key_id": managed_services_customer_managed_key_id,  # noqa
        "storage_customer_managed_key_id": storage_customer_managed_key_id,
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
        account_id:
            Account id used in formatting the endpoint URL.
        workspace_id:
            Workspace id used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/workspaces/{workspace_id}?](
    https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/workspaces/{workspace_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The workspace was successfully deleted. |
    | 401 | The request is unauthenticated. The user's credentials are missing or incorrect. |
    | 404 | The requested resource does not exist. |
    | 409 | The request conflicts with the current state of the target resource. |
    | 500 | The request is not handled correctly due to a server error. |
    """  # noqa
    url = f"https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/workspaces/{workspace_id}"  # noqa
    responses = {
        200: "The workspace was successfully deleted.",  # noqa
        401: "The request is unauthenticated. The user's credentials are missing or incorrect.",  # noqa
        404: "The requested resource does not exist.",  # noqa
        409: "The request conflicts with the current state of the target resource.",  # noqa
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
        account_id:
            Account id used in formatting the endpoint URL.
        workspace_id:
            Workspace id used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/workspaces/{workspace_id}/customer-managed-key-history?](
    https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/workspaces/{workspace_id}/customer-managed-key-history?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The workspace's key history was successfully returned. |
    | 400 | The request is malformed. |
    | 401 | The request is unauthenticated. The user's credentials are missing or incorrect. |
    | 500 | The request is not handled correctly due to a server error. |
    """  # noqa
    url = f"https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/workspaces/{workspace_id}/customer-managed-key-history"  # noqa
    responses = {
        200: "The workspace's key history was successfully returned.",  # noqa
        400: "The request is malformed.",  # noqa
        401: "The request is unauthenticated. The user's credentials are missing or incorrect.",  # noqa
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
        account_id:
            Account id used in formatting the endpoint URL.
        status:
            Filter by status `ENABLED` or `DISABLED`.
        credentials_id:
            Filter by credential configuration ID.
        storage_configuration_id:
            Filter by storage configuration ID.
        databricks_credentials:
            Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/log-delivery?&status=%s&credentials_id=%s&storage_configuration_id=%s](
    https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/log-delivery?&status=%s&credentials_id=%s&storage_configuration_id=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Log delivery configurations were returned successfully. |
    | 400 | The request is malformed. |
    | 401 | The request is unauthenticated. The user's credentials are missing or incorrect. |
    | 500 | The request is not handled correctly due to a server error. |
    """  # noqa
    url = f"https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/log-delivery"  # noqa
    responses = {
        200: "Log delivery configurations were returned successfully.",  # noqa
        400: "The request is malformed.",  # noqa
        401: "The request is unauthenticated. The user's credentials are missing or incorrect.",  # noqa
        500: "The request is not handled correctly due to a server error.",  # noqa
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
        params=params,
        responses=responses,
    )
    return result


@task
async def post_accounts_account_id_log_delivery(
    account_id: str,
    log_delivery_configuration: str,
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
        account_id:
            Account id used in formatting the endpoint URL.
        log_delivery_configuration:

        databricks_credentials:
            Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/log-delivery?](
    https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/log-delivery?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The log delivery configuration creation request succeeded. |
    | 400 | The request is malformed. |
    | 401 | The request is unauthenticated. The user's credentials are missing or incorrect. |
    | 404 | The requested resource does not exist. |
    | 500 | The request is not handled correctly due to a server error. |
    """  # noqa
    url = f"https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/log-delivery"  # noqa
    responses = {
        200: "The log delivery configuration creation request succeeded.",  # noqa
        400: "The request is malformed.",  # noqa
        401: "The request is unauthenticated. The user's credentials are missing or incorrect.",  # noqa
        404: "The requested resource does not exist.",  # noqa
        500: "The request is not handled correctly due to a server error.",  # noqa
    }

    data = {
        "log_delivery_configuration": log_delivery_configuration,
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
async def get_accounts_account_id_log_delivery_log_delivery_configuration_id(
    account_id: str,
    log_delivery_configuration_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Get a Databricks log delivery configuration object for an account, both
    specified by ID.

    Args:
        account_id:
            Account id used in formatting the endpoint URL.
        log_delivery_configuration_id:
            Log delivery configuration id used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/log-delivery/{log_delivery_configuration_id}?](
    https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/log-delivery/{log_delivery_configuration_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The log delivery configuration was successfully returned. |
    | 400 | The request is malformed. |
    | 401 | The request is unauthenticated. The user's credentials are missing or incorrect. |
    | 404 | The requested resource does not exist. |
    | 500 | The request is not handled correctly due to a server error. |
    """  # noqa
    url = f"https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/log-delivery/{log_delivery_configuration_id}"  # noqa
    responses = {
        200: "The log delivery configuration was successfully returned.",  # noqa
        400: "The request is malformed.",  # noqa
        401: "The request is unauthenticated. The user's credentials are missing or incorrect.",  # noqa
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
async def patch_accounts_account_id_log_delivery_log_delivery_configuration_id(
    account_id: str,
    log_delivery_configuration_id: str,
    status: str,
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
        account_id:
            Account id used in formatting the endpoint URL.
        log_delivery_configuration_id:
            Log delivery configuration id used in formatting the endpoint URL.
        status:
            Status of log delivery configuration. Set to `ENABLED` (enabled) or
            `DISABLED` (disabled). Defaults to `ENABLED`. You can
            [enable or disable the configuration](
            operation/patch-log-delivery-config-status) later. Deletion
            of a configuration is not supported, so disable a log
            delivery configuration that is no longer needed.
        databricks_credentials:
            Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/log-delivery/{log_delivery_configuration_id}?](
    https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/log-delivery/{log_delivery_configuration_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The log delivery configuration was successfully updated. |
    | 400 | The request is malformed. |
    | 401 | The request is unauthenticated. The user's credentials are missing or incorrect. |
    | 404 | The requested resource does not exist. |
    | 500 | The request is not handled correctly due to a server error. |
    """  # noqa
    url = f"https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/log-delivery/{log_delivery_configuration_id}"  # noqa
    responses = {
        200: "The log delivery configuration was successfully updated.",  # noqa
        400: "The request is malformed.",  # noqa
        401: "The request is unauthenticated. The user's credentials are missing or incorrect.",  # noqa
        404: "The requested resource does not exist.",  # noqa
        500: "The request is not handled correctly due to a server error.",  # noqa
    }

    data = {
        "status": status,
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
async def get_accounts_account_id_usage_download(
    account_id: str,
    start_month: str,
    end_month: str,
    databricks_credentials: "DatabricksCredentials",
    personal_data: bool = False,
) -> Dict[str, Any]:
    """
    Return billable usage logs in CSV format for the specified account and date
    range. See [CSV file schema](https://docs.databricks.com/administration-
    guide/account-settings/billable-usage-delivery.html
    csv-file-schema) for the data schema. Note that this method may take
    multiple seconds to complete.

    Args:
        account_id:
            Account id used in formatting the endpoint URL.
        start_month:
            Format: `YYYY-MM`. First month to return billable usage logs for. This
            field is required.
        end_month:
            Format: `YYYY-MM`. Last month to return billable usage logs for. This
            field is required.
        databricks_credentials:
            Credentials to use for authentication with Databricks.
        personal_data:
            Specify whether to include personally identifiable information in the
            billable usage logs, for example the email addresses of
            cluster creators. Handle this information with care.
            Defaults to false.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/usage/download?&start_month=%s&end_month=%s&personal_data=%s](
    https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/usage/download?&start_month=%s&end_month=%s&personal_data=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Billable usage data was returned successfully. |
    | 400 | The request is malformed. |
    | 401 | The request is unauthenticated. The user's credentials are missing or incorrect. |
    | 500 | The request is not handled correctly due to a server error. |
    """  # noqa
    url = f"https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/usage/download"  # noqa
    responses = {
        200: "Billable usage data was returned successfully.",  # noqa
        400: "The request is malformed.",  # noqa
        401: "The request is unauthenticated. The user's credentials are missing or incorrect.",  # noqa
        500: "The request is not handled correctly due to a server error.",  # noqa
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
        params=params,
        responses=responses,
    )
    return result


@task
async def post_accounts_account_id_budget(
    account_id: str,
    budget: str,
    account_id_dual_use: str,
    account_id_e2: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Create a new budget in this account.

    Args:
        account_id:
            Databricks account ID of any type. For non-E2 account types, get your
            account ID from the [Accounts
            Console](https://docs.databricks.com/administration-
            guide/account-settings/usage.html).
        budget:
            Budget configuration to be created. Key-values:
            - name:
                Human-readable name of the budget.
            - period:
                 Period length in years, months, weeks and/or days.  Examples: `1
                            month`, `30 days`, `1 year, 2 months, 1 week, 2 days`, e.g.
                            `1 month`.
            - start_date:
                Start date of the budget period calculation.
            - end_date:
                Optional end date of the budget.
            - target_amount:
                Target amount of the budget per period in USD, e.g.
                `1234.56`.
            - filter:
                 SQL-like filter expression with workspaceId, SKU and tag. Usage in your
                            account that matches this expression will be counted in this
                            budget.  Supported properties on left-hand side of
                            comparison:  * `workspaceId` - the ID of the workspace  *
                            `sku` - SKU of the cluster, e.g.
                            `STANDARD_ALL_PURPOSE_COMPUTE`   * `tag.tagName`, `tag.'tag
                            name'` - tag of the cluster             Supported comparison
                            operators:  * `=` - equal   * `!=` -             not equal
                            Supported logical operators: `AND`, `OR`.  Examples:  *
                            `workspaceId=123 OR (sku='STANDARD_ALL_PURPOSE_COMPUTE' AND
                            tag.'my tag'='my value')`  * `workspaceId!=456`  *
                            `sku='STANDARD_ALL_PURPOSE_COMPUTE' OR
                            sku='PREMIUM_ALL_PURPOSE_COMPUTE'`  * `tag.name1='value1'
                            AND tag.name2='value2'`, e.g. `workspaceId=123 OR
                            (sku='STANDARD_ALL_PURPOSE_COMPUTE' AND tag.'my tag'='my
                            value')`.
            - alerts:

        account_id_dual_use:
            Databricks account ID. When you create or manage workspaces, your
            account must be on the E2 version of the platform or on a
            select custom plan that allows multiple workspaces per
            account. If you are configuring log delivery, all account
            types are supported. For non-E2 account types, get your
            account ID from the [Accounts
            Console](https://docs.databricks.com/administration-
            guide/account-settings/usage.html).
        account_id_e2:
            Databricks account ID. Your account must be on the E2 version of the
            platform or on a select custom plan that allows multiple
            workspaces per account.
        databricks_credentials:
            Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/budget?](
    https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/budget?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The budget was successfully created. |
    | 401 | The request is unauthenticated. The user's credentials are missing or incorrect. |
    | 404 | The requested resource does not exist. |
    | 500 | The request is not handled correctly due to a server error. |
    """  # noqa
    url = f"https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/budget"  # noqa
    responses = {
        200: "The budget was successfully created.",  # noqa
        401: "The request is unauthenticated. The user's credentials are missing or incorrect.",  # noqa
        404: "The requested resource does not exist.",  # noqa
        500: "The request is not handled correctly due to a server error.",  # noqa
    }

    data = {
        "budget": budget,
        "account_id_dual_use": account_id_dual_use,
        "account_id_e2": account_id_e2,
        "account_id": account_id,
        "account_id_dual_use": account_id_dual_use,
        "account_id_e2": account_id_e2,
        "account_id": account_id,
        "account_id_dual_use": account_id_dual_use,
        "account_id_e2": account_id_e2,
        "account_id": account_id,
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
async def get_accounts_account_id_budget(
    account_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Get all budgets associated with this account, including non-cumulative status
    for each day the budget is configured for.

    Args:
        account_id:
            Account id used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/budget?](
    https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/budget?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The list of budgets was successfully returned. |
    | 401 | The request is unauthenticated. The user's credentials are missing or incorrect. |
    | 404 | The requested resource does not exist. |
    | 500 | The request is not handled correctly due to a server error. |
    """  # noqa
    url = f"https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/budget"  # noqa
    responses = {
        200: "The list of budgets was successfully returned.",  # noqa
        401: "The request is unauthenticated. The user's credentials are missing or incorrect.",  # noqa
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
async def get_accounts_account_id_budget_budget_id(
    account_id: str,
    budget_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Get budget specified by its UUID, including non-cumulative status for each day
    the budget is configured for.

    Args:
        account_id:
            Account id used in formatting the endpoint URL.
        budget_id:
            Budget id used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/budget/{budget_id}?](
    https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/budget/{budget_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The budget was successfully returned. |
    | 401 | The request is unauthenticated. The user's credentials are missing or incorrect. |
    | 404 | The requested resource does not exist. |
    | 500 | The request is not handled correctly due to a server error. |
    """  # noqa
    url = f"https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/budget/{budget_id}"  # noqa
    responses = {
        200: "The budget was successfully returned.",  # noqa
        401: "The request is unauthenticated. The user's credentials are missing or incorrect.",  # noqa
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
async def delete_accounts_account_id_budget_budget_id(
    account_id: str,
    budget_id: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Delete budget specified by its UUID.

    Args:
        account_id:
            Account id used in formatting the endpoint URL.
        budget_id:
            Budget id used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/budget/{budget_id}?](
    https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/budget/{budget_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The budget that was successfully deleted. |
    | 401 | The request is unauthenticated. The user's credentials are missing or incorrect. |
    | 404 | The requested resource does not exist. |
    | 500 | The request is not handled correctly due to a server error. |
    """  # noqa
    url = f"https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/budget/{budget_id}"  # noqa
    responses = {
        200: "The budget that was successfully deleted.",  # noqa
        401: "The request is unauthenticated. The user's credentials are missing or incorrect.",  # noqa
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
async def patch_accounts_account_id_budget_budget_id(
    account_id: str,
    budget_id: str,
    budget: str,
    account_id_dual_use: str,
    account_id_e2: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Modify a budget in this account. Budget properties will be fully overwritten.

    Args:
        account_id:
            Databricks account ID of any type. For non-E2 account types, get your
            account ID from the [Accounts
            Console](https://docs.databricks.com/administration-
            guide/account-settings/usage.html).
        budget_id:
            Budget id used in formatting the endpoint URL.
        budget:
            Budget configuration to be created. Key-values:
            - name:
                Human-readable name of the budget.
            - period:
                 Period length in years, months, weeks and/or days.  Examples: `1
                            month`, `30 days`, `1 year, 2 months, 1 week, 2 days`, e.g.
                            `1 month`.
            - start_date:
                Start date of the budget period calculation.
            - end_date:
                Optional end date of the budget.
            - target_amount:
                Target amount of the budget per period in USD, e.g.
                `1234.56`.
            - filter:
                 SQL-like filter expression with workspaceId, SKU and tag. Usage in your
                            account that matches this expression will be counted in this
                            budget.  Supported properties on left-hand side of
                            comparison:  * `workspaceId` - the ID of the workspace  *
                            `sku` - SKU of the cluster, e.g.
                            `STANDARD_ALL_PURPOSE_COMPUTE`   * `tag.tagName`, `tag.'tag
                            name'` - tag of the cluster             Supported comparison
                            operators:  * `=` - equal   * `!=` -             not equal
                            Supported logical operators: `AND`, `OR`.  Examples:  *
                            `workspaceId=123 OR (sku='STANDARD_ALL_PURPOSE_COMPUTE' AND
                            tag.'my tag'='my value')`  * `workspaceId!=456`  *
                            `sku='STANDARD_ALL_PURPOSE_COMPUTE' OR
                            sku='PREMIUM_ALL_PURPOSE_COMPUTE'`  * `tag.name1='value1'
                            AND tag.name2='value2'`, e.g. `workspaceId=123 OR
                            (sku='STANDARD_ALL_PURPOSE_COMPUTE' AND tag.'my tag'='my
                            value')`.
            - alerts:

        account_id_dual_use:
            Databricks account ID. When you create or manage workspaces, your
            account must be on the E2 version of the platform or on a
            select custom plan that allows multiple workspaces per
            account. If you are configuring log delivery, all account
            types are supported. For non-E2 account types, get your
            account ID from the [Accounts
            Console](https://docs.databricks.com/administration-
            guide/account-settings/usage.html).
        account_id_e2:
            Databricks account ID. Your account must be on the E2 version of the
            platform or on a select custom plan that allows multiple
            workspaces per account.
        databricks_credentials:
            Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/budget/{budget_id}?](
    https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/budget/{budget_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    """  # noqa
    url = f"https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/budget/{budget_id}"  # noqa
    responses = {}

    data = {
        "budget": budget,
        "account_id_dual_use": account_id_dual_use,
        "account_id_e2": account_id_e2,
        "account_id": account_id,
        "account_id_dual_use": account_id_dual_use,
        "account_id_e2": account_id_e2,
        "account_id": account_id,
        "account_id_dual_use": account_id_dual_use,
        "account_id_e2": account_id_e2,
        "account_id": account_id,
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
        account_id:
            Account id used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/private-access-settings?](
    https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/private-access-settings?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The private access settings object was successfully returned. |
    | 401 | The request is unauthenticated. The user's credentials are missing or incorrect. |
    | 404 | The requested resource does not exist. |
    | 500 | The request is not handled correctly due to a server error. |
    """  # noqa
    url = f"https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/private-access-settings"  # noqa
    responses = {
        200: "The private access settings object was successfully returned.",  # noqa
        401: "The request is unauthenticated. The user's credentials are missing or incorrect.",  # noqa
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
async def post_accounts_account_id_private_access_settings(
    account_id: str,
    private_access_settings_name: str,
    region: str,
    allowed_vpc_endpoint_ids: list,
    databricks_credentials: "DatabricksCredentials",
    public_access_enabled: bool = False,
    private_access_level: str = "ANY",
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
        account_id:
            Account id used in formatting the endpoint URL.
        private_access_settings_name:
            The human-readable name of the private access settings object.
        region:
            The AWS region for workspaces associated with this private access
            settings object. This must be a [region that Databricks
            supports for
            PrivateLink](https://docs.databricks.com/administration-
            guide/cloud-configurations/aws/regions.html).
        allowed_vpc_endpoint_ids:
            An array of Databricks VPC endpoint IDs. This is the Databricks ID that
            is returned when registering the VPC endpoint configuration
            in your Databricks account. This is not the ID of the VPC
            endpoint in AWS.  Only used when `private_access_level` is
            set to `ENDPOINT`. This is an allow list of VPC endpoints
            that in your account that can connect to your workspace over
            AWS PrivateLink.  If hybrid access to your workspace is
            enabled by setting `public_access_enabled` to `true`, then
            this control only works for PrivateLink connections. To
            control how your workspace is accessed via public internet,
            see the article for [IP access
            lists](https://docs.databricks.com/security/network/ip-
            access-list.html).
        databricks_credentials:
            Credentials to use for authentication with Databricks.
        public_access_enabled:
            Determines if the workspace can be accessed over public internet. For
            fully private workspaces, you can optionally specify
            `false`, but only if you implement both the front-end and
            the back-end PrivateLink connections. Otherwise, specify
            `true`, which means that public access is still enabled.
        private_access_level:
            The private access level controls which VPC endpoints can connect to the
            UI or API of any workspace that attaches this private access
            settings object. * `ANY` level access lets any VPC endpoint
            connect to your workspace. * `ACCOUNT` level access lets
            only VPC endpoints that are registered in your Databricks
            account connect to your workspace. * `ENDPOINT` level access
            lets only specified VPC endpoints connect to your workspace.
            Please see the `allowed_vpc_endpoint_ids` documentation for
            more details, e.g. `ENDPOINT`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/private-access-settings?](
    https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/private-access-settings?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The private access settings object was successfully created. |
    | 400 | The request is malformed. |
    | 401 | The request is unauthenticated. The user's credentials are missing or incorrect. |
    | 404 | The requested resource does not exist. |
    | 500 | The request is not handled correctly due to a server error. |
    """  # noqa
    url = f"https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/private-access-settings"  # noqa
    responses = {
        200: "The private access settings object was successfully created.",  # noqa
        400: "The request is malformed.",  # noqa
        401: "The request is unauthenticated. The user's credentials are missing or incorrect.",  # noqa
        404: "The requested resource does not exist.",  # noqa
        500: "The request is not handled correctly due to a server error.",  # noqa
    }

    data = {
        "private_access_settings_name": private_access_settings_name,
        "region": region,
        "public_access_enabled": public_access_enabled,
        "private_access_level": private_access_level,
        "allowed_vpc_endpoint_ids": allowed_vpc_endpoint_ids,
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
        account_id:
            Account id used in formatting the endpoint URL.
        private_access_settings_id:
            Private access settings id used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/private-access-settings/{private_access_settings_id}?](
    https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/private-access-settings/{private_access_settings_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The private access settings object was successfully returned. |
    | 401 | The request is unauthenticated. The user's credentials are missing or incorrect. |
    | 404 | The requested resource does not exist. |
    | 500 | The request is not handled correctly due to a server error. |
    """  # noqa
    url = f"https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/private-access-settings/{private_access_settings_id}"  # noqa
    responses = {
        200: "The private access settings object was successfully returned.",  # noqa
        401: "The request is unauthenticated. The user's credentials are missing or incorrect.",  # noqa
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
        account_id:
            Account id used in formatting the endpoint URL.
        private_access_settings_id:
            Private access settings id used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/private-access-settings/{private_access_settings_id}?](
    https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/private-access-settings/{private_access_settings_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The private access settings was successfully deleted. |
    | 401 | The request is unauthenticated. The user's credentials are missing or incorrect. |
    | 404 | The requested resource does not exist. |
    | 409 | The request conflicts with the current state of the target resource. |
    | 500 | The request is not handled correctly due to a server error. |
    """  # noqa
    url = f"https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/private-access-settings/{private_access_settings_id}"  # noqa
    responses = {
        200: "The private access settings was successfully deleted.",  # noqa
        401: "The request is unauthenticated. The user's credentials are missing or incorrect.",  # noqa
        404: "The requested resource does not exist.",  # noqa
        409: "The request conflicts with the current state of the target resource.",  # noqa
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
async def put_accounts_account_id_private_access_settings_private_access_settings_id(
    account_id: str,
    private_access_settings_id: str,
    private_access_settings_name: str,
    region: str,
    allowed_vpc_endpoint_ids: list,
    databricks_credentials: "DatabricksCredentials",
    public_access_enabled: bool = False,
    private_access_level: str = "ANY",
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
        account_id:
            Account id used in formatting the endpoint URL.
        private_access_settings_id:
            Private access settings id used in formatting the endpoint URL.
        private_access_settings_name:
            The human-readable name of the private access settings object.
        region:
            The AWS region for workspaces associated with this private access
            settings object. This must be a [region that Databricks
            supports for
            PrivateLink](https://docs.databricks.com/administration-
            guide/cloud-configurations/aws/regions.html).
        allowed_vpc_endpoint_ids:
            An array of Databricks VPC endpoint IDs. This is the Databricks ID that
            is returned when registering the VPC endpoint configuration
            in your Databricks account. This is not the ID of the VPC
            endpoint in AWS.  Only used when `private_access_level` is
            set to `ENDPOINT`. This is an allow list of VPC endpoints
            that in your account that can connect to your workspace over
            AWS PrivateLink.  If hybrid access to your workspace is
            enabled by setting `public_access_enabled` to `true`, then
            this control only works for PrivateLink connections. To
            control how your workspace is accessed via public internet,
            see the article for [IP access
            lists](https://docs.databricks.com/security/network/ip-
            access-list.html).
        databricks_credentials:
            Credentials to use for authentication with Databricks.
        public_access_enabled:
            Determines if the workspace can be accessed over public internet. For
            fully private workspaces, you can optionally specify
            `false`, but only if you implement both the front-end and
            the back-end PrivateLink connections. Otherwise, specify
            `true`, which means that public access is still enabled.
        private_access_level:
            The private access level controls which VPC endpoints can connect to the
            UI or API of any workspace that attaches this private access
            settings object. * `ANY` level access lets any VPC endpoint
            connect to your workspace. * `ACCOUNT` level access lets
            only VPC endpoints that are registered in your Databricks
            account connect to your workspace. * `ENDPOINT` level access
            lets only specified VPC endpoints connect to your workspace.
            Please see the `allowed_vpc_endpoint_ids` documentation for
            more details, e.g. `ENDPOINT`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/private-access-settings/{private_access_settings_id}?](
    https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/private-access-settings/{private_access_settings_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The private access settings object was successfully updated. |
    | 400 | The request is malformed. |
    | 401 | The request is unauthenticated. The user's credentials are missing or incorrect. |
    | 404 | The requested resource does not exist. |
    | 500 | The request is not handled correctly due to a server error. |
    """  # noqa
    url = f"https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/private-access-settings/{private_access_settings_id}"  # noqa
    responses = {
        200: "The private access settings object was successfully updated.",  # noqa
        400: "The request is malformed.",  # noqa
        401: "The request is unauthenticated. The user's credentials are missing or incorrect.",  # noqa
        404: "The requested resource does not exist.",  # noqa
        500: "The request is not handled correctly due to a server error.",  # noqa
    }

    data = {
        "private_access_settings_name": private_access_settings_name,
        "region": region,
        "public_access_enabled": public_access_enabled,
        "private_access_level": private_access_level,
        "allowed_vpc_endpoint_ids": allowed_vpc_endpoint_ids,
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
        account_id:
            Account id used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/vpc-endpoints?](
    https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/vpc-endpoints?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The VPC endpoints were successfully returned. |
    | 401 | The request is unauthenticated. The user's credentials are missing or incorrect. |
    | 404 | The requested resource does not exist. |
    | 500 | The request is not handled correctly due to a server error. |
    """  # noqa
    url = f"https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/vpc-endpoints"  # noqa
    responses = {
        200: "The VPC endpoints were successfully returned.",  # noqa
        401: "The request is unauthenticated. The user's credentials are missing or incorrect.",  # noqa
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
async def post_accounts_account_id_vpc_endpoints(
    account_id: str,
    vpc_endpoint_name: str,
    aws_vpc_endpoint_id: str,
    region: str,
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
        account_id:
            Account id used in formatting the endpoint URL.
        vpc_endpoint_name:
            The human-readable name of the storage configuration.
        aws_vpc_endpoint_id:
            The ID of the VPC endpoint object in AWS.
        region:
            The AWS region in which this VPC endpoint object exists.
        databricks_credentials:
            Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/vpc-endpoints?](
    https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/vpc-endpoints?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The VPC endpoint configuration was successfully created. |
    | 400 | The request is malformed. |
    | 401 | The request is unauthenticated. The user's credentials are missing or incorrect. |
    | 404 | The requested resource does not exist. |
    | 500 | The request is not handled correctly due to a server error. |
    """  # noqa
    url = f"https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/vpc-endpoints"  # noqa
    responses = {
        200: "The VPC endpoint configuration was successfully created.",  # noqa
        400: "The request is malformed.",  # noqa
        401: "The request is unauthenticated. The user's credentials are missing or incorrect.",  # noqa
        404: "The requested resource does not exist.",  # noqa
        500: "The request is not handled correctly due to a server error.",  # noqa
    }

    data = {
        "vpc_endpoint_name": vpc_endpoint_name,
        "aws_vpc_endpoint_id": aws_vpc_endpoint_id,
        "region": region,
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
        account_id:
            Account id used in formatting the endpoint URL.
        vpc_endpoint_id:
            Vpc endpoint id used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/vpc-endpoints/{vpc_endpoint_id}?](
    https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/vpc-endpoints/{vpc_endpoint_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The VPC endpoint was successfully returned. |
    | 401 | The request is unauthenticated. The user's credentials are missing or incorrect. |
    | 404 | The requested resource does not exist. |
    | 500 | The request is not handled correctly due to a server error. |
    """  # noqa
    url = f"https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/vpc-endpoints/{vpc_endpoint_id}"  # noqa
    responses = {
        200: "The VPC endpoint was successfully returned.",  # noqa
        401: "The request is unauthenticated. The user's credentials are missing or incorrect.",  # noqa
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
        account_id:
            Account id used in formatting the endpoint URL.
        vpc_endpoint_id:
            Vpc endpoint id used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/vpc-endpoints/{vpc_endpoint_id}?](
    https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/vpc-endpoints/{vpc_endpoint_id}?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | The VPC endpoint configuration was successfully deleted. |
    | 401 | The request is unauthenticated. The user's credentials are missing or incorrect. |
    | 404 | The requested resource does not exist. |
    | 409 | The request conflicts with the current state of the target resource. |
    | 500 | The request is not handled correctly due to a server error. |
    """  # noqa
    url = f"https://accounts.cloud.databricks.com/api/2.0/accounts/{account_id}/vpc-endpoints/{vpc_endpoint_id}"  # noqa
    responses = {
        200: "The VPC endpoint configuration was successfully deleted.",  # noqa
        401: "The request is unauthenticated. The user's credentials are missing or incorrect.",  # noqa
        404: "The requested resource does not exist.",  # noqa
        409: "The request conflicts with the current state of the target resource.",  # noqa
        500: "The request is not handled correctly due to a server error.",  # noqa
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.DELETE,
        responses=responses,
    )
    return result
