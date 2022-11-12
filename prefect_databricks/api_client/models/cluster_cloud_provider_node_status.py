from enum import Enum


class ClusterCloudProviderNodeStatus(str, Enum):
    NOTENABLEDONSUBSCRIPTION = "NotEnabledOnSubscription"
    NOTAVAILABLEINREGION = "NotAvailableInRegion"

    def __str__(self) -> str:
        return str(self.value)
