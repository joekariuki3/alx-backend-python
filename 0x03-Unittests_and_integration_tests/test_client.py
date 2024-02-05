#!/usr/bin/env python3
"""TestGithubOrgClient class implementation"""

import unittest
from parameterized import parameterized
from unittest.mock import patch, PropertyMock
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

    def test_public_repos_url(self):
        """test for property method public urls"""
        with patch.object(GithubOrgClient,
                          "_public_repos_url",
                          new_call=PropertyMock) as mock_public_urls:
            fake_url_list = "https://api.github.com/orgs/google/repos"
            mock_public_urls.return_value = fake_url_list

        new_company = GithubOrgClient("google")
        urls = new_company._public_repos_url
        self.assertEqual(urls, fake_url_list)
