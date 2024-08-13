#!/usr/bin/python3
"""
This script takes GitHub credentials and uses
the GitHub API to display the user's ID.
"""
import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    sk_url = 'https://api.github.com/user'

    result = requests.get(sk_url, auth=(username, password))

    if result.status_code == 200:
        user_sk_info = result.json()
        print(user_sk_info.get('id'))
    else:
        print(None)
