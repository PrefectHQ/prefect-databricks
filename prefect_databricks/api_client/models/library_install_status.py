from enum import Enum


class LibraryInstallStatus(str, Enum):
    PENDING = "PENDING"
    RESOLVING = "RESOLVING"
    INSTALLING = "INSTALLING"
    INSTALLED = "INSTALLED"
    SKIPPED = "SKIPPED"
    FAILED = "FAILED"
    UNINSTALL_ON_RESTART = "UNINSTALL_ON_RESTART"

    def __str__(self) -> str:
        return str(self.value)
