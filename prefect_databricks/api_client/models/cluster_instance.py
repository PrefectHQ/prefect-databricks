from typing import Any, Dict, List, Type, TypeVar, Union

from pydantic import BaseModel, Field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ClusterInstance")


class ClusterInstance(BaseModel):
    """
    Attributes:
        cluster_id (Union[Unset, str]): The canonical identifier for the cluster used by a run. This field is always
            available for runs on existing clusters. For runs on new clusters, it becomes available once the cluster is
            created. This value can be used to view logs by browsing to `/#setting/sparkui/$cluster_id/driver-logs`. The
            logs continue to be available after the run completes.

            The response won’t include this field if the identifier is not available yet. Example: 0923-164208-meows279.
        spark_context_id (Union[Unset, str]): The canonical identifier for the Spark context used by a run. This field
            is filled in once the run begins execution. This value can be used to view the Spark UI by browsing to
            `/#setting/sparkui/$cluster_id/$spark_context_id`. The Spark UI continues to be available after the run has
            completed.

            The response won’t include this field if the identifier is not available yet.
    """

    cluster_id: Union[Unset, str] = UNSET
    spark_context_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = Field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cluster_id = self.cluster_id
        spark_context_id = self.spark_context_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cluster_id is not UNSET:
            field_dict["cluster_id"] = cluster_id
        if spark_context_id is not UNSET:
            field_dict["spark_context_id"] = spark_context_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        if src_dict is None or src_dict is UNSET:
            return {}
        d = {k: v if v is not None else UNSET for k, v in src_dict.items()}
        cluster_id = d.pop("cluster_id", UNSET)

        spark_context_id = d.pop("spark_context_id", UNSET)

        cluster_instance = cls(
            cluster_id=cluster_id,
            spark_context_id=spark_context_id,
        )

        cluster_instance.additional_properties = d
        return cluster_instance

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
