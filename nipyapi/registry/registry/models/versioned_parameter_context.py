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


class VersionedParameterContext(object):
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
        'name': 'str',
        'description': 'str',
        'parameters': 'list[VersionedParameter]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'parameters': 'parameters'
    }

    def __init__(self, name=None, description=None, parameters=None):
        """
        VersionedParameterContext - a model defined in Swagger
        """

        self._name = None
        self._description = None
        self._parameters = None

        if name is not None:
          self.name = name
        if description is not None:
          self.description = description
        if parameters is not None:
          self.parameters = parameters

    @property
    def name(self):
        """
        Gets the name of this VersionedParameterContext.
        The name of the context

        :return: The name of this VersionedParameterContext.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this VersionedParameterContext.
        The name of the context

        :param name: The name of this VersionedParameterContext.
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this VersionedParameterContext.
        The description of the parameter context

        :return: The description of this VersionedParameterContext.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this VersionedParameterContext.
        The description of the parameter context

        :param description: The description of this VersionedParameterContext.
        :type: str
        """

        self._description = description

    @property
    def parameters(self):
        """
        Gets the parameters of this VersionedParameterContext.
        The parameters in the context

        :return: The parameters of this VersionedParameterContext.
        :rtype: list[VersionedParameter]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """
        Sets the parameters of this VersionedParameterContext.
        The parameters in the context

        :param parameters: The parameters of this VersionedParameterContext.
        :type: list[VersionedParameter]
        """

        self._parameters = parameters

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
        if not isinstance(other, VersionedParameterContext):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
