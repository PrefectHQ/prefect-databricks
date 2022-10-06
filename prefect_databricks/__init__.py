from . import _version
from .credentials import DatabricksCredentials  # noqa: E501, F401

__version__ = _version.get_versions()["version"]
