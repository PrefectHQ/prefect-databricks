from typing import Any, Dict, List, Type, TypeVar, Union

from pydantic import BaseModel, Field

from ..types import UNSET, Unset

T = TypeVar("T", bound="S3StorageInfo")


class S3StorageInfo(BaseModel):
    """
    Attributes:
        canned_acl (Union[Unset, str]): (Optional) Set canned access control list. For example: `bucket-owner-full-
            control`. If canned_acl is set, the cluster instance profile must have `s3:PutObjectAcl` permission on the
            destination bucket and prefix. The full list of possible canned ACLs can be found at
            <https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl>. By default only the object owner
            gets full control. If you are using cross account role for writing data, you may want to set `bucket-owner-full-
            control` to make bucket owner able to read the logs.
        destination (Union[Unset, str]): S3 destination. For example: `s3://my-bucket/some-prefix` You must configure
            the cluster with an instance profile and the instance profile must have write access to the destination. You
            _cannot_ use AWS keys.
        enable_encryption (Union[Unset, bool]): (Optional)Enable server side encryption, `false` by default.
        encryption_type (Union[Unset, str]): (Optional) The encryption type, it could be `sse-s3` or `sse-kms`. It is
            used only when encryption is enabled and the default type is `sse-s3`.
        endpoint (Union[Unset, str]): S3 endpoint. For example: `https://s3-us-west-2.amazonaws.com`. Either region or
            endpoint must be set. If both are set, endpoint is used.
        kms_key (Union[Unset, str]): (Optional) KMS key used if encryption is enabled and encryption type is set to
            `sse-kms`.
        region (Union[Unset, str]): S3 region. For example: `us-west-2`. Either region or endpoint must be set. If both
            are set, endpoint is used.
    """

    canned_acl: Union[Unset, str] = UNSET
    destination: Union[Unset, str] = UNSET
    enable_encryption: Union[Unset, bool] = UNSET
    encryption_type: Union[Unset, str] = UNSET
    endpoint: Union[Unset, str] = UNSET
    kms_key: Union[Unset, str] = UNSET
    region: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = Field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        canned_acl = self.canned_acl
        destination = self.destination
        enable_encryption = self.enable_encryption
        encryption_type = self.encryption_type
        endpoint = self.endpoint
        kms_key = self.kms_key
        region = self.region

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if canned_acl is not UNSET:
            field_dict["canned_acl"] = canned_acl
        if destination is not UNSET:
            field_dict["destination"] = destination
        if enable_encryption is not UNSET:
            field_dict["enable_encryption"] = enable_encryption
        if encryption_type is not UNSET:
            field_dict["encryption_type"] = encryption_type
        if endpoint is not UNSET:
            field_dict["endpoint"] = endpoint
        if kms_key is not UNSET:
            field_dict["kms_key"] = kms_key
        if region is not UNSET:
            field_dict["region"] = region

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        if src_dict is None or src_dict is UNSET:
            return {}
        d = {k: v if v is not None else UNSET for k, v in src_dict.items()}
        canned_acl = d.pop("canned_acl", UNSET)

        destination = d.pop("destination", UNSET)

        enable_encryption = d.pop("enable_encryption", UNSET)

        encryption_type = d.pop("encryption_type", UNSET)

        endpoint = d.pop("endpoint", UNSET)

        kms_key = d.pop("kms_key", UNSET)

        region = d.pop("region", UNSET)

        s3_storage_info = cls(
            canned_acl=canned_acl,
            destination=destination,
            enable_encryption=enable_encryption,
            encryption_type=encryption_type,
            endpoint=endpoint,
            kms_key=kms_key,
            region=region,
        )

        s3_storage_info.additional_properties = d
        return s3_storage_info

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
