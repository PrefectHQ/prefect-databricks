import pytest
from httpx import AsyncClient

from prefect_databricks import DatabricksCredentials


@pytest.mark.parametrize("token", [None, "token_value"])
def test_databricks_credentials_get_client(token):
    client = DatabricksCredentials(token=token).get_client()
    assert isinstance(client, AsyncClient)
    if token is not None:
        assert client.headers["authorization"] == "Bearer token_value"
