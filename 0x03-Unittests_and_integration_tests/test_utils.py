#!/usr/bin/env python3
"""TestAccessNestedMap class"""

import unittest
from utils import access_nested_map
from typing import Sequence, Mapping, Any, Callable
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """test class for NestedMap in utils module"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(self, nested_map, path, output):
        """test case for output of access_nested_map"""
        self.assertEqual(access_nested_map(nested_map, path), output)

    @parameterized.expand([
        ({}, ("a")),
        ({"a", 1}, ("a", "b"))
        ])
    def test_access_nested_map_exception(self, nested_map, path):
        """test for KeyError exception"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)
