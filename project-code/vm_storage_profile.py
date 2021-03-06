# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.vm_storage_profile_image_ref import VMStorageProfileImageRef  # noqa: F401,E501
from swagger_server import util


class VMStorageProfile(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, image_ref=None):  # noqa: E501
        """VMStorageProfile - a model defined in Swagger

        :param image_ref: The image_ref of this VMStorageProfile.  # noqa: E501
        :type image_ref: VMStorageProfileImageRef
        """
        self.swagger_types = {
            'image_ref': VMStorageProfileImageRef
        }

        self.attribute_map = {
            'image_ref': 'image_ref'
        }

        self._image_ref = image_ref

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The VM_storage_profile of this VMStorageProfile.  # noqa: E501
        :rtype: VMStorageProfile
        """
        return util.deserialize_model(dikt, cls)

    @property
    def image_ref(self):
        """Gets the image_ref of this VMStorageProfile.


        :return: The image_ref of this VMStorageProfile.
        :rtype: VMStorageProfileImageRef
        """
        return self._image_ref

    @image_ref.setter
    def image_ref(self, image_ref):
        """Sets the image_ref of this VMStorageProfile.


        :param image_ref: The image_ref of this VMStorageProfile.
        :type image_ref: VMStorageProfileImageRef
        """

        self._image_ref = image_ref
