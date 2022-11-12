from typing import Any, Dict, List, Type, TypeVar, Union

from pydantic import BaseModel, Field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SparkVersion")


class SparkVersion(BaseModel):
    """
    Attributes:
        key (Union[Unset, str]): [Databricks Runtime version](https://docs.databricks.com/dev-
            tools/api/latest/index.html#programmatic-version) key, for example `7.3.x-scala2.12`. The value that must be
            provided as the `spark_version` when creating a new cluster. The exact runtime version may change over time for
            a “wildcard” version (that is, `7.3.x-scala2.12` is a “wildcard” version) with minor bug fixes.
        name (Union[Unset, str]): A descriptive name for the runtime version, for example “Databricks Runtime 7.3 LTS”.
    """

    key: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = Field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        key = self.key
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if key is not UNSET:
            field_dict["key"] = key
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        if src_dict is None or src_dict is UNSET:
            return {}
        d = {k: v if v is not None else UNSET for k, v in src_dict.items()}
        key = d.pop("key", UNSET)

        name = d.pop("name", UNSET)

        spark_version = cls(
            key=key,
            name=name,
        )

        spark_version.additional_properties = d
        return spark_version

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
