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
async def post_mlflow_comments_create(
    databricks_instance: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Make a comment on a model version. A comment can be submitted either by a user
    or programmatically to display relevant information about the model. For
    example, test results or deployment errors.

    Args:
        databricks_instance: Databricks instance used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://{databricks_instance}/api/2.0/mlflow/comments/create?](
    https://{databricks_instance}/api/2.0/mlflow/comments/create?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Comment was made successfully. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/mlflow/comments/create"  # noqa
    responses = {
        200: "Comment was made successfully.",
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.POST,
        responses=responses,
    )
    return result


@task
async def delete_mlflow_comments_delete(
    databricks_instance: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Delete a comment on a model version.

    Args:
        databricks_instance: Databricks instance used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://{databricks_instance}/api/2.0/mlflow/comments/delete?](
    https://{databricks_instance}/api/2.0/mlflow/comments/delete?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Comment was deleted successfully. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/mlflow/comments/delete"  # noqa
    responses = {
        200: "Comment was deleted successfully.",
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.DELETE,
        responses=responses,
    )
    return result


@task
async def post_mlflow_comments_update(
    databricks_instance: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Edit a comment on a model version.

    Args:
        databricks_instance: Databricks instance used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://{databricks_instance}/api/2.0/mlflow/comments/update?](
    https://{databricks_instance}/api/2.0/mlflow/comments/update?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Comment was updated successfully. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/mlflow/comments/update"  # noqa
    responses = {
        200: "Comment was updated successfully.",
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.POST,
        responses=responses,
    )
    return result


@task
async def post_mlflow_databricks_model_versions_transition_stage(
    databricks_instance: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Transition a model version's stage. This is a Databricks version of the [MLflow
    endpoint](https://www.mlflow.org/docs/latest/rest-api.html
    transition-modelversion-stage) that also accepts a comment associated with
    the transition to be recorded.

    Args:
        databricks_instance: Databricks instance used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://{databricks_instance}/api/2.0/mlflow/databricks/model-versions/transition-stage?](
    https://{databricks_instance}/api/2.0/mlflow/databricks/model-versions/transition-stage?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Model version's stage was updated successfully. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/mlflow/databricks/model-versions/transition-stage"  # noqa
    responses = {
        200: "Model version's stage was updated successfully.",
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.POST,
        responses=responses,
    )
    return result


@task
async def get_mlflow_databricks_registered_models_get(
    databricks_instance: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Get the details of a model. This is a Databricks version of the [MLflow
    endpoint](https://www.mlflow.org/docs/latest/rest-api.html
    get-registeredmodel) that also returns the model's Databricks ID and the
    permission level of the requesting user on the model.

    Args:
        databricks_instance: Databricks instance used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://{databricks_instance}/api/2.0/mlflow/databricks/registered-models/get?](
    https://{databricks_instance}/api/2.0/mlflow/databricks/registered-models/get?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Model details were returned successfully. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/mlflow/databricks/registered-models/get"  # noqa
    responses = {
        200: "Model details were returned successfully.",
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result


@task
async def post_mlflow_registry_webhooks_create(
    databricks_instance: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    This endpoint is in Public Preview.  Create a registry webhook.

    Args:
        databricks_instance: Databricks instance used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://{databricks_instance}/api/2.0/mlflow/registry-webhooks/create?](
    https://{databricks_instance}/api/2.0/mlflow/registry-webhooks/create?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Registry webhook was created successfully. |
    """  # noqa
    url = (
        f"https://{databricks_instance}/api/2.0/mlflow/registry-webhooks/create"  # noqa
    )
    responses = {
        200: "Registry webhook was created successfully.",
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.POST,
        responses=responses,
    )
    return result


@task
async def delete_mlflow_registry_webhooks_delete(
    databricks_instance: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    This endpoint is in Public Preview.  Delete a registry webhook.

    Args:
        databricks_instance: Databricks instance used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://{databricks_instance}/api/2.0/mlflow/registry-webhooks/delete?](
    https://{databricks_instance}/api/2.0/mlflow/registry-webhooks/delete?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Registry webhook was deleted successfully. |
    """  # noqa
    url = (
        f"https://{databricks_instance}/api/2.0/mlflow/registry-webhooks/delete"  # noqa
    )
    responses = {
        200: "Registry webhook was deleted successfully.",
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.DELETE,
        responses=responses,
    )
    return result


@task
async def get_mlflow_registry_webhooks_list(
    databricks_instance: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    This endpoint is in Public Preview.  List registry webhooks.

    Args:
        databricks_instance: Databricks instance used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://{databricks_instance}/api/2.0/mlflow/registry-webhooks/list?](
    https://{databricks_instance}/api/2.0/mlflow/registry-webhooks/list?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Registry webhooks listed successfully. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/mlflow/registry-webhooks/list"  # noqa
    responses = {
        200: "Registry webhooks listed successfully.",
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result


@task
async def post_mlflow_registry_webhooks_test(
    databricks_instance: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    This endpoint is in Public Preview.  Test a registry webhook.

    Args:
        databricks_instance: Databricks instance used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://{databricks_instance}/api/2.0/mlflow/registry-webhooks/test?](
    https://{databricks_instance}/api/2.0/mlflow/registry-webhooks/test?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Registry webhook was tested successfully. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/mlflow/registry-webhooks/test"  # noqa
    responses = {
        200: "Registry webhook was tested successfully.",
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.POST,
        responses=responses,
    )
    return result


@task
async def patch_mlflow_registry_webhooks_update(
    databricks_instance: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    This endpoint is in Public Preview.  Update a registry webhook.

    Args:
        databricks_instance: Databricks instance used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://{databricks_instance}/api/2.0/mlflow/registry-webhooks/update?](
    https://{databricks_instance}/api/2.0/mlflow/registry-webhooks/update?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Registry webhook was updated successfully. |
    """  # noqa
    url = (
        f"https://{databricks_instance}/api/2.0/mlflow/registry-webhooks/update"  # noqa
    )
    responses = {
        200: "Registry webhook was updated successfully.",
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.PATCH,
        responses=responses,
    )
    return result


@task
async def post_mlflow_transition_requests_approve(
    databricks_instance: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Approve model version stage transition request.

    Args:
        databricks_instance: Databricks instance used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://{databricks_instance}/api/2.0/mlflow/transition-requests/approve?](
    https://{databricks_instance}/api/2.0/mlflow/transition-requests/approve?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Model version's stage was updated successfully. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/mlflow/transition-requests/approve"  # noqa
    responses = {
        200: "Model version's stage was updated successfully.",
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.POST,
        responses=responses,
    )
    return result


@task
async def post_mlflow_transition_requests_create(
    databricks_instance: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Make a model version stage transition request.

    Args:
        databricks_instance: Databricks instance used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://{databricks_instance}/api/2.0/mlflow/transition-requests/create?](
    https://{databricks_instance}/api/2.0/mlflow/transition-requests/create?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Transition request was made successfully. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/mlflow/transition-requests/create"  # noqa
    responses = {
        200: "Transition request was made successfully.",
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.POST,
        responses=responses,
    )
    return result


@task
async def delete_mlflow_transition_requests_delete(
    databricks_instance: str,
    stage: str,
    creator: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Cancel model version stage transition request.

    Args:
        databricks_instance: Databricks instance used in formatting the endpoint URL.
        stage: Target stage of the transition request. Valid values are:  * `None`: The
            initial stage of a model version.  * `Staging`: Staging or
            pre-production stage.  * `Production`: Production stage.  *
            `Archived`: Archived stage.
        creator: Username of the user who created this request. Of the transition
            requests matching the specified details, only the one
            transition created by this user will be deleted.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://{databricks_instance}/api/2.0/mlflow/transition-requests/delete?&stage=%s&creator=%s](
    https://{databricks_instance}/api/2.0/mlflow/transition-requests/delete?&stage=%s&creator=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Transition request was deleted successfully. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/mlflow/transition-requests/delete"  # noqa
    responses = {
        200: "Transition request was deleted successfully.",
    }

    params = {
        "stage": stage,
        "creator": creator,
    }
    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.DELETE,
        responses=responses,
        **params,
    )
    return result


@task
async def get_mlflow_transition_requests_list(
    databricks_instance: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Get all open stage transition requests for the model version.

    Args:
        databricks_instance: Databricks instance used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://{databricks_instance}/api/2.0/mlflow/transition-requests/list?](
    https://{databricks_instance}/api/2.0/mlflow/transition-requests/list?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Fetched all open requests successfully. |
    """  # noqa
    url = (
        f"https://{databricks_instance}/api/2.0/mlflow/transition-requests/list"  # noqa
    )
    responses = {
        200: "Fetched all open requests successfully.",
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
    )
    return result


@task
async def post_mlflow_transition_requests_reject(
    databricks_instance: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Reject model version stage transition request.

    Args:
        databricks_instance: Databricks instance used in formatting the endpoint URL.
        databricks_credentials: Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    [https://{databricks_instance}/api/2.0/mlflow/transition-requests/reject?](
    https://{databricks_instance}/api/2.0/mlflow/transition-requests/reject?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Transition request was rejected successfully. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/mlflow/transition-requests/reject"  # noqa
    responses = {
        200: "Transition request was rejected successfully.",
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.POST,
        responses=responses,
    )
    return result
