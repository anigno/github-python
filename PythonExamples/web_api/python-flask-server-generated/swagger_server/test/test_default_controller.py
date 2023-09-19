# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_histogram_get(self):
        """Test case for histogram_get

        Get Histogram
        """
        response = self.client.open(
            '/histogram',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_passengers_get(self):
        """Test case for passengers_get

        Get All Passengers
        """
        response = self.client.open(
            '/passengers',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_passengers_id_get(self):
        """Test case for passengers_id_get

        Get Passenger Data by ID
        """
        query_string = [('attributes', 'attributes_example')]
        response = self.client.open(
            '/passengers/{id}'.format(id=789),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
