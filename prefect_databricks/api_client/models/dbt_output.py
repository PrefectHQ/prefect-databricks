from typing import Any, Dict, List, Type, TypeVar, Union

from pydantic import BaseModel, Field

from ..models.dbt_output_artifacts_headers import DbtOutputArtifactsHeaders
from ..types import UNSET, Unset

T = TypeVar("T", bound="DbtOutput")


class DbtOutput(BaseModel):
    """
    Attributes:
        artifacts_headers (Union[Unset, DbtOutputArtifactsHeaders]): An optional map of headers to send when retrieving
            the artifact from the `artifacts_link`.
        artifacts_link (Union[Unset, str]): A pre-signed URL to download the (compressed) dbt artifacts. This link is
            valid for a limited time (30 minutes). This information is only available after the run has finished.
    """

    artifacts_headers: Union[Unset, DbtOutputArtifactsHeaders] = UNSET
    artifacts_link: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = Field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        artifacts_headers: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.artifacts_headers, Unset):
            artifacts_headers = self.artifacts_headers.to_dict()

        artifacts_link = self.artifacts_link

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if artifacts_headers is not UNSET:
            field_dict["artifacts_headers"] = artifacts_headers
        if artifacts_link is not UNSET:
            field_dict["artifacts_link"] = artifacts_link

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        if src_dict is None or src_dict is UNSET:
            return {}
        d = {k: v if v is not None else UNSET for k, v in src_dict.items()}
        _artifacts_headers = d.pop("artifacts_headers", UNSET)
        artifacts_headers: Union[Unset, DbtOutputArtifactsHeaders]
        if isinstance(_artifacts_headers, Unset):
            artifacts_headers = UNSET
        else:
            artifacts_headers = DbtOutputArtifactsHeaders.from_dict(_artifacts_headers)

        artifacts_link = d.pop("artifacts_link", UNSET)

        dbt_output = cls(
            artifacts_headers=artifacts_headers,
            artifacts_link=artifacts_link,
        )

        dbt_output.additional_properties = d
        return dbt_output

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
