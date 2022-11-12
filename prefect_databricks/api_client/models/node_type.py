from typing import Any, Dict, List, Type, TypeVar, Union

from pydantic import BaseModel, Field

from ..models.cluster_cloud_provider_node_info import ClusterCloudProviderNodeInfo
from ..types import UNSET, Unset

T = TypeVar("T", bound="NodeType")


class NodeType(BaseModel):
    """
    Attributes:
        description (str): A string description associated with this node type. This field is required.
        instance_type_id (str): An identifier for the type of hardware that this node runs on. This field is required.
        memory_mb (int): Memory (in MB) available for this node type. This field is required.
        node_type_id (str): Unique identifier for this node type. This field is required.
        is_deprecated (Union[Unset, bool]): Whether the node type is deprecated. Non-deprecated node types offer greater
            performance.
        node_info (Union[Unset, ClusterCloudProviderNodeInfo]):
        num_cores (Union[Unset, float]): Number of CPU cores available for this node type. This can be fractional if the
            number of cores on a machine instance is not divisible by the number of Spark nodes on that machine. This field
            is required.
    """

    description: str = None
    instance_type_id: str = None
    memory_mb: int = None
    node_type_id: str = None
    is_deprecated: Union[Unset, bool] = UNSET
    node_info: Union[Unset, ClusterCloudProviderNodeInfo] = UNSET
    num_cores: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = Field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description
        instance_type_id = self.instance_type_id
        memory_mb = self.memory_mb
        node_type_id = self.node_type_id
        is_deprecated = self.is_deprecated
        node_info: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.node_info, Unset):
            node_info = self.node_info.to_dict()

        num_cores = self.num_cores

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "description": description,
                "instance_type_id": instance_type_id,
                "memory_mb": memory_mb,
                "node_type_id": node_type_id,
            }
        )
        if is_deprecated is not UNSET:
            field_dict["is_deprecated"] = is_deprecated
        if node_info is not UNSET:
            field_dict["node_info"] = node_info
        if num_cores is not UNSET:
            field_dict["num_cores"] = num_cores

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        if src_dict is None or src_dict is UNSET:
            return {}
        d = {k: v if v is not None else UNSET for k, v in src_dict.items()}
        description = d.pop("description")

        instance_type_id = d.pop("instance_type_id")

        memory_mb = d.pop("memory_mb")

        node_type_id = d.pop("node_type_id")

        is_deprecated = d.pop("is_deprecated", UNSET)

        _node_info = d.pop("node_info", UNSET)
        node_info: Union[Unset, ClusterCloudProviderNodeInfo]
        if isinstance(_node_info, Unset):
            node_info = UNSET
        else:
            node_info = ClusterCloudProviderNodeInfo.from_dict(_node_info)

        num_cores = d.pop("num_cores", UNSET)

        node_type = cls(
            description=description,
            instance_type_id=instance_type_id,
            memory_mb=memory_mb,
            node_type_id=node_type_id,
            is_deprecated=is_deprecated,
            node_info=node_info,
            num_cores=num_cores,
        )

        node_type.additional_properties = d
        return node_type

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
