from enum import Enum


class TerminationType(str, Enum):
    SUCCESS = "SUCCESS"
    CLIENT_ERROR = "CLIENT_ERROR"
    SERVICE_FAULT = "SERVICE_FAULT"
    CLOUD_FAILURE = "CLOUD_FAILURE"

    def __str__(self) -> str:
        return str(self.value)
