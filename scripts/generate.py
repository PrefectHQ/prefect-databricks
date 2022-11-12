"""
Used for generating the repository from scratch.
"""
from pathlib import Path

from prefect_collection_generator.preprocess import (
    convert_required_to_sequence,
    migrate_required_directly_under_model,
    set_item_type_for_array,
)
from prefect_collection_generator.rest import populate_collection_repo

THIS_DIRECTORY = Path(__file__).parent.absolute()
REPO_DIRECTORY = THIS_DIRECTORY.parent

# USE THIS IF NEED TO REGENERATE FROM SCRATCH; IF NOT SKIP TO NEXT SECTION
# from cookiecutter.main import cookiecutter

# extra_context = {
#     "full_name": "Prefect Technologies, Inc.",  # e.g. "Prefect Technologies, Inc.",
#     "email": "help@prefect.io",  # e.g. "help@prefect.io",
#     "github_organization": "PrefectHQ",  # e.g. "PrefectHQ",
#     "collection_name": "prefect-databricks",
#     "collection_short_description": "Prefect integrations interacting with Databricks",  # noqa
# }

# collection_template_url = "https://github.com/PrefectHQ/prefect-collection-template"
# cookiecutter(
#     collection_template_url,
#     no_input=True,
#     checkout="generated_rest",
#     extra_context=extra_context,
#     overwrite_if_exists=True,
# )
# REPO_DIRECTORY = THIS_DIRECTORY / "prefect-databricks"  # redirects repo_directory

# UPDATE THESE AS DESIRED
service_name = "Databricks"
urls = ["https://docs.databricks.com/_static/api-refs/jobs-2.1-aws.yaml"]
routes = None
overwrite = True


if __name__ == "__main__":
    populate_collection_repo(
        service_name,
        urls,
        routes=routes,
        overwrite=overwrite,
        preprocess_hooks=[
            migrate_required_directly_under_model,
            convert_required_to_sequence,
            set_item_type_for_array,
        ],
        repo_directory=REPO_DIRECTORY,
    )
