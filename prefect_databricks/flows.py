"""
Module containing flows for interacting with Databricks
"""

import asyncio
from typing import TYPE_CHECKING, Dict, List

from prefect import flow, get_run_logger

from prefect_databricks.jobs import (
    jobs_runs_get,
    jobs_runs_get_output,
    jobs_runs_submit,
)
from prefect_databricks.models.jobs import RunLifeCycleState, RunResultState

if TYPE_CHECKING:
    from prefect_databricks import DatabricksCredentials
    from prefect_databricks.models import jobs as models


class DatabricksJobTerminated(Exception):
    """Raised when a Databricks jobs runs submit terminates"""

    pass


class DatabricksJobSkipped(Exception):
    """Raised when a Databricks jobs runs submit skips"""

    pass


class DatabricksJobInternalError(Exception):
    """Raised when a Databricks jobs runs submit encounters internal error"""

    pass


@flow(
    name="Submit jobs runs and wait for completion",
    description="Triggers a Databricks jobs runs and waits for the"
    "triggered runs to complete.",
)
async def jobs_runs_submit_and_wait_for_completion(
    databricks_credentials: "DatabricksCredentials",
    tasks: List["models.RunSubmitTaskSettings"] = None,
    run_name: str = None,
    max_wait_seconds: int = 900,
    poll_frequency_seconds: int = 10,
    **jobs_runs_submit_kwargs,
) -> Dict:
    """
    Flow that triggers a job run and waits for the triggered run to complete.

    Args:

    Examples:

    """  # noqa
    logger = get_run_logger()

    multi_task_jobs_runs_future = await jobs_runs_submit.submit(
        databricks_credentials=databricks_credentials,
        tasks=tasks,
        run_name=run_name,
        **jobs_runs_submit_kwargs,
    )
    multi_task_jobs_runs = await multi_task_jobs_runs_future.result()
    multi_task_jobs_runs_id = multi_task_jobs_runs["run_id"]

    seconds_waited_for_run_completion = 0
    while seconds_waited_for_run_completion <= max_wait_seconds:
        jobs_runs_metadata_future = await jobs_runs_get.submit(
            run_id=multi_task_jobs_runs_id,
            databricks_credentials=databricks_credentials,
            wait_for=[multi_task_jobs_runs_future],
        )
        jobs_runs_metadata = await jobs_runs_metadata_future.result()
        jobs_runs_state = jobs_runs_metadata["state"]
        jobs_runs_life_cycle_state = jobs_runs_state["life_cycle_state"]

        if jobs_runs_life_cycle_state == RunLifeCycleState.terminated.value:
            jobs_runs_result_state = jobs_runs_life_cycle_state.get(
                "result_state", None
            )
            if jobs_runs_result_state == RunResultState.success.value:
                task_notebook_outputs = {}
                for task in jobs_runs_metadata["task"]:
                    task_key = task["task_key"]
                    task_run_id = task["run_id"]
                    task_run_notebook_output_future = jobs_runs_get_output.submit(
                        run_id=task_run_id,
                        databricks_credentials=databricks_credentials,
                        wait_for=[jobs_runs_metadata_future],
                    )
                    task_notebook_outputs[
                        task_key
                    ] = await task_run_notebook_output_future.result()[
                        "notebook_output"
                    ]
                logger.info(
                    "Databricks Jobs Runs Submit (ID %s) completed successfully!",
                    multi_task_jobs_runs_id,
                )
                return task_notebook_outputs
            else:
                raise DatabricksJobTerminated(
                    f"Databricks Jobs Runs Submit (ID {multi_task_jobs_runs_id}) "
                    f"terminated with result state: {jobs_runs_result_state}"
                )
        elif jobs_runs_life_cycle_state == RunLifeCycleState.skipped.value:
            logger.warning(
                "Databricks Jobs Runs Submit (ID %s) was skipped.",
                multi_task_jobs_runs_id,
            )
        elif jobs_runs_life_cycle_state == RunLifeCycleState.internalerror.value:
            logger.warning(
                "Databricks Jobs Runs Submit (ID %s) encountered an internal error.",
                multi_task_jobs_runs_id,
            )
        else:
            logger.info(
                "Databricks Jobs Runs Submit (ID %s) has status %s. "
                "Waiting for %i seconds.",
                multi_task_jobs_runs_id,
                RunLifeCycleState(jobs_runs_life_cycle_state).name,
                poll_frequency_seconds,
            )
            await asyncio.sleep(poll_frequency_seconds)
            seconds_waited_for_run_completion += poll_frequency_seconds

    raise TimeoutError(
        f"Max wait time of {max_wait_seconds} seconds exceeded while waiting "
        f"for job run with ID {multi_task_jobs_runs_id}"
    )
