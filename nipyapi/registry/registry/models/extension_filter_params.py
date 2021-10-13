# coding: utf-8

"""
    Apache NiFi Registry REST API

    The REST API provides an interface to a registry with operations for saving, versioning, reading NiFi flows and components.

    OpenAPI spec version: 0.8.0
    Contact: dev@nifi.apache.org
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ExtensionFilterParams(object):
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
        'bundle_type': 'str',
        'extension_type': 'str',
        'tags': 'list[str]'
    }

    attribute_map = {
        'bundle_type': 'bundleType',
        'extension_type': 'extensionType',
        'tags': 'tags'
    }

    def __init__(self, bundle_type=None, extension_type=None, tags=None):
        """
        ExtensionFilterParams - a model defined in Swagger
        """

        self._bundle_type = None
        self._extension_type = None
        self._tags = None

        if bundle_type is not None:
          self.bundle_type = bundle_type
        if extension_type is not None:
          self.extension_type = extension_type
        if tags is not None:
          self.tags = tags

    @property
    def bundle_type(self):
        """
        Gets the bundle_type of this ExtensionFilterParams.
        The type of bundle

        :return: The bundle_type of this ExtensionFilterParams.
        :rtype: str
        """
        return self._bundle_type

    @bundle_type.setter
    def bundle_type(self, bundle_type):
        """
        Sets the bundle_type of this ExtensionFilterParams.
        The type of bundle

        :param bundle_type: The bundle_type of this ExtensionFilterParams.
        :type: str
        """
        allowed_values = ["NIFI_NAR", "MINIFI_CPP"]
        if bundle_type not in allowed_values:
            raise ValueError(
                "Invalid value for `bundle_type` ({0}), must be one of {1}"
                .format(bundle_type, allowed_values)
            )

        self._bundle_type = bundle_type

    @property
    def extension_type(self):
        """
        Gets the extension_type of this ExtensionFilterParams.
        The type of extension

        :return: The extension_type of this ExtensionFilterParams.
        :rtype: str
        """
        return self._extension_type

    @extension_type.setter
    def extension_type(self, extension_type):
        """
        Sets the extension_type of this ExtensionFilterParams.
        The type of extension

        :param extension_type: The extension_type of this ExtensionFilterParams.
        :type: str
        """
        allowed_values = ["PROCESSOR", "CONTROLLER_SERVICE", "REPORTING_TASK"]
        if extension_type not in allowed_values:
            raise ValueError(
                "Invalid value for `extension_type` ({0}), must be one of {1}"
                .format(extension_type, allowed_values)
            )

        self._extension_type = extension_type

    @property
    def tags(self):
        """
        Gets the tags of this ExtensionFilterParams.
        The tags

        :return: The tags of this ExtensionFilterParams.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this ExtensionFilterParams.
        The tags

        :param tags: The tags of this ExtensionFilterParams.
        :type: list[str]
        """

        self._tags = tags

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
        if not isinstance(other, ExtensionFilterParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
