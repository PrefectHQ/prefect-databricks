from typing import Any, Dict, List, Type, TypeVar, Union, cast

from pydantic import BaseModel, Field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SparkSubmitTask")


class SparkSubmitTask(BaseModel):
    """
    Attributes:
        parameters (Union[Unset, List[str]]): Command-line parameters passed to spark submit.

            Use [Task parameter variables](https://docs.databricks.com/jobs.html#parameter-variables) to set parameters
            containing information about job runs. Example: ['--class', 'org.apache.spark.examples.SparkPi',
            'dbfs:/path/to/examples.jar', '10'].
    """

    parameters: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = Field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        parameters: Union[Unset, List[str]] = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = self.parameters

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if parameters is not UNSET:
            field_dict["parameters"] = parameters

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        if src_dict is None or src_dict is UNSET:
            return {}
        d = {k: v if v is not None else UNSET for k, v in src_dict.items()}
        parameters = cast(List[str], d.pop("parameters", UNSET))

        spark_submit_task = cls(
            parameters=parameters,
        )

        spark_submit_task.additional_properties = d
        return spark_submit_task

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
