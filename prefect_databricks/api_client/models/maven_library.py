from typing import Any, Dict, List, Type, TypeVar, Union, cast

from pydantic import BaseModel, Field

from ..types import UNSET, Unset

T = TypeVar("T", bound="MavenLibrary")


class MavenLibrary(BaseModel):
    """
    Attributes:
        coordinates (str): Gradle-style Maven coordinates. For example: `org.jsoup:jsoup:1.7.2`. This field is required.
            Example: org.jsoup:jsoup:1.7.2.
        exclusions (Union[Unset, List[str]]): List of dependences to exclude. For example: `["slf4j:slf4j", "*:hadoop-
            client"]`.

            Maven dependency exclusions: <https://maven.apache.org/guides/introduction/introduction-to-optional-and-
            excludes-dependencies.html>. Example: ['slf4j:slf4j', '*:hadoop-client'].
        repo (Union[Unset, str]): Maven repo to install the Maven package from. If omitted, both Maven Central
            Repository and Spark Packages are searched. Example: https://my-repo.com.
    """

    coordinates: str = None
    exclusions: Union[Unset, List[str]] = UNSET
    repo: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = Field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        coordinates = self.coordinates
        exclusions: Union[Unset, List[str]] = UNSET
        if not isinstance(self.exclusions, Unset):
            exclusions = self.exclusions

        repo = self.repo

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "coordinates": coordinates,
            }
        )
        if exclusions is not UNSET:
            field_dict["exclusions"] = exclusions
        if repo is not UNSET:
            field_dict["repo"] = repo

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        if src_dict is None or src_dict is UNSET:
            return {}
        d = {k: v if v is not None else UNSET for k, v in src_dict.items()}
        coordinates = d.pop("coordinates")

        exclusions = cast(List[str], d.pop("exclusions", UNSET))

        repo = d.pop("repo", UNSET)

        maven_library = cls(
            coordinates=coordinates,
            exclusions=exclusions,
            repo=repo,
        )

        maven_library.additional_properties = d
        return maven_library

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
