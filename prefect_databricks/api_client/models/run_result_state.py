from enum import Enum


class RunResultState(str, Enum):
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"
    TIMEDOUT = "TIMEDOUT"
    CANCELED = "CANCELED"

    def __str__(self) -> str:
        return str(self.value)
