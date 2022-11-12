from typing import Any, Dict, List, Type, TypeVar, Union, cast

from pydantic import BaseModel, Field

from ..types import UNSET, Unset

T = TypeVar("T", bound="JobEmailNotifications")


class JobEmailNotifications(BaseModel):
    """
    Attributes:
        no_alert_for_skipped_runs (Union[Unset, bool]): If true, do not send email to recipients specified in
            `on_failure` if the run is skipped.
        on_failure (Union[Unset, List[str]]): A list of email addresses to notify when a run completes unsuccessfully. A
            run is considered unsuccessful if it ends with an `INTERNAL_ERROR` `life_cycle_state` or a `SKIPPED`, `FAILED`,
            or `TIMED_OUT` `result_state`. If not specified on job creation, reset, or update, or the list is empty, then
            notifications are not sent. Job-level failure notifications are sent only once after the entire job run
            (including all of its retries) has failed. Notifications are not sent when failed job runs are retried. To
            receive a failure notification after every failed task (including every failed retry), use task-level
            notifications instead. Example: ['user.name@databricks.com'].
        on_start (Union[Unset, List[str]]): A list of email addresses to be notified when a run begins. If not specified
            on job creation, reset, or update, the list is empty, and notifications are not sent. Example:
            ['user.name@databricks.com'].
        on_success (Union[Unset, List[str]]): A list of email addresses to be notified when a run successfully
            completes. A run is considered to have completed successfully if it ends with a `TERMINATED` `life_cycle_state`
            and a `SUCCESSFUL` result_state. If not specified on job creation, reset, or update, the list is empty, and
            notifications are not sent. Example: ['user.name@databricks.com'].
    """

    no_alert_for_skipped_runs: Union[Unset, bool] = UNSET
    on_failure: Union[Unset, List[str]] = UNSET
    on_start: Union[Unset, List[str]] = UNSET
    on_success: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = Field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        no_alert_for_skipped_runs = self.no_alert_for_skipped_runs
        on_failure: Union[Unset, List[str]] = UNSET
        if not isinstance(self.on_failure, Unset):
            on_failure = self.on_failure

        on_start: Union[Unset, List[str]] = UNSET
        if not isinstance(self.on_start, Unset):
            on_start = self.on_start

        on_success: Union[Unset, List[str]] = UNSET
        if not isinstance(self.on_success, Unset):
            on_success = self.on_success

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if no_alert_for_skipped_runs is not UNSET:
            field_dict["no_alert_for_skipped_runs"] = no_alert_for_skipped_runs
        if on_failure is not UNSET:
            field_dict["on_failure"] = on_failure
        if on_start is not UNSET:
            field_dict["on_start"] = on_start
        if on_success is not UNSET:
            field_dict["on_success"] = on_success

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        if src_dict is None or src_dict is UNSET:
            return {}
        d = {k: v if v is not None else UNSET for k, v in src_dict.items()}
        no_alert_for_skipped_runs = d.pop("no_alert_for_skipped_runs", UNSET)

        on_failure = cast(List[str], d.pop("on_failure", UNSET))

        on_start = cast(List[str], d.pop("on_start", UNSET))

        on_success = cast(List[str], d.pop("on_success", UNSET))

        job_email_notifications = cls(
            no_alert_for_skipped_runs=no_alert_for_skipped_runs,
            on_failure=on_failure,
            on_start=on_start,
            on_success=on_success,
        )

        job_email_notifications.additional_properties = d
        return job_email_notifications

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
