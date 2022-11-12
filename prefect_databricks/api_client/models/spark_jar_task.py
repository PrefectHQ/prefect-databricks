from typing import Any, Dict, List, Type, TypeVar, Union, cast

from pydantic import BaseModel, Field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SparkJarTask")


class SparkJarTask(BaseModel):
    """
    Attributes:
        jar_uri (Union[Unset, str]): Deprecated since 04/2016\. Provide a `jar` through the `libraries` field instead.
            For an example, see [Create](https://docs.databricks.com/dev-tools/api/latest/jobs.html#operation/JobsCreate).
        main_class_name (Union[Unset, str]): The full name of the class containing the main method to be executed. This
            class must be contained in a JAR provided as a library.

            The code must use `SparkContext.getOrCreate` to obtain a Spark context; otherwise, runs of the job fail.
            Example: com.databricks.ComputeModels.
        parameters (Union[Unset, List[str]]): Parameters passed to the main method.

            Use [Task parameter variables](https://docs.databricks.com/jobs.html#parameter-variables) to set parameters
            containing information about job runs. Example: ['--data', 'dbfs:/path/to/data.json'].
    """

    jar_uri: Union[Unset, str] = UNSET
    main_class_name: Union[Unset, str] = UNSET
    parameters: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = Field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        jar_uri = self.jar_uri
        main_class_name = self.main_class_name
        parameters: Union[Unset, List[str]] = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = self.parameters

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if jar_uri is not UNSET:
            field_dict["jar_uri"] = jar_uri
        if main_class_name is not UNSET:
            field_dict["main_class_name"] = main_class_name
        if parameters is not UNSET:
            field_dict["parameters"] = parameters

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        if src_dict is None or src_dict is UNSET:
            return {}
        d = {k: v if v is not None else UNSET for k, v in src_dict.items()}
        jar_uri = d.pop("jar_uri", UNSET)

        main_class_name = d.pop("main_class_name", UNSET)

        parameters = cast(List[str], d.pop("parameters", UNSET))

        spark_jar_task = cls(
            jar_uri=jar_uri,
            main_class_name=main_class_name,
            parameters=parameters,
        )

        spark_jar_task.additional_properties = d
        return spark_jar_task

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
