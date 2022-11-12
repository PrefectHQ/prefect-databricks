from typing import Any, Dict, List, Type, TypeVar, Union

from pydantic import BaseModel, Field

from ..models.view_type import ViewType
from ..types import UNSET, Unset

T = TypeVar("T", bound="ViewItem")


class ViewItem(BaseModel):
    """
    Attributes:
        content (Union[Unset, str]): Content of the view.
        name (Union[Unset, str]): Name of the view item. In the case of code view, it would be the notebook’s name. In
            the case of dashboard view, it would be the dashboard’s name.
        type (Union[Unset, ViewType]): * `NOTEBOOK`: Notebook view item.
            * `DASHBOARD`: Dashboard view item.
    """

    content: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    type: Union[Unset, ViewType] = UNSET
    additional_properties: Dict[str, Any] = Field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        content = self.content
        name = self.name
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if content is not UNSET:
            field_dict["content"] = content
        if name is not UNSET:
            field_dict["name"] = name
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        if src_dict is None or src_dict is UNSET:
            return {}
        d = {k: v if v is not None else UNSET for k, v in src_dict.items()}
        content = d.pop("content", UNSET)

        name = d.pop("name", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, ViewType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = ViewType(_type)

        view_item = cls(
            content=content,
            name=name,
            type=type,
        )

        view_item.additional_properties = d
        return view_item

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
