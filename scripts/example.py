# SECTION 1
from prefect import flow, task
from prefect_databricks import DatabricksCredentials
from prefect_databricks.flows import jobs_runs_submit_and_wait_for_completion
from prefect_databricks.models.jobs import (
    AutoScale,
    AwsAttributes,
    JobTaskSettings,
    NewCluster,
    NotebookTask,
)

# SECTION 2
# SECTION 3
@task
def create_job_task_settings(notebook_path, base_parameters):
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
        new_cluster=new_cluster, notebook_task=notebook_task, task_key="prefect-task"
    )

    return job_task_settings

# SECTION 4
@flow(name="Databricks Flow")
def jobs_runs_submit_flow(notebook_path, **base_parameters):
    databricks_credentials = DatabricksCredentials.load("my-block")
    job_task_settings = create_job_task_settings(notebook_path, base_parameters)
    run = jobs_runs_submit_and_wait_for_completion(
        databricks_credentials=databricks_credentials,
        run_name="prefect-job",
        tasks=[job_task_settings],
    )
    return run

# SECTION 5
jobs_runs_submit_flow(
    notebook_path="/Users/username@email.com/example.ipynb",
    base_parameters={"name": "Marvin"},
)