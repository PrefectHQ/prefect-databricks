from typing import Any, Dict, List, Type, TypeVar, Union

from pydantic import BaseModel, Field

from ..models.maven_library import MavenLibrary
from ..models.python_py_pi_library import PythonPyPiLibrary
from ..models.r_cran_library import RCranLibrary
from ..types import UNSET, Unset

T = TypeVar("T", bound="Library")


class Library(BaseModel):
    """
    Attributes:
        cran (Union[Unset, RCranLibrary]):
        egg (Union[Unset, str]): If egg, URI of the egg to be installed. DBFS and S3 URIs are supported. For example: `{
            "egg": "dbfs:/my/egg" }` or `{ "egg": "s3://my-bucket/egg" }`. If S3 is used, make sure the cluster has read
            access on the library. You may need to launch the cluster with an instance profile to access the S3 URI.
            Example: dbfs:/my/egg.
        jar (Union[Unset, str]): If jar, URI of the JAR to be installed. DBFS and S3 URIs are supported. For example: `{
            "jar": "dbfs:/mnt/databricks/library.jar" }` or `{ "jar": "s3://my-bucket/library.jar" }`. If S3 is used, make
            sure the cluster has read access on the library. You may need to launch the cluster with an instance profile to
            access the S3 URI. Example: dbfs:/my-jar.jar.
        maven (Union[Unset, MavenLibrary]):
        pypi (Union[Unset, PythonPyPiLibrary]):
        whl (Union[Unset, str]): If whl, URI of the wheel or zipped wheels to be installed. DBFS and S3 URIs are
            supported. For example: `{ "whl": "dbfs:/my/whl" }` or `{ "whl": "s3://my-bucket/whl" }`. If S3 is used, make
            sure the cluster has read access on the library. You may need to launch the cluster with an instance profile to
            access the S3 URI. Also the wheel file name needs to use the [correct
            convention](https://www.python.org/dev/peps/pep-0427/#file-format). If zipped wheels are to be installed, the
            file name suffix should be `.wheelhouse.zip`. Example: dbfs:/my/whl.
    """

    cran: Union[Unset, RCranLibrary] = UNSET
    egg: Union[Unset, str] = UNSET
    jar: Union[Unset, str] = UNSET
    maven: Union[Unset, MavenLibrary] = UNSET
    pypi: Union[Unset, PythonPyPiLibrary] = UNSET
    whl: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = Field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cran: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cran, Unset):
            cran = self.cran.to_dict()

        egg = self.egg
        jar = self.jar
        maven: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.maven, Unset):
            maven = self.maven.to_dict()

        pypi: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pypi, Unset):
            pypi = self.pypi.to_dict()

        whl = self.whl

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cran is not UNSET:
            field_dict["cran"] = cran
        if egg is not UNSET:
            field_dict["egg"] = egg
        if jar is not UNSET:
            field_dict["jar"] = jar
        if maven is not UNSET:
            field_dict["maven"] = maven
        if pypi is not UNSET:
            field_dict["pypi"] = pypi
        if whl is not UNSET:
            field_dict["whl"] = whl

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        if src_dict is None or src_dict is UNSET:
            return {}
        d = {k: v if v is not None else UNSET for k, v in src_dict.items()}
        _cran = d.pop("cran", UNSET)
        cran: Union[Unset, RCranLibrary]
        if isinstance(_cran, Unset):
            cran = UNSET
        else:
            cran = RCranLibrary.from_dict(_cran)

        egg = d.pop("egg", UNSET)

        jar = d.pop("jar", UNSET)

        _maven = d.pop("maven", UNSET)
        maven: Union[Unset, MavenLibrary]
        if isinstance(_maven, Unset):
            maven = UNSET
        else:
            maven = MavenLibrary.from_dict(_maven)

        _pypi = d.pop("pypi", UNSET)
        pypi: Union[Unset, PythonPyPiLibrary]
        if isinstance(_pypi, Unset):
            pypi = UNSET
        else:
            pypi = PythonPyPiLibrary.from_dict(_pypi)

        whl = d.pop("whl", UNSET)

        library = cls(
            cran=cran,
            egg=egg,
            jar=jar,
            maven=maven,
            pypi=pypi,
            whl=whl,
        )

        library.additional_properties = d
        return library

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
