#!/usr/bin/env python3
"""Tests for github org utils."""
import json
from unittest.mock import patch, Mock
import unittest

from utils import (
    access_nested_map,
    get_json,
    memoize,
)


class TestAccessNestedMap(unittest.TestCase):
    """Test access_nested_map."""

    def test_access_nested_map(self):
        """Test access_nested_map."""
        assert access_nested_map({"a": {"b": {"c": 1}}}, ["a", "b", "c"]) == 1
