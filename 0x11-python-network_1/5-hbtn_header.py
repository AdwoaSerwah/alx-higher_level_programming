#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL,
and displays the 'X-Request-Id' value found in response header
"""
import requests
import sys

if __name__ == "__main__":
    sk_url = sys.argv[1]

    result = requests.get(sk_url)
    print(result.headers.get('X-Request-Id'))
