from typing import Any, Dict, List, Type, TypeVar, Union

from pydantic import BaseModel, Field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TerminationParameter")


class TerminationParameter(BaseModel):
    """
    Attributes:
        aws_api_error_code (Union[Unset, str]): The AWS provided error code describing why cluster nodes could not be
            provisioned. For example, `InstanceLimitExceeded` indicates that the limit of EC2 instances for a specific
            instance type has been exceeded. For reference, see:
            <https://docs.aws.amazon.com/AWSEC2/latest/APIReference/query-api-troubleshooting.html>.
        aws_error_message (Union[Unset, str]): Human-readable context of various failures from AWS. This field is
            unstructured, and its exact format is subject to change.
        aws_impaired_status_details (Union[Unset, str]): The AWS provided status check which failed and induced a node
            loss. This status may correspond to a failed instance or system check. For reference, see
            <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitoring-system-instance-status-check.html>.
        aws_instance_state_reason (Union[Unset, str]): The AWS provided state reason describing why the driver node was
            terminated. For example, `Client.VolumeLimitExceeded` indicates that the limit of EBS volumes or total EBS
            volume storage has been exceeded. For reference, see
            <https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_StateReason.html>.
        aws_instance_status_event (Union[Unset, str]): The AWS provided scheduled event (for example reboot) which
            induced a node loss. For reference, see <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitoring-
            instances-status-check_sched.html>.
        aws_spot_request_fault_code (Union[Unset, str]): Provides additional details when a spot request fails. For
            example `InsufficientFreeAddressesInSubnet` indicates the subnet does not have free IP addresses to accommodate
            the new instance. For reference, see <https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-spot-
            instance-requests.html>.
        aws_spot_request_status (Union[Unset, str]): Describes why a spot request could not be fulfilled. For example,
            `price-too-low` indicates that the max price was lower than the current spot price. For reference, see:
            <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-bid-status.html#spot-instance-bid-status-understand>.
        databricks_error_message (Union[Unset, str]): Additional context that may explain the reason for cluster
            termination. This field is unstructured, and its exact format is subject to change.
        inactivity_duration_min (Union[Unset, str]): An idle cluster was shut down after being inactive for this
            duration.
        instance_id (Union[Unset, str]): The ID of the instance that was hosting the Spark driver.
        instance_pool_error_code (Union[Unset, str]): The [error code](https://docs.databricks.com/dev-
            tools/api/latest/clusters.html#clusterterminationreasonpoolclusterterminationcode) for cluster failures specific
            to a pool.
        instance_pool_id (Union[Unset, str]): The ID of the instance pool the cluster is using.
        username (Union[Unset, str]): The username of the user who terminated the cluster.
    """

    aws_api_error_code: Union[Unset, str] = UNSET
    aws_error_message: Union[Unset, str] = UNSET
    aws_impaired_status_details: Union[Unset, str] = UNSET
    aws_instance_state_reason: Union[Unset, str] = UNSET
    aws_instance_status_event: Union[Unset, str] = UNSET
    aws_spot_request_fault_code: Union[Unset, str] = UNSET
    aws_spot_request_status: Union[Unset, str] = UNSET
    databricks_error_message: Union[Unset, str] = UNSET
    inactivity_duration_min: Union[Unset, str] = UNSET
    instance_id: Union[Unset, str] = UNSET
    instance_pool_error_code: Union[Unset, str] = UNSET
    instance_pool_id: Union[Unset, str] = UNSET
    username: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = Field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        aws_api_error_code = self.aws_api_error_code
        aws_error_message = self.aws_error_message
        aws_impaired_status_details = self.aws_impaired_status_details
        aws_instance_state_reason = self.aws_instance_state_reason
        aws_instance_status_event = self.aws_instance_status_event
        aws_spot_request_fault_code = self.aws_spot_request_fault_code
        aws_spot_request_status = self.aws_spot_request_status
        databricks_error_message = self.databricks_error_message
        inactivity_duration_min = self.inactivity_duration_min
        instance_id = self.instance_id
        instance_pool_error_code = self.instance_pool_error_code
        instance_pool_id = self.instance_pool_id
        username = self.username

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if aws_api_error_code is not UNSET:
            field_dict["aws_api_error_code"] = aws_api_error_code
        if aws_error_message is not UNSET:
            field_dict["aws_error_message"] = aws_error_message
        if aws_impaired_status_details is not UNSET:
            field_dict["aws_impaired_status_details"] = aws_impaired_status_details
        if aws_instance_state_reason is not UNSET:
            field_dict["aws_instance_state_reason"] = aws_instance_state_reason
        if aws_instance_status_event is not UNSET:
            field_dict["aws_instance_status_event"] = aws_instance_status_event
        if aws_spot_request_fault_code is not UNSET:
            field_dict["aws_spot_request_fault_code"] = aws_spot_request_fault_code
        if aws_spot_request_status is not UNSET:
            field_dict["aws_spot_request_status"] = aws_spot_request_status
        if databricks_error_message is not UNSET:
            field_dict["databricks_error_message"] = databricks_error_message
        if inactivity_duration_min is not UNSET:
            field_dict["inactivity_duration_min"] = inactivity_duration_min
        if instance_id is not UNSET:
            field_dict["instance_id"] = instance_id
        if instance_pool_error_code is not UNSET:
            field_dict["instance_pool_error_code"] = instance_pool_error_code
        if instance_pool_id is not UNSET:
            field_dict["instance_pool_id"] = instance_pool_id
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        if src_dict is None or src_dict is UNSET:
            return {}
        d = {k: v if v is not None else UNSET for k, v in src_dict.items()}
        aws_api_error_code = d.pop("aws_api_error_code", UNSET)

        aws_error_message = d.pop("aws_error_message", UNSET)

        aws_impaired_status_details = d.pop("aws_impaired_status_details", UNSET)

        aws_instance_state_reason = d.pop("aws_instance_state_reason", UNSET)

        aws_instance_status_event = d.pop("aws_instance_status_event", UNSET)

        aws_spot_request_fault_code = d.pop("aws_spot_request_fault_code", UNSET)

        aws_spot_request_status = d.pop("aws_spot_request_status", UNSET)

        databricks_error_message = d.pop("databricks_error_message", UNSET)

        inactivity_duration_min = d.pop("inactivity_duration_min", UNSET)

        instance_id = d.pop("instance_id", UNSET)

        instance_pool_error_code = d.pop("instance_pool_error_code", UNSET)

        instance_pool_id = d.pop("instance_pool_id", UNSET)

        username = d.pop("username", UNSET)

        termination_parameter = cls(
            aws_api_error_code=aws_api_error_code,
            aws_error_message=aws_error_message,
            aws_impaired_status_details=aws_impaired_status_details,
            aws_instance_state_reason=aws_instance_state_reason,
            aws_instance_status_event=aws_instance_status_event,
            aws_spot_request_fault_code=aws_spot_request_fault_code,
            aws_spot_request_status=aws_spot_request_status,
            databricks_error_message=databricks_error_message,
            inactivity_duration_min=inactivity_duration_min,
            instance_id=instance_id,
            instance_pool_error_code=instance_pool_error_code,
            instance_pool_id=instance_pool_id,
            username=username,
        )

        termination_parameter.additional_properties = d
        return termination_parameter

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
