"""Credential classes used to perform authenticated interactions with Databricks"""

from dataclasses import dataclass

from httpx import AsyncClient


@dataclass
class DatabricksCredentials:
    """
    Dataclass used to manage Databricks authentication.

    Args:
        token: the token to authenticate into Databricks.
    """

    token: str = None

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
                databricks_credentials = DatabricksCredentials(token)
                endpoint = databricks_credentials.get_client()
                return endpoint

            example_get_client_flow()
            ```
        """
        if self.token is not None:
            headers = {"Authorization": f"Bearer {self.token}"}
        else:
            headers = None
        client = AsyncClient(headers=headers)
        return client
