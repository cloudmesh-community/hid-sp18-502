# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.resourcegroup import Resourcegroup  # noqa: E501
from swagger_server.models.vm import VM  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_create_resource_group_by_id(self):
        """Test case for create_resource_group_by_id

        
        """
        response = self.client.open(
            '/cloudmesh/azure/resourcegroup/create/{id}'.format(id='id_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_virtual_machine_by_id(self):
        """Test case for create_virtual_machine_by_id

        
        """
        response = self.client.open(
            '/cloudmesh/azure/vm/create/{id}'.format(id='id_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_resource_group_by_id(self):
        """Test case for get_resource_group_by_id

        
        """
        response = self.client.open(
            '/cloudmesh/azure/resourcegroup/{id}'.format(id='id_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_virtual_machine_by_id(self):
        """Test case for get_virtual_machine_by_id

        
        """
        response = self.client.open(
            '/cloudmesh/azure/vm/{id}'.format(id='id_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_start_virtual_machine_by_id(self):
        """Test case for start_virtual_machine_by_id

        
        """
        response = self.client.open(
            '/cloudmesh/azure/vm/start/{id}'.format(id='id_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_stop_virtual_machine_by_id(self):
        """Test case for stop_virtual_machine_by_id

        
        """
        response = self.client.open(
            '/cloudmesh/azure/vm/stop/{id}'.format(id='id_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
