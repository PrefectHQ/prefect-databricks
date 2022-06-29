"""
This is a module for interacting with Databricks REST tasks.
It was auto-generated using prefect-collection-generator so
manually editing this file is not recommended.

OpenAPI spec: mlflow-2.0-aws.yaml
Updated at: 2022-06-29T19:47:34.622314
"""

from typing import TYPE_CHECKING, Any, Dict, List, Union  # noqa

from prefect import task

from prefect_databricks.rest import HTTPMethod, execute_endpoint

if TYPE_CHECKING:
    from prefect_databricks import DatabricksCredentials


@task
async def create_comment(
    databricks_instance: str,
    databricks_credentials: "DatabricksCredentials",
    comment: str = None,
    name: str = None,
    version: str = None,
) -> Dict[str, Any]:
    """
    Make a comment on a model version. A comment can be submitted either by a user
    or programmatically to display relevant information about the model. For
    example, test results or deployment errors.

    Args:
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.
        comment:
            User-provided comment on the action, e.g. `This version is great!`.
        name:
            Name of the model, e.g. `search_ads_model`.
        version:
            Version of the model, e.g. `1`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/mlflow/comments/create?](
    https://{databricks_instance}/api/2.0/mlflow/comments/create?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Comment was made successfully. |
    | 400 | The request is malformed. |
    | 403 | The request is forbidden. |
    | 404 | The requested resource does not exist. |
    | 409 | The request conflicts with the current state of the resource. |
    | 500 | The request is not handled correctly due to a server error. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/mlflow/comments/create"  # noqa
    responses = {
        200: "Comment was made successfully.",  # noqa
        400: "The request is malformed.",  # noqa
        403: "The request is forbidden.",  # noqa
        404: "The requested resource does not exist.",  # noqa
        409: "The request conflicts with the current state of the resource.",  # noqa
        500: "The request is not handled correctly due to a server error.",  # noqa
    }

    data = {
        "comment": comment,
        "name": name,
        "version": version,
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
async def delete_comment(
    databricks_instance: str,
    databricks_credentials: "DatabricksCredentials",
    id: str = None,
) -> Dict[str, Any]:
    """
    Delete a comment on a model version.

    Args:
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.
        id:
            Unique identifier of an activity, e.g.
            `6fc74c92704341aaa49e74dcc6031057`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/mlflow/comments/delete?](
    https://{databricks_instance}/api/2.0/mlflow/comments/delete?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Comment was deleted successfully. |
    | 400 | The request is malformed. |
    | 403 | The request is forbidden. |
    | 404 | The requested resource does not exist. |
    | 500 | The request is not handled correctly due to a server error. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/mlflow/comments/delete"  # noqa
    responses = {
        200: "Comment was deleted successfully.",  # noqa
        400: "The request is malformed.",  # noqa
        403: "The request is forbidden.",  # noqa
        404: "The requested resource does not exist.",  # noqa
        500: "The request is not handled correctly due to a server error.",  # noqa
    }

    data = {
        "id": id,
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.DELETE,
        responses=responses,
        data=data,
    )
    return result


@task
async def update_comment(
    databricks_instance: str,
    databricks_credentials: "DatabricksCredentials",
    comment: str = None,
    id: str = None,
) -> Dict[str, Any]:
    """
    Edit a comment on a model version.

    Args:
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.
        comment:
            User-provided comment on the action, e.g. `This version is great!`.
        id:
            Unique identifier of an activity, e.g.
            `6fc74c92704341aaa49e74dcc6031057`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/mlflow/comments/update?](
    https://{databricks_instance}/api/2.0/mlflow/comments/update?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Comment was updated successfully. |
    | 400 | The request is malformed. |
    | 403 | The request is forbidden. |
    | 404 | The requested resource does not exist. |
    | 500 | The request is not handled correctly due to a server error. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/mlflow/comments/update"  # noqa
    responses = {
        200: "Comment was updated successfully.",  # noqa
        400: "The request is malformed.",  # noqa
        403: "The request is forbidden.",  # noqa
        404: "The requested resource does not exist.",  # noqa
        500: "The request is not handled correctly due to a server error.",  # noqa
    }

    data = {
        "comment": comment,
        "id": id,
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
async def transition_model_version_stage(
    databricks_instance: str,
    databricks_credentials: "DatabricksCredentials",
    archive_existing_versions: str = None,
    comment: str = None,
    name: str = None,
    stage: str = None,
    version: str = None,
) -> Dict[str, Any]:
    """
    Transition a model version's stage. This is a Databricks version of the [MLflow
    endpoint](https://www.mlflow.org/docs/latest/rest-api.html
    transition-modelversion-stage) that also accepts a comment associated with
    the transition to be recorded.

    Args:
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.
        archive_existing_versions:
            Specifies whether to archive all current model versions in the target
            stage, e.g. `True`.
        comment:
            User-provided comment on the action, e.g. `This version is great!`.
        name:
            Name of the model, e.g. `search_ads_model`.
        stage:
            Target stage of the transition. Valid values are:  * `None`: The initial
            stage of a model version.  * `Staging`: Staging or pre-
            production stage.  * `Production`: Production stage.  *
            `Archived`: Archived stage.
        version:
            Version of the model, e.g. `1`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/mlflow/databricks/model-versions/transition-stage?](
    https://{databricks_instance}/api/2.0/mlflow/databricks/model-versions/transition-stage?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Model version's stage was updated successfully. |
    | 400 | The request is malformed. |
    | 403 | The request is forbidden. |
    | 404 | The requested resource does not exist. |
    | 409 | The request conflicts with the current state of the resource. |
    | 500 | The request is not handled correctly due to a server error. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/mlflow/databricks/model-versions/transition-stage"  # noqa
    responses = {
        200: "Model version's stage was updated successfully.",  # noqa
        400: "The request is malformed.",  # noqa
        403: "The request is forbidden.",  # noqa
        404: "The requested resource does not exist.",  # noqa
        409: "The request conflicts with the current state of the resource.",  # noqa
        500: "The request is not handled correctly due to a server error.",  # noqa
    }

    data = {
        "archive_existing_versions": archive_existing_versions,
        "comment": comment,
        "name": name,
        "stage": stage,
        "version": version,
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
async def get_registered_model(
    name: str,
    databricks_instance: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Get the details of a model. This is a Databricks version of the [MLflow
    endpoint](https://www.mlflow.org/docs/latest/rest-api.html
    get-registeredmodel) that also returns the model's Databricks ID and the
    permission level of the requesting user on the model.

    Args:
        name:
            Name of the model, e.g. `search_ads_model`.
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/mlflow/databricks/registered-models/get?&name=%s](
    https://{databricks_instance}/api/2.0/mlflow/databricks/registered-models/get?&name=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Model details were returned successfully. |
    | 403 | The request is forbidden. |
    | 404 | The requested resource does not exist. |
    | 500 | The request is not handled correctly due to a server error. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/mlflow/databricks/registered-models/get"  # noqa
    responses = {
        200: "Model details were returned successfully.",  # noqa
        403: "The request is forbidden.",  # noqa
        404: "The requested resource does not exist.",  # noqa
        500: "The request is not handled correctly due to a server error.",  # noqa
    }

    params = {
        "name": name,
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
async def create_registry_webhook(
    databricks_instance: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    This endpoint is in Public Preview.  Create a registry webhook.

    Args:
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/mlflow/registry-webhooks/create?](
    https://{databricks_instance}/api/2.0/mlflow/registry-webhooks/create?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Registry webhook was created successfully. |
    | 400 | The request is malformed. |
    | 403 | The request is forbidden. |
    | 404 | The requested resource does not exist. |
    | 500 | The request is not handled correctly due to a server error. |
    """  # noqa
    url = (
        f"https://{databricks_instance}/api/2.0/mlflow/registry-webhooks/create"  # noqa
    )
    responses = {
        200: "Registry webhook was created successfully.",  # noqa
        400: "The request is malformed.",  # noqa
        403: "The request is forbidden.",  # noqa
        404: "The requested resource does not exist.",  # noqa
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
async def delete_registry_webhook(
    name: str,
    version: str,
    databricks_instance: str,
    databricks_credentials: "DatabricksCredentials",
    id: str = None,
    comment: str = None,
) -> Dict[str, Any]:
    """
    This endpoint is in Public Preview.  Delete a registry webhook.

    Args:
        name:
            Name of the model, e.g. `search_ads_model`.
        version:
            Version of the model, e.g. `1`.
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.
        id:
            Webhook ID, e.g. `124323`.
        comment:
            User-provided comment on the action, e.g. `This version is great!`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/mlflow/registry-webhooks/delete?](
    https://{databricks_instance}/api/2.0/mlflow/registry-webhooks/delete?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Registry webhook was deleted successfully. |
    | 400 | The request is malformed. |
    | 403 | The request is forbidden. |
    | 404 | The requested resource does not exist. |
    | 500 | The request is not handled correctly due to a server error. |
    """  # noqa
    url = (
        f"https://{databricks_instance}/api/2.0/mlflow/registry-webhooks/delete"  # noqa
    )
    responses = {
        200: "Registry webhook was deleted successfully.",  # noqa
        400: "The request is malformed.",  # noqa
        403: "The request is forbidden.",  # noqa
        404: "The requested resource does not exist.",  # noqa
        500: "The request is not handled correctly due to a server error.",  # noqa
    }

    data = {
        "id": id,
        "comment": comment,
        "name": name,
        "version": version,
        "comment": comment,
        "name": name,
        "version": version,
        "comment": comment,
        "name": name,
        "version": version,
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.DELETE,
        responses=responses,
        data=data,
    )
    return result


@task
async def list_registry_webhooks(
    databricks_instance: str,
    databricks_credentials: "DatabricksCredentials",
    events: str = None,
    model_name: str = None,
) -> Dict[str, Any]:
    """
    This endpoint is in Public Preview.  List registry webhooks.

    Args:
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.
        events:
            If `events` is specified, any webhook with one or more of the specified
            trigger events is included in the output. If `events` is not
            specified, webhooks of all event types are included in the
            output.
        model_name:
            If `model_name` is not specified, all webhooks associated with the
            specified events are listed, regardless of their associated
            model.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/mlflow/registry-webhooks/list?](
    https://{databricks_instance}/api/2.0/mlflow/registry-webhooks/list?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Registry webhooks listed successfully. |
    | 400 | The request is malformed. |
    | 403 | The request is forbidden. |
    | 404 | The requested resource does not exist. |
    | 500 | The request is not handled correctly due to a server error. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/mlflow/registry-webhooks/list"  # noqa
    responses = {
        200: "Registry webhooks listed successfully.",  # noqa
        400: "The request is malformed.",  # noqa
        403: "The request is forbidden.",  # noqa
        404: "The requested resource does not exist.",  # noqa
        500: "The request is not handled correctly due to a server error.",  # noqa
    }

    data = {
        "events": events,
        "model_name": model_name,
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.GET,
        responses=responses,
        data=data,
    )
    return result


@task
async def test_registry_webhook(
    databricks_instance: str,
    databricks_credentials: "DatabricksCredentials",
    event: str = None,
    id: str = None,
) -> Dict[str, Any]:
    """
    This endpoint is in Public Preview.  Test a registry webhook.

    Args:
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.
        event:
            If `event` is specified, the test trigger uses the specified event. If
            `event` is not specified, the test trigger uses a randomly
            chosen event associated with the webhook.
        id:
            Webhook ID, e.g. `124323`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/mlflow/registry-webhooks/test?](
    https://{databricks_instance}/api/2.0/mlflow/registry-webhooks/test?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Registry webhook was tested successfully. |
    | 400 | The request is malformed. |
    | 403 | The request is forbidden. |
    | 404 | The requested resource does not exist. |
    | 500 | The request is not handled correctly due to a server error. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/mlflow/registry-webhooks/test"  # noqa
    responses = {
        200: "Registry webhook was tested successfully.",  # noqa
        400: "The request is malformed.",  # noqa
        403: "The request is forbidden.",  # noqa
        404: "The requested resource does not exist.",  # noqa
        500: "The request is not handled correctly due to a server error.",  # noqa
    }

    data = {
        "event": event,
        "id": id,
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
async def update_registry_webhook(
    databricks_instance: str,
    databricks_credentials: "DatabricksCredentials",
    description: str = None,
    events: str = None,
    http_url_spec: str = None,
    id: str = None,
    job_spec: str = None,
    status: str = None,
) -> Dict[str, Any]:
    """
    This endpoint is in Public Preview.  Update a registry webhook.

    Args:
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.
        description:
            User-specified description for the webhook, e.g. `Webhook for comment
            creation`.
        events:
            Events that can trigger a registry webhook: * `MODEL_VERSION_CREATED`: A
            new model version was created for the associated model.  *
            `MODEL_VERSION_TRANSITIONED_STAGE`: A model version’s stage
            was changed.  * `TRANSITION_REQUEST_CREATED`: A user
            requested a model version’s stage be transitioned.  *
            `COMMENT_CREATED`: A user wrote a comment on a registered
            model.  * `REGISTERED_MODEL_CREATED`: A new registered model
            was created. This event type can only be specified for a
            registry-wide webhook, which can be created by not
            specifying a model name in the create request.  *
            `MODEL_VERSION_TAG_SET`: A user set a tag on the model
            version.  * `MODEL_VERSION_TRANSITIONED_TO_STAGING`: A model
            version was transitioned to staging.  *
            `MODEL_VERSION_TRANSITIONED_TO_PRODUCTION`: A model version
            was transitioned to production.  *
            `MODEL_VERSION_TRANSITIONED_TO_ARCHIVED`: A model version
            was archived.  * `TRANSITION_REQUEST_TO_STAGING_CREATED`: A
            user requested a model version be transitioned to staging.
            * `TRANSITION_REQUEST_TO_PRODUCTION_CREATED`: A user
            requested a model version be transitioned to production.  *
            `TRANSITION_REQUEST_TO_ARCHIVED_CREATED`: A user requested a
            model version be archived, e.g.
            ```
            [
                "MODEL_VERSION_CREATED",
                "MODEL_VERSION_TRANSITIONED_TO_STAGING",
                "COMMENT_CREATED",
            ]
            ```
        http_url_spec:
             Key-values:
            - authorization:
                Value of the authorization header that should be sent in the
                request sent by the wehbook. It should be of the form
                `'<auth type> <credentials>'`. If set to an empty string, no
                authorization header will be included in the request, e.g.
                `Bearer <access_token>`.
            - enable_ssl_verification:
                Enable/disable SSL certificate validation. Default is true.
                For self-signed certificates, this field must be false AND
                the destination server must disable certificate validation
                as well. For security purposes, it is encouraged to perform
                secret validation with the HMAC-encoded portion of the
                payload and acknowledge the risk associated with disabling
                hostname validation whereby it becomes more likely that
                requests can be maliciously routed to an unintended host.
            - secret:
                Shared secret required for HMAC encoding payload. The HMAC-
                encoded payload will be sent in the header as: {
                'X-Databricks-Signature': $encoded_payload }, e.g.
                `anyRandomString`.
            - url:
                External HTTPS URL called on event trigger (by using a POST
                request), e.g. `https://hooks.slack.com/services/...`.
        id:
            Webhook ID, e.g. `124323`.
        job_spec:
             Key-values:
            - access_token:
                The personal access token used to authorize webhook's job
                runs, e.g. `dapi12345678935845824`.
            - job_id:
                ID of the job that the webhook runs, e.g. `1`.
            - workspace_url:
                URL of the workspace containing the job that this webhook
                runs. If not specified, the job’s workspace URL is assumed
                to be the same as the workspace where the webhook is
                created, e.g. `<databricks-instance>.cloud.databricks.com`.
        status:
            Enable or disable triggering the webhook, or put the webhook into test
            mode. The default is `ACTIVE`: * `ACTIVE`: Webhook is
            triggered when an associated event happens.  * `DISABLED`:
            Webhook is not triggered.  * `TEST_MODE`: Webhook can be
            triggered through the test endpoint, but is not triggered on
            a real event, e.g. `ACTIVE`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/mlflow/registry-webhooks/update?](
    https://{databricks_instance}/api/2.0/mlflow/registry-webhooks/update?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Registry webhook was updated successfully. |
    | 400 | The request is malformed. |
    | 403 | The request is forbidden. |
    | 404 | The requested resource does not exist. |
    | 500 | The request is not handled correctly due to a server error. |
    """  # noqa
    url = (
        f"https://{databricks_instance}/api/2.0/mlflow/registry-webhooks/update"  # noqa
    )
    responses = {
        200: "Registry webhook was updated successfully.",  # noqa
        400: "The request is malformed.",  # noqa
        403: "The request is forbidden.",  # noqa
        404: "The requested resource does not exist.",  # noqa
        500: "The request is not handled correctly due to a server error.",  # noqa
    }

    data = {
        "description": description,
        "events": events,
        "http_url_spec": http_url_spec,
        "id": id,
        "job_spec": job_spec,
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
async def approve_transition_request(
    databricks_instance: str,
    databricks_credentials: "DatabricksCredentials",
    archive_existing_versions: str = None,
    comment: str = None,
    name: str = None,
    stage: str = None,
    version: str = None,
) -> Dict[str, Any]:
    """
    Approve model version stage transition request.

    Args:
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.
        archive_existing_versions:
            Specifies whether to archive all current model versions in the target
            stage, e.g. `True`.
        comment:
            User-provided comment on the action, e.g. `This version is great!`.
        name:
            Name of the model, e.g. `search_ads_model`.
        stage:
            Target stage of the transition. Valid values are:  * `None`: The initial
            stage of a model version.  * `Staging`: Staging or pre-
            production stage.  * `Production`: Production stage.  *
            `Archived`: Archived stage.
        version:
            Version of the model, e.g. `1`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/mlflow/transition-requests/approve?](
    https://{databricks_instance}/api/2.0/mlflow/transition-requests/approve?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Model version's stage was updated successfully. |
    | 400 | The request is malformed. |
    | 403 | The request is forbidden. |
    | 404 | The requested resource does not exist. |
    | 500 | The request is not handled correctly due to a server error. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/mlflow/transition-requests/approve"  # noqa
    responses = {
        200: "Model version's stage was updated successfully.",  # noqa
        400: "The request is malformed.",  # noqa
        403: "The request is forbidden.",  # noqa
        404: "The requested resource does not exist.",  # noqa
        500: "The request is not handled correctly due to a server error.",  # noqa
    }

    data = {
        "archive_existing_versions": archive_existing_versions,
        "comment": comment,
        "name": name,
        "stage": stage,
        "version": version,
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
async def create_transition_request(
    databricks_instance: str,
    databricks_credentials: "DatabricksCredentials",
    comment: str = None,
    name: str = None,
    stage: str = None,
    version: str = None,
) -> Dict[str, Any]:
    """
    Make a model version stage transition request.

    Args:
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.
        comment:
            User-provided comment on the action, e.g. `This version is great!`.
        name:
            Name of the model, e.g. `search_ads_model`.
        stage:
            Target stage of the transition. Valid values are:  * `None`: The initial
            stage of a model version.  * `Staging`: Staging or pre-
            production stage.  * `Production`: Production stage.  *
            `Archived`: Archived stage.
        version:
            Version of the model, e.g. `1`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/mlflow/transition-requests/create?](
    https://{databricks_instance}/api/2.0/mlflow/transition-requests/create?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Transition request was made successfully. |
    | 400 | The request is malformed. |
    | 403 | The request is forbidden. |
    | 404 | The requested resource does not exist. |
    | 409 | The request conflicts with the current state of the resource. |
    | 500 | The request is not handled correctly due to a server error. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/mlflow/transition-requests/create"  # noqa
    responses = {
        200: "Transition request was made successfully.",  # noqa
        400: "The request is malformed.",  # noqa
        403: "The request is forbidden.",  # noqa
        404: "The requested resource does not exist.",  # noqa
        409: "The request conflicts with the current state of the resource.",  # noqa
        500: "The request is not handled correctly due to a server error.",  # noqa
    }

    data = {
        "comment": comment,
        "name": name,
        "stage": stage,
        "version": version,
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
async def delete_transition_request(
    name: str,
    version: str,
    stage: str,
    creator: str,
    databricks_instance: str,
    databricks_credentials: "DatabricksCredentials",
    comment: str = None,
) -> Dict[str, Any]:
    """
    Cancel model version stage transition request.

    Args:
        name:
            Name of the model, e.g. `search_ads_model`.
        version:
            Version of the model, e.g. `1`.
        stage:
            Target stage of the transition request. Valid values are:  * `None`: The
            initial stage of a model version.  * `Staging`: Staging or
            pre-production stage.  * `Production`: Production stage.  *
            `Archived`: Archived stage, e.g. `Staging`.
        creator:
            Username of the user who created this request. Of the transition
            requests matching the specified details, only the one
            transition created by this user will be deleted, e.g.
            `jane.doe@example.com`.
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.
        comment:
            User-provided comment on the action, e.g. `This version is great!`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/mlflow/transition-requests/delete?&name=%s&version=%s&stage=%s&creator=%s&comment=%s](
    https://{databricks_instance}/api/2.0/mlflow/transition-requests/delete?&name=%s&version=%s&stage=%s&creator=%s&comment=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Transition request was deleted successfully. |
    | 400 | The request is malformed. |
    | 403 | The request is forbidden. |
    | 404 | The requested resource does not exist. |
    | 500 | The request is not handled correctly due to a server error. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/mlflow/transition-requests/delete"  # noqa
    responses = {
        200: "Transition request was deleted successfully.",  # noqa
        400: "The request is malformed.",  # noqa
        403: "The request is forbidden.",  # noqa
        404: "The requested resource does not exist.",  # noqa
        500: "The request is not handled correctly due to a server error.",  # noqa
    }

    params = {
        "name": name,
        "version": version,
        "stage": stage,
        "creator": creator,
        "comment": comment,
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.DELETE,
        params=params,
        responses=responses,
    )
    return result


@task
async def get_transition_requests(
    name: str,
    version: str,
    databricks_instance: str,
    databricks_credentials: "DatabricksCredentials",
) -> Dict[str, Any]:
    """
    Get all open stage transition requests for the model version.

    Args:
        name:
            Name of the model, e.g. `search_ads_model`.
        version:
            Version of the model, e.g. `1`.
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/mlflow/transition-requests/list?&name=%s&version=%s](
    https://{databricks_instance}/api/2.0/mlflow/transition-requests/list?&name=%s&version=%s)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Fetched all open requests successfully. |
    | 400 | The request is malformed. |
    | 403 | The request is forbidden. |
    | 404 | The requested resource does not exist. |
    | 500 | The request is not handled correctly due to a server error. |
    """  # noqa
    url = (
        f"https://{databricks_instance}/api/2.0/mlflow/transition-requests/list"  # noqa
    )
    responses = {
        200: "Fetched all open requests successfully.",  # noqa
        400: "The request is malformed.",  # noqa
        403: "The request is forbidden.",  # noqa
        404: "The requested resource does not exist.",  # noqa
        500: "The request is not handled correctly due to a server error.",  # noqa
    }

    params = {
        "name": name,
        "version": version,
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
async def reject_transition_request(
    databricks_instance: str,
    databricks_credentials: "DatabricksCredentials",
    comment: str = None,
    name: str = None,
    stage: str = None,
    version: str = None,
) -> Dict[str, Any]:
    """
    Reject model version stage transition request.

    Args:
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        databricks_credentials:
            Credentials to use for authentication with Databricks.
        comment:
            User-provided comment on the action, e.g. `This version is great!`.
        name:
            Name of the model, e.g. `search_ads_model`.
        stage:
            Target stage of the transition. Valid values are:  * `None`: The initial
            stage of a model version.  * `Staging`: Staging or pre-
            production stage.  * `Production`: Production stage.  *
            `Archived`: Archived stage.
        version:
            Version of the model, e.g. `1`.

    Returns:
        A dict of the response.

    <h4>API Endpoint URL Format:</h4>
    To format the URL, replace the placeholders, `%s`, with desired values.<br>
    [https://{databricks_instance}/api/2.0/mlflow/transition-requests/reject?](
    https://{databricks_instance}/api/2.0/mlflow/transition-requests/reject?)

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Transition request was rejected successfully. |
    | 400 | The request is malformed. |
    | 403 | The request is forbidden. |
    | 404 | The requested resource does not exist. |
    | 500 | The request is not handled correctly due to a server error. |
    """  # noqa
    url = f"https://{databricks_instance}/api/2.0/mlflow/transition-requests/reject"  # noqa
    responses = {
        200: "Transition request was rejected successfully.",  # noqa
        400: "The request is malformed.",  # noqa
        403: "The request is forbidden.",  # noqa
        404: "The requested resource does not exist.",  # noqa
        500: "The request is not handled correctly due to a server error.",  # noqa
    }

    data = {
        "comment": comment,
        "name": name,
        "stage": stage,
        "version": version,
    }

    result = await execute_endpoint.fn(
        url,
        databricks_credentials,
        http_method=HTTPMethod.POST,
        responses=responses,
        data=data,
    )
    return result
