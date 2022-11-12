from typing import Any, Dict, List, Type, TypeVar, Union, cast

from pydantic import BaseModel, Field

from ..models.aws_attributes import AwsAttributes
from ..models.cluster_log_conf import ClusterLogConf
from ..models.cluster_source import ClusterSource
from ..models.cluster_tag import ClusterTag
from ..models.docker_image import DockerImage
from ..models.init_script_info import InitScriptInfo
from ..models.spark_conf_pair import SparkConfPair
from ..models.spark_env_pair import SparkEnvPair
from ..types import UNSET, Unset

T = TypeVar("T", bound="ClusterAttributes")


class ClusterAttributes(BaseModel):
    """
    Attributes:
        autotermination_minutes (Union[Unset, int]): Automatically terminates the cluster after it is inactive for this
            time in minutes. If not set, this cluster is not be automatically terminated. If specified, the threshold must
            be between 10 and 10000 minutes. You can also set this value to 0 to explicitly disable automatic termination.
        aws_attributes (Union[Unset, AwsAttributes]):
        cluster_log_conf (Union[Unset, ClusterLogConf]):
        cluster_name (Union[Unset, str]): Cluster name requested by the user. This doesn’t have to be unique. If not
            specified at creation, the cluster name is an empty string.
        cluster_source (Union[Unset, ClusterSource]): * UI: Cluster created through the UI.
            * JOB: Cluster created by the Databricks job scheduler.
            * API: Cluster created through an API call.
        custom_tags (Union[Unset, ClusterTag]): An object with key value pairs. The key length must be between 1 and 127
            UTF-8 characters, inclusive. The value length must be less than or equal to 255 UTF-8 characters. For a list of
            all restrictions, see AWS Tag Restrictions:
            <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html#tag-restrictions>
        docker_image (Union[Unset, DockerImage]):
        driver_node_type_id (Union[Unset, str]): The node type of the Spark driver. This field is optional; if unset,
            the driver node type is set as the same value as `node_type_id` defined above.
        enable_elastic_disk (Union[Unset, bool]): Autoscaling Local Storage: when enabled, this cluster dynamically
            acquires additional disk space when its Spark workers are running low on disk space. This feature requires
            specific AWS permissions to function correctly. Refer to [Autoscaling local
            storage](https://docs.databricks.com/clusters/configure.html#autoscaling-local-storage) for details.
        init_scripts (Union[Unset, List[InitScriptInfo]]): The configuration for storing init scripts. Any number of
            destinations can be specified. The scripts are executed sequentially in the order provided. If
            `cluster_log_conf` is specified, init script logs are sent to `<destination>/<cluster-ID>/init_scripts`.
        instance_pool_id (Union[Unset, str]): The optional ID of the instance pool to which the cluster belongs. Refer
            to [Pools](https://docs.databricks.com/clusters/instance-pools/index.html) for details.
        node_type_id (Union[Unset, str]): This field encodes, through a single value, the resources available to each of
            the Spark nodes in this cluster. For example, the Spark nodes can be provisioned and optimized for memory or
            compute intensive workloads A list of available node types can be retrieved by using the [List node
            types](https://docs.databricks.com/dev-tools/api/latest/clusters.html#list-node-types) API call.
        policy_id (Union[Unset, str]): A [cluster policy](https://docs.databricks.com/dev-
            tools/api/latest/policies.html) ID.
        spark_conf (Union[Unset, SparkConfPair]): An arbitrary object where the object key is a configuration propery
            name and the value is a configuration property value.
        spark_env_vars (Union[Unset, SparkEnvPair]): An arbitrary object where the object key is an environment variable
            name and the value is an environment variable value.
        spark_version (Union[Unset, str]): The runtime version of the cluster, for example “5.0.x-scala2.11”. You can
            retrieve a list of available runtime versions by using the [Runtime versions](https://docs.databricks.com/dev-
            tools/api/latest/clusters.html#runtime-versions) API call.
        ssh_public_keys (Union[Unset, List[str]]): SSH public key contents that is added to each Spark node in this
            cluster. The corresponding private keys can be used to login with the user name `ubuntu` on port `2200`. Up to
            10 keys can be specified.
    """

    autotermination_minutes: Union[Unset, int] = UNSET
    aws_attributes: Union[Unset, AwsAttributes] = UNSET
    cluster_log_conf: Union[Unset, ClusterLogConf] = UNSET
    cluster_name: Union[Unset, str] = UNSET
    cluster_source: Union[Unset, ClusterSource] = UNSET
    custom_tags: Union[Unset, ClusterTag] = UNSET
    docker_image: Union[Unset, DockerImage] = UNSET
    driver_node_type_id: Union[Unset, str] = UNSET
    enable_elastic_disk: Union[Unset, bool] = UNSET
    init_scripts: Union[Unset, List[InitScriptInfo]] = UNSET
    instance_pool_id: Union[Unset, str] = UNSET
    node_type_id: Union[Unset, str] = UNSET
    policy_id: Union[Unset, str] = UNSET
    spark_conf: Union[Unset, SparkConfPair] = UNSET
    spark_env_vars: Union[Unset, SparkEnvPair] = UNSET
    spark_version: Union[Unset, str] = UNSET
    ssh_public_keys: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = Field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        autotermination_minutes = self.autotermination_minutes
        aws_attributes: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.aws_attributes, Unset):
            aws_attributes = self.aws_attributes.to_dict()

        cluster_log_conf: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cluster_log_conf, Unset):
            cluster_log_conf = self.cluster_log_conf.to_dict()

        cluster_name = self.cluster_name
        cluster_source: Union[Unset, str] = UNSET
        if not isinstance(self.cluster_source, Unset):
            cluster_source = self.cluster_source.value

        custom_tags: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.custom_tags, Unset):
            custom_tags = self.custom_tags.to_dict()

        docker_image: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.docker_image, Unset):
            docker_image = self.docker_image.to_dict()

        driver_node_type_id = self.driver_node_type_id
        enable_elastic_disk = self.enable_elastic_disk
        init_scripts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.init_scripts, Unset):
            init_scripts = []
            for init_scripts_item_data in self.init_scripts:
                init_scripts_item = init_scripts_item_data.to_dict()

                init_scripts.append(init_scripts_item)

        instance_pool_id = self.instance_pool_id
        node_type_id = self.node_type_id
        policy_id = self.policy_id
        spark_conf: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.spark_conf, Unset):
            spark_conf = self.spark_conf.to_dict()

        spark_env_vars: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.spark_env_vars, Unset):
            spark_env_vars = self.spark_env_vars.to_dict()

        spark_version = self.spark_version
        ssh_public_keys: Union[Unset, List[str]] = UNSET
        if not isinstance(self.ssh_public_keys, Unset):
            ssh_public_keys = self.ssh_public_keys

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if autotermination_minutes is not UNSET:
            field_dict["autotermination_minutes"] = autotermination_minutes
        if aws_attributes is not UNSET:
            field_dict["aws_attributes"] = aws_attributes
        if cluster_log_conf is not UNSET:
            field_dict["cluster_log_conf"] = cluster_log_conf
        if cluster_name is not UNSET:
            field_dict["cluster_name"] = cluster_name
        if cluster_source is not UNSET:
            field_dict["cluster_source"] = cluster_source
        if custom_tags is not UNSET:
            field_dict["custom_tags"] = custom_tags
        if docker_image is not UNSET:
            field_dict["docker_image"] = docker_image
        if driver_node_type_id is not UNSET:
            field_dict["driver_node_type_id"] = driver_node_type_id
        if enable_elastic_disk is not UNSET:
            field_dict["enable_elastic_disk"] = enable_elastic_disk
        if init_scripts is not UNSET:
            field_dict["init_scripts"] = init_scripts
        if instance_pool_id is not UNSET:
            field_dict["instance_pool_id"] = instance_pool_id
        if node_type_id is not UNSET:
            field_dict["node_type_id"] = node_type_id
        if policy_id is not UNSET:
            field_dict["policy_id"] = policy_id
        if spark_conf is not UNSET:
            field_dict["spark_conf"] = spark_conf
        if spark_env_vars is not UNSET:
            field_dict["spark_env_vars"] = spark_env_vars
        if spark_version is not UNSET:
            field_dict["spark_version"] = spark_version
        if ssh_public_keys is not UNSET:
            field_dict["ssh_public_keys"] = ssh_public_keys

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        if src_dict is None or src_dict is UNSET:
            return {}
        d = {k: v if v is not None else UNSET for k, v in src_dict.items()}
        autotermination_minutes = d.pop("autotermination_minutes", UNSET)

        _aws_attributes = d.pop("aws_attributes", UNSET)
        aws_attributes: Union[Unset, AwsAttributes]
        if isinstance(_aws_attributes, Unset):
            aws_attributes = UNSET
        else:
            aws_attributes = AwsAttributes.from_dict(_aws_attributes)

        _cluster_log_conf = d.pop("cluster_log_conf", UNSET)
        cluster_log_conf: Union[Unset, ClusterLogConf]
        if isinstance(_cluster_log_conf, Unset):
            cluster_log_conf = UNSET
        else:
            cluster_log_conf = ClusterLogConf.from_dict(_cluster_log_conf)

        cluster_name = d.pop("cluster_name", UNSET)

        _cluster_source = d.pop("cluster_source", UNSET)
        cluster_source: Union[Unset, ClusterSource]
        if isinstance(_cluster_source, Unset):
            cluster_source = UNSET
        else:
            cluster_source = ClusterSource(_cluster_source)

        _custom_tags = d.pop("custom_tags", UNSET)
        custom_tags: Union[Unset, ClusterTag]
        if isinstance(_custom_tags, Unset):
            custom_tags = UNSET
        else:
            custom_tags = ClusterTag.from_dict(_custom_tags)

        _docker_image = d.pop("docker_image", UNSET)
        docker_image: Union[Unset, DockerImage]
        if isinstance(_docker_image, Unset):
            docker_image = UNSET
        else:
            docker_image = DockerImage.from_dict(_docker_image)

        driver_node_type_id = d.pop("driver_node_type_id", UNSET)

        enable_elastic_disk = d.pop("enable_elastic_disk", UNSET)

        init_scripts = []
        _init_scripts = d.pop("init_scripts", UNSET)
        for init_scripts_item_data in _init_scripts or []:
            init_scripts_item = InitScriptInfo.from_dict(init_scripts_item_data)

            init_scripts.append(init_scripts_item)

        instance_pool_id = d.pop("instance_pool_id", UNSET)

        node_type_id = d.pop("node_type_id", UNSET)

        policy_id = d.pop("policy_id", UNSET)

        _spark_conf = d.pop("spark_conf", UNSET)
        spark_conf: Union[Unset, SparkConfPair]
        if isinstance(_spark_conf, Unset):
            spark_conf = UNSET
        else:
            spark_conf = SparkConfPair.from_dict(_spark_conf)

        _spark_env_vars = d.pop("spark_env_vars", UNSET)
        spark_env_vars: Union[Unset, SparkEnvPair]
        if isinstance(_spark_env_vars, Unset):
            spark_env_vars = UNSET
        else:
            spark_env_vars = SparkEnvPair.from_dict(_spark_env_vars)

        spark_version = d.pop("spark_version", UNSET)

        ssh_public_keys = cast(List[str], d.pop("ssh_public_keys", UNSET))

        cluster_attributes = cls(
            autotermination_minutes=autotermination_minutes,
            aws_attributes=aws_attributes,
            cluster_log_conf=cluster_log_conf,
            cluster_name=cluster_name,
            cluster_source=cluster_source,
            custom_tags=custom_tags,
            docker_image=docker_image,
            driver_node_type_id=driver_node_type_id,
            enable_elastic_disk=enable_elastic_disk,
            init_scripts=init_scripts,
            instance_pool_id=instance_pool_id,
            node_type_id=node_type_id,
            policy_id=policy_id,
            spark_conf=spark_conf,
            spark_env_vars=spark_env_vars,
            spark_version=spark_version,
            ssh_public_keys=ssh_public_keys,
        )

        cluster_attributes.additional_properties = d
        return cluster_attributes

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
