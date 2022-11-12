from typing import Any, Dict, List, Type, TypeVar, Union

from pydantic import BaseModel, Field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NotebookOutput")


class NotebookOutput(BaseModel):
    """
    Attributes:
        result (Union[Unset, str]): The value passed to
            [dbutils.notebook.exit()](https://docs.databricks.com/notebooks/notebook-workflows.html#notebook-workflows-
            exit). Databricks restricts this API to return the first 5 MB of the value. For a larger result, your job can
            store the results in a cloud storage service. This field is absent if `dbutils.notebook.exit()` was never
            called. Example: An arbitrary string passed by calling dbutils.notebook.exit(...).
        truncated (Union[Unset, bool]): Whether or not the result was truncated.
    """

    result: Union[Unset, str] = UNSET
    truncated: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = Field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        result = self.result
        truncated = self.truncated

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if result is not UNSET:
            field_dict["result"] = result
        if truncated is not UNSET:
            field_dict["truncated"] = truncated

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        if src_dict is None or src_dict is UNSET:
            return {}
        d = {k: v if v is not None else UNSET for k, v in src_dict.items()}
        result = d.pop("result", UNSET)

        truncated = d.pop("truncated", UNSET)

        notebook_output = cls(
            result=result,
            truncated=truncated,
        )

        notebook_output.additional_properties = d
        return notebook_output

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
