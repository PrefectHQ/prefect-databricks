from typing import Any, Dict, List, Type, TypeVar, Union

from pydantic import BaseModel, Field

from ..models.dbfs_storage_info import DbfsStorageInfo
from ..models.file_storage_info import FileStorageInfo
from ..models.s3_storage_info import S3StorageInfo
from ..types import UNSET, Unset

T = TypeVar("T", bound="InitScriptInfo")


class InitScriptInfo(BaseModel):
    """
    Attributes:
        s3 (Union[Unset, S3StorageInfo]):
        dbfs (Union[Unset, DbfsStorageInfo]):
        file (Union[Unset, FileStorageInfo]):
    """

    s3: Union[Unset, S3StorageInfo] = UNSET
    dbfs: Union[Unset, DbfsStorageInfo] = UNSET
    file: Union[Unset, FileStorageInfo] = UNSET
    additional_properties: Dict[str, Any] = Field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        s3: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.s3, Unset):
            s3 = self.s3.to_dict()

        dbfs: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.dbfs, Unset):
            dbfs = self.dbfs.to_dict()

        file: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.file, Unset):
            file = self.file.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if s3 is not UNSET:
            field_dict["S3"] = s3
        if dbfs is not UNSET:
            field_dict["dbfs"] = dbfs
        if file is not UNSET:
            field_dict["file"] = file

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        if src_dict is None or src_dict is UNSET:
            return {}
        d = {k: v if v is not None else UNSET for k, v in src_dict.items()}
        _s3 = d.pop("S3", UNSET)
        s3: Union[Unset, S3StorageInfo]
        if isinstance(_s3, Unset):
            s3 = UNSET
        else:
            s3 = S3StorageInfo.from_dict(_s3)

        _dbfs = d.pop("dbfs", UNSET)
        dbfs: Union[Unset, DbfsStorageInfo]
        if isinstance(_dbfs, Unset):
            dbfs = UNSET
        else:
            dbfs = DbfsStorageInfo.from_dict(_dbfs)

        _file = d.pop("file", UNSET)
        file: Union[Unset, FileStorageInfo]
        if isinstance(_file, Unset):
            file = UNSET
        else:
            file = FileStorageInfo.from_dict(_file)

        init_script_info = cls(
            s3=s3,
            dbfs=dbfs,
            file=file,
        )

        init_script_info.additional_properties = d
        return init_script_info

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
