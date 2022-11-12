from typing import Any, Dict, List, Type, TypeVar, Union

from pydantic import BaseModel, Field

from ..models.cluster_event_type import ClusterEventType
from ..models.event_details import EventDetails
from ..types import UNSET, Unset

T = TypeVar("T", bound="ClusterEvent")


class ClusterEvent(BaseModel):
    """
    Attributes:
        cluster_id (str): Canonical identifier for the cluster. This field is required.
        details (EventDetails):
        type (ClusterEventType): * `CREATING`: Indicates that the cluster is being created.
            * `DID_NOT_EXPAND_DISK`: Indicates that a disk is low on space, but adding disks would put it over the max
            capacity.
            * `EXPANDED_DISK`: Indicates that a disk was low on space and the disks were expanded.
            * `FAILED_TO_EXPAND_DISK`: Indicates that a disk was low on space and disk space could not be expanded.
            * `INIT_SCRIPTS_STARTING`: Indicates that the cluster scoped init script has started.
            * `INIT_SCRIPTS_FINISHED`: Indicates that the cluster scoped init script has finished.
            * `STARTING`: Indicates that the cluster is being started.
            * `RESTARTING`: Indicates that the cluster is being started.
            * `TERMINATING`: Indicates that the cluster is being terminated.
            * `EDITED`: Indicates that the cluster has been edited.
            * `RUNNING`: Indicates the cluster has finished being created. Includes the number of nodes in the cluster and a
            failure reason if some nodes could not be acquired.
            * `RESIZING`: Indicates a change in the target size of the cluster (upsize or downsize).
            * `UPSIZE_COMPLETED`: Indicates that nodes finished being added to the cluster. Includes the number of nodes in
            the cluster and a failure reason if some nodes could not be acquired.
            * `NODES_LOST`: Indicates that some nodes were lost from the cluster.
            * `DRIVER_HEALTHY`: Indicates that the driver is healthy and the cluster is ready for use.
            * `DRIVER_UNAVAILABLE`: Indicates that the driver is unavailable.
            * `SPARK_EXCEPTION`: Indicates that a Spark exception was thrown from the driver.
            * `DRIVER_NOT_RESPONDING`: Indicates that the driver is up but is not responsive, likely due to GC.
            * `DBFS_DOWN`: Indicates that the driver is up but DBFS is down.
            * `METASTORE_DOWN`: Indicates that the driver is up but the metastore is down.
            * `NODE_BLACKLISTED`: Indicates that a node is not allowed by Spark.
            * `PINNED`: Indicates that the cluster was pinned.
            * `UNPINNED`: Indicates that the cluster was unpinned.
        timestamp (Union[Unset, int]): The timestamp when the event occurred, stored as the number of milliseconds since
            the unix epoch. Assigned by the Timeline service.
    """

    cluster_id: str = None
    details: EventDetails = None
    type: ClusterEventType = None
    timestamp: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = Field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cluster_id = self.cluster_id
        details = self.details.to_dict()

        type = self.type.value

        timestamp = self.timestamp

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "cluster_id": cluster_id,
                "details": details,
                "type": type,
            }
        )
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        if src_dict is None or src_dict is UNSET:
            return {}
        d = {k: v if v is not None else UNSET for k, v in src_dict.items()}
        cluster_id = d.pop("cluster_id")

        details = EventDetails.from_dict(d.pop("details"))

        type = ClusterEventType(d.pop("type"))

        timestamp = d.pop("timestamp", UNSET)

        cluster_event = cls(
            cluster_id=cluster_id,
            details=details,
            type=type,
            timestamp=timestamp,
        )

        cluster_event.additional_properties = d
        return cluster_event

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
