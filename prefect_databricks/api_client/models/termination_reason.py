from typing import Any, Dict, List, Type, TypeVar, Union

from pydantic import BaseModel, Field

from ..models.parameter_pair import ParameterPair
from ..models.termination_code import TerminationCode
from ..models.termination_type import TerminationType
from ..types import UNSET, Unset

T = TypeVar("T", bound="TerminationReason")


class TerminationReason(BaseModel):
    """
    Attributes:
        code (Union[Unset, TerminationCode]): * USER_REQUEST: A user terminated the cluster directly. Parameters should
            include a `username` field that indicates the specific user who terminated the cluster.
            * JOB_FINISHED: The cluster was launched by a job, and terminated when the job completed.
            * INACTIVITY: The cluster was terminated since it was idle.
            * CLOUD_PROVIDER_SHUTDOWN: The instance that hosted the Spark driver was terminated by the cloud provider. In
            AWS, for example, AWS may retire instances and directly shut them down. Parameters should include an
            `aws_instance_state_reason` field indicating the AWS-provided reason why the instance was terminated.
            * COMMUNICATION_LOST: Databricks lost connection to services on the driver instance. For example, this can
            happen when problems arise in cloud networking infrastructure, or when the instance itself becomes unhealthy.
            * CLOUD_PROVIDER_LAUNCH_FAILURE: Databricks experienced a cloud provider failure when requesting instances to
            launch clusters. For example, AWS limits the number of running instances and EBS volumes. If you ask Databricks
            to launch a cluster that requires instances or EBS volumes that exceed your AWS limit, the cluster fails with
            this status code. Parameters should include one of `aws_api_error_code`, `aws_instance_state_reason`, or
            `aws_spot_request_status` to indicate the AWS-provided reason why Databricks could not request the required
            instances for the cluster.
            * SPARK_STARTUP_FAILURE: The cluster failed to initialize. Possible reasons may include failure to create the
            environment for Spark or issues launching the Spark master and worker processes.
            * INVALID_ARGUMENT: Cannot launch the cluster because the user specified an invalid argument. For example, the
            user might specify an invalid runtime version for the cluster.
            * UNEXPECTED_LAUNCH_FAILURE: While launching this cluster, Databricks failed to complete critical setup steps,
            terminating the cluster.
            * INTERNAL_ERROR: Databricks encountered an unexpected error that forced the running cluster to be terminated.
            Contact Databricks support for additional details.
            * SPARK_ERROR: The Spark driver failed to start. Possible reasons may include incompatible libraries and
            initialization scripts that corrupted the Spark container.
            * METASTORE_COMPONENT_UNHEALTHY: The cluster failed to start because the external metastore could not be
            reached. Refer to [Troubleshooting](https://docs.databricks.com/data/metastores/external-hive-
            metastore.html#troubleshooting).
            * DBFS_COMPONENT_UNHEALTHY: The cluster failed to start because Databricks File System (DBFS) could not be
            reached.
            * DRIVER_UNREACHABLE: Databricks was not able to access the Spark driver, because it was not reachable.
            * DRIVER_UNRESPONSIVE: Databricks was not able to access the Spark driver, because it was unresponsive.
            * INSTANCE_UNREACHABLE: Databricks was not able to access instances in order to start the cluster. This can be a
            transient networking issue. If the problem persists, this usually indicates a networking environment
            misconfiguration.
            * CONTAINER_LAUNCH_FAILURE: Databricks was unable to launch containers on worker nodes for the cluster. Have
            your admin check your network configuration.
            * INSTANCE_POOL_CLUSTER_FAILURE: Pool backed cluster specific failure. Refer to
            [Pools](https://docs.databricks.com/clusters/instance-pools/index.html) for details.
            * REQUEST_REJECTED: Databricks cannot handle the request at this moment. Try again later and contact Databricks
            if the problem persists.
            * INIT_SCRIPT_FAILURE: Databricks cannot load and run a cluster-scoped init script on one of the cluster’s
            nodes, or the init script terminates with a non-zero exit code. Refer to [Init script
            logs](https://docs.databricks.com/clusters/init-scripts.html#init-script-log).
            * TRIAL_EXPIRED: The Databricks trial subscription expired.
        parameters (Union[Unset, ParameterPair]): An object with additional information about why a cluster was
            terminated. The object keys are one of `TerminationParameter` and the value is the termination information.
        type (Union[Unset, TerminationType]): * SUCCESS: Termination succeeded.
            * CLIENT_ERROR: Non-retriable. Client must fix parameters before reattempting the cluster creation.
            * SERVICE_FAULT: Databricks service issue. Client can retry.
            * CLOUD_FAILURECloud provider infrastructure issue. Client can retry after the underlying issue is resolved.
    """

    code: Union[Unset, TerminationCode] = UNSET
    parameters: Union[Unset, ParameterPair] = UNSET
    type: Union[Unset, TerminationType] = UNSET
    additional_properties: Dict[str, Any] = Field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        code: Union[Unset, str] = UNSET
        if not isinstance(self.code, Unset):
            code = self.code.value

        parameters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.parameters, Unset):
            parameters = self.parameters.to_dict()

        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if parameters is not UNSET:
            field_dict["parameters"] = parameters
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        if src_dict is None or src_dict is UNSET:
            return {}
        d = {k: v if v is not None else UNSET for k, v in src_dict.items()}
        _code = d.pop("code", UNSET)
        code: Union[Unset, TerminationCode]
        if isinstance(_code, Unset):
            code = UNSET
        else:
            code = TerminationCode(_code)

        _parameters = d.pop("parameters", UNSET)
        parameters: Union[Unset, ParameterPair]
        if isinstance(_parameters, Unset):
            parameters = UNSET
        else:
            parameters = ParameterPair.from_dict(_parameters)

        _type = d.pop("type", UNSET)
        type: Union[Unset, TerminationType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = TerminationType(_type)

        termination_reason = cls(
            code=code,
            parameters=parameters,
            type=type,
        )

        termination_reason.additional_properties = d
        return termination_reason

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
