from typing import Any, Dict, List, Type, TypeVar, Union, cast

from pydantic import BaseModel, Field

from ..models.library import Library
from ..models.library_install_status import LibraryInstallStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="LibraryFullStatus")


class LibraryFullStatus(BaseModel):
    """
    Attributes:
        is_library_for_all_clusters (Union[Unset, bool]): Whether the library was set to be installed on all clusters
            via the libraries UI.
        library (Union[Unset, Library]):
        messages (Union[Unset, List[str]]): All the info and warning messages that have occurred so far for this
            library.
        status (Union[Unset, LibraryInstallStatus]): * `PENDING`: No action has yet been taken to install the library.
            This state should be very short lived.
            * `RESOLVING`: Metadata necessary to install the library is being retrieved from the provided repository. For
            Jar, Egg, and Whl libraries, this step is a no-op.
            * `INSTALLING`: The library is actively being installed, either by adding resources to Spark or executing system
            commands inside the Spark nodes.
            * `INSTALLED`: The library has been successfully instally.
            * `SKIPPED`: Installation on a Databricks Runtime 7.0 or above cluster was skipped due to Scala version
            incompatibility.
            * `FAILED`: Some step in installation failed. More information can be found in the messages field.
            * `UNINSTALL_ON_RESTART`: The library has been marked for removal. Libraries can be removed only when clusters
            are restarted, so libraries that enter this state remains until the cluster is restarted.
    """

    is_library_for_all_clusters: Union[Unset, bool] = UNSET
    library: Union[Unset, Library] = UNSET
    messages: Union[Unset, List[str]] = UNSET
    status: Union[Unset, LibraryInstallStatus] = UNSET
    additional_properties: Dict[str, Any] = Field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        is_library_for_all_clusters = self.is_library_for_all_clusters
        library: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.library, Unset):
            library = self.library.to_dict()

        messages: Union[Unset, List[str]] = UNSET
        if not isinstance(self.messages, Unset):
            messages = self.messages

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_library_for_all_clusters is not UNSET:
            field_dict["is_library_for_all_clusters"] = is_library_for_all_clusters
        if library is not UNSET:
            field_dict["library"] = library
        if messages is not UNSET:
            field_dict["messages"] = messages
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        if src_dict is None or src_dict is UNSET:
            return {}
        d = {k: v if v is not None else UNSET for k, v in src_dict.items()}
        is_library_for_all_clusters = d.pop("is_library_for_all_clusters", UNSET)

        _library = d.pop("library", UNSET)
        library: Union[Unset, Library]
        if isinstance(_library, Unset):
            library = UNSET
        else:
            library = Library.from_dict(_library)

        messages = cast(List[str], d.pop("messages", UNSET))

        _status = d.pop("status", UNSET)
        status: Union[Unset, LibraryInstallStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = LibraryInstallStatus(_status)

        library_full_status = cls(
            is_library_for_all_clusters=is_library_for_all_clusters,
            library=library,
            messages=messages,
            status=status,
        )

        library_full_status.additional_properties = d
        return library_full_status

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties.get(key)

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
