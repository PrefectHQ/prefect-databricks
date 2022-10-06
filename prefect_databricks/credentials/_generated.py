"""Credential classes used to perform authenticated interactions with Databricks"""

from typing import Any, Dict, Optional

from httpx import AsyncClient
from prefect.blocks.core import Block
from pydantic import Field, SecretStr


class DatabricksCredentials(Block):
    """
    Block used to manage Databricks authentication.

    Attributes:
        databricks_instance:
            Databricks instance used in formatting the endpoint URL.
        token: The token to authenticate with Databricks.


    Examples:
        Load stored Databricks credentials:
        ```python
        from prefect_databricks import DatabricksCredentials
        databricks_credentials_block = DatabricksCredentials.load("BLOCK_NAME")
        ```
    """

    _block_type_name = "Databricks Credentials"
    # _logo_url = "<LOGO_URL_HERE>"  # noqa

    databricks_instance: str = Field(
        default=..., description="Used in formatting the base URL."
    )
    token: SecretStr = Field(default=..., description="Token used for authentication.")
    client_kwargs: Dict[str, Any] = Field(
        default_factory=dict,
        description="Additional keyword arguments to pass to AsyncClient.",
    )

    def get_client(self) -> AsyncClient:
        """
        Gets a Databricks REST AsyncClient.

        Returns:
            A Databricks REST AsyncClient.

        Example:
            Gets a Databricks REST AsyncClient.
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
        client_kwargs["headers"] = {
            "Authorization": f"Bearer {self.token.get_secret_value()}"
        }
        client = AsyncClient(base_url=base_url, **client_kwargs)
        return client
