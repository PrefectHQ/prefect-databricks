from typing import Any, Dict, List, Type, TypeVar, Union

from pydantic import BaseModel, Field

from ..models.sql_statement_output import SqlStatementOutput
from ..types import UNSET, Unset

T = TypeVar("T", bound="SqlQueryOutput")


class SqlQueryOutput(BaseModel):
    """
    Attributes:
        output_link (Union[Unset, str]): The link to find the output results.
        query_text (Union[Unset, str]): The text of the SQL query. Can Run permission of the SQL query is required to
            view this field.
        sql_statements (Union[Unset, SqlStatementOutput]):
        warehouse_id (Union[Unset, str]): The canonical identifier of the SQL warehouse.
    """

    output_link: Union[Unset, str] = UNSET
    query_text: Union[Unset, str] = UNSET
    sql_statements: Union[Unset, SqlStatementOutput] = UNSET
    warehouse_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = Field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        output_link = self.output_link
        query_text = self.query_text
        sql_statements: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.sql_statements, Unset):
            sql_statements = self.sql_statements.to_dict()

        warehouse_id = self.warehouse_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if output_link is not UNSET:
            field_dict["output_link"] = output_link
        if query_text is not UNSET:
            field_dict["query_text"] = query_text
        if sql_statements is not UNSET:
            field_dict["sql_statements"] = sql_statements
        if warehouse_id is not UNSET:
            field_dict["warehouse_id"] = warehouse_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        if src_dict is None or src_dict is UNSET:
            return {}
        d = {k: v if v is not None else UNSET for k, v in src_dict.items()}
        output_link = d.pop("output_link", UNSET)

        query_text = d.pop("query_text", UNSET)

        _sql_statements = d.pop("sql_statements", UNSET)
        sql_statements: Union[Unset, SqlStatementOutput]
        if isinstance(_sql_statements, Unset):
            sql_statements = UNSET
        else:
            sql_statements = SqlStatementOutput.from_dict(_sql_statements)

        warehouse_id = d.pop("warehouse_id", UNSET)

        sql_query_output = cls(
            output_link=output_link,
            query_text=query_text,
            sql_statements=sql_statements,
            warehouse_id=warehouse_id,
        )

        sql_query_output.additional_properties = d
        return sql_query_output

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
