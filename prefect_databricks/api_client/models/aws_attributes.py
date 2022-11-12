from typing import Any, Dict, List, Type, TypeVar, Union

from pydantic import BaseModel, Field

from ..models.aws_attributes_availability import AwsAttributesAvailability
from ..models.aws_attributes_ebs_volume_type import AwsAttributesEbsVolumeType
from ..types import UNSET, Unset

T = TypeVar("T", bound="AwsAttributes")


class AwsAttributes(BaseModel):
    """
    Attributes:
        availability (Union[Unset, AwsAttributesAvailability]): Availability type used for all subsequent nodes past the
            `first_on_demand` ones. **Note:** If `first_on_demand` is zero, this availability type is used for the entire
            cluster.

            `SPOT`: use spot instances.
            `ON_DEMAND`: use on-demand instances.
            `SPOT_WITH_FALLBACK`: preferably use spot instances, but fall back to on-demand instances if spot instances
            cannot be acquired (for example, if AWS spot prices are too high).
        ebs_volume_count (Union[Unset, int]): The number of volumes launched for each instance. You can choose up to 10
            volumes. This feature is only enabled for supported node types. Legacy node types cannot specify custom EBS
            volumes. For node types with no instance store, at least one EBS volume needs to be specified; otherwise,
            cluster creation fails.

            These EBS volumes are mounted at `/ebs0`, `/ebs1`, and etc. Instance store volumes are mounted at
            `/local_disk0`, `/local_disk1`, and etc.

            If EBS volumes are attached, Databricks configures Spark to use only the EBS volumes for scratch storage because
            heterogeneously sized scratch devices can lead to inefficient disk utilization. If no EBS volumes are attached,
            Databricks configures Spark to use instance store volumes.

            If EBS volumes are specified, then the Spark configuration `spark.local.dir` is overridden.
        ebs_volume_iops (Union[Unset, int]): The number of IOPS per EBS gp3 volume.

            This value must be between 3000 and 16000.

            The value of IOPS and throughput is calculated based on AWS documentation to match the maximum performance of a
            gp2 volume with the same volume size.

            For more information, see the [EBS volume limit calculator](https://github.com/awslabs/aws-support-
            tools/tree/master/EBS/VolumeLimitCalculator).
        ebs_volume_size (Union[Unset, int]): The size of each EBS volume (in GiB) launched for each instance. For
            general purpose SSD, this value must be within the range 100 - 4096\. For throughput optimized HDD, this value
            must be within the range 500 - 4096\. Custom EBS volumes cannot be specified for the legacy node types (_memory-
            optimized_ and _compute-optimized_).
        ebs_volume_throughput (Union[Unset, int]): The throughput per EBS gp3 volume, in MiB per second.

            This value must be between 125 and 1000.
        ebs_volume_type (Union[Unset, AwsAttributesEbsVolumeType]): The type of EBS volume that is launched with this
            cluster.

            `GENERAL_PURPOSE_SSD`: provision extra storage using AWS gp2 EBS volumes.
            `THROUGHPUT_OPTIMIZED_HDD`: provision extra storage using AWS st1 volumes.
        first_on_demand (Union[Unset, int]): The first first_on_demand nodes of the cluster are placed on on-demand
            instances. If this value is greater than 0, the cluster driver node is placed on an on-demand instance. If this
            value is greater than or equal to the current cluster size, all nodes are placed on on-demand instances. If this
            value is less than the current cluster size, first_on_demand nodes are placed on on-demand instances and the
            remainder are placed on `availability` instances. This value does not affect cluster size and cannot be mutated
            over the lifetime of a cluster.
        instance_profile_arn (Union[Unset, str]): Nodes for this cluster are only be placed on AWS instances with this
            instance profile. If omitted, nodes are placed on instances without an instance profile. The instance profile
            must have previously been added to the Databricks environment by an account administrator.

            This feature may only be available to certain customer plans.
        spot_bid_price_percent (Union[Unset, int]): The max price for AWS spot instances, as a percentage of the
            corresponding instance type’s on-demand price. For example, if this field is set to 50, and the cluster needs a
            new `i3.xlarge` spot instance, then the max price is half of the price of on-demand `i3.xlarge` instances.
            Similarly, if this field is set to 200, the max price is twice the price of on-demand `i3.xlarge` instances. If
            not specified, the default value is 100\. When spot instances are requested for this cluster, only spot
            instances whose max price percentage matches this field is considered. For safety, we enforce this field to be
            no more than 10000.
        zone_id (Union[Unset, str]): Identifier for the availability zone/datacenter in which the cluster resides. You
            have three options:

            **Specify an availability zone as a string**, for example: “us-west-2a”. The provided availability zone must be
            in the same region as the Databricks deployment. For example, “us-west-2a” is not a valid zone ID if the
            Databricks deployment resides in the “us-east-1” region.

            **Enable automatic availability zone selection (“Auto-AZ”)**, by setting the value “auto”. Databricks selects
            the AZ based on available IPs in the workspace subnets and retries in other availability zones if AWS returns
            insufficient capacity errors.

            **Do not specify a value**. If not specified, a default zone is used.

            The list of available zones as well as the default value can be found by using the [List
            zones](https://docs.databricks.com/dev-tools/api/latest/clusters.html#list-zones) API.
    """

    availability: Union[Unset, AwsAttributesAvailability] = UNSET
    ebs_volume_count: Union[Unset, int] = UNSET
    ebs_volume_iops: Union[Unset, int] = UNSET
    ebs_volume_size: Union[Unset, int] = UNSET
    ebs_volume_throughput: Union[Unset, int] = UNSET
    ebs_volume_type: Union[Unset, AwsAttributesEbsVolumeType] = UNSET
    first_on_demand: Union[Unset, int] = UNSET
    instance_profile_arn: Union[Unset, str] = UNSET
    spot_bid_price_percent: Union[Unset, int] = UNSET
    zone_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = Field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        availability: Union[Unset, str] = UNSET
        if not isinstance(self.availability, Unset):
            availability = self.availability.value

        ebs_volume_count = self.ebs_volume_count
        ebs_volume_iops = self.ebs_volume_iops
        ebs_volume_size = self.ebs_volume_size
        ebs_volume_throughput = self.ebs_volume_throughput
        ebs_volume_type: Union[Unset, str] = UNSET
        if not isinstance(self.ebs_volume_type, Unset):
            ebs_volume_type = self.ebs_volume_type.value

        first_on_demand = self.first_on_demand
        instance_profile_arn = self.instance_profile_arn
        spot_bid_price_percent = self.spot_bid_price_percent
        zone_id = self.zone_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if availability is not UNSET:
            field_dict["availability"] = availability
        if ebs_volume_count is not UNSET:
            field_dict["ebs_volume_count"] = ebs_volume_count
        if ebs_volume_iops is not UNSET:
            field_dict["ebs_volume_iops"] = ebs_volume_iops
        if ebs_volume_size is not UNSET:
            field_dict["ebs_volume_size"] = ebs_volume_size
        if ebs_volume_throughput is not UNSET:
            field_dict["ebs_volume_throughput"] = ebs_volume_throughput
        if ebs_volume_type is not UNSET:
            field_dict["ebs_volume_type"] = ebs_volume_type
        if first_on_demand is not UNSET:
            field_dict["first_on_demand"] = first_on_demand
        if instance_profile_arn is not UNSET:
            field_dict["instance_profile_arn"] = instance_profile_arn
        if spot_bid_price_percent is not UNSET:
            field_dict["spot_bid_price_percent"] = spot_bid_price_percent
        if zone_id is not UNSET:
            field_dict["zone_id"] = zone_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        if src_dict is None or src_dict is UNSET:
            return {}
        d = {k: v if v is not None else UNSET for k, v in src_dict.items()}
        _availability = d.pop("availability", UNSET)
        availability: Union[Unset, AwsAttributesAvailability]
        if isinstance(_availability, Unset):
            availability = UNSET
        else:
            availability = AwsAttributesAvailability(_availability)

        ebs_volume_count = d.pop("ebs_volume_count", UNSET)

        ebs_volume_iops = d.pop("ebs_volume_iops", UNSET)

        ebs_volume_size = d.pop("ebs_volume_size", UNSET)

        ebs_volume_throughput = d.pop("ebs_volume_throughput", UNSET)

        _ebs_volume_type = d.pop("ebs_volume_type", UNSET)
        ebs_volume_type: Union[Unset, AwsAttributesEbsVolumeType]
        if isinstance(_ebs_volume_type, Unset):
            ebs_volume_type = UNSET
        else:
            ebs_volume_type = AwsAttributesEbsVolumeType(_ebs_volume_type)

        first_on_demand = d.pop("first_on_demand", UNSET)

        instance_profile_arn = d.pop("instance_profile_arn", UNSET)

        spot_bid_price_percent = d.pop("spot_bid_price_percent", UNSET)

        zone_id = d.pop("zone_id", UNSET)

        aws_attributes = cls(
            availability=availability,
            ebs_volume_count=ebs_volume_count,
            ebs_volume_iops=ebs_volume_iops,
            ebs_volume_size=ebs_volume_size,
            ebs_volume_throughput=ebs_volume_throughput,
            ebs_volume_type=ebs_volume_type,
            first_on_demand=first_on_demand,
            instance_profile_arn=instance_profile_arn,
            spot_bid_price_percent=spot_bid_price_percent,
            zone_id=zone_id,
        )

        aws_attributes.additional_properties = d
        return aws_attributes

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
