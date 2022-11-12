from typing import Any, Dict, List, Type, TypeVar, Union

from pydantic import BaseModel, Field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AutoScale")


class AutoScale(BaseModel):
    """
    Attributes:
        max_workers (Union[Unset, int]): The maximum number of workers to which the cluster can scale up when
            overloaded. max_workers must be strictly greater than min_workers.
        min_workers (Union[Unset, int]): The minimum number of workers to which the cluster can scale down when
            underutilized. It is also the initial number of workers the cluster has after creation.
    """

    max_workers: Union[Unset, int] = UNSET
    min_workers: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = Field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        max_workers = self.max_workers
        min_workers = self.min_workers

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if max_workers is not UNSET:
            field_dict["max_workers"] = max_workers
        if min_workers is not UNSET:
            field_dict["min_workers"] = min_workers

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        if src_dict is None or src_dict is UNSET:
            return {}
        d = {k: v if v is not None else UNSET for k, v in src_dict.items()}
        max_workers = d.pop("max_workers", UNSET)

        min_workers = d.pop("min_workers", UNSET)

        auto_scale = cls(
            max_workers=max_workers,
            min_workers=min_workers,
        )

        auto_scale.additional_properties = d
        return auto_scale

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
