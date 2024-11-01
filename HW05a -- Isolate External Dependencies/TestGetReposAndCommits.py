import requests
import unittest
from unittest.mock import patch
from GetReposAndCommits import get_repos_and_commits

class TestGetReposAndCommits(unittest.TestCase):
    @patch("requests.get")
    def test_valid_user_with_repos(self, mock_get):
        mock_get.side_effect = [
            unittest.mock.Mock(status_code = 200, json = lambda: [
                {"name": "repo1"},
                {"name": "repo2"}
            ]),
            unittest.mock.Mock(status_code = 200, json = lambda: ["commit1", "commit2"]),
            unittest.mock.Mock(status_code = 200, json = lambda: ["commit1", "commit2", "commit3"])
        ]

        result = get_repos_and_commits("jasonmccauley")
        expected_result = ["Repo: repo1 Number of commits: 2", "Repo: repo2 Number of commits: 3"]
        self.assertEqual(result, expected_result)

    @patch("requests.get")
    def test_user_not_found(self, mock_get):
        mock_get.return_value = unittest.mock.Mock(status_code = 404)

        result = get_repos_and_commits("nonexistent_user")
        self.assertEqual(result, "User was not found")
    
    @patch("requests.get")
    def test_user_with_no_repos(self, mock_get):
        mock_get.return_value = unittest.mock.Mock(status_code = 200, json = lambda: [])

        result = get_repos_and_commits("no_repos_user")
        self.assertEqual(result, "User has no repos")

    def test_id_not_string(self):
        result = get_repos_and_commits(3303)
        self.assertEqual(result, "Id must be a string")

    def test_id_empty_string(self):
        result = get_repos_and_commits("      ")
        self.assertEqual(result, "Id cannot be an empty string")

if __name__ == "__main__":
    unittest.main()
    