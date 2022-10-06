"""
This is a module containing tasks for interacting with:
Databricks jobs
"""

# This module was auto-generated using prefect-collection-generator so
# manually editing this file is not recommended. If this module
# is outdated, rerun scripts/generate.py.

# OpenAPI spec: jobs-2.1-aws.yaml
# Updated at: 2022-10-06T01:13:18.902464

from typing import Any, Dict, List, Optional, Union  # noqa

from prefect import task

from prefect_databricks import DatabricksCredentials
from prefect_databricks.models import jobs as models  # noqa
from prefect_databricks.rest._generated import (
    HTTPMethod,
    _unpack_contents,
    execute_endpoint,
)


@task
async def jobs_create(
    databricks_credentials: "DatabricksCredentials",
    name: str = "Untitled",
    tags: Dict = None,
    tasks: Optional[List["models.JobTaskSettings"]] = None,
    job_clusters: Optional[List["models.JobCluster"]] = None,
    email_notifications: "models.JobEmailNotifications" = None,
    timeout_seconds: Optional[int] = None,
    schedule: "models.CronSchedule" = None,
    max_concurrent_runs: Optional[int] = None,
    git_source: "models.GitSource" = None,
    format: Optional[str] = None,
    access_control_list: Optional[List["models.AccessControlRequest"]] = None,
) -> Dict[str, Any]:  # pragma: no cover
    """
    Create a new job.

    Args:
        databricks_credentials:
            Credentials to use for authentication with Databricks.
        name:
            An optional name for the job, e.g. `A multitask job`.
        tags:
            A map of tags associated with the job. These are forwarded to the
            cluster as cluster tags for jobs clusters, and are subject
            to the same limitations as cluster tags. A maximum of 25
            tags can be added to the job, e.g.
            ```
            {"cost-center": "engineering", "team": "jobs"}
            ```
        tasks:
            A list of task specifications to be executed by this job, e.g.
            ```
            [
                {
                    "task_key": "Sessionize",
                    "description": "Extracts session data from events",
                    "depends_on": [],
                    "existing_cluster_id": "0923-164208-meows279",
                    "spark_jar_task": {
                        "main_class_name": "com.databricks.Sessionize",
                        "parameters": ["--data", "dbfs:/path/to/data.json"],
                    },
                    "libraries": [{"jar": "dbfs:/mnt/databricks/Sessionize.jar"}],
                    "timeout_seconds": 86400,
                    "max_retries": 3,
                    "min_retry_interval_millis": 2000,
                    "retry_on_timeout": False,
                },
                {
                    "task_key": "Orders_Ingest",
                    "description": "Ingests order data",
                    "depends_on": [],
                    "job_cluster_key": "auto_scaling_cluster",
                    "spark_jar_task": {
                        "main_class_name": "com.databricks.OrdersIngest",
                        "parameters": ["--data", "dbfs:/path/to/order-data.json"],
                    },
                    "libraries": [{"jar": "dbfs:/mnt/databricks/OrderIngest.jar"}],
                    "timeout_seconds": 86400,
                    "max_retries": 3,
                    "min_retry_interval_millis": 2000,
                    "retry_on_timeout": False,
                },
                {
                    "task_key": "Match",
                    "description": "Matches orders with user sessions",
                    "depends_on": [
                        {"task_key": "Orders_Ingest"},
                        {"task_key": "Sessionize"},
                    ],
                    "new_cluster": {
                        "spark_version": "7.3.x-scala2.12",
                        "node_type_id": "i3.xlarge",
                        "spark_conf": {"spark.speculation": True},
                        "aws_attributes": {
                            "availability": "SPOT",
                            "zone_id": "us-west-2a",
                        },
                        "autoscale": {"min_workers": 2, "max_workers": 16},
                    },
                    "notebook_task": {
                        "notebook_path": "/Users/user.name@databricks.com/Match",
                        "source": "WORKSPACE",
                        "base_parameters": {"name": "John Doe", "age": "35"},
                    },
                    "timeout_seconds": 86400,
                    "max_retries": 3,
                    "min_retry_interval_millis": 2000,
                    "retry_on_timeout": False,
                },
            ]
            ```
        job_clusters:
            A list of job cluster specifications that can be shared and reused by
            tasks of this job. Libraries cannot be declared in a shared
            job cluster. You must declare dependent libraries in task
            settings, e.g.
            ```
            [
                {
                    "job_cluster_key": "auto_scaling_cluster",
                    "new_cluster": {
                        "spark_version": "7.3.x-scala2.12",
                        "node_type_id": "i3.xlarge",
                        "spark_conf": {"spark.speculation": True},
                        "aws_attributes": {
                            "availability": "SPOT",
                            "zone_id": "us-west-2a",
                        },
                        "autoscale": {"min_workers": 2, "max_workers": 16},
                    },
                }
            ]
            ```
        email_notifications:
            An optional set of email addresses that is notified when runs of this
            job begin or complete as well as when this job is deleted.
            The default behavior is to not send any emails. Key-values:
            - on_start:
                A list of email addresses to be notified when a run begins.
                If not specified on job creation, reset, or update, the list
                is empty, and notifications are not sent, e.g.
                ```
                ["user.name@databricks.com"]
                ```
            - on_success:
                A list of email addresses to be notified when a run
                successfully completes. A run is considered to have
                completed successfully if it ends with a `TERMINATED`
                `life_cycle_state` and a `SUCCESSFUL` result_state. If not
                specified on job creation, reset, or update, the list is
                empty, and notifications are not sent, e.g.
                ```
                ["user.name@databricks.com"]
                ```
            - on_failure:
                A list of email addresses to be notified when a run
                unsuccessfully completes. A run is considered to have
                completed unsuccessfully if it ends with an `INTERNAL_ERROR`
                `life_cycle_state` or a `SKIPPED`, `FAILED`, or `TIMED_OUT`
                result_state. If this is not specified on job creation,
                reset, or update the list is empty, and notifications are
                not sent, e.g.
                ```
                ["user.name@databricks.com"]
                ```
            - no_alert_for_skipped_runs:
                If true, do not send email to recipients specified in
                `on_failure` if the run is skipped.
        timeout_seconds:
            An optional timeout applied to each run of this job. The default
            behavior is to have no timeout, e.g. `86400`.
        schedule:
            An optional periodic schedule for this job. The default behavior is that
            the job only runs when triggered by clicking “Run Now” in
            the Jobs UI or sending an API request to `runNow`. Key-values:
            - quartz_cron_expression:
                A Cron expression using Quartz syntax that describes the
                schedule for a job. See [Cron Trigger](http://www.quartz-
                scheduler.org/documentation/quartz-2.3.0/tutorials/crontrigger.html)
                for details. This field is required, e.g. `20 30 * * * ?`.
            - timezone_id:
                A Java timezone ID. The schedule for a job is resolved with
                respect to this timezone. See [Java
                TimeZone](https://docs.oracle.com/javase/7/docs/api/java/util/TimeZone.html)
                for details. This field is required, e.g. `Europe/London`.
            - pause_status:
                Indicate whether this schedule is paused or not, e.g.
                `PAUSED`.
        max_concurrent_runs:
            An optional maximum allowed number of concurrent runs of the job.  Set
            this value if you want to be able to execute multiple runs
            of the same job concurrently. This is useful for example if
            you trigger your job on a frequent schedule and want to
            allow consecutive runs to overlap with each other, or if you
            want to trigger multiple runs which differ by their input
            parameters.  This setting affects only new runs. For
            example, suppose the job’s concurrency is 4 and there are 4
            concurrent active runs. Then setting the concurrency to 3
            won’t kill any of the active runs. However, from then on,
            new runs are skipped unless there are fewer than 3 active
            runs.  This value cannot exceed 1000\. Setting this value to
            0 causes all new runs to be skipped. The default behavior is
            to allow only 1 concurrent run, e.g. `10`.
        git_source:
            This functionality is in Public Preview.  An optional specification for
            a remote repository containing the notebooks used by this
            job's notebook tasks, e.g.
            ```
            {
                "git_url": "https://github.com/databricks/databricks-cli",
                "git_branch": "main",
                "git_provider": "gitHub",
            }
            ``` Key-values:
            - git_url:
                URL of the repository to be cloned by this job. The maximum
                length is 300 characters, e.g.
                `https://github.com/databricks/databricks-cli`.
            - git_provider:
                Unique identifier of the service used to host the Git
                repository. The value is case insensitive, e.g. `github`.
            - git_branch:
                Name of the branch to be checked out and used by this job.
                This field cannot be specified in conjunction with git_tag
                or git_commit. The maximum length is 255 characters, e.g.
                `main`.
            - git_tag:
                Name of the tag to be checked out and used by this job. This
                field cannot be specified in conjunction with git_branch or
                git_commit. The maximum length is 255 characters, e.g.
                `release-1.0.0`.
            - git_commit:
                Commit to be checked out and used by this job. This field
                cannot be specified in conjunction with git_branch or
                git_tag. The maximum length is 64 characters, e.g.
                `e0056d01`.
            - git_snapshot:
                Read-only state of the remote repository at the time the job was run.
                            This field is only included on job runs.
        format:
            Used to tell what is the format of the job. This field is ignored in
            Create/Update/Reset calls. When using the Jobs API 2.1 this
            value is always set to `'MULTI_TASK'`, e.g. `MULTI_TASK`.
        access_control_list:
            List of permissions to set on the job.

    Returns:
        Upon success, a dict of the response. </br>- `job_id: Optional[int]`</br>

    <h4>API Endpoint:</h4>
    `/2.1/jobs/create`

    <h4>API Responses:</h4>
    | Response | Description |
    | --- | --- |
    | 200 | Job was created successfully. |
    | 400 | The request was malformed. See JSON response for error details. |
    | 401 | The request was unauthorized. |
    | 500 | The request was not handled correctly due to a server error. |
    """  # noqa
    endpoint = "/2.1/jobs/create"  # noqa

    responses = {
        200: "Job was created successfully.",  # noqa
        400: "The request was malformed. See JSON response for error details.",  # noqa
        401: "The request was unauthorized.",  # noqa
        500: "The request was not handled correctly due to a server error.",  # noqa
    }

    json_payload = {
        "name": name,
        "tags": tags,
        "tasks": tasks,
        "job_clusters": job_clusters,
        "email_notifications": email_notifications,
        "timeout_seconds": timeout_seconds,
        "schedule": schedule,
        "max_concurrent_runs": max_concurrent_runs,
        "git_source": git_source,
        "format": format,
        "access_control_list": access_control_list,
    }

    response = await execute_endpoint.fn(
        endpoint,
        databricks_credentials,
        http_method=HTTPMethod.POST,
        json=json_payload,
    )

    contents = _unpack_contents(response, responses)
    return contents
