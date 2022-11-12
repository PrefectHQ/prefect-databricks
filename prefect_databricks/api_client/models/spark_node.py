from typing import Any, Dict, List, Type, TypeVar, Union

from pydantic import BaseModel, Field

from ..models.spark_node_aws_attributes import SparkNodeAwsAttributes
from ..types import UNSET, Unset

T = TypeVar("T", bound="SparkNode")


class SparkNode(BaseModel):
    """
    Attributes:
        host_private_ip (Union[Unset, str]): The private IP address of the host instance.
        instance_id (Union[Unset, str]): Globally unique identifier for the host instance from the cloud provider.
        node_aws_attributes (Union[Unset, SparkNodeAwsAttributes]):
        node_id (Union[Unset, str]): Globally unique identifier for this node.
        private_ip (Union[Unset, str]): Private IP address (typically a 10.x.x.x address) of the Spark node. This is
            different from the private IP address of the host instance.
        public_dns (Union[Unset, str]): Public DNS address of this node. This address can be used to access the Spark
            JDBC server on the driver node. To communicate with the JDBC server, traffic must be manually authorized by
            adding security group rules to the “worker-unmanaged” security group via the AWS console.
        start_timestamp (Union[Unset, int]): The timestamp (in millisecond) when the Spark node is launched.
    """

    host_private_ip: Union[Unset, str] = UNSET
    instance_id: Union[Unset, str] = UNSET
    node_aws_attributes: Union[Unset, SparkNodeAwsAttributes] = UNSET
    node_id: Union[Unset, str] = UNSET
    private_ip: Union[Unset, str] = UNSET
    public_dns: Union[Unset, str] = UNSET
    start_timestamp: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = Field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        host_private_ip = self.host_private_ip
        instance_id = self.instance_id
        node_aws_attributes: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.node_aws_attributes, Unset):
            node_aws_attributes = self.node_aws_attributes.to_dict()

        node_id = self.node_id
        private_ip = self.private_ip
        public_dns = self.public_dns
        start_timestamp = self.start_timestamp

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if host_private_ip is not UNSET:
            field_dict["host_private_ip"] = host_private_ip
        if instance_id is not UNSET:
            field_dict["instance_id"] = instance_id
        if node_aws_attributes is not UNSET:
            field_dict["node_aws_attributes"] = node_aws_attributes
        if node_id is not UNSET:
            field_dict["node_id"] = node_id
        if private_ip is not UNSET:
            field_dict["private_ip"] = private_ip
        if public_dns is not UNSET:
            field_dict["public_dns"] = public_dns
        if start_timestamp is not UNSET:
            field_dict["start_timestamp"] = start_timestamp

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        if src_dict is None or src_dict is UNSET:
            return {}
        d = {k: v if v is not None else UNSET for k, v in src_dict.items()}
        host_private_ip = d.pop("host_private_ip", UNSET)

        instance_id = d.pop("instance_id", UNSET)

        _node_aws_attributes = d.pop("node_aws_attributes", UNSET)
        node_aws_attributes: Union[Unset, SparkNodeAwsAttributes]
        if isinstance(_node_aws_attributes, Unset):
            node_aws_attributes = UNSET
        else:
            node_aws_attributes = SparkNodeAwsAttributes.from_dict(_node_aws_attributes)

        node_id = d.pop("node_id", UNSET)

        private_ip = d.pop("private_ip", UNSET)

        public_dns = d.pop("public_dns", UNSET)

        start_timestamp = d.pop("start_timestamp", UNSET)

        spark_node = cls(
            host_private_ip=host_private_ip,
            instance_id=instance_id,
            node_aws_attributes=node_aws_attributes,
            node_id=node_id,
            private_ip=private_ip,
            public_dns=public_dns,
            start_timestamp=start_timestamp,
        )

        spark_node.additional_properties = d
        return spark_node

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
