# coding: utf-8

"""
    蓝鲸用户管理 API

    蓝鲸用户管理后台服务 API  # noqa: E501

    OpenAPI spec version: v2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from bkuser_sdk.models.related_resource_slz import RelatedResourceSLZ  # noqa: F401,E501


class AuthInfoSLZ(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'id': 'str',
        'display_name': 'str',
        'related_resources': 'list[RelatedResourceSLZ]'
    }

    attribute_map = {
        'id': 'id',
        'display_name': 'display_name',
        'related_resources': 'related_resources'
    }

    def __init__(self, id=None, display_name=None, related_resources=None):  # noqa: E501
        """AuthInfoSLZ - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._display_name = None
        self._related_resources = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if display_name is not None:
            self.display_name = display_name
        if related_resources is not None:
            self.related_resources = related_resources

    @property
    def id(self):
        """Gets the id of this AuthInfoSLZ.  # noqa: E501


        :return: The id of this AuthInfoSLZ.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AuthInfoSLZ.


        :param id: The id of this AuthInfoSLZ.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def display_name(self):
        """Gets the display_name of this AuthInfoSLZ.  # noqa: E501


        :return: The display_name of this AuthInfoSLZ.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this AuthInfoSLZ.


        :param display_name: The display_name of this AuthInfoSLZ.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def related_resources(self):
        """Gets the related_resources of this AuthInfoSLZ.  # noqa: E501


        :return: The related_resources of this AuthInfoSLZ.  # noqa: E501
        :rtype: list[RelatedResourceSLZ]
        """
        return self._related_resources

    @related_resources.setter
    def related_resources(self, related_resources):
        """Sets the related_resources of this AuthInfoSLZ.


        :param related_resources: The related_resources of this AuthInfoSLZ.  # noqa: E501
        :type: list[RelatedResourceSLZ]
        """

        self._related_resources = related_resources

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(AuthInfoSLZ, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AuthInfoSLZ):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
