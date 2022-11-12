from typing import Any, Dict, List, Type, TypeVar, Union

from pydantic import BaseModel, Field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GitSnapshot")


class GitSnapshot(BaseModel):
    """Read-only state of the remote repository at the time the job was run. This field is only included on job runs.

    Attributes:
        used_commit (Union[Unset, str]): Commit that was used to execute the run. If git_branch was specified, this
            points to the HEAD of the branch at the time of the run; if git_tag was specified, this points to the commit the
            tag points to. Example: 4506fdf41e9fa98090570a34df7a5bce163ff15f.
    """

    used_commit: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = Field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        used_commit = self.used_commit

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if used_commit is not UNSET:
            field_dict["used_commit"] = used_commit

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        if src_dict is None or src_dict is UNSET:
            return {}
        d = {k: v if v is not None else UNSET for k, v in src_dict.items()}
        used_commit = d.pop("used_commit", UNSET)

        git_snapshot = cls(
            used_commit=used_commit,
        )

        git_snapshot.additional_properties = d
        return git_snapshot

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
