#!/usr/bin/python3
"""
This script takes a repository name and an owner name as arguments,
uses the GitHub API to list the 10 most recent commits of the repository
by the user, and prints the commit SHA and author name in the format
'<sha>: <author name>'.
"""
import requests
import sys

if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]

    sk_url = f'https://api.github.com/repos/{owner}/{repo}/commits'
    result = requests.get(sk_url)

    if result.status_code == 200:
        sk_commits = result.json()
        newest_commits = []

        for commit in sk_commits:
            if len(newest_commits) >= 10:
                break

            sha = commit.get('sha')
            author = commit.get('commit', {}).get('author', {}).get('name')

            if sha and author:
                newest_commits.append(f"{sha}: {author}")

        for commit in newest_commits:
            print(commit)
