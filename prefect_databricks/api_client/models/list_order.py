from enum import Enum


class ListOrder(str, Enum):
    DESC = "DESC"
    ASC = "ASC"

    def __str__(self) -> str:
        return str(self.value)
