#!/usr/bin/env python3
"""TestGithubOrgClient class implementation"""

import unittest
from parameterized import parameterized
from unittest.mock import patch
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    
    @parameterized.expand([("google"), ("abc")])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        fake_dict = {"company": org_name}
        mock_get_json.return_value = fake_dict

        new_company = GithubOrgClient(org_name)
        new_comp_info = new_company.org()
        print(new_comp_info)
        mock_get_json.assert_called_once_with(new_company.ORG_URL)
