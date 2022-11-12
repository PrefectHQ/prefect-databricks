from typing import Any, Dict, List, Type, TypeVar, Union

from pydantic import BaseModel, Field

from ..models.cluster_cloud_provider_node_status import ClusterCloudProviderNodeStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="ClusterCloudProviderNodeInfo")


class ClusterCloudProviderNodeInfo(BaseModel):
    """
    Attributes:
        available_core_quota (Union[Unset, int]): Available CPU core quota.
        status (Union[Unset, ClusterCloudProviderNodeStatus]): * NotEnabledOnSubscription: Node type not available for
            subscription.
            * NotAvailableInRegion: Node type not available in region.
        total_core_quota (Union[Unset, int]): Total CPU core quota.
    """

    available_core_quota: Union[Unset, int] = UNSET
    status: Union[Unset, ClusterCloudProviderNodeStatus] = UNSET
    total_core_quota: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = Field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        available_core_quota = self.available_core_quota
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        total_core_quota = self.total_core_quota

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if available_core_quota is not UNSET:
            field_dict["available_core_quota"] = available_core_quota
        if status is not UNSET:
            field_dict["status"] = status
        if total_core_quota is not UNSET:
            field_dict["total_core_quota"] = total_core_quota

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        if src_dict is None or src_dict is UNSET:
            return {}
        d = {k: v if v is not None else UNSET for k, v in src_dict.items()}
        available_core_quota = d.pop("available_core_quota", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, ClusterCloudProviderNodeStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = ClusterCloudProviderNodeStatus(_status)

        total_core_quota = d.pop("total_core_quota", UNSET)

        cluster_cloud_provider_node_info = cls(
            available_core_quota=available_core_quota,
            status=status,
            total_core_quota=total_core_quota,
        )

        cluster_cloud_provider_node_info.additional_properties = d
        return cluster_cloud_provider_node_info

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
