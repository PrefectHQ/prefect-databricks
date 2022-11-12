from typing import Any, Dict, List, Type, TypeVar, Union

from pydantic import BaseModel, Field

from ..models.cron_schedule_pause_status import CronSchedulePauseStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="CronSchedule")


class CronSchedule(BaseModel):
    """
    Attributes:
        quartz_cron_expression (str): A Cron expression using Quartz syntax that describes the schedule for a job. See
            [Cron Trigger](http://www.quartz-scheduler.org/documentation/quartz-2.3.0/tutorials/crontrigger.html) for
            details. This field is required. Example: 20 30 * * * ?.
        timezone_id (str): A Java timezone ID. The schedule for a job is resolved with respect to this timezone. See
            [Java TimeZone](https://docs.oracle.com/javase/7/docs/api/java/util/TimeZone.html) for details. This field is
            required. Example: Europe/London.
        pause_status (Union[Unset, CronSchedulePauseStatus]): Indicate whether this schedule is paused or not. Example:
            PAUSED.
    """

    quartz_cron_expression: str = None
    timezone_id: str = None
    pause_status: Union[Unset, CronSchedulePauseStatus] = UNSET
    additional_properties: Dict[str, Any] = Field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        quartz_cron_expression = self.quartz_cron_expression
        timezone_id = self.timezone_id
        pause_status: Union[Unset, str] = UNSET
        if not isinstance(self.pause_status, Unset):
            pause_status = self.pause_status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "quartz_cron_expression": quartz_cron_expression,
                "timezone_id": timezone_id,
            }
        )
        if pause_status is not UNSET:
            field_dict["pause_status"] = pause_status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        if src_dict is None or src_dict is UNSET:
            return {}
        d = {k: v if v is not None else UNSET for k, v in src_dict.items()}
        quartz_cron_expression = d.pop("quartz_cron_expression")

        timezone_id = d.pop("timezone_id")

        _pause_status = d.pop("pause_status", UNSET)
        pause_status: Union[Unset, CronSchedulePauseStatus]
        if isinstance(_pause_status, Unset):
            pause_status = UNSET
        else:
            pause_status = CronSchedulePauseStatus(_pause_status)

        cron_schedule = cls(
            quartz_cron_expression=quartz_cron_expression,
            timezone_id=timezone_id,
            pause_status=pause_status,
        )

        cron_schedule.additional_properties = d
        return cron_schedule

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
