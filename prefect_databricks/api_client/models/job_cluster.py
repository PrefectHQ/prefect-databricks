from typing import Any, Dict, List, Type, TypeVar, Union

from pydantic import BaseModel, Field

from ..models.new_cluster import NewCluster
from ..types import UNSET, Unset

T = TypeVar("T", bound="JobCluster")


class JobCluster(BaseModel):
    """
    Attributes:
        job_cluster_key (str): A unique name for the job cluster. This field is required and must be unique within the
            job.
            `JobTaskSettings` may refer to this field to determine which cluster to launch for the task execution. Example:
            auto_scaling_cluster.
        new_cluster (Union[Unset, NewCluster]):
    """

    job_cluster_key: str = None
    new_cluster: Union[Unset, NewCluster] = UNSET
    additional_properties: Dict[str, Any] = Field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        job_cluster_key = self.job_cluster_key
        new_cluster: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.new_cluster, Unset):
            new_cluster = self.new_cluster.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "job_cluster_key": job_cluster_key,
            }
        )
        if new_cluster is not UNSET:
            field_dict["new_cluster"] = new_cluster

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        if src_dict is None or src_dict is UNSET:
            return {}
        d = {k: v if v is not None else UNSET for k, v in src_dict.items()}
        job_cluster_key = d.pop("job_cluster_key")

        _new_cluster = d.pop("new_cluster", UNSET)
        new_cluster: Union[Unset, NewCluster]
        if isinstance(_new_cluster, Unset):
            new_cluster = UNSET
        else:
            new_cluster = NewCluster.from_dict(_new_cluster)

        job_cluster = cls(
            job_cluster_key=job_cluster_key,
            new_cluster=new_cluster,
        )

        job_cluster.additional_properties = d
        return job_cluster

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
