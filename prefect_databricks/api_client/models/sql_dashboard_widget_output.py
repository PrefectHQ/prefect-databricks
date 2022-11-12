from typing import Any, Dict, List, Type, TypeVar, Union

from pydantic import BaseModel, Field

from ..models.sql_dashboard_widget_output_status import SqlDashboardWidgetOutputStatus
from ..models.sql_output_error import SqlOutputError
from ..types import UNSET, Unset

T = TypeVar("T", bound="SqlDashboardWidgetOutput")


class SqlDashboardWidgetOutput(BaseModel):
    """
    Attributes:
        end_time (Union[Unset, int]): Time (in epoch milliseconds) when execution of the SQL widget ends.
        error (Union[Unset, SqlOutputError]):
        output_link (Union[Unset, str]): The link to find the output results.
        start_time (Union[Unset, int]): Time (in epoch milliseconds) when execution of the SQL widget starts.
        status (Union[Unset, SqlDashboardWidgetOutputStatus]): The execution status of the SQL widget.
        widget_id (Union[Unset, str]): The canonical identifier of the SQL widget.
        widget_title (Union[Unset, str]): The title of the SQL widget.
    """

    end_time: Union[Unset, int] = UNSET
    error: Union[Unset, SqlOutputError] = UNSET
    output_link: Union[Unset, str] = UNSET
    start_time: Union[Unset, int] = UNSET
    status: Union[Unset, SqlDashboardWidgetOutputStatus] = UNSET
    widget_id: Union[Unset, str] = UNSET
    widget_title: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = Field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        end_time = self.end_time
        error: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.error, Unset):
            error = self.error.to_dict()

        output_link = self.output_link
        start_time = self.start_time
        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        widget_id = self.widget_id
        widget_title = self.widget_title

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if end_time is not UNSET:
            field_dict["end_time"] = end_time
        if error is not UNSET:
            field_dict["error"] = error
        if output_link is not UNSET:
            field_dict["output_link"] = output_link
        if start_time is not UNSET:
            field_dict["start_time"] = start_time
        if status is not UNSET:
            field_dict["status"] = status
        if widget_id is not UNSET:
            field_dict["widget_id"] = widget_id
        if widget_title is not UNSET:
            field_dict["widget_title"] = widget_title

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        if src_dict is None or src_dict is UNSET:
            return {}
        d = {k: v if v is not None else UNSET for k, v in src_dict.items()}
        end_time = d.pop("end_time", UNSET)

        _error = d.pop("error", UNSET)
        error: Union[Unset, SqlOutputError]
        if isinstance(_error, Unset):
            error = UNSET
        else:
            error = SqlOutputError.from_dict(_error)

        output_link = d.pop("output_link", UNSET)

        start_time = d.pop("start_time", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, SqlDashboardWidgetOutputStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = SqlDashboardWidgetOutputStatus(_status)

        widget_id = d.pop("widget_id", UNSET)

        widget_title = d.pop("widget_title", UNSET)

        sql_dashboard_widget_output = cls(
            end_time=end_time,
            error=error,
            output_link=output_link,
            start_time=start_time,
            status=status,
            widget_id=widget_id,
            widget_title=widget_title,
        )

        sql_dashboard_widget_output.additional_properties = d
        return sql_dashboard_widget_output

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
