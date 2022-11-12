from typing import Any, Dict, List, Type, TypeVar, Union

from pydantic import BaseModel, Field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RunParametersPipelineParams")


class RunParametersPipelineParams(BaseModel):
    """
    Attributes:
        full_refresh (Union[Unset, bool]): If true, triggers a full refresh on the delta live table.
    """

    full_refresh: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = Field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        full_refresh = self.full_refresh

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if full_refresh is not UNSET:
            field_dict["full_refresh"] = full_refresh

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        if src_dict is None or src_dict is UNSET:
            return {}
        d = {k: v if v is not None else UNSET for k, v in src_dict.items()}
        full_refresh = d.pop("full_refresh", UNSET)

        run_parameters_pipeline_params = cls(
            full_refresh=full_refresh,
        )

        run_parameters_pipeline_params.additional_properties = d
        return run_parameters_pipeline_params

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
