class DatabricksException(Exception):
    """Base exception for Databricks errors"""


class DatabricksJobTerminated(DatabricksException):
    """Raised when Databricks jobs runs submit terminates"""


class DatabricksJobSkipped(DatabricksException):
    """Raised when Databricks jobs runs submit skips"""


class DatabricksJobInternalError(DatabricksException):
    """Raised when Databricks jobs runs submit encounters internal error"""


class DatabricksJobRunTimedOut(DatabricksException):
    """
    Raised when Databricks jobs runs does not complete in the configured max
    wait seconds
    """
