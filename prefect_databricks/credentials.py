"""Credential classes used to perform authenticated interactions with Databricks"""

from httpx import AsyncClient
from prefect.blocks.core import Block
from pydantic import SecretStr


class DatabricksCredentials(Block):
    """
    Block used to manage Databricks authentication.

    Args:
        token: the token to authenticate into Databricks.

    Examples:
        Load stored Databricks credentials:
        ```python
        from prefect_databricks import DatabricksCredentials
        databricks_credentials_block = DatabricksCredentials.load("BLOCK_NAME")
        ```
    """

    token: SecretStr = None

    def get_client(self) -> AsyncClient:
        """
        Gets an authenticated Databricks REST AsyncClient.

        Returns:
            An authenticated Databricks REST AsyncClient

        Example:
            Gets an authenticated Databricks REST AsyncClient.
            ```python
            from prefect import flow
            from prefect_databricks import DatabricksCredentials

            @flow
            def example_get_client_flow():
                token = "consumer_key"
                databricks_credentials = DatabricksCredentials(token=token)
                endpoint = databricks_credentials.get_client()
                return endpoint

            example_get_client_flow()
            ```
        """
        if self.token is not None:
            headers = {"Authorization": f"Bearer {self.token.get_secret_value()}"}
        else:
            headers = None
        client = AsyncClient(headers=headers)
        return client
