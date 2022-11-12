from enum import Enum


class ClusterSource(str, Enum):
    UI = "UI"
    JOB = "JOB"
    API = "API"

    def __str__(self) -> str:
        return str(self.value)
