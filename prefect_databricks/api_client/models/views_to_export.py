from enum import Enum


class ViewsToExport(str, Enum):
    CODE = "CODE"
    DASHBOARDS = "DASHBOARDS"
    ALL = "ALL"

    def __str__(self) -> str:
        return str(self.value)
