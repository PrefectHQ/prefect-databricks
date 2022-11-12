from enum import Enum


class AwsAttributesAvailability(str, Enum):
    SPOT = "SPOT"
    ON_DEMAND = "ON_DEMAND"
    SPOT_WITH_FALLBACK = "SPOT_WITH_FALLBACK"

    def __str__(self) -> str:
        return str(self.value)
