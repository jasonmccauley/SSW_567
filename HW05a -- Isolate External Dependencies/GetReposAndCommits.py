import requests
import json

def get_repos_and_commits(id):
    if(not isinstance(id, str)):
        return "Id must be a string"
    if(len(id.strip()) == 0):
        return "Id cannot be an empty string"

    github_url = "https://api.github.com/users/" + id + "/repos"
    response = requests.get(github_url)

    if(response.status_code == 404):
        return "User was not found"
    
    repos = response.json()

    if(len(repos) == 0):
        return "User has no repos"
    
    repo_and_commit_count = []
    for repo in repos:
        repo_name = repo["name"]
        commits_url = "https://api.github.com/repos/" + id + "/" + repo_name + "/commits"
        commits_response = requests.get(commits_url)
        commits = commits_response.json()
        commit_count = len(commits)
        repo_and_commit_count.append("Repo: " + repo_name + " Number of commits: " + str(commit_count))
    
    return repo_and_commit_count
