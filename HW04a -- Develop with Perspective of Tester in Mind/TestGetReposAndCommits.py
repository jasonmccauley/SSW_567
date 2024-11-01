import requests
import unittest
from GetReposAndCommits import get_repos_and_commits

class TestGetReposAndCommits(unittest.TestCase):
    def test_valid_user_with_repos(self):
        result = get_repos_and_commits("jasonmccauley")
        expected_result = ["Repo: SSW_345 Number of commits: 4"]
        self.assertEqual(result, expected_result)

    def test_user_not_found(self):
        result = get_repos_and_commits("lakldalkwpkpas")
        self.assertEqual(result, "User was not found")
    
    def test_user_with_no_repos(self):
        result = get_repos_and_commits("benwatson42")
        self.assertEqual(result, "User has no repos")

    def test_id_not_string(self):
        result = get_repos_and_commits(3303)
        self.assertEqual(result, "Id must be a string")

    def test_id_empty_string(self):
        result = get_repos_and_commits("      ")
        self.assertEqual(result, "Id cannot be an empty string")

if __name__ == "__main__":
    unittest.main()
    