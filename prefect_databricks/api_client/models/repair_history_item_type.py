from enum import Enum


class RepairHistoryItemType(str, Enum):
    ORIGINAL = "ORIGINAL"
    REPAIR = "REPAIR"

    def __str__(self) -> str:
        return str(self.value)
