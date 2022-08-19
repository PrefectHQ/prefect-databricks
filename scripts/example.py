# SECTION 1
from prefect import Flow, Parameter, task
from prefect.client.secrets import Secret
from prefect.tasks.databricks import DatabricksSubmitMultitaskRun
from prefect.tasks.databricks.models import (
    AutoScale,
    AwsAttributes,
    JobTaskSettings,
    NewCluster,
    NotebookTask,
)

# SECTION 2
databricks_conn = Secret("DATABRICKS_CONNECTION_STRING").get()

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
with Flow("Databricks Flow") as flow:
    notebook_path = Parameter("notebook_path")
    base_parameters = Parameter("base_parameters")
    job_task_settings = create_job_task_settings(notebook_path, base_parameters)
    run = DatabricksSubmitMultitaskRun(databricks_conn_secret=databricks_conn)(
        run_name="prefect-job",
        tasks=[job_task_settings],
    )

# SECTION 5
flow.run(
    notebook_path="/Users/username@email.com/example.ipynb",
    base_parameters={"name": "Marvin"},
)