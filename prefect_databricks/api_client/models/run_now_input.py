from typing import Any, Dict, List, Type, TypeVar, Union

from pydantic import BaseModel, Field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RunNowInput")


class RunNowInput(BaseModel):
    """
    Attributes:
        idempotency_token (Union[Unset, str]): An optional token to guarantee the idempotency of job run requests. If a
            run with the provided token already exists, the request does not create a new run but returns the ID of the
            existing run instead. If a run with the provided token is deleted, an error is returned.

            If you specify the idempotency token, upon failure you can retry until the request succeeds. Databricks
            guarantees that exactly one run is launched with that idempotency token.

            This token must have at most 64 characters.

            For more information, see [How to ensure idempotency for jobs](https://kb.databricks.com/jobs/jobs-
            idempotency.html). Example: 8f018174-4792-40d5-bcbc-3e6a527352c8.
        job_id (Union[Unset, int]): The ID of the job to be executed Example: 11223344.
    """

    idempotency_token: Union[Unset, str] = UNSET
    job_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = Field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        idempotency_token = self.idempotency_token
        job_id = self.job_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if idempotency_token is not UNSET:
            field_dict["idempotency_token"] = idempotency_token
        if job_id is not UNSET:
            field_dict["job_id"] = job_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        if src_dict is None or src_dict is UNSET:
            return {}
        d = {k: v if v is not None else UNSET for k, v in src_dict.items()}
        idempotency_token = d.pop("idempotency_token", UNSET)

        job_id = d.pop("job_id", UNSET)

        run_now_input = cls(
            idempotency_token=idempotency_token,
            job_id=job_id,
        )

        run_now_input.additional_properties = d
        return run_now_input

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
