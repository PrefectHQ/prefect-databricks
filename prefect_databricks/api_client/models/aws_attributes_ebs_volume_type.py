from enum import Enum


class AwsAttributesEbsVolumeType(str, Enum):
    GENERAL_PURPOSE_SSD = "GENERAL_PURPOSE_SSD"
    THROUGHPUT_OPTIMIZED_HDD = "THROUGHPUT_OPTIMIZED_HDD"

    def __str__(self) -> str:
        return str(self.value)
