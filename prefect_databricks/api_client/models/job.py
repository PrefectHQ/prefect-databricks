from typing import Any, Dict, List, Type, TypeVar, Union

from pydantic import BaseModel, Field

from ..models.job_settings import JobSettings
from ..types import UNSET, Unset

T = TypeVar("T", bound="Job")


class Job(BaseModel):
    """
    Attributes:
        created_time (Union[Unset, int]): The time at which this job was created in epoch milliseconds (milliseconds
            since 1/1/1970 UTC). Example: 1601370337343.
        creator_user_name (Union[Unset, str]): The creator user name. This field won’t be included in the response if
            the user has already been deleted. Example: user.name@databricks.com.
        job_id (Union[Unset, int]): The canonical identifier for this job. Example: 11223344.
        settings (Union[Unset, JobSettings]):
    """

    created_time: Union[Unset, int] = UNSET
    creator_user_name: Union[Unset, str] = UNSET
    job_id: Union[Unset, int] = UNSET
    settings: Union[Unset, JobSettings] = UNSET
    additional_properties: Dict[str, Any] = Field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_time = self.created_time
        creator_user_name = self.creator_user_name
        job_id = self.job_id
        settings: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.settings, Unset):
            settings = self.settings.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created_time is not UNSET:
            field_dict["created_time"] = created_time
        if creator_user_name is not UNSET:
            field_dict["creator_user_name"] = creator_user_name
        if job_id is not UNSET:
            field_dict["job_id"] = job_id
        if settings is not UNSET:
            field_dict["settings"] = settings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        if src_dict is None or src_dict is UNSET:
            return {}
        d = {k: v if v is not None else UNSET for k, v in src_dict.items()}
        created_time = d.pop("created_time", UNSET)

        creator_user_name = d.pop("creator_user_name", UNSET)

        job_id = d.pop("job_id", UNSET)

        _settings = d.pop("settings", UNSET)
        settings: Union[Unset, JobSettings]
        if isinstance(_settings, Unset):
            settings = UNSET
        else:
            settings = JobSettings.from_dict(_settings)

        job = cls(
            created_time=created_time,
            creator_user_name=creator_user_name,
            job_id=job_id,
            settings=settings,
        )

        job.additional_properties = d
        return job

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
