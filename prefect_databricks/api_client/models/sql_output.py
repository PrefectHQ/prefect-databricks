from typing import Any, Dict, List, Type, TypeVar, Union

from pydantic import BaseModel, Field

from ..models.sql_alert_output import SqlAlertOutput
from ..models.sql_dashboard_output import SqlDashboardOutput
from ..models.sql_query_output import SqlQueryOutput
from ..types import UNSET, Unset

T = TypeVar("T", bound="SqlOutput")


class SqlOutput(BaseModel):
    """
    Attributes:
        alert_output (Union[Unset, SqlAlertOutput]):
        dashboard_output (Union[Unset, SqlDashboardOutput]):
        query_output (Union[Unset, SqlQueryOutput]):
    """

    alert_output: Union[Unset, SqlAlertOutput] = UNSET
    dashboard_output: Union[Unset, SqlDashboardOutput] = UNSET
    query_output: Union[Unset, SqlQueryOutput] = UNSET
    additional_properties: Dict[str, Any] = Field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        alert_output: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.alert_output, Unset):
            alert_output = self.alert_output.to_dict()

        dashboard_output: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.dashboard_output, Unset):
            dashboard_output = self.dashboard_output.to_dict()

        query_output: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.query_output, Unset):
            query_output = self.query_output.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if alert_output is not UNSET:
            field_dict["alert_output"] = alert_output
        if dashboard_output is not UNSET:
            field_dict["dashboard_output"] = dashboard_output
        if query_output is not UNSET:
            field_dict["query_output"] = query_output

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        if src_dict is None or src_dict is UNSET:
            return {}
        d = {k: v if v is not None else UNSET for k, v in src_dict.items()}
        _alert_output = d.pop("alert_output", UNSET)
        alert_output: Union[Unset, SqlAlertOutput]
        if isinstance(_alert_output, Unset):
            alert_output = UNSET
        else:
            alert_output = SqlAlertOutput.from_dict(_alert_output)

        _dashboard_output = d.pop("dashboard_output", UNSET)
        dashboard_output: Union[Unset, SqlDashboardOutput]
        if isinstance(_dashboard_output, Unset):
            dashboard_output = UNSET
        else:
            dashboard_output = SqlDashboardOutput.from_dict(_dashboard_output)

        _query_output = d.pop("query_output", UNSET)
        query_output: Union[Unset, SqlQueryOutput]
        if isinstance(_query_output, Unset):
            query_output = UNSET
        else:
            query_output = SqlQueryOutput.from_dict(_query_output)

        sql_output = cls(
            alert_output=alert_output,
            dashboard_output=dashboard_output,
            query_output=query_output,
        )

        sql_output.additional_properties = d
        return sql_output

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
