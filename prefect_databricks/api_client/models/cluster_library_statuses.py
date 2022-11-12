from typing import Any, Dict, List, Type, TypeVar, Union

from pydantic import BaseModel, Field

from ..models.library_full_status import LibraryFullStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="ClusterLibraryStatuses")


class ClusterLibraryStatuses(BaseModel):
    """
    Attributes:
        cluster_id (Union[Unset, str]): Unique identifier for the cluster.
        library_statuses (Union[Unset, List[LibraryFullStatus]]): Status of all libraries on the cluster.
    """

    cluster_id: Union[Unset, str] = UNSET
    library_statuses: Union[Unset, List[LibraryFullStatus]] = UNSET
    additional_properties: Dict[str, Any] = Field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cluster_id = self.cluster_id
        library_statuses: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.library_statuses, Unset):
            library_statuses = []
            for library_statuses_item_data in self.library_statuses:
                library_statuses_item = library_statuses_item_data.to_dict()

                library_statuses.append(library_statuses_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cluster_id is not UNSET:
            field_dict["cluster_id"] = cluster_id
        if library_statuses is not UNSET:
            field_dict["library_statuses"] = library_statuses

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        if src_dict is None or src_dict is UNSET:
            return {}
        d = {k: v if v is not None else UNSET for k, v in src_dict.items()}
        cluster_id = d.pop("cluster_id", UNSET)

        library_statuses = []
        _library_statuses = d.pop("library_statuses", UNSET)
        for library_statuses_item_data in _library_statuses or []:
            library_statuses_item = LibraryFullStatus.from_dict(
                library_statuses_item_data
            )

            library_statuses.append(library_statuses_item)

        cluster_library_statuses = cls(
            cluster_id=cluster_id,
            library_statuses=library_statuses,
        )

        cluster_library_statuses.additional_properties = d
        return cluster_library_statuses

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
