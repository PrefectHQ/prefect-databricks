from enum import Enum


class NotebookTaskSource(str, Enum):
    WORKSPACE = "WORKSPACE"
    GIT = "GIT"

    def __str__(self) -> str:
        return str(self.value)
