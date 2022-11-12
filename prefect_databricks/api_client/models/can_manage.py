from enum import Enum


class CanManage(str, Enum):
    CAN_MANAGE = "CAN_MANAGE"

    def __str__(self) -> str:
        return str(self.value)
