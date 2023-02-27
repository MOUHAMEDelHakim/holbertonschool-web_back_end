

#!/usr/bin/env python3
"""Test utils"""
import unittest
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized
from typing import Mapping, Sequence
from unittest import mock
from unittest.mock import patch


class TestAccessNestedMap(unittest.TestCase):
    """test accessnestedmap"""
    @parameterized.expand([
        ({"a": 1}, ["a"], 1),
        ({"a": {"b": 2}}, ["a"], {"b": 2}),
        ({"a": {"b": 2}}, ["a", "b"], 2),
    ])
    def test_access_nested_map(self, nested_map:
                               Mapping, path: Sequence,
                               expected):
        """method to test that access_nested_map method
        returns what it is supposed to."""
        self.assertEqual(access_nested_map(nested_map, path), expected)
    def test_access_nested_map_exception(self, nested_map:
                                         Mapping, path: Sequence,
                                         expected):

        """test that a KeyError is raised"""
        with self.assertRaises(KeyError) as raises:
            access_nested_map(nested_map, path)
class TestGetJson(unittest.TestCase):
    """test get_json"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url, payload):
        """method that tests if utils.get_json
        returns the expected result."""
        response = mock.Mock()
        response.json.return_value = payload

        with mock.patch('requests.get', return_value=response):
            request = get_json(url)
            self.assertEqual(request, payload)
            response.json.assert_called_once()
    