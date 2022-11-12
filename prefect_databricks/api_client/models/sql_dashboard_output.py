from typing import Any, Dict, List, Type, TypeVar, Union

from pydantic import BaseModel, Field

from ..models.sql_dashboard_widget_output import SqlDashboardWidgetOutput
from ..types import UNSET, Unset

T = TypeVar("T", bound="SqlDashboardOutput")


class SqlDashboardOutput(BaseModel):
    """
    Attributes:
        widgets (Union[Unset, SqlDashboardWidgetOutput]):
    """

    widgets: Union[Unset, SqlDashboardWidgetOutput] = UNSET
    additional_properties: Dict[str, Any] = Field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        widgets: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.widgets, Unset):
            widgets = self.widgets.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if widgets is not UNSET:
            field_dict["widgets"] = widgets

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        if src_dict is None or src_dict is UNSET:
            return {}
        d = {k: v if v is not None else UNSET for k, v in src_dict.items()}
        _widgets = d.pop("widgets", UNSET)
        widgets: Union[Unset, SqlDashboardWidgetOutput]
        if isinstance(_widgets, Unset):
            widgets = UNSET
        else:
            widgets = SqlDashboardWidgetOutput.from_dict(_widgets)

        sql_dashboard_output = cls(
            widgets=widgets,
        )

        sql_dashboard_output.additional_properties = d
        return sql_dashboard_output

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
