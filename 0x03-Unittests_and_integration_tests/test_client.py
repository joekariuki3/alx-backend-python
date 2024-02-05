#!/usr/bin/env python3
"""TestGithubOrgClient class implementation"""

import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """implementation of unitTests on methods in GithubOrgClient class"""

    @parameterized.expand([("google"), ("abc")])
    @patch.object(GithubOrgClient, "org")
    def test_org(self, org_name, mock_org):
        """test implementation for org method"""
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

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """test the public repo method"""
    # Mocked payload for get_json
        mocked_payload = [
            {"name": "google", "license": {"key": "mit"}},
            {"name": "facebook", "license": {"key": "apache"}},
            {"name": "tesla", "license": {"key": "mit"}}
        ]
        with patch.object(GithubOrgClient,
                          '_public_repos_url',
                          new_callable=PropertyMock) as mock_public_repos_url:
            # Mocking the property and method
            url = "https://api.github.com/orgs/google/repos"
            mock_public_repos_url.return_value = url
            mock_get_json.return_value = mocked_payload

            # Initialize the GithubOrgClient
            github_client = GithubOrgClient("google")

            # Call the method being tested
            repos = github_client.public_repos(license="mit")

            # Assertions
            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with(url)
            self.assertEqual(repos, ["google", "tesla"])

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
        ])
    def test_has_license(self, repo, license_key, output):
        """test for has_license method for GithubOrgClient class"""
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, output)


@parameterized_class(('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'), [()])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """integration test for methods that sends external requests"""

    @classmethod
    @patch("requests.get")
    def setUpClass(cls, mock_request_get):
        """setup class"""
        mock_request_get.return_value = TEST_PAYLOAD
        payload = requests.get()

    @classmethod
    def tearDownClass(cls):
        """teardown class"""
        pass
