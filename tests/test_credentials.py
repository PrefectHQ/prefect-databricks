from prefect_databricks import DatabricksCredentials
from prefect_databricks.api_client.client import AuthenticatedClient


def test_databricks_credentials_get_client():
    client = DatabricksCredentials(
        databricks_instance="databricks_instance", token="token_value"
    ).get_client()
    assert isinstance(client, AuthenticatedClient)
    assert client.auth_header_name == "Authorization"
    assert client.token == "token_value"
