from enum import Enum


class CanView(str, Enum):
    CAN_VIEW = "CAN_VIEW"

    def __str__(self) -> str:
        return str(self.value)
