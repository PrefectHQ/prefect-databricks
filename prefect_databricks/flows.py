"""
Module containing flows for interacting with Databricks
"""
import asyncio
import time
from logging import Logger
from typing import Any, Awaitable, Callable, Dict, List, Optional

from prefect import flow, get_run_logger
from prefect.blocks.abstract import JobBlock, JobRun
from prefect.exceptions import JobRunIsRunning
from prefect.utilities.asyncutils import sync_compatible

from prefect_databricks import DatabricksCredentials
from prefect_databricks.exceptions import (
    DatabricksJobInternalError,
    DatabricksJobRunTimedOut,
    DatabricksJobSkipped,
    DatabricksJobTerminated,
)
from prefect_databricks.jobs import (
    jobs_run_now,
    jobs_runs_get,
    jobs_runs_get_output,
    jobs_runs_submit,
)
from prefect_databricks.models.jobs import (
    AccessControlRequest,
    GitSource,
    RunLifeCycleState,
    RunResultState,
    RunSubmitTaskSettings,
)

TERMINAL_STATUS_CODES = (
    RunLifeCycleState.terminated.value,
    RunLifeCycleState.skipped.value,
    RunLifeCycleState.internalerror.value,
)


@flow(
    name="Submit jobs runs and wait for completion",
    description=(
        "Triggers a Databricks jobs runs and waits for the "
        "triggered runs to complete."
    ),
)
async def jobs_runs_submit_and_wait_for_completion(
    databricks_credentials: DatabricksCredentials,
    tasks: List[RunSubmitTaskSettings] = None,
    run_name: Optional[str] = None,
    max_wait_seconds: int = 900,
    poll_frequency_seconds: int = 10,
    git_source: Optional[GitSource] = None,
    timeout_seconds: Optional[int] = None,
    idempotency_token: Optional[str] = None,
    access_control_list: Optional[List[AccessControlRequest]] = None,
    **jobs_runs_submit_kwargs: Dict[str, Any],
) -> Dict:
    """
    Flow that triggers a job run and waits for the triggered run to complete.

    Args:
        databricks_credentials:
            Credentials to use for authentication with Databricks.
        tasks: Tasks to run, e.g.
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
                },
                {
                    "task_key": "Orders_Ingest",
                    "description": "Ingests order data",
                    "depends_on": [],
                    "existing_cluster_id": "0923-164208-meows279",
                    "spark_jar_task": {
                        "main_class_name": "com.databricks.OrdersIngest",
                        "parameters": ["--data", "dbfs:/path/to/order-data.json"],
                    },
                    "libraries": [{"jar": "dbfs:/mnt/databricks/OrderIngest.jar"}],
                    "timeout_seconds": 86400,
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
                        "base_parameters": {"name": "John Doe", "age": "35"},
                    },
                    "timeout_seconds": 86400,
                },
            ]
            ```
        run_name:
            An optional name for the run. The default value is `Untitled`, e.g. `A
            multitask job run`.
        git_source:
            This functionality is in Public Preview.  An optional specification for
            a remote repository containing the notebooks used by this
            job's notebook tasks. Key-values:
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
        timeout_seconds:
            An optional timeout applied to each run of this job. The default
            behavior is to have no timeout, e.g. `86400`.
        idempotency_token:
            An optional token that can be used to guarantee the idempotency of job
            run requests. If a run with the provided token already
            exists, the request does not create a new run but returns
            the ID of the existing run instead. If a run with the
            provided token is deleted, an error is returned.  If you
            specify the idempotency token, upon failure you can retry
            until the request succeeds. Databricks guarantees that
            exactly one run is launched with that idempotency token.
            This token must have at most 64 characters.  For more
            information, see [How to ensure idempotency for
            jobs](https://kb.databricks.com/jobs/jobs-idempotency.html),
            e.g. `8f018174-4792-40d5-bcbc-3e6a527352c8`.
        access_control_list:
            List of permissions to set on the job.
        max_wait_seconds: Maximum number of seconds to wait for the entire flow to complete.
        poll_frequency_seconds: Number of seconds to wait in between checks for
            run completion.
        **jobs_runs_submit_kwargs: Additional keyword arguments to pass to `jobs_runs_submit`.

    Returns:
        A dictionary of task keys to its corresponding notebook output.

    Examples:
        Submit jobs runs and wait.
        ```python
        from prefect import flow
        from prefect_databricks import DatabricksCredentials
        from prefect_databricks.flows import jobs_runs_submit_and_wait_for_completion
        from prefect_databricks.models.jobs import (
            AutoScale,
            AwsAttributes,
            JobTaskSettings,
            NotebookTask,
            NewCluster,
        )

        @flow
        def jobs_runs_submit_and_wait_for_completion_flow(notebook_path, **base_parameters):
            databricks_credentials = await DatabricksCredentials.load("BLOCK_NAME")

            # specify new cluster settings
            aws_attributes = AwsAttributes(
                availability="SPOT",
                zone_id="us-west-2a",
                ebs_volume_type="GENERAL_PURPOSE_SSD",
                ebs_volume_count=3,
                ebs_volume_size=100,
            )
            auto_scale = AutoScale(min_workers=1, max_workers=2)
            new_cluster = NewCluster(
                aws_attributes=aws_attributes,
                autoscale=auto_scale,
                node_type_id="m4.large",
                spark_version="10.4.x-scala2.12",
                spark_conf={"spark.speculation": True},
            )

            # specify notebook to use and parameters to pass
            notebook_task = NotebookTask(
                notebook_path=notebook_path,
                base_parameters=base_parameters,
            )

            # compile job task settings
            job_task_settings = JobTaskSettings(
                new_cluster=new_cluster,
                notebook_task=notebook_task,
                task_key="prefect-task"
            )

            multi_task_runs = jobs_runs_submit_and_wait_for_completion(
                databricks_credentials=databricks_credentials,
                run_name="prefect-job",
                tasks=[job_task_settings]
            )

            return multi_task_runs
        ```
    """  # noqa
    logger = get_run_logger()

    # submit the jobs runs
    multi_task_jobs_runs_future = await jobs_runs_submit.submit(
        databricks_credentials=databricks_credentials,
        tasks=tasks,
        run_name=run_name,
        git_source=git_source,
        timeout_seconds=timeout_seconds,
        idempotency_token=idempotency_token,
        access_control_list=access_control_list,
        **jobs_runs_submit_kwargs,
    )
    multi_task_jobs_runs = await multi_task_jobs_runs_future.result()
    multi_task_jobs_runs_id = multi_task_jobs_runs["run_id"]

    # wait for all the jobs runs to complete in a separate flow
    # for a cleaner radar interface
    jobs_runs_state, jobs_runs_metadata = await jobs_runs_wait_for_completion(
        multi_task_jobs_runs_id=multi_task_jobs_runs_id,
        databricks_credentials=databricks_credentials,
        run_name=run_name,
        max_wait_seconds=max_wait_seconds,
        poll_frequency_seconds=poll_frequency_seconds,
    )

    # fetch the state results
    jobs_runs_life_cycle_state = jobs_runs_state["life_cycle_state"]
    jobs_runs_state_message = jobs_runs_state["state_message"]

    # return results or raise error
    if jobs_runs_life_cycle_state == RunLifeCycleState.terminated.value:
        jobs_runs_result_state = jobs_runs_state.get("result_state", None)
        if jobs_runs_result_state == RunResultState.success.value:
            task_notebook_outputs = {}
            for task in jobs_runs_metadata["tasks"]:
                task_key = task["task_key"]
                task_run_id = task["run_id"]
                task_run_output_future = await jobs_runs_get_output.submit(
                    run_id=task_run_id,
                    databricks_credentials=databricks_credentials,
                )
                task_run_output = await task_run_output_future.result()
                task_run_notebook_output = task_run_output.get("notebook_output", {})
                task_notebook_outputs[task_key] = task_run_notebook_output
            logger.info(
                "Databricks Jobs Runs Submit (%s ID %s) completed successfully!",
                run_name,
                multi_task_jobs_runs_id,
            )
            return task_notebook_outputs
        else:
            raise DatabricksJobTerminated(
                f"Databricks Jobs Runs Submit "
                f"({run_name} ID {multi_task_jobs_runs_id}) "
                f"terminated with result state, {jobs_runs_result_state}: "
                f"{jobs_runs_state_message}"
            )
    elif jobs_runs_life_cycle_state == RunLifeCycleState.skipped.value:
        raise DatabricksJobSkipped(
            f"Databricks Jobs Runs Submit ({run_name} ID "
            f"{multi_task_jobs_runs_id}) was skipped: {jobs_runs_state_message}.",
        )
    elif jobs_runs_life_cycle_state == RunLifeCycleState.internalerror.value:
        raise DatabricksJobInternalError(
            f"Databricks Jobs Runs Submit ({run_name} ID "
            f"{multi_task_jobs_runs_id}) "
            f"encountered an internal error: {jobs_runs_state_message}.",
        )


def _update_and_log_state_changes(
    job_or_task_states: Dict[str, Any],
    job_or_task_metadata: Dict[str, Any],
    logger: Logger,
    run_type: str = "Task",
) -> Dict[str, Any]:
    """
    Stores the states of a job or task to its collection and logs the output
    if it changes.

    Args:
        job_or_task_states: The dictionary of job or task states.
        job_or_task_metadata: Metadata object containing run, url and state
        logger: Logger instance to log with.
        run_type: String indicating if is job or task, defaults to Task

    Returns
        A copy of the job_or_task_states dictionary with any state updates
    """

    run_id = job_or_task_metadata.get("run_id", "")
    run_page_url = job_or_task_metadata.get("run_page_url", "")
    state = job_or_task_metadata.get("state", {})

    string_run_id = str(run_id)

    job_or_task_states_copy = job_or_task_states.copy()

    if string_run_id not in job_or_task_states_copy:
        job_or_task_states_copy[string_run_id] = {}

    new_item = {}
    new_item["run_page_url"] = run_page_url
    new_item["run_id"] = run_id
    new_item["state"] = state

    life_cycle_state = state.get("life_cycle_state", "")
    state_message = state.get("state_message", "")
    result_state = state.get("result_state", "")

    if "state" in job_or_task_states_copy[string_run_id]:
        existing_state = job_or_task_states_copy[string_run_id]["state"]
        existing_life_cycle_state = existing_state.get("life_cycle_state", "")
        existing_state_message = existing_state.get("state_message", "")
        existing_result_state = existing_state.get("result_state", "")

        if (
            life_cycle_state == existing_life_cycle_state
            and state_message == existing_state_message
            and result_state == existing_result_state
        ):
            return job_or_task_states_copy

    logger.info(
        "%s Run '%s' states updated!\n"
        "Life cycle: '%s'\n"
        "Result: '%s'\n"
        "Message '%s'\n"
        "Url: %s\n",
        run_type,
        run_id,
        life_cycle_state,
        result_state,
        state_message,
        run_page_url,
    )

    job_or_task_states_copy[string_run_id] = new_item
    return job_or_task_states_copy


@flow(
    name="Wait for completion of jobs runs",
    description="Waits for the jobs runs to finish running",
)
async def jobs_runs_wait_for_completion(
    multi_task_jobs_runs_id: int,
    databricks_credentials: DatabricksCredentials,
    run_name: Optional[str] = None,
    max_wait_seconds: int = 900,
    poll_frequency_seconds: int = 10,
):
    """
    Flow that triggers a job run and waits for the triggered run to complete.

    Args:
        run_name: The name of the jobs runs task.
        multi_task_jobs_run_id: The ID of the jobs runs task to watch.
        databricks_credentials:
            Credentials to use for authentication with Databricks.
        max_wait_seconds:
            Maximum number of seconds to wait for the entire flow to complete.
        poll_frequency_seconds: Number of seconds to wait in between checks for
            run completion.

    Returns:
        jobs_runs_state: A dict containing the jobs runs life cycle state and message.
        jobs_runs_metadata: A dict containing IDs of the jobs runs tasks.

    Example:
        Waits for completion on jobs runs.
        ```python
        from prefect import flow
        from prefect_databricks import DatabricksCredentials
        from prefect_databricks.flows import jobs_runs_wait_for_completion

        @flow
        def jobs_runs_wait_for_completion_flow():
            databricks_credentials = DatabricksCredentials.load("BLOCK_NAME")
            return jobs_runs_wait_for_completion(
                multi_task_jobs_run_id=45429,
                databricks_credentials=databricks_credentials,
                run_name="my_run_name",
                max_wait_seconds=1800,  # 30 minutes
                poll_frequency_seconds=120,  # 2 minutes
            )
        ```
    """
    logger = get_run_logger()

    seconds_waited_for_run_completion = 0
    wait_for = []

    jobs_status = {}
    tasks_status = {}
    while seconds_waited_for_run_completion <= max_wait_seconds:
        jobs_runs_metadata_future = await jobs_runs_get.submit(
            run_id=multi_task_jobs_runs_id,
            databricks_credentials=databricks_credentials,
            wait_for=wait_for,
        )
        wait_for = [jobs_runs_metadata_future]

        jobs_runs_metadata = await jobs_runs_metadata_future.result()
        jobs_status = _update_and_log_state_changes(
            jobs_status, jobs_runs_metadata, logger, "Job"
        )
        jobs_runs_metadata_tasks = jobs_runs_metadata.get("tasks", [])
        for task_metadata in jobs_runs_metadata_tasks:
            tasks_status = _update_and_log_state_changes(
                tasks_status, task_metadata, logger, "Task"
            )

        jobs_runs_state = jobs_runs_metadata.get("state", {})
        jobs_runs_life_cycle_state = jobs_runs_state["life_cycle_state"]
        if jobs_runs_life_cycle_state in TERMINAL_STATUS_CODES:
            return jobs_runs_state, jobs_runs_metadata

        logger.info("Waiting for %s seconds.", poll_frequency_seconds)
        await asyncio.sleep(poll_frequency_seconds)
        seconds_waited_for_run_completion += poll_frequency_seconds

    raise DatabricksJobRunTimedOut(
        f"Max wait time of {max_wait_seconds} seconds exceeded while waiting "
        f"for job run ({run_name} ID {multi_task_jobs_runs_id})"
    )


class DatabricksJob(JobBlock):
    """
    Block that holds the information and methods to interact with a Databricks job.

    Example:
        Triggers a Databricks job, waits for completion, and fetches the results.
        ```python
        from prefect import flow
        from prefect_databricks import DatabricksCredentials, DatabricksJob

        @flow
        def databricks_job_flow():
            databricks_credentials = DatabricksCredentials.load("databricks-token")
            databricks_job = DatabricksJob(
                databricks_credentials=databricks_credentials,
                job_id=154217
            )
            databricks_job_run = databricks_job.trigger()
            databricks_job_run.wait_for_completion()
            databricks_job_run.fetch_results()
            return databricks_job_run

        databricks_job_flow()
        ```
    """

    databricks_credentials: DatabricksCredentials
    job_id: int
    timeout_seconds: int = 900
    interval_seconds: int = 10

    class DatabricksJobRun(JobRun):  # NOT A BLOCK
        """
        Class that holds the information and methods to interact
        with the resulting run of a databricks job.
        """

        def __init__(self, run_id: int, databricks_job: "DatabricksJob"):
            self.run_id = run_id
            self._databricks_job = databricks_job
            self._databricks_credentials = databricks_job.databricks_credentials

        @property
        def _log_prefix(self):
            return f"Databricks job {self._databricks_job.job_id} run {self.run_id}."

        async def _wait_until_state(
            self,
            in_final_state_fn: Awaitable[Callable],
            get_state_fn: Awaitable[Callable],
            log_state_fn: Callable = None,
            timeout_seconds: int = 60,
            interval_seconds: int = 1,
        ):
            """
            Wait until the job run reaches a specific state.

            Args:
                in_final_state_fn: An async function that accepts a run state
                    and returns a boolean indicating whether the job run is
                    in a final state.
                get_state_fn: An async function that returns
                    the current state of the job run.
                log_state_fn: A callable that accepts a run
                    state and makes it human readable.
                timeout_seconds: The maximum amount of time, in seconds, to wait
                    for the job run to reach the final state.
                interval_seconds: The number of seconds to wait between checks of
                    the job run's state.
            """
            start_time = time.time()
            last_state = run_state = None
            while not in_final_state_fn(run_state):
                run_state = await get_state_fn()
                if run_state != last_state:
                    if self.logger is not None:
                        self.logger.info(
                            "%s has new state: %s",
                            self._log_prefix,
                            log_state_fn(run_state),
                        )
                    last_state = run_state

                elapsed_time_seconds = time.time() - start_time
                if elapsed_time_seconds > timeout_seconds:
                    raise DatabricksJobRunTimedOut(
                        f"Max wait time of {timeout_seconds} "
                        "seconds exceeded while waiting"
                    )
                await asyncio.sleep(interval_seconds)

        @sync_compatible
        async def get_run(self) -> Dict[str, Any]:
            """
            Makes a request to the Databricks API to get the run metadata.

            Returns:
                The run data.
            """
            return await jobs_runs_get.fn(
                self.run_id, databricks_credentials=self._databricks_credentials
            )

        @sync_compatible
        async def get_lifecycle_state(self) -> Dict[str, Any]:
            """
            Makes a request to the Databricks API to get the run metadata.

            Returns:
                The run data.
            """
            run = await self.get_run()
            life_cycle_state = run["state"].get("life_cycle_state", "")
            return life_cycle_state

        @sync_compatible
        async def wait_for_completion(self) -> None:
            """
            Waits for the job run to reach a terminal state.
            """
            run = self.get_run()
            url = run.get("run_page_url", "")
            self.logger.info(
                f"{self._log_prefix} waiting for completion; "
                f"you can view the status of this run at {url}"
            )
            await self._wait_until_state(
                in_final_state_fn=lambda status_code: status_code
                in TERMINAL_STATUS_CODES,
                get_state_fn=self.get_lifecycle_state,
                log_state_fn=RunLifeCycleState,
                timeout_seconds=self._databricks_job.timeout_seconds,
                interval_seconds=self._databricks_job.interval_seconds,
            )

        @sync_compatible
        async def fetch_results(self, step: Optional[int] = None) -> Dict[str, Any]:
            """
            Gets the results from the job run. Since the results
            may not be ready, use wait_for_completion before calling this method.
            Args:
                step: The index of the step in the run to query for artifacts. The
                    first step in the run has the index 1. If the step parameter is
                    omitted, then this method will return the artifacts compiled
                    for the last step in the run.
            """
            run = await self.get_run()
            life_cycle_state = run["state"].get("life_cycle_state", "")
            state_message = run["state"].get("state_message", "")

            if life_cycle_state == RunLifeCycleState.terminated.value:
                result_state = run["state"].get("result_state", "")
                if result_state == RunResultState.success.value:
                    task_notebook_outputs = {}
                    for task in run["tasks"]:
                        task_key = task["task_key"]
                        task_run_id = task["run_id"]
                        task_run_output = await jobs_runs_get_output.fn(
                            run_id=task_run_id,
                            databricks_credentials=self._databricks_credentials,
                        )
                        task_run_notebook_output = task_run_output.get(
                            "notebook_output", {}
                        )
                        task_notebook_outputs[task_key] = task_run_notebook_output
                    self.logger.info("%s completed successfully!", self._log_prefix)
                    return task_notebook_outputs
                else:
                    raise DatabricksJobTerminated(
                        f"{self._log_prefix} was terminated with result state "
                        f"{result_state}: {state_message}."
                    )
            elif life_cycle_state == RunLifeCycleState.skipped.value:
                raise DatabricksJobSkipped(
                    f"{self._log_prefix} was cancelled: {state_message}.",
                )
            elif life_cycle_state == RunLifeCycleState.internalerror.value:
                raise DatabricksJobInternalError(
                    f"{self._log_prefix} has encountered an internal error: "
                    f"{state_message}.",
                )
            else:
                raise JobRunIsRunning(
                    f"{self._log_prefix} is still running; "
                    "use wait_for_completion() to wait until results are ready."
                )

    # beginning of DatabricksJob methods
    @sync_compatible
    async def trigger(
        self,
        idempotency_token: Optional[str] = None,
        jar_params: Optional[List[str]] = None,
        notebook_params: Optional[Dict] = None,
        python_params: Optional[List[str]] = None,
        spark_submit_params: Optional[List[str]] = None,
        python_named_params: Optional[Dict] = None,
        pipeline_params: Optional[str] = None,
        sql_params: Optional[Dict] = None,
        dbt_commands: Optional[List] = None,
    ) -> DatabricksJobRun:
        """
        Triggers a Databricks job.

        Args:
            databricks_credentials:
                Credentials to use for authentication with Databricks.
            job_id:
                The ID of the job to be executed, e.g. `11223344`.
            idempotency_token:
                An optional token to guarantee the idempotency of job run requests. If a
                run with the provided token already exists, the request does
                not create a new run but returns the ID of the existing run
                instead. If a run with the provided token is deleted, an
                error is returned.  If you specify the idempotency token,
                upon failure you can retry until the request succeeds.
                Databricks guarantees that exactly one run is launched with
                that idempotency token.  This token must have at most 64
                characters.  For more information, see [How to ensure
                idempotency for jobs](https://kb.databricks.com/jobs/jobs-
                idempotency.html), e.g.
                `8f018174-4792-40d5-bcbc-3e6a527352c8`.
            jar_params:
                A list of parameters for jobs with Spark JAR tasks, for example
                `'jar_params': ['john doe', '35']`. The parameters are used
                to invoke the main function of the main class specified in
                the Spark JAR task. If not specified upon `run-now`, it
                defaults to an empty list. jar_params cannot be specified in
                conjunction with notebook_params. The JSON representation of
                this field (for example `{'jar_params':['john doe','35']}`)
                cannot exceed 10,000 bytes.  Use [Task parameter
                variables](https://docs.databricks.com/jobs.html
                parameter-variables) to set parameters containing
                information about job runs, e.g.
                ```
                ["john", "doe", "35"]
                ```
            notebook_params:
                A map from keys to values for jobs with notebook task, for example
                `'notebook_params': {'name': 'john doe', 'age': '35'}`. The
                map is passed to the notebook and is accessible through the
                [dbutils.widgets.get](https://docs.databricks.com/dev-
                tools/databricks-utils.html
                dbutils-widgets) function.  If not specified upon `run-now`,
                the triggered run uses the job’s base parameters.
                notebook_params cannot be specified in conjunction with
                jar_params.  Use [Task parameter
                variables](https://docs.databricks.com/jobs.html
                parameter-variables) to set parameters containing
                information about job runs.  The JSON representation of this
                field (for example `{'notebook_params':{'name':'john
                doe','age':'35'}}`) cannot exceed 10,000 bytes, e.g.
                ```
                {"name": "john doe", "age": "35"}
                ```
            python_params:
                A list of parameters for jobs with Python tasks, for example
                `'python_params': ['john doe', '35']`. The parameters are
                passed to Python file as command-line parameters. If
                specified upon `run-now`, it would overwrite the parameters
                specified in job setting. The JSON representation of this
                field (for example `{'python_params':['john doe','35']}`)
                cannot exceed 10,000 bytes.  Use [Task parameter
                variables](https://docs.databricks.com/jobs.html
                parameter-variables) to set parameters containing
                information about job runs.  Important  These parameters
                accept only Latin characters (ASCII character set). Using
                non-ASCII characters returns an error. Examples of invalid,
                non-ASCII characters are Chinese, Japanese kanjis, and
                emojis, e.g.
                ```
                ["john doe", "35"]
                ```
            spark_submit_params:
                A list of parameters for jobs with spark submit task, for example
                `'spark_submit_params': ['--class',
                'org.apache.spark.examples.SparkPi']`. The parameters are
                passed to spark-submit script as command-line parameters. If
                specified upon `run-now`, it would overwrite the parameters
                specified in job setting. The JSON representation of this
                field (for example `{'python_params':['john doe','35']}`)
                cannot exceed 10,000 bytes.  Use [Task parameter
                variables](https://docs.databricks.com/jobs.html
                parameter-variables) to set parameters containing
                information about job runs.  Important  These parameters
                accept only Latin characters (ASCII character set). Using
                non-ASCII characters returns an error. Examples of invalid,
                non-ASCII characters are Chinese, Japanese kanjis, and
                emojis, e.g.
                ```
                ["--class", "org.apache.spark.examples.SparkPi"]
                ```
            python_named_params:
                A map from keys to values for jobs with Python wheel task, for example
                `'python_named_params': {'name': 'task', 'data':
                'dbfs:/path/to/data.json'}`, e.g.
                ```
                {"name": "task", "data": "dbfs:/path/to/data.json"}
                ```
            pipeline_params:

            sql_params:
                A map from keys to values for SQL tasks, for example `'sql_params':
                {'name': 'john doe', 'age': '35'}`. The SQL alert task does
                not support custom parameters, e.g.
                ```
                {"name": "john doe", "age": "35"}
                ```
            dbt_commands:
                An array of commands to execute for jobs with the dbt task, for example
                `'dbt_commands': ['dbt deps', 'dbt seed', 'dbt run']`, e.g.
                ```
                ["dbt deps", "dbt seed", "dbt run"]
                ```

        Returns:
            A representation of the Databricks job run.
        """
        jobs_runs_now_kwargs = {
            "job_id": self.job_id,
            "idempotency_token": idempotency_token,
            "jar_params": jar_params,
            "notebook_params": notebook_params,
            "python_params": python_params,
            "spark_submit_params": spark_submit_params,
            "python_named_params": python_named_params,
            "pipeline_params": pipeline_params,
            "sql_params": sql_params,
            "dbt_commands": dbt_commands,
        }
        run_data = await jobs_run_now.fn(**jobs_runs_now_kwargs)
        run_id = run_data.get("run_id")
        run = self.DatabricksJobRun(
            databricks_job=self,
            run_id=run_id,
        )

        self.logger.info(
            f"Databricks job {self.job_id} run {run_id} successfully triggered."
        )
        return run


@flow
async def trigger_wait_retry_databricks_job_run(
    databricks_job: DatabricksJob,
) -> Dict[str, Any]:
    """
    Flow that triggers and waits for a databricks job run, retrying a
    subset of failed nodes if necessary.
    Args:
        databricks_job: Block that holds the information and
            methods to interact with a databricks job.

    Examples:
        ```python
        from prefect import flow
        from prefect_databricks import DatabricksCredentials, DatabricksJob
        from prefect_databricks.flows import trigger_wait_retry_databricks_job_run

        @flow
        def trigger_wait_retry_databricks_job_run_flow():
            databricks_credentials = DatabricksCredentials.load("databricks-token")
            databricks_job = DatabricksJob(
                databricks_credentials=databricks_credentials, job_id=154217
            )
            return trigger_wait_retry_databricks_job_run(databricks_job=databricks_job)

        trigger_wait_retry_databricks_job_run_flow()
        ```
    """
    run = await databricks_job.trigger()
    await run.wait_for_completion()
    result = await run.fetch_results()
    return result
