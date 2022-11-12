from enum import Enum


class ViewType(str, Enum):
    NOTEBOOK = "NOTEBOOK"
    DASHBOARD = "DASHBOARD"

    def __str__(self) -> str:
        return str(self.value)
