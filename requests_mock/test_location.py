import json
import unittest
import unittest.mock
import requests

import location


class MockResponse:

    def __init__(self, text, status_code):
        self.text = text
        self.status_code = status_code

    def json(self):
        return json.loads(self.text)

    def __iter__(self):
        return self

    def __next__(self):
        return self


def mock_requests_get_success(*args, **kwargs):
    text = """
    {"status":"success",
     "data":{
         "ipv4":"50.225.254.26",
         "continent_name":"North America",
         "country_name":"United States",
         "subdivision_1_name":null,
         "subdivision_2_name":null,
         "city_name":null,
         "latitude":"37.75100",
         "longitude":"-97.82200"
    }}
    """
    response = MockResponse(text, 200)
    return response

def mock_requests_get_error(*args, **kwargs):
    response = MockResponse("", 500)
    return response


class TestLocation(unittest.TestCase):

    @unittest.mock.patch('requests.get', mock_requests_get_success)
    def test_get_location(self):
        longitude, latitude = location.get_location()
        self.assertEqual("-97.82200", longitude)
        self.assertEqual("37.75100", latitude)

    @unittest.mock.patch('requests.get', mock_requests_get_error)
    def test_get_location_error(self):
        with self.assertRaises(Exception):
            location.get_location()
