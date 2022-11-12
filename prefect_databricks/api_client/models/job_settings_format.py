from enum import Enum


class JobSettingsFormat(str, Enum):
    SINGLE_TASK = "SINGLE_TASK"
    MULTI_TASK = "MULTI_TASK"

    def __str__(self) -> str:
        return str(self.value)
