# coding: utf-8

"""
    NiFi Rest Api

    The Rest Api provides programmatic access to command and control a NiFi instance in real time. Start and                                              stop processors, monitor queues, query provenance data, and more. Each endpoint below includes a description,                                             definitions of the expected input and output, potential response codes, and the authorizations required                                             to invoke each service.

    OpenAPI spec version: 1.13.3-SNAPSHOT
    Contact: dev@nifi.apache.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class VersionInfoDTO(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'ni_fi_version': 'str',
        'java_vendor': 'str',
        'java_version': 'str',
        'os_name': 'str',
        'os_version': 'str',
        'os_architecture': 'str',
        'build_tag': 'str',
        'build_revision': 'str',
        'build_branch': 'str',
        'build_timestamp': 'datetime'
    }

    attribute_map = {
        'ni_fi_version': 'niFiVersion',
        'java_vendor': 'javaVendor',
        'java_version': 'javaVersion',
        'os_name': 'osName',
        'os_version': 'osVersion',
        'os_architecture': 'osArchitecture',
        'build_tag': 'buildTag',
        'build_revision': 'buildRevision',
        'build_branch': 'buildBranch',
        'build_timestamp': 'buildTimestamp'
    }

    def __init__(self, ni_fi_version=None, java_vendor=None, java_version=None, os_name=None, os_version=None, os_architecture=None, build_tag=None, build_revision=None, build_branch=None, build_timestamp=None):
        """
        VersionInfoDTO - a model defined in Swagger
        """

        self._ni_fi_version = None
        self._java_vendor = None
        self._java_version = None
        self._os_name = None
        self._os_version = None
        self._os_architecture = None
        self._build_tag = None
        self._build_revision = None
        self._build_branch = None
        self._build_timestamp = None

        if ni_fi_version is not None:
          self.ni_fi_version = ni_fi_version
        if java_vendor is not None:
          self.java_vendor = java_vendor
        if java_version is not None:
          self.java_version = java_version
        if os_name is not None:
          self.os_name = os_name
        if os_version is not None:
          self.os_version = os_version
        if os_architecture is not None:
          self.os_architecture = os_architecture
        if build_tag is not None:
          self.build_tag = build_tag
        if build_revision is not None:
          self.build_revision = build_revision
        if build_branch is not None:
          self.build_branch = build_branch
        if build_timestamp is not None:
          self.build_timestamp = build_timestamp

    @property
    def ni_fi_version(self):
        """
        Gets the ni_fi_version of this VersionInfoDTO.
        The version of this NiFi.

        :return: The ni_fi_version of this VersionInfoDTO.
        :rtype: str
        """
        return self._ni_fi_version

    @ni_fi_version.setter
    def ni_fi_version(self, ni_fi_version):
        """
        Sets the ni_fi_version of this VersionInfoDTO.
        The version of this NiFi.

        :param ni_fi_version: The ni_fi_version of this VersionInfoDTO.
        :type: str
        """

        self._ni_fi_version = ni_fi_version

    @property
    def java_vendor(self):
        """
        Gets the java_vendor of this VersionInfoDTO.
        Java JVM vendor

        :return: The java_vendor of this VersionInfoDTO.
        :rtype: str
        """
        return self._java_vendor

    @java_vendor.setter
    def java_vendor(self, java_vendor):
        """
        Sets the java_vendor of this VersionInfoDTO.
        Java JVM vendor

        :param java_vendor: The java_vendor of this VersionInfoDTO.
        :type: str
        """

        self._java_vendor = java_vendor

    @property
    def java_version(self):
        """
        Gets the java_version of this VersionInfoDTO.
        Java version

        :return: The java_version of this VersionInfoDTO.
        :rtype: str
        """
        return self._java_version

    @java_version.setter
    def java_version(self, java_version):
        """
        Sets the java_version of this VersionInfoDTO.
        Java version

        :param java_version: The java_version of this VersionInfoDTO.
        :type: str
        """

        self._java_version = java_version

    @property
    def os_name(self):
        """
        Gets the os_name of this VersionInfoDTO.
        Host operating system name

        :return: The os_name of this VersionInfoDTO.
        :rtype: str
        """
        return self._os_name

    @os_name.setter
    def os_name(self, os_name):
        """
        Sets the os_name of this VersionInfoDTO.
        Host operating system name

        :param os_name: The os_name of this VersionInfoDTO.
        :type: str
        """

        self._os_name = os_name

    @property
    def os_version(self):
        """
        Gets the os_version of this VersionInfoDTO.
        Host operating system version

        :return: The os_version of this VersionInfoDTO.
        :rtype: str
        """
        return self._os_version

    @os_version.setter
    def os_version(self, os_version):
        """
        Sets the os_version of this VersionInfoDTO.
        Host operating system version

        :param os_version: The os_version of this VersionInfoDTO.
        :type: str
        """

        self._os_version = os_version

    @property
    def os_architecture(self):
        """
        Gets the os_architecture of this VersionInfoDTO.
        Host operating system architecture

        :return: The os_architecture of this VersionInfoDTO.
        :rtype: str
        """
        return self._os_architecture

    @os_architecture.setter
    def os_architecture(self, os_architecture):
        """
        Sets the os_architecture of this VersionInfoDTO.
        Host operating system architecture

        :param os_architecture: The os_architecture of this VersionInfoDTO.
        :type: str
        """

        self._os_architecture = os_architecture

    @property
    def build_tag(self):
        """
        Gets the build_tag of this VersionInfoDTO.
        Build tag

        :return: The build_tag of this VersionInfoDTO.
        :rtype: str
        """
        return self._build_tag

    @build_tag.setter
    def build_tag(self, build_tag):
        """
        Sets the build_tag of this VersionInfoDTO.
        Build tag

        :param build_tag: The build_tag of this VersionInfoDTO.
        :type: str
        """

        self._build_tag = build_tag

    @property
    def build_revision(self):
        """
        Gets the build_revision of this VersionInfoDTO.
        Build revision or commit hash

        :return: The build_revision of this VersionInfoDTO.
        :rtype: str
        """
        return self._build_revision

    @build_revision.setter
    def build_revision(self, build_revision):
        """
        Sets the build_revision of this VersionInfoDTO.
        Build revision or commit hash

        :param build_revision: The build_revision of this VersionInfoDTO.
        :type: str
        """

        self._build_revision = build_revision

    @property
    def build_branch(self):
        """
        Gets the build_branch of this VersionInfoDTO.
        Build branch

        :return: The build_branch of this VersionInfoDTO.
        :rtype: str
        """
        return self._build_branch

    @build_branch.setter
    def build_branch(self, build_branch):
        """
        Sets the build_branch of this VersionInfoDTO.
        Build branch

        :param build_branch: The build_branch of this VersionInfoDTO.
        :type: str
        """

        self._build_branch = build_branch

    @property
    def build_timestamp(self):
        """
        Gets the build_timestamp of this VersionInfoDTO.
        Build timestamp

        :return: The build_timestamp of this VersionInfoDTO.
        :rtype: datetime
        """
        return self._build_timestamp

    @build_timestamp.setter
    def build_timestamp(self, build_timestamp):
        """
        Sets the build_timestamp of this VersionInfoDTO.
        Build timestamp

        :param build_timestamp: The build_timestamp of this VersionInfoDTO.
        :type: datetime
        """

        self._build_timestamp = build_timestamp

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, VersionInfoDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
