from typing import Any, Dict, List, Type, TypeVar, Union

from pydantic import BaseModel, Field

from ..models.docker_basic_auth import DockerBasicAuth
from ..types import UNSET, Unset

T = TypeVar("T", bound="DockerImage")


class DockerImage(BaseModel):
    """
    Attributes:
        basic_auth (Union[Unset, DockerBasicAuth]):
        url (Union[Unset, str]): URL for the Docker image.
    """

    basic_auth: Union[Unset, DockerBasicAuth] = UNSET
    url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = Field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        basic_auth: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.basic_auth, Unset):
            basic_auth = self.basic_auth.to_dict()

        url = self.url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if basic_auth is not UNSET:
            field_dict["basic_auth"] = basic_auth
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        if src_dict is None or src_dict is UNSET:
            return {}
        d = {k: v if v is not None else UNSET for k, v in src_dict.items()}
        _basic_auth = d.pop("basic_auth", UNSET)
        basic_auth: Union[Unset, DockerBasicAuth]
        if isinstance(_basic_auth, Unset):
            basic_auth = UNSET
        else:
            basic_auth = DockerBasicAuth.from_dict(_basic_auth)

        url = d.pop("url", UNSET)

        docker_image = cls(
            basic_auth=basic_auth,
            url=url,
        )

        docker_image.additional_properties = d
        return docker_image

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
