from typing import Any, Dict, List, Type, TypeVar, Union, cast

from pydantic import BaseModel, Field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DbtTask")


class DbtTask(BaseModel):
    """
    Attributes:
        commands (List[str]): A list of dbt commands to execute. All commands must start with `dbt`. This parameter must
            not be empty. A maximum of up to 10 commands can be provided. Example: ['dbt deps', 'dbt seed', 'dbt run
            --models 123'].
        profiles_directory (Union[Unset, str]): Optional (relative) path to the profiles directory. Can only be
            specified if no warehouse_id is specified. If no warehouse_id is specified and this folder is unset, the root
            directory is used.
        project_directory (Union[Unset, str]): Optional (relative) path to the project directory, if no value is
            provided, the root of the git repository is used.
        schema (Union[Unset, str]): Optional schema to write to. This parameter is only used when a warehouse_id is also
            provided. If not provided, the `default` schema is used.
        warehouse_id (Union[Unset, str]): ID of the SQL warehouse to connect to. If provided, we automatically generate
            and provide the profile and connection details to dbt. It can be overridden on a per-command basis by using the
            `--profiles-dir` command line argument. Example: 30dade0507d960d1.
    """

    commands: List[str] = None
    profiles_directory: Union[Unset, str] = UNSET
    project_directory: Union[Unset, str] = UNSET
    schema_: str = Field(default=None, alias="schema")
    warehouse_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = Field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        commands = self.commands

        profiles_directory = self.profiles_directory
        project_directory = self.project_directory
        schema = self.schema
        warehouse_id = self.warehouse_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "commands": commands,
            }
        )
        if profiles_directory is not UNSET:
            field_dict["profiles_directory"] = profiles_directory
        if project_directory is not UNSET:
            field_dict["project_directory"] = project_directory
        if schema is not UNSET:
            field_dict["schema"] = schema
        if warehouse_id is not UNSET:
            field_dict["warehouse_id"] = warehouse_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        if src_dict is None or src_dict is UNSET:
            return {}
        d = {k: v if v is not None else UNSET for k, v in src_dict.items()}
        commands = cast(List[str], d.pop("commands"))

        profiles_directory = d.pop("profiles_directory", UNSET)

        project_directory = d.pop("project_directory", UNSET)

        schema = d.pop("schema", UNSET)

        warehouse_id = d.pop("warehouse_id", UNSET)

        dbt_task = cls(
            commands=commands,
            profiles_directory=profiles_directory,
            project_directory=project_directory,
            schema=schema,
            warehouse_id=warehouse_id,
        )

        dbt_task.additional_properties = d
        return dbt_task

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
