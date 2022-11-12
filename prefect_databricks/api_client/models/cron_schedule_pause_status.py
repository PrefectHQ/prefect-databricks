from enum import Enum


class CronSchedulePauseStatus(str, Enum):
    PAUSED = "PAUSED"
    UNPAUSED = "UNPAUSED"

    def __str__(self) -> str:
        return str(self.value)
