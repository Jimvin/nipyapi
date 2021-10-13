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


class TagCount(object):
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
        'tag': 'str',
        'count': 'int'
    }

    attribute_map = {
        'tag': 'tag',
        'count': 'count'
    }

    def __init__(self, tag=None, count=None):
        """
        TagCount - a model defined in Swagger
        """

        self._tag = None
        self._count = None

        if tag is not None:
          self.tag = tag
        if count is not None:
          self.count = count

    @property
    def tag(self):
        """
        Gets the tag of this TagCount.
        The tag label

        :return: The tag of this TagCount.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """
        Sets the tag of this TagCount.
        The tag label

        :param tag: The tag of this TagCount.
        :type: str
        """

        self._tag = tag

    @property
    def count(self):
        """
        Gets the count of this TagCount.
        The number of occurrences of the given tag

        :return: The count of this TagCount.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """
        Sets the count of this TagCount.
        The number of occurrences of the given tag

        :param count: The count of this TagCount.
        :type: int
        """

        self._count = count

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
        if not isinstance(other, TagCount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
