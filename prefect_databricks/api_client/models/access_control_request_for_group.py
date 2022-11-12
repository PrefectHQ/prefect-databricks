from typing import Any, Dict, List, Type, TypeVar, Union

from pydantic import BaseModel, Field

from ..models.can_manage import CanManage
from ..models.can_manage_run import CanManageRun
from ..models.can_view import CanView
from ..types import UNSET, Unset

T = TypeVar("T", bound="AccessControlRequestForGroup")


class AccessControlRequestForGroup(BaseModel):
    """
    Attributes:
        group_name (Union[Unset, str]): Group name. There are two built-in groups: `users` for all users, and `admins`
            for administrators. Example: users.
        permission_level (Union[CanManage, CanManageRun, CanView, Unset]): Permission level to grant.
    """

    group_name: Union[Unset, str] = UNSET
    permission_level: Union[CanManage, CanManageRun, CanView, Unset] = UNSET
    additional_properties: Dict[str, Any] = Field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        group_name = self.group_name
        permission_level: Union[Unset, str]
        if isinstance(self.permission_level, Unset):
            permission_level = UNSET

        elif isinstance(self.permission_level, CanManage):
            permission_level = self.permission_level.value

        elif isinstance(self.permission_level, CanManageRun):
            permission_level = self.permission_level.value

        else:
            permission_level = self.permission_level.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if group_name is not UNSET:
            field_dict["group_name"] = group_name
        if permission_level is not UNSET:
            field_dict["permission_level"] = permission_level

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        if src_dict is None or src_dict is UNSET:
            return {}
        d = {k: v if v is not None else UNSET for k, v in src_dict.items()}
        group_name = d.pop("group_name", UNSET)

        def _parse_permission_level(
            data: object,
        ) -> Union[CanManage, CanManageRun, CanView, Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                componentsschemas_permission_level_for_group_type_0 = CanManage(data)

                return componentsschemas_permission_level_for_group_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                componentsschemas_permission_level_for_group_type_1 = CanManageRun(data)

                return componentsschemas_permission_level_for_group_type_1
            except:  # noqa: E722
                pass
            if not isinstance(data, str):
                raise TypeError()
            componentsschemas_permission_level_for_group_type_2 = CanView(data)

            return componentsschemas_permission_level_for_group_type_2

        permission_level = _parse_permission_level(d.pop("permission_level", UNSET))

        access_control_request_for_group = cls(
            group_name=group_name,
            permission_level=permission_level,
        )

        access_control_request_for_group.additional_properties = d
        return access_control_request_for_group

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
