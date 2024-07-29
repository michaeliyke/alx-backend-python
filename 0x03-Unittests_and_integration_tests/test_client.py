#!/usr/bin/env python3
"""Tests for github org client."""
import json
from unittest.mock import patch, Mock
import unittest
from parameterized import parameterized

from client import GithubOrgClient
from utils import memoize
