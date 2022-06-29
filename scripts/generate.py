
# from cookiecutter.main import cookiecutter
from prefect_collection_generator.rest import populate_collection_repo

# UPDATE THIS SECTION
extra_context = {
    "collection_name": "prefect-databricks",
    "collection_short_description": "Prefect integrations interacting with Databricks",  # noqa
}
collection_template_url = "https://github.com/PrefectHQ/prefect-collection-template"
service_name = "Databricks"
urls = [
#     "https://docs.databricks.com/_static/api-refs/account-2.0-aws.yaml",  # noqa
#     "https://docs.databricks.com/_static/api-refs/queries-dashboards-2.0-aws.json",  # noqa
#     "https://docs.databricks.com/_static/api-refs/history-2.0-aws.yaml",  # noqa
#     "https://docs.databricks.com/_static/api-refs/gitcredentials-2.0-aws.yaml",  # noqa
#     "https://docs.databricks.com/_static/api-refs/global-init-scripts-2.0-aws.json",  # noqa
#     "https://docs.databricks.com/_static/api-refs/ip-access-list-aws.yaml",  # noqa
    "https://docs.databricks.com/_static/api-refs/jobs-2.1-aws.yaml",  # noqa
#     "https://docs.databricks.com/_static/api-refs/mlflow-2.0-aws.yaml",  # noqa
#     "https://docs.databricks.com/_static/api-refs/permissions-2.0-aws.yaml",  # noqa
#     "https://docs.databricks.com/_static/api-refs/repos-2.0-aws.yaml",  # noqa
#     "https://docs.databricks.com/_static/api-refs/token-management-2.0-aws.json",  # noqa
]
routes = None
overwrite = True

def preprocess_fn(schema):
    for key, value in schema.items():
        if isinstance(value, dict):
            value = preprocess_fn(value)
        if key == "required":
            if isinstance(value, list):
                schema[key] = value
            else:
                schema[key] = [value]
        elif key == "items":
            if isinstance(value, (dict, list)):
                schema[key] = value
            else:
                schema[key] = {"type": value}
        else:
            schema[key] = value
    return schema

# cookiecutter(
#     collection_template_url,
#     no_input=True,
#     checkout="generated_rest",
#     extra_context=extra_context,
#     overwrite_if_exists=True,
# )

populate_collection_repo(
    service_name,
    urls,
    routes=routes,
    preprocess_fn=preprocess_fn,
    overwrite=overwrite,
    repo_directory=".."
)
