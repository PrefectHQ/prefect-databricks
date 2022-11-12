from typing import Any, Dict, List, Type, TypeVar, Union

from pydantic import BaseModel, Field

from ..models.aws_attributes import AwsAttributes
from ..models.cluster_size import ClusterSize
from ..models.resize_cause import ResizeCause
from ..models.termination_reason import TerminationReason
from ..types import UNSET, Unset

T = TypeVar("T", bound="EventDetails")


class EventDetails(BaseModel):
    """
    Attributes:
        attributes (Union[Unset, AwsAttributes]):
        cause (Union[Unset, ResizeCause]): * `AUTOSCALE`: Automatically resized based on load.
            * `USER_REQUEST`: User requested a new size.
            * `AUTORECOVERY`: Autorecovery monitor resized the cluster after it lost a node.
        cluster_size (Union[Unset, ClusterSize]):
        current_num_workers (Union[Unset, int]): The number of nodes in the cluster.
        previous_attributes (Union[Unset, AwsAttributes]):
        previous_cluster_size (Union[Unset, ClusterSize]):
        reason (Union[Unset, TerminationReason]):
        target_num_workers (Union[Unset, int]): The targeted number of nodes in the cluster.
        user (Union[Unset, str]): The user that caused the event to occur. (Empty if it was done by Databricks.)
    """

    attributes: Union[Unset, AwsAttributes] = UNSET
    cause: Union[Unset, ResizeCause] = UNSET
    cluster_size: Union[Unset, ClusterSize] = UNSET
    current_num_workers: Union[Unset, int] = UNSET
    previous_attributes: Union[Unset, AwsAttributes] = UNSET
    previous_cluster_size: Union[Unset, ClusterSize] = UNSET
    reason: Union[Unset, TerminationReason] = UNSET
    target_num_workers: Union[Unset, int] = UNSET
    user: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = Field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        attributes: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        cause: Union[Unset, str] = UNSET
        if not isinstance(self.cause, Unset):
            cause = self.cause.value

        cluster_size: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cluster_size, Unset):
            cluster_size = self.cluster_size.to_dict()

        current_num_workers = self.current_num_workers
        previous_attributes: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.previous_attributes, Unset):
            previous_attributes = self.previous_attributes.to_dict()

        previous_cluster_size: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.previous_cluster_size, Unset):
            previous_cluster_size = self.previous_cluster_size.to_dict()

        reason: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.reason, Unset):
            reason = self.reason.to_dict()

        target_num_workers = self.target_num_workers
        user = self.user

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if cause is not UNSET:
            field_dict["cause"] = cause
        if cluster_size is not UNSET:
            field_dict["cluster_size"] = cluster_size
        if current_num_workers is not UNSET:
            field_dict["current_num_workers"] = current_num_workers
        if previous_attributes is not UNSET:
            field_dict["previous_attributes"] = previous_attributes
        if previous_cluster_size is not UNSET:
            field_dict["previous_cluster_size"] = previous_cluster_size
        if reason is not UNSET:
            field_dict["reason"] = reason
        if target_num_workers is not UNSET:
            field_dict["target_num_workers"] = target_num_workers
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        if src_dict is None or src_dict is UNSET:
            return {}
        d = {k: v if v is not None else UNSET for k, v in src_dict.items()}
        _attributes = d.pop("attributes", UNSET)
        attributes: Union[Unset, AwsAttributes]
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = AwsAttributes.from_dict(_attributes)

        _cause = d.pop("cause", UNSET)
        cause: Union[Unset, ResizeCause]
        if isinstance(_cause, Unset):
            cause = UNSET
        else:
            cause = ResizeCause(_cause)

        _cluster_size = d.pop("cluster_size", UNSET)
        cluster_size: Union[Unset, ClusterSize]
        if isinstance(_cluster_size, Unset):
            cluster_size = UNSET
        else:
            cluster_size = ClusterSize.from_dict(_cluster_size)

        current_num_workers = d.pop("current_num_workers", UNSET)

        _previous_attributes = d.pop("previous_attributes", UNSET)
        previous_attributes: Union[Unset, AwsAttributes]
        if isinstance(_previous_attributes, Unset):
            previous_attributes = UNSET
        else:
            previous_attributes = AwsAttributes.from_dict(_previous_attributes)

        _previous_cluster_size = d.pop("previous_cluster_size", UNSET)
        previous_cluster_size: Union[Unset, ClusterSize]
        if isinstance(_previous_cluster_size, Unset):
            previous_cluster_size = UNSET
        else:
            previous_cluster_size = ClusterSize.from_dict(_previous_cluster_size)

        _reason = d.pop("reason", UNSET)
        reason: Union[Unset, TerminationReason]
        if isinstance(_reason, Unset):
            reason = UNSET
        else:
            reason = TerminationReason.from_dict(_reason)

        target_num_workers = d.pop("target_num_workers", UNSET)

        user = d.pop("user", UNSET)

        event_details = cls(
            attributes=attributes,
            cause=cause,
            cluster_size=cluster_size,
            current_num_workers=current_num_workers,
            previous_attributes=previous_attributes,
            previous_cluster_size=previous_cluster_size,
            reason=reason,
            target_num_workers=target_num_workers,
            user=user,
        )

        event_details.additional_properties = d
        return event_details

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
