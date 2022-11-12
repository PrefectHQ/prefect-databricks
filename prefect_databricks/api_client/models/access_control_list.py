from typing import Any, Dict, List, Type, TypeVar, Union

from pydantic import BaseModel, Field

from ..models.access_control_request_for_group import AccessControlRequestForGroup
from ..models.access_control_request_for_user import AccessControlRequestForUser
from ..types import UNSET, Unset

T = TypeVar("T", bound="AccessControlList")


class AccessControlList(BaseModel):
    """
    Attributes:
        access_control_list (Union[Unset, List[Union[AccessControlRequestForGroup, AccessControlRequestForUser]]]): List
            of permissions to set on the job.
    """

    access_control_list: Union[
        Unset, List[Union[AccessControlRequestForGroup, AccessControlRequestForUser]]
    ] = UNSET
    additional_properties: Dict[str, Any] = Field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        access_control_list: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.access_control_list, Unset):
            access_control_list = []
            for access_control_list_item_data in self.access_control_list:
                access_control_list_item: Dict[str, Any]

                if isinstance(
                    access_control_list_item_data, AccessControlRequestForUser
                ):
                    access_control_list_item = access_control_list_item_data.to_dict()

                else:
                    access_control_list_item = access_control_list_item_data.to_dict()

                access_control_list.append(access_control_list_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if access_control_list is not UNSET:
            field_dict["access_control_list"] = access_control_list

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        if src_dict is None or src_dict is UNSET:
            return {}
        d = {k: v if v is not None else UNSET for k, v in src_dict.items()}
        access_control_list = []
        _access_control_list = d.pop("access_control_list", UNSET)
        for access_control_list_item_data in _access_control_list or []:

            def _parse_access_control_list_item(
                data: object,
            ) -> Union[AccessControlRequestForGroup, AccessControlRequestForUser]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_access_control_request_type_0 = (
                        AccessControlRequestForUser.from_dict(data)
                    )

                    return componentsschemas_access_control_request_type_0
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_access_control_request_type_1 = (
                    AccessControlRequestForGroup.from_dict(data)
                )

                return componentsschemas_access_control_request_type_1

            access_control_list_item = _parse_access_control_list_item(
                access_control_list_item_data
            )

            access_control_list.append(access_control_list_item)

        access_control_list = cls(
            access_control_list=access_control_list,
        )

        access_control_list.additional_properties = d
        return access_control_list

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
