#!/usr/bin/env python3
"""Tests for github org utils."""
import json
from unittest.mock import patch, Mock
import unittest
from parameterized import parameterized

from utils import (
    access_nested_map,
    get_json,
    memoize,
)


class TestMemoize(unittest.TestCase):
    """Testing memoize."""

    def test_memoize(self):
        """Test memoize returns the right value."""
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as mocked_fn:
            test = TestClass()
            result1 = test.a_property
            result2 = test.a_property

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
            mocked_fn.assert_called_once()


class TestGetJson(unittest.TestCase):
    """Testing get_json."""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch("utils.requests")
    def test_get_json(self, url, expected, mock_requests):
        """Test get_json returns the right value.
        NOTE:
        mock_requests: comes from the patch decorator utils.requests import
        """
        mock_response = Mock()
        mock_requests.get.return_value = mock_response
        mock_response.json.return_value = expected

        self.assertEqual(get_json(url), expected)


class TestAccessNestedMap(unittest.TestCase):
    """Testing access_nested_map."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map returns the right value."""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("b",), None),
        ({"a": 1}, ("a", "b"), None),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """Test access_nested_map raises a KeyError for invalid path.
        Use None as expected value since the function should raise an exception
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)
