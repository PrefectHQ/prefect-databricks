from typing import Any, Dict, List, Type, TypeVar, Union

from pydantic import BaseModel, Field

from ..models.run import Run
from ..types import UNSET, Unset

T = TypeVar("T", bound="JobsRunsListResponse200")


class JobsRunsListResponse200(BaseModel):
    """
    Attributes:
        has_more (Union[Unset, bool]): If true, additional runs matching the provided filter are available for listing.
        runs (Union[Unset, List[Run]]): A list of runs, from most recently started to least.
    """

    has_more: Union[Unset, bool] = UNSET
    runs: Union[Unset, List[Run]] = UNSET
    additional_properties: Dict[str, Any] = Field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        has_more = self.has_more
        runs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.runs, Unset):
            runs = []
            for runs_item_data in self.runs:
                runs_item = runs_item_data.to_dict()

                runs.append(runs_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if has_more is not UNSET:
            field_dict["has_more"] = has_more
        if runs is not UNSET:
            field_dict["runs"] = runs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        if src_dict is None or src_dict is UNSET:
            return {}
        d = {k: v if v is not None else UNSET for k, v in src_dict.items()}
        has_more = d.pop("has_more", UNSET)

        runs = []
        _runs = d.pop("runs", UNSET)
        for runs_item_data in _runs or []:
            runs_item = Run.from_dict(runs_item_data)

            runs.append(runs_item)

        jobs_runs_list_response_200 = cls(
            has_more=has_more,
            runs=runs,
        )

        jobs_runs_list_response_200.additional_properties = d
        return jobs_runs_list_response_200

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
