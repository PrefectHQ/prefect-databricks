from . import _version
from .credentials import DatabricksCredentials  # noqa
from .flows import jobs_runs_submit_and_wait_for_completion # noqa

__version__ = _version.get_versions()["version"]
