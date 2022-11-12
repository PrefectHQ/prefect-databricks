from typing import Any, Dict, List, Type, TypeVar, Union

from pydantic import BaseModel, Field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LogSyncStatus")


class LogSyncStatus(BaseModel):
    """
    Attributes:
        last_attempted (Union[Unset, int]): The timestamp of last attempt. If the last attempt fails, last_exception
            contains the exception in the last attempt.
        last_exception (Union[Unset, str]): The exception thrown in the last attempt, it would be null (omitted in the
            response) if there is no exception in last attempted.
    """

    last_attempted: Union[Unset, int] = UNSET
    last_exception: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = Field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        last_attempted = self.last_attempted
        last_exception = self.last_exception

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if last_attempted is not UNSET:
            field_dict["last_attempted"] = last_attempted
        if last_exception is not UNSET:
            field_dict["last_exception"] = last_exception

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        if src_dict is None or src_dict is UNSET:
            return {}
        d = {k: v if v is not None else UNSET for k, v in src_dict.items()}
        last_attempted = d.pop("last_attempted", UNSET)

        last_exception = d.pop("last_exception", UNSET)

        log_sync_status = cls(
            last_attempted=last_attempted,
            last_exception=last_exception,
        )

        log_sync_status.additional_properties = d
        return log_sync_status

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
