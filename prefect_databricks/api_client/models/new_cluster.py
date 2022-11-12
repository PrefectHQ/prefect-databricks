from typing import Any, Dict, List, Type, TypeVar, Union, cast

from pydantic import BaseModel, Field

from ..models.auto_scale import AutoScale
from ..models.aws_attributes import AwsAttributes
from ..models.cluster_log_conf import ClusterLogConf
from ..models.cluster_tag import ClusterTag
from ..models.init_script_info import InitScriptInfo
from ..models.spark_conf_pair import SparkConfPair
from ..models.spark_env_pair import SparkEnvPair
from ..types import UNSET, Unset

T = TypeVar("T", bound="NewCluster")


class NewCluster(BaseModel):
    """
    Attributes:
        spark_version (str): The Spark version of the cluster. A list of available Spark versions can be retrieved by
            using the [Runtime versions](https://docs.databricks.com/dev-tools/api/latest/clusters.html#runtime-versions)
            API call.
        autoscale (Union[Unset, AutoScale]):
        aws_attributes (Union[Unset, AwsAttributes]):
        cluster_log_conf (Union[Unset, ClusterLogConf]):
        custom_tags (Union[Unset, ClusterTag]): An object with key value pairs. The key length must be between 1 and 127
            UTF-8 characters, inclusive. The value length must be less than or equal to 255 UTF-8 characters. For a list of
            all restrictions, see AWS Tag Restrictions:
            <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html#tag-restrictions>
        driver_instance_pool_id (Union[Unset, str]): The optional ID of the instance pool to use for the driver node.
            You must also specify `instance_pool_id`. Refer to [Instance Pools API](https://docs.databricks.com/dev-
            tools/api/latest/instance-pools.html) for details.
        driver_node_type_id (Union[Unset, str]): The node type of the Spark driver. This field is optional; if unset,
            the driver node type is set as the same value as `node_type_id` defined above.
        enable_elastic_disk (Union[Unset, bool]): Autoscaling Local Storage: when enabled, this cluster dynamically
            acquires additional disk space when its Spark workers are running low on disk space. This feature requires
            specific AWS permissions to function correctly - refer to [Autoscaling local
            storage](https://docs.databricks.com/clusters/configure.html#autoscaling-local-storage) for details.
        init_scripts (Union[Unset, List[InitScriptInfo]]): The configuration for storing init scripts. Any number of
            scripts can be specified. The scripts are executed sequentially in the order provided. If `cluster_log_conf` is
            specified, init script logs are sent to `<destination>/<cluster-id>/init_scripts`.
        instance_pool_id (Union[Unset, str]): The optional ID of the instance pool to use for cluster nodes. If
            `driver_instance_pool_id` is present, `instance_pool_id` is used for worker nodes only. Otherwise, it is used
            for both the driver node and worker nodes. Refer to [Instance Pools API](https://docs.databricks.com/dev-
            tools/api/latest/instance-pools.html) for details.
        node_type_id (Union[Unset, str]): This field encodes, through a single value, the resources available to each of
            the Spark nodes in this cluster. For example, the Spark nodes can be provisioned and optimized for memory or
            compute intensive workloads A list of available node types can be retrieved by using the [List node
            types](https://docs.databricks.com/dev-tools/api/latest/clusters.html#list-node-types) API call.
        num_workers (Union[Unset, int]): If num_workers, number of worker nodes that this cluster must have. A cluster
            has one Spark driver and num_workers executors for a total of num_workers + 1 Spark nodes. When reading the
            properties of a cluster, this field reflects the desired number of workers rather than the actual current number
            of workers. For example, if a cluster is resized from 5 to 10 workers, this field immediately updates to reflect
            the target size of 10 workers, whereas the workers listed in `spark_info` gradually increase from 5 to 10 as the
            new nodes are provisioned.
        policy_id (Union[Unset, str]): A [cluster policy](https://docs.databricks.com/dev-
            tools/api/latest/policies.html) ID. Either `node_type_id` or `instance_pool_id` must be specified in the cluster
            policy if they are not specified in this job cluster object.
        spark_conf (Union[Unset, SparkConfPair]): An arbitrary object where the object key is a configuration propery
            name and the value is a configuration property value.
        spark_env_vars (Union[Unset, SparkEnvPair]): An arbitrary object where the object key is an environment variable
            name and the value is an environment variable value.
        ssh_public_keys (Union[Unset, List[str]]): SSH public key contents that are added to each Spark node in this
            cluster. The corresponding private keys can be used to login with the user name `ubuntu` on port `2200`. Up to
            10 keys can be specified.
    """

    spark_version: str = None
    autoscale: Union[Unset, AutoScale] = UNSET
    aws_attributes: Union[Unset, AwsAttributes] = UNSET
    cluster_log_conf: Union[Unset, ClusterLogConf] = UNSET
    custom_tags: Union[Unset, ClusterTag] = UNSET
    driver_instance_pool_id: Union[Unset, str] = UNSET
    driver_node_type_id: Union[Unset, str] = UNSET
    enable_elastic_disk: Union[Unset, bool] = UNSET
    init_scripts: Union[Unset, List[InitScriptInfo]] = UNSET
    instance_pool_id: Union[Unset, str] = UNSET
    node_type_id: Union[Unset, str] = UNSET
    num_workers: Union[Unset, int] = UNSET
    policy_id: Union[Unset, str] = UNSET
    spark_conf: Union[Unset, SparkConfPair] = UNSET
    spark_env_vars: Union[Unset, SparkEnvPair] = UNSET
    ssh_public_keys: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = Field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        spark_version = self.spark_version
        autoscale: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.autoscale, Unset):
            autoscale = self.autoscale.to_dict()

        aws_attributes: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.aws_attributes, Unset):
            aws_attributes = self.aws_attributes.to_dict()

        cluster_log_conf: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cluster_log_conf, Unset):
            cluster_log_conf = self.cluster_log_conf.to_dict()

        custom_tags: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.custom_tags, Unset):
            custom_tags = self.custom_tags.to_dict()

        driver_instance_pool_id = self.driver_instance_pool_id
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
        num_workers = self.num_workers
        policy_id = self.policy_id
        spark_conf: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.spark_conf, Unset):
            spark_conf = self.spark_conf.to_dict()

        spark_env_vars: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.spark_env_vars, Unset):
            spark_env_vars = self.spark_env_vars.to_dict()

        ssh_public_keys: Union[Unset, List[str]] = UNSET
        if not isinstance(self.ssh_public_keys, Unset):
            ssh_public_keys = self.ssh_public_keys

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "spark_version": spark_version,
            }
        )
        if autoscale is not UNSET:
            field_dict["autoscale"] = autoscale
        if aws_attributes is not UNSET:
            field_dict["aws_attributes"] = aws_attributes
        if cluster_log_conf is not UNSET:
            field_dict["cluster_log_conf"] = cluster_log_conf
        if custom_tags is not UNSET:
            field_dict["custom_tags"] = custom_tags
        if driver_instance_pool_id is not UNSET:
            field_dict["driver_instance_pool_id"] = driver_instance_pool_id
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
        if num_workers is not UNSET:
            field_dict["num_workers"] = num_workers
        if policy_id is not UNSET:
            field_dict["policy_id"] = policy_id
        if spark_conf is not UNSET:
            field_dict["spark_conf"] = spark_conf
        if spark_env_vars is not UNSET:
            field_dict["spark_env_vars"] = spark_env_vars
        if ssh_public_keys is not UNSET:
            field_dict["ssh_public_keys"] = ssh_public_keys

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        if src_dict is None or src_dict is UNSET:
            return {}
        d = {k: v if v is not None else UNSET for k, v in src_dict.items()}
        spark_version = d.pop("spark_version")

        _autoscale = d.pop("autoscale", UNSET)
        autoscale: Union[Unset, AutoScale]
        if isinstance(_autoscale, Unset):
            autoscale = UNSET
        else:
            autoscale = AutoScale.from_dict(_autoscale)

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

        _custom_tags = d.pop("custom_tags", UNSET)
        custom_tags: Union[Unset, ClusterTag]
        if isinstance(_custom_tags, Unset):
            custom_tags = UNSET
        else:
            custom_tags = ClusterTag.from_dict(_custom_tags)

        driver_instance_pool_id = d.pop("driver_instance_pool_id", UNSET)

        driver_node_type_id = d.pop("driver_node_type_id", UNSET)

        enable_elastic_disk = d.pop("enable_elastic_disk", UNSET)

        init_scripts = []
        _init_scripts = d.pop("init_scripts", UNSET)
        for init_scripts_item_data in _init_scripts or []:
            init_scripts_item = InitScriptInfo.from_dict(init_scripts_item_data)

            init_scripts.append(init_scripts_item)

        instance_pool_id = d.pop("instance_pool_id", UNSET)

        node_type_id = d.pop("node_type_id", UNSET)

        num_workers = d.pop("num_workers", UNSET)

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

        ssh_public_keys = cast(List[str], d.pop("ssh_public_keys", UNSET))

        new_cluster = cls(
            spark_version=spark_version,
            autoscale=autoscale,
            aws_attributes=aws_attributes,
            cluster_log_conf=cluster_log_conf,
            custom_tags=custom_tags,
            driver_instance_pool_id=driver_instance_pool_id,
            driver_node_type_id=driver_node_type_id,
            enable_elastic_disk=enable_elastic_disk,
            init_scripts=init_scripts,
            instance_pool_id=instance_pool_id,
            node_type_id=node_type_id,
            num_workers=num_workers,
            policy_id=policy_id,
            spark_conf=spark_conf,
            spark_env_vars=spark_env_vars,
            ssh_public_keys=ssh_public_keys,
        )

        new_cluster.additional_properties = d
        return new_cluster

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
