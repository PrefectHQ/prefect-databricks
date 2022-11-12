from typing import Any, Dict, List, Type, TypeVar, Union

from pydantic import BaseModel, Field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SparkNodeAwsAttributes")


class SparkNodeAwsAttributes(BaseModel):
    """
    Attributes:
        is_spot (Union[Unset, bool]): Whether this node is on an Amazon spot instance.
    """

    is_spot: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = Field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        is_spot = self.is_spot

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_spot is not UNSET:
            field_dict["is_spot"] = is_spot

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        if src_dict is None or src_dict is UNSET:
            return {}
        d = {k: v if v is not None else UNSET for k, v in src_dict.items()}
        is_spot = d.pop("is_spot", UNSET)

        spark_node_aws_attributes = cls(
            is_spot=is_spot,
        )

        spark_node_aws_attributes.additional_properties = d
        return spark_node_aws_attributes

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
