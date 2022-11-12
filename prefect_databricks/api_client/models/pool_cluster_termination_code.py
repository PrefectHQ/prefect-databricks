from enum import Enum


class PoolClusterTerminationCode(str, Enum):
    INSTANCE_POOL_MAX_CAPACITY_FAILURE = "INSTANCE_POOL_MAX_CAPACITY_FAILURE"
    INSTANCE_POOL_NOT_FOUND_FAILURE = "INSTANCE_POOL_NOT_FOUND_FAILURE"

    def __str__(self) -> str:
        return str(self.value)
