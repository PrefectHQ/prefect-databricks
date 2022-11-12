from enum import Enum


class RunType(str, Enum):
    JOB_RUN = "JOB_RUN"
    WORKFLOW_RUN = "WORKFLOW_RUN"
    SUBMIT_RUN = "SUBMIT_RUN"

    def __str__(self) -> str:
        return str(self.value)
