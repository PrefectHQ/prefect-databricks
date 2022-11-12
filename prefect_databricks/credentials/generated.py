"""
This is a module containing credentials, auto-generated, used
to perform authenticated interactions with Databricks.
"""

# This module was auto-generated using prefect-collection-generator so
# manually editing this file is not recommended. If this module is outdated
# rerun scripts/generate.py. To override the default generated output:
# 1. create a separate module and rewrite the class / function
# 2. import in `__init__.py`, under the `from .generated import *` line
# 3. hide the generated function in `docs/.md` under `options`


from typing import Any, Dict

from prefect.blocks.core import Block
from pydantic import Field, SecretStr

from prefect_databricks.api_client.client import AuthenticatedClient


class DatabricksCredentials(Block):
    """
    Block used to manage Databricks authentication.

    Attributes:
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        token: The token to authenticate with Databricks.

        timeout: Number of seconds before the request times out.
        client_kwargs: Additional keyword arguments to pass to
            `prefect_databricks.api_client.client.AuthenticatedClient`.

    Examples:
        Load stored Databricks credentials:
        ```python
        from prefect_databricks import DatabricksCredentials
        databricks_credentials_block = DatabricksCredentials.load("BLOCK_NAME")
        ```
    """

    _block_type_name = "Databricks Credentials"
    # _logo_url = "<UPDATE _logo_url IN __init__.py>"  # noqa

    databricks_instance: str = Field(
        default=..., description="Used in formatting the base URL."
    )
    token: SecretStr = Field(default=..., description="Token used for authentication.")
    timeout: float = Field(
        default=5.0, description="Number of seconds before the request times out."
    )
    client_kwargs: Dict[str, Any] = Field(
        default_factory=dict,
        title="Additional configuration",
        description=(
            "Additional keyword arguments to pass to "
            "`prefect_databricks.api_client.client.AuthenticatedClient`."
        ),
    )

    def get_client(self) -> AuthenticatedClient:
        """
        Gets a Databricks REST API Authenticated Client.

        Returns:
            A Databricks REST API Authenticated Client.

        Example:
            Gets a Databricks REST API Authenticated Client.
            ```python
            from prefect import flow
            from prefect_databricks import DatabricksCredentials

            @flow
            def example_get_client_flow():
                token = "consumer_key"
                databricks_credentials = DatabricksCredentials(token=token)
                client = databricks_credentials.get_client()
                return client

            example_get_client_flow()
            ```
        """

        base_url = f"https://{self.databricks_instance}/api/"

        client_kwargs = self.client_kwargs.copy()
        token = self.token.get_secret_value()
        prefix = "Bearer"
        client = AuthenticatedClient(
            base_url=base_url,
            token=token,
            prefix=prefix,
            timeout=self.timeout,
            **client_kwargs,
        )
        return client
