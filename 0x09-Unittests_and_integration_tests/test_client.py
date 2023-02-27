#!/usr/bin/env python3
"""test client"""
import unittest
from client import GithubOrgClient
from parameterized import parameterized
from unittest.mock import PropertyMock, patch


class TestGithubOrgClient(unittest.TestCase):
    """"""
    @parameterized.expand([
        ["google"],
        ["abc"],
    ])
