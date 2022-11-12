from enum import Enum


class CanManageRun(str, Enum):
    CAN_MANAGE_RUN = "CAN_MANAGE_RUN"

    def __str__(self) -> str:
        return str(self.value)
