from enum import Enum


class IsOwner(str, Enum):
    IS_OWNER = "IS_OWNER"

    def __str__(self) -> str:
        return str(self.value)
