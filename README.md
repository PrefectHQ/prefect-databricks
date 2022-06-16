# prefect-databricks

## Welcome!

Prefect tasks and subflows for interacting with Databricks.

The tasks within this collection were created by a code generator using the service's OpenAPI spec.

The service's REST API documentation can be found [here](https://docs.databricks.com/dev-tools/api/index.html).

## Getting Started

### Python setup

Requires an installation of Python 3.7+.

We recommend using a Python virtual environment manager such as pipenv, conda or virtualenv.

These tasks are designed to work with Prefect 2.0. For more information about how to use Prefect, please refer to the [Prefect documentation](https://orion-docs.prefect.io/).

### Installation

Install `prefect-databricks` with `pip`:

```bash
pip install prefect-databricks
```

### Write and run a flow

```python
from prefect import flow
from prefect_databricks import DatabricksCredentials
from prefect_databricks.jobs import get_2_1_jobs_list

@flow
def get_2_1_jobs_list_flow():
    token = "dapi..."
    databricks_instance = "dbc-ab1c23d4-567e.cloud.databricks.com"
    databricks_credentials = DatabricksCredentials(token=token)
    params = dict(limit=5, offset=0, expand_tasks=True)
    return get_2_1_jobs_list(databricks_instance, databricks_credentials, **params)

get_2_1_jobs_list_flow()
```

## Resources

If you encounter any bugs while using `prefect-databricks`, feel free to open an issue in the [prefect-databricks](https://github.com/PrefectHQ/prefect-databricks) repository.

If you have any questions or issues while using `prefect-databricks`, you can find help in either the [Prefect Discourse forum](https://discourse.prefect.io/) or the [Prefect Slack community](https://prefect.io/slack).

## Development

If you'd like to install a version of `prefect-databricks` for development, clone the repository and perform an editable install with `pip`:

```bash
git clone https://github.com/PrefectHQ/prefect-databricks.git

cd prefect-databricks/

pip install -e ".[dev]"

# Install linting pre-commit hooks
pre-commit install
```
