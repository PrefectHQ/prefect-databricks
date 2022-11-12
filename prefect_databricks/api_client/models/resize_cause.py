from enum import Enum


class ResizeCause(str, Enum):
    AUTOSCALE = "AUTOSCALE"
    USER_REQUEST = "USER_REQUEST"
    AUTORECOVERY = "AUTORECOVERY"

    def __str__(self) -> str:
        return str(self.value)
