from enum import Enum


class TriggerType(str, Enum):
    PERIODIC = "PERIODIC"
    ONE_TIME = "ONE_TIME"
    RETRY = "RETRY"

    def __str__(self) -> str:
        return str(self.value)
