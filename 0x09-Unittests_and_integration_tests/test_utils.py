

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

