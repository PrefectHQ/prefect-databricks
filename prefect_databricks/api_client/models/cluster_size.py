from typing import Any, Dict, List, Type, TypeVar, Union

from pydantic import BaseModel, Field

from ..models.auto_scale import AutoScale
from ..types import UNSET, Unset

T = TypeVar("T", bound="ClusterSize")


class ClusterSize(BaseModel):
    """
    Attributes:
        autoscale (Union[Unset, AutoScale]):
        num_workers (Union[Unset, int]): If num_workers, number of worker nodes that this cluster must have. A cluster
            has one Spark driver and num_workers executors for a total of num_workers + 1 Spark nodes. When reading the
            properties of a cluster, this field reflects the desired number of workers rather than the actual number of
            workers. For instance, if a cluster is resized from 5 to 10 workers, this field is updated to reflect the target
            size of 10 workers, whereas the workers listed in executors gradually increase from 5 to 10 as the new nodes are
            provisioned.
    """

    autoscale: Union[Unset, AutoScale] = UNSET
    num_workers: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = Field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        autoscale: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.autoscale, Unset):
            autoscale = self.autoscale.to_dict()

        num_workers = self.num_workers

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if autoscale is not UNSET:
            field_dict["autoscale"] = autoscale
        if num_workers is not UNSET:
            field_dict["num_workers"] = num_workers

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        if src_dict is None or src_dict is UNSET:
            return {}
        d = {k: v if v is not None else UNSET for k, v in src_dict.items()}
        _autoscale = d.pop("autoscale", UNSET)
        autoscale: Union[Unset, AutoScale]
        if isinstance(_autoscale, Unset):
            autoscale = UNSET
        else:
            autoscale = AutoScale.from_dict(_autoscale)

        num_workers = d.pop("num_workers", UNSET)

        cluster_size = cls(
            autoscale=autoscale,
            num_workers=num_workers,
        )

        cluster_size.additional_properties = d
        return cluster_size

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
