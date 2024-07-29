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


class TestAccessNestedMap(unittest.TestCase):
    """Testing access_nested_map."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
        # ({"a": {"b": {"c": 1}}}, ("a", "b", "c"), 1),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map returns the right value."""
        self.assertEqual(access_nested_map(nested_map, path), expected)
