# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Detail(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, group_name=None, vm_name=None, location=None, disk_size=None, ip_name=None, vnet_name=None, subnet_name=None, nic_name=None, computer_name=None, username=None, password=None, vm_size=None, publisher=None, offer=None, sku=None, version=None):  # noqa: E501
        """Detail - a model defined in Swagger

        :param group_name: The group_name of this Detail.  # noqa: E501
        :type group_name: str
        :param vm_name: The vm_name of this Detail.  # noqa: E501
        :type vm_name: str
        :param location: The location of this Detail.  # noqa: E501
        :type location: str
        :param disk_size: The disk_size of this Detail.  # noqa: E501
        :type disk_size: str
        :param ip_name: The ip_name of this Detail.  # noqa: E501
        :type ip_name: str
        :param vnet_name: The vnet_name of this Detail.  # noqa: E501
        :type vnet_name: str
        :param subnet_name: The subnet_name of this Detail.  # noqa: E501
        :type subnet_name: str
        :param nic_name: The nic_name of this Detail.  # noqa: E501
        :type nic_name: str
        :param computer_name: The computer_name of this Detail.  # noqa: E501
        :type computer_name: str
        :param username: The username of this Detail.  # noqa: E501
        :type username: str
        :param password: The password of this Detail.  # noqa: E501
        :type password: str
        :param vm_size: The vm_size of this Detail.  # noqa: E501
        :type vm_size: str
        :param publisher: The publisher of this Detail.  # noqa: E501
        :type publisher: str
        :param offer: The offer of this Detail.  # noqa: E501
        :type offer: str
        :param sku: The sku of this Detail.  # noqa: E501
        :type sku: str
        :param version: The version of this Detail.  # noqa: E501
        :type version: str
        """
        self.swagger_types = {
            'group_name': str,
            'vm_name': str,
            'location': str,
            'disk_size': str,
            'ip_name': str,
            'vnet_name': str,
            'subnet_name': str,
            'nic_name': str,
            'computer_name': str,
            'username': str,
            'password': str,
            'vm_size': str,
            'publisher': str,
            'offer': str,
            'sku': str,
            'version': str
        }

        self.attribute_map = {
            'group_name': 'group_name',
            'vm_name': 'vm_name',
            'location': 'location',
            'disk_size': 'disk_size',
            'ip_name': 'ip_name',
            'vnet_name': 'vnet_name',
            'subnet_name': 'subnet_name',
            'nic_name': 'nic_name',
            'computer_name': 'computer_name',
            'username': 'username',
            'password': 'password',
            'vm_size': 'vm_size',
            'publisher': 'publisher',
            'offer': 'offer',
            'sku': 'sku',
            'version': 'version'
        }

        self._group_name = group_name
        self._vm_name = vm_name
        self._location = location
        self._disk_size = disk_size
        self._ip_name = ip_name
        self._vnet_name = vnet_name
        self._subnet_name = subnet_name
        self._nic_name = nic_name
        self._computer_name = computer_name
        self._username = username
        self._password = password
        self._vm_size = vm_size
        self._publisher = publisher
        self._offer = offer
        self._sku = sku
        self._version = version

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The detail of this Detail.  # noqa: E501
        :rtype: Detail
        """
        return util.deserialize_model(dikt, cls)

    @property
    def group_name(self):
        """Gets the group_name of this Detail.


        :return: The group_name of this Detail.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this Detail.


        :param group_name: The group_name of this Detail.
        :type group_name: str
        """

        self._group_name = group_name

    @property
    def vm_name(self):
        """Gets the vm_name of this Detail.


        :return: The vm_name of this Detail.
        :rtype: str
        """
        return self._vm_name

    @vm_name.setter
    def vm_name(self, vm_name):
        """Sets the vm_name of this Detail.


        :param vm_name: The vm_name of this Detail.
        :type vm_name: str
        """

        self._vm_name = vm_name

    @property
    def location(self):
        """Gets the location of this Detail.


        :return: The location of this Detail.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this Detail.


        :param location: The location of this Detail.
        :type location: str
        """

        self._location = location

    @property
    def disk_size(self):
        """Gets the disk_size of this Detail.


        :return: The disk_size of this Detail.
        :rtype: str
        """
        return self._disk_size

    @disk_size.setter
    def disk_size(self, disk_size):
        """Sets the disk_size of this Detail.


        :param disk_size: The disk_size of this Detail.
        :type disk_size: str
        """

        self._disk_size = disk_size

    @property
    def ip_name(self):
        """Gets the ip_name of this Detail.


        :return: The ip_name of this Detail.
        :rtype: str
        """
        return self._ip_name

    @ip_name.setter
    def ip_name(self, ip_name):
        """Sets the ip_name of this Detail.


        :param ip_name: The ip_name of this Detail.
        :type ip_name: str
        """

        self._ip_name = ip_name

    @property
    def vnet_name(self):
        """Gets the vnet_name of this Detail.


        :return: The vnet_name of this Detail.
        :rtype: str
        """
        return self._vnet_name

    @vnet_name.setter
    def vnet_name(self, vnet_name):
        """Sets the vnet_name of this Detail.


        :param vnet_name: The vnet_name of this Detail.
        :type vnet_name: str
        """

        self._vnet_name = vnet_name

    @property
    def subnet_name(self):
        """Gets the subnet_name of this Detail.


        :return: The subnet_name of this Detail.
        :rtype: str
        """
        return self._subnet_name

    @subnet_name.setter
    def subnet_name(self, subnet_name):
        """Sets the subnet_name of this Detail.


        :param subnet_name: The subnet_name of this Detail.
        :type subnet_name: str
        """

        self._subnet_name = subnet_name

    @property
    def nic_name(self):
        """Gets the nic_name of this Detail.


        :return: The nic_name of this Detail.
        :rtype: str
        """
        return self._nic_name

    @nic_name.setter
    def nic_name(self, nic_name):
        """Sets the nic_name of this Detail.


        :param nic_name: The nic_name of this Detail.
        :type nic_name: str
        """

        self._nic_name = nic_name

    @property
    def computer_name(self):
        """Gets the computer_name of this Detail.


        :return: The computer_name of this Detail.
        :rtype: str
        """
        return self._computer_name

    @computer_name.setter
    def computer_name(self, computer_name):
        """Sets the computer_name of this Detail.


        :param computer_name: The computer_name of this Detail.
        :type computer_name: str
        """

        self._computer_name = computer_name

    @property
    def username(self):
        """Gets the username of this Detail.


        :return: The username of this Detail.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this Detail.


        :param username: The username of this Detail.
        :type username: str
        """

        self._username = username

    @property
    def password(self):
        """Gets the password of this Detail.


        :return: The password of this Detail.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this Detail.


        :param password: The password of this Detail.
        :type password: str
        """

        self._password = password

    @property
    def vm_size(self):
        """Gets the vm_size of this Detail.


        :return: The vm_size of this Detail.
        :rtype: str
        """
        return self._vm_size

    @vm_size.setter
    def vm_size(self, vm_size):
        """Sets the vm_size of this Detail.


        :param vm_size: The vm_size of this Detail.
        :type vm_size: str
        """

        self._vm_size = vm_size

    @property
    def publisher(self):
        """Gets the publisher of this Detail.


        :return: The publisher of this Detail.
        :rtype: str
        """
        return self._publisher

    @publisher.setter
    def publisher(self, publisher):
        """Sets the publisher of this Detail.


        :param publisher: The publisher of this Detail.
        :type publisher: str
        """

        self._publisher = publisher

    @property
    def offer(self):
        """Gets the offer of this Detail.


        :return: The offer of this Detail.
        :rtype: str
        """
        return self._offer

    @offer.setter
    def offer(self, offer):
        """Sets the offer of this Detail.


        :param offer: The offer of this Detail.
        :type offer: str
        """

        self._offer = offer

    @property
    def sku(self):
        """Gets the sku of this Detail.


        :return: The sku of this Detail.
        :rtype: str
        """
        return self._sku

    @sku.setter
    def sku(self, sku):
        """Sets the sku of this Detail.


        :param sku: The sku of this Detail.
        :type sku: str
        """

        self._sku = sku

    @property
    def version(self):
        """Gets the version of this Detail.


        :return: The version of this Detail.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Detail.


        :param version: The version of this Detail.
        :type version: str
        """

        self._version = version
