from typing import Any, Dict, List, Type, TypeVar, Union

from pydantic import BaseModel, Field

from ..models.sql_task_alert import SqlTaskAlert
from ..models.sql_task_dashboard import SqlTaskDashboard
from ..models.sql_task_parameters import SqlTaskParameters
from ..models.sql_task_query import SqlTaskQuery
from ..types import UNSET, Unset

T = TypeVar("T", bound="SqlTask")


class SqlTask(BaseModel):
    """
    Attributes:
        warehouse_id (str): The canonical identifier of the SQL warehouse. Only serverless and pro SQL warehouses are
            supported.
        alert (Union[Unset, SqlTaskAlert]):
        dashboard (Union[Unset, SqlTaskDashboard]):
        parameters (Union[Unset, SqlTaskParameters]): Parameters to be used for each run of this job. The SQL alert task
            does not support custom parameters. Example: {'age': 35, 'name': 'John Doe'}.
        query (Union[Unset, SqlTaskQuery]):
    """

    warehouse_id: str = None
    alert: Union[Unset, SqlTaskAlert] = UNSET
    dashboard: Union[Unset, SqlTaskDashboard] = UNSET
    parameters: Union[Unset, SqlTaskParameters] = UNSET
    query: Union[Unset, SqlTaskQuery] = UNSET
    additional_properties: Dict[str, Any] = Field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        warehouse_id = self.warehouse_id
        alert: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.alert, Unset):
            alert = self.alert.to_dict()

        dashboard: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.dashboard, Unset):
            dashboard = self.dashboard.to_dict()

        parameters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = self.parameters.to_dict()

        query: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.query, Unset):
            query = self.query.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "warehouse_id": warehouse_id,
            }
        )
        if alert is not UNSET:
            field_dict["alert"] = alert
        if dashboard is not UNSET:
            field_dict["dashboard"] = dashboard
        if parameters is not UNSET:
            field_dict["parameters"] = parameters
        if query is not UNSET:
            field_dict["query"] = query

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        if src_dict is None or src_dict is UNSET:
            return {}
        d = {k: v if v is not None else UNSET for k, v in src_dict.items()}
        warehouse_id = d.pop("warehouse_id")

        _alert = d.pop("alert", UNSET)
        alert: Union[Unset, SqlTaskAlert]
        if isinstance(_alert, Unset):
            alert = UNSET
        else:
            alert = SqlTaskAlert.from_dict(_alert)

        _dashboard = d.pop("dashboard", UNSET)
        dashboard: Union[Unset, SqlTaskDashboard]
        if isinstance(_dashboard, Unset):
            dashboard = UNSET
        else:
            dashboard = SqlTaskDashboard.from_dict(_dashboard)

        _parameters = d.pop("parameters", UNSET)
        parameters: Union[Unset, SqlTaskParameters]
        if isinstance(_parameters, Unset):
            parameters = UNSET
        else:
            parameters = SqlTaskParameters.from_dict(_parameters)

        _query = d.pop("query", UNSET)
        query: Union[Unset, SqlTaskQuery]
        if isinstance(_query, Unset):
            query = UNSET
        else:
            query = SqlTaskQuery.from_dict(_query)

        sql_task = cls(
            warehouse_id=warehouse_id,
            alert=alert,
            dashboard=dashboard,
            parameters=parameters,
            query=query,
        )

        sql_task.additional_properties = d
        return sql_task

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
