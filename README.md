# Integrate Databricks jobs into your dataflow with prefect-databricks
 
<p align="center">
    <img src="https://user-images.githubusercontent.com/15331990/219822439-70ec82fb-e93a-4983-bec7-8c8250fbb7ac.png">
    <br>
    <a href="https://pypi.python.org/pypi/prefect-databricks/" alt="PyPI version">
        <img alt="PyPI" src="https://img.shields.io/pypi/v/prefect-databricks?color=0052FF&labelColor=090422"></a>
    <a href="https://github.com/PrefectHQ/prefect-databricks/" alt="Stars">
        <img src="https://img.shields.io/github/stars/PrefectHQ/prefect-databricks?color=0052FF&labelColor=090422" /></a>
    <a href="https://pepy.tech/badge/prefect-databricks/" alt="Downloads">
        <img src="https://img.shields.io/pypi/dm/prefect-databricks?color=0052FF&labelColor=090422" /></a>
    <a href="https://github.com/PrefectHQ/prefect-databricks/pulse" alt="Activity">
        <img src="https://img.shields.io/github/commit-activity/m/PrefectHQ/prefect-databricks?color=0052FF&labelColor=090422" /></a>
    <br>
    <a href="https://prefect-community.slack.com" alt="Slack">
        <img src="https://img.shields.io/badge/slack-join_community-red.svg?color=0052FF&labelColor=090422&logo=slack" /></a>
    <a href="https://discourse.prefect.io/" alt="Discourse">
        <img src="https://img.shields.io/badge/discourse-browse_forum-red.svg?color=0052FF&labelColor=090422&logo=discourse" /></a>
</p>

Visit the full docs [here](https://PrefectHQ.github.io/prefect-databricks) to see additional examples and the API reference.

The prefect-databricks collection makes it easy to coordiante Databricks jobs with other tools in your data stack using Prefect. Check out the examples below to get started!

## Getting Started

### Integrate with Prefect flows

Using Prefect with Databricks allows you to define and orchestrate complex data workflows that take advantage of the scalability and performance of Databricks.

This can be especially useful for data-intensive tasks such as ETL (extract, transform, load) pipelines, machine learning training and inference, and real-time data processing.

Below is an example of how you can incorporate Databricks notebooks within your Prefect flows.

Be sure to install [prefect-databricks](#installation) and [save a credentials block](#saving-credentials-to-block) to run the examples below!

If you don't have an existing notebook ready on Databricks, you can copy the following, and name it `example.ipynb`. This notebook, accepts a name parameter from the flow and simply prints a message.

```python
name = dbutils.widgets.get("name")
message = f"Don't worry {name}, I got your request! Welcome to prefect-databricks!"
print(message)
```

Here, the flow launches a new cluster to run `example.ipynb` and waits for the completion of the notebook run. Replace the placeholders and run.

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
def jobs_runs_submit_flow(block_name: str, notebook_path: str, **base_parameters):
    databricks_credentials = DatabricksCredentials.load(block_name)

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

    run = jobs_runs_submit_and_wait_for_completion(
        databricks_credentials=databricks_credentials,
        run_name="prefect-job",
        tasks=[job_task_settings]
    )

    return run


jobs_runs_submit_flow(
    block_name="BLOCK-NAME-PLACEHOLDER"
    notebook_path="/Users/<EMAIL_ADDRESS_PLACEHOLDER>/example.ipynb",
    name="Marvin"
)
```

Upon execution, the notebook run should output:

```
Don't worry Marvin, I got your request! Welcome to prefect-databricks!
```

!!! info "Input dictionaries in the place of models"
    
    Instead of using the built-in models, you may also input a valid dictionary.
    
    For example, the following are equivalent:

    ```python
    auto_scale=AutoScale(min_workers=1, max_workers=2)
    ```

    ```python
    auto_scale={"min_workers": 1, "max_workers": 2}
    ```

If you have an existing Databricks job, you can run it using `jobs_runs_submit_by_id_and_wait_for_completion`:

```python
from prefect import flow

from prefect_databricks import DatabricksCredentials
from prefect_databricks.flows import (
    jobs_runs_submit_by_id_and_wait_for_completion,
)


@flow
def existing_job_submit(databricks_credentials_block_name: str, job_id):
    databricks_credentials = DatabricksCredentials.load(name=block_name)

    run = jobs_runs_submit_by_id_and_wait_for_completion(
        databricks_credentials=databricks_credentials, job_id=job_id
    )

    return run

existing_job_submit(databricks_credentials_block_name="db-creds", job_id="YOUR-JOB-NAME")
```

## Resources

For more tips on how to use tasks and flows in a Collection, check out [Using Collections](https://orion-docs.prefect.io/collections/usage/)!

Note, the tasks within this collection were created by a code generator using the service's OpenAPI spec.

The service's REST API documentation can be found [here](https://docs.databricks.com/dev-tools/api/latest/index.html).

### Installation

Install `prefect-databricks` with `pip`:

```bash
pip install prefect-databricks
```

Requires an installation of Python 3.7+.

We recommend using a Python virtual environment manager such as pipenv, conda or virtualenv.

These tasks are designed to work with Prefect 2. For more information about how to use Prefect, please refer to the [Prefect documentation](https://orion-docs.prefect.io/).

### Saving Credentials to Block

To use the `load` method on Blocks, you must already have a block document [saved through code](https://orion-docs.prefect.io/concepts/blocks/#saving-blocks) or [saved through the UI](https://orion-docs.prefect.io/ui/blocks/).

Below is a walkthrough on saving block documents through code; simply create a short script, replacing the placeholders. 

1. Head over to [Databricks](https://accounts.cloud.databricks.com/).
2. Login to your Databricks account and select a workspace.
3. On the top right side of the nav bar, click on your account name -> User Settings.
4. Click Access tokens -> Generate new token -> Generate and copy the token.
5. Note down your Databricks instance from the browser URL, formatted like `https://<DATABRICKS-INSTANCE>.cloud.databricks.com/`
6. Create a short script, replacing the placeholders.

```python
from prefect_databricks import DatabricksCredentials

credentials = DatabricksCredentials(
    databricks_instance="DATABRICKS-INSTANCE-PLACEHOLDER"
    token="TOKEN-PLACEHOLDER"
)

connector.save("BLOCK_NAME-PLACEHOLDER")
```

Congrats! You can now easily load the saved block, which holds your credentials:

```python
from prefect_databricks import DatabricksCredentials

DatabricksCredentials.load("BLOCK_NAME-PLACEHOLDER")
```

!!! info "Registering blocks"

    Register blocks in this module to
    [view and edit them](https://orion-docs.prefect.io/ui/blocks/)
    on Prefect Cloud:

    ```bash
    prefect block register -m prefect_databricks
    ```

### Feedback

If you encounter any bugs while using `prefect-databricks`, feel free to open an issue in the [prefect-databricks](https://github.com/PrefectHQ/prefect-databricks) repository.

If you have any questions or issues while using `prefect-databricks`, you can find help in either the [Prefect Discourse forum](https://discourse.prefect.io/) or the [Prefect Slack community](https://prefect.io/slack).

Feel free to star or watch [`prefect-databricks`](https://github.com/PrefectHQ/prefect-databricks) for updates too!

### Contributing

If you'd like to help contribute to fix an issue or add a feature to `prefect-databricks`, please [propose changes through a pull request from a fork of the repository](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork).

Here are the steps:

1. [Fork the repository](https://docs.github.com/en/get-started/quickstart/fork-a-repo#forking-a-repository)
2. [Clone the forked repository](https://docs.github.com/en/get-started/quickstart/fork-a-repo#cloning-your-forked-repository)
3. Install the repository and its dependencies:
```
pip install -e ".[dev]"
```
4. Make desired changes
5. Add tests
6. Insert an entry to [CHANGELOG.md](https://github.com/PrefectHQ/prefect-databricks/blob/main/CHANGELOG.md)
7. Install `pre-commit` to perform quality checks prior to commit:
```
pre-commit install
```
8. `git commit`, `git push`, and create a pull request
