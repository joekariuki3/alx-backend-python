#!/usr/bin/env python3
"""TestGithubOrgClient class implementation"""

import unittest
from parameterized import parameterized
from unittest.mock import patch
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):

    @parameterized.expand([("google"), ("abc")])
    @patch.object(GithubOrgClient, "org")
    def test_org(self, org_name, mock_org):
        url = f"https://api.github.com/orgs/{org_name}"
        fake_dict = {"company": org_name}
        mock_org.return_value = fake_dict

        new_company = GithubOrgClient(org_name)
        new_comp_info = new_company.org()
        mock_org.assert_called_once_with()
