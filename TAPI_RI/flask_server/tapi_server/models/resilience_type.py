# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server import util


class ResilienceType(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, restoration_policy: str=None, protection_type: str=None):  # noqa: E501
        """ResilienceType - a model defined in Swagger

        :param restoration_policy: The restoration_policy of this ResilienceType.  # noqa: E501
        :type restoration_policy: str
        :param protection_type: The protection_type of this ResilienceType.  # noqa: E501
        :type protection_type: str
        """
        self.swagger_types = {
            'restoration_policy': str,
            'protection_type': str
        }

        self.attribute_map = {
            'restoration_policy': 'restoration-policy',
            'protection_type': 'protection-type'
        }

        self._restoration_policy = restoration_policy
        self._protection_type = protection_type

    @classmethod
    def from_dict(cls, dikt) -> 'ResilienceType':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The resilience-type of this ResilienceType.  # noqa: E501
        :rtype: ResilienceType
        """
        return util.deserialize_model(dikt, cls)

    @property
    def restoration_policy(self) -> str:
        """Gets the restoration_policy of this ResilienceType.


        :return: The restoration_policy of this ResilienceType.
        :rtype: str
        """
        return self._restoration_policy

    @restoration_policy.setter
    def restoration_policy(self, restoration_policy: str):
        """Sets the restoration_policy of this ResilienceType.


        :param restoration_policy: The restoration_policy of this ResilienceType.
        :type restoration_policy: str
        """
        allowed_values = ["PER_DOMAIN_RESTORATION", "END_TO_END_RESTORATION", "NA"]  # noqa: E501
        if restoration_policy not in allowed_values:
            raise ValueError(
                "Invalid value for `restoration_policy` ({0}), must be one of {1}"
                .format(restoration_policy, allowed_values)
            )

        self._restoration_policy = restoration_policy

    @property
    def protection_type(self) -> str:
        """Gets the protection_type of this ResilienceType.


        :return: The protection_type of this ResilienceType.
        :rtype: str
        """
        return self._protection_type

    @protection_type.setter
    def protection_type(self, protection_type: str):
        """Sets the protection_type of this ResilienceType.


        :param protection_type: The protection_type of this ResilienceType.
        :type protection_type: str
        """
        allowed_values = ["NO_PROTECTON", "ONE_PLUS_ONE_PROTECTION", "ONE_PLUS_ONE_PROTECTION_WITH_DYNAMIC_RESTORATION", "PERMANENT_ONE_PLUS_ONE_PROTECTION", "ONE_FOR_ONE_PROTECTION", "DYNAMIC_RESTORATION", "PRE_COMPUTED_RESTORATION"]  # noqa: E501
        if protection_type not in allowed_values:
            raise ValueError(
                "Invalid value for `protection_type` ({0}), must be one of {1}"
                .format(protection_type, allowed_values)
            )

        self._protection_type = protection_type
