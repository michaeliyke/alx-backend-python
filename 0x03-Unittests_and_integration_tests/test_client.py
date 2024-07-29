#!/usr/bin/env python3
"""Tests for github org client."""
from unittest.mock import patch, Mock
import unittest
from parameterized import parameterized
from client import GithubOrgClient
from unittest.mock import patch, Mock
import unittest
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Testing GithubOrgClient."""

    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """Test GithubOrgClient.org returns the correct value"""
        test = GithubOrgClient(org_name)
        self.assertEqual(test.org["login"], "google")


class TestGithubOrgClient(unittest.TestCase):
    """Testing GithubOrgClient."""

    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """Test GithubOrgClient.org returns the correct value"""
        mock_response = {
            "login": org_name,
            "name": "Test Org",
            "description": "This is a test organization",
            "public_repos": 10,
        }

        mock_get_json.return_value = mock_response
        test = GithubOrgClient(org_name)
        self.assertEqual(test.org["login"], org_name)
