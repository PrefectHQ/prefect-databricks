import httpx
import pytest

from prefect_databricks import DatabricksCredentials
from prefect_databricks.rest import HTTPMethod, execute_endpoint, strip_kwargs


@pytest.mark.parametrize("params", [dict(a="A", b="B"), None])
@pytest.mark.parametrize("http_method", ["get", HTTPMethod.GET, "post"])
async def test_execute_endpoint(params, http_method, respx_mock):
    url = "https://prefect.io/"

    respx_mock.get(url).mock(return_value=httpx.Response(200))
    respx_mock.post(url).mock(return_value=httpx.Response(200))

    execute_kwargs = dict()
    if http_method == "post":
        execute_kwargs["json"] = {"key": "val"}

    credentials = DatabricksCredentials()
    response = await execute_endpoint.fn(
        url, credentials, http_method=http_method, params=params, **execute_kwargs
    )
    assert response.status_code == 200


def test_strip_kwargs():
    assert strip_kwargs(**{"a": None, "b": None}) == {}
    assert strip_kwargs(**{"a": "", "b": None}) == {"a": ""}
    assert strip_kwargs(**{"a": "abc", "b": "def"}) == {"a": "abc", "b": "def"}
    assert strip_kwargs(a="abc", b="def") == {"a": "abc", "b": "def"}
    assert strip_kwargs(**dict(a=[])) == {"a": []}
