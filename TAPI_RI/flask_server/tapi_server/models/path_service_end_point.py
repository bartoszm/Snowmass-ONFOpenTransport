# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from tapi_server.models.base_model_ import Model
from tapi_server.models.local_class import LocalClass  # noqa: F401,E501
from tapi_server.models.name_and_value import NameAndValue  # noqa: F401,E501
from tapi_server import util


class PathServiceEndPoint(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, local_id: str=None, name: List[NameAndValue]=None, service_interface_point: str=None, role: str=None, direction: str=None, service_layer: str=None):  # noqa: E501
        """PathServiceEndPoint - a model defined in Swagger

        :param local_id: The local_id of this PathServiceEndPoint.  # noqa: E501
        :type local_id: str
        :param name: The name of this PathServiceEndPoint.  # noqa: E501
        :type name: List[NameAndValue]
        :param service_interface_point: The service_interface_point of this PathServiceEndPoint.  # noqa: E501
        :type service_interface_point: str
        :param role: The role of this PathServiceEndPoint.  # noqa: E501
        :type role: str
        :param direction: The direction of this PathServiceEndPoint.  # noqa: E501
        :type direction: str
        :param service_layer: The service_layer of this PathServiceEndPoint.  # noqa: E501
        :type service_layer: str
        """
        self.swagger_types = {
            'local_id': str,
            'name': List[NameAndValue],
            'service_interface_point': str,
            'role': str,
            'direction': str,
            'service_layer': str
        }

        self.attribute_map = {
            'local_id': 'local-id',
            'name': 'name',
            'service_interface_point': 'service-interface-point',
            'role': 'role',
            'direction': 'direction',
            'service_layer': 'service-layer'
        }

        self._local_id = local_id
        self._name = name
        self._service_interface_point = service_interface_point
        self._role = role
        self._direction = direction
        self._service_layer = service_layer

    @classmethod
    def from_dict(cls, dikt) -> 'PathServiceEndPoint':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The path-service-end-point of this PathServiceEndPoint.  # noqa: E501
        :rtype: PathServiceEndPoint
        """
        return util.deserialize_model(dikt, cls)

    @property
    def local_id(self) -> str:
        """Gets the local_id of this PathServiceEndPoint.


        :return: The local_id of this PathServiceEndPoint.
        :rtype: str
        """
        return self._local_id

    @local_id.setter
    def local_id(self, local_id: str):
        """Sets the local_id of this PathServiceEndPoint.


        :param local_id: The local_id of this PathServiceEndPoint.
        :type local_id: str
        """

        self._local_id = local_id

    @property
    def name(self) -> List[NameAndValue]:
        """Gets the name of this PathServiceEndPoint.

        List of names. A property of an entity with a value that is unique in some namespace but may change during the life of the entity. A name carries no semantics with respect to the purpose of the entity.  # noqa: E501

        :return: The name of this PathServiceEndPoint.
        :rtype: List[NameAndValue]
        """
        return self._name

    @name.setter
    def name(self, name: List[NameAndValue]):
        """Sets the name of this PathServiceEndPoint.

        List of names. A property of an entity with a value that is unique in some namespace but may change during the life of the entity. A name carries no semantics with respect to the purpose of the entity.  # noqa: E501

        :param name: The name of this PathServiceEndPoint.
        :type name: List[NameAndValue]
        """

        self._name = name

    @property
    def service_interface_point(self) -> str:
        """Gets the service_interface_point of this PathServiceEndPoint.


        :return: The service_interface_point of this PathServiceEndPoint.
        :rtype: str
        """
        return self._service_interface_point

    @service_interface_point.setter
    def service_interface_point(self, service_interface_point: str):
        """Sets the service_interface_point of this PathServiceEndPoint.


        :param service_interface_point: The service_interface_point of this PathServiceEndPoint.
        :type service_interface_point: str
        """

        self._service_interface_point = service_interface_point

    @property
    def role(self) -> str:
        """Gets the role of this PathServiceEndPoint.

        Each EP of the FC has a role (e.g., working, protection, protected, symmetric, hub, spoke, leaf, root)  in the context of the FC with respect to the FC function.   # noqa: E501

        :return: The role of this PathServiceEndPoint.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role: str):
        """Sets the role of this PathServiceEndPoint.

        Each EP of the FC has a role (e.g., working, protection, protected, symmetric, hub, spoke, leaf, root)  in the context of the FC with respect to the FC function.   # noqa: E501

        :param role: The role of this PathServiceEndPoint.
        :type role: str
        """
        allowed_values = ["SYMMETRIC", "ROOT", "LEAF", "TRUNK", "UNKNOWN"]  # noqa: E501
        if role not in allowed_values:
            raise ValueError(
                "Invalid value for `role` ({0}), must be one of {1}"
                .format(role, allowed_values)
            )

        self._role = role

    @property
    def direction(self) -> str:
        """Gets the direction of this PathServiceEndPoint.

        The orientation of defined flow at the EndPoint.  # noqa: E501

        :return: The direction of this PathServiceEndPoint.
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction: str):
        """Sets the direction of this PathServiceEndPoint.

        The orientation of defined flow at the EndPoint.  # noqa: E501

        :param direction: The direction of this PathServiceEndPoint.
        :type direction: str
        """
        allowed_values = ["BIDIRECTIONAL", "INPUT", "OUTPUT", "UNIDENTIFIED_OR_UNKNOWN"]  # noqa: E501
        if direction not in allowed_values:
            raise ValueError(
                "Invalid value for `direction` ({0}), must be one of {1}"
                .format(direction, allowed_values)
            )

        self._direction = direction

    @property
    def service_layer(self) -> str:
        """Gets the service_layer of this PathServiceEndPoint.


        :return: The service_layer of this PathServiceEndPoint.
        :rtype: str
        """
        return self._service_layer

    @service_layer.setter
    def service_layer(self, service_layer: str):
        """Sets the service_layer of this PathServiceEndPoint.


        :param service_layer: The service_layer of this PathServiceEndPoint.
        :type service_layer: str
        """
        allowed_values = ["OTSiA", "OCH", "OTU", "ODU", "ETH", "ETY", "DSR"]  # noqa: E501
        if service_layer not in allowed_values:
            raise ValueError(
                "Invalid value for `service_layer` ({0}), must be one of {1}"
                .format(service_layer, allowed_values)
            )

        self._service_layer = service_layer
