#!/usr/bin/env python3
"""TestAccessNestedMap class"""

import unittest
from utils import access_nested_map, get_json
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


class TestGetJson(unittest.TestCase):
    """TestGetJson class implementation"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
        ])
    def test_get_json(self, test_url, test_payload):
        """test get json call using mock using the request.get
        method"""
        with unittest.mock.patch("requests.get") as mget:
            # asign return value as json cause get_json uses json()
            # then on json() assign now the real data test_payload
            mget.return_value.json.return_value = test_payload
            # call get_json
            response = get_json(test_url)
            # make sure get_json was clalled with test_url
            mget.assert_called_once_with(test_url)
            # assert the call result and our expected result
            self.assertEqual(response, test_payload)
