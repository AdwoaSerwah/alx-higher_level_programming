#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL,
and displays 'X-Request-Id' value from the response header.
"""
import urllib.request
import sys

if __name__ == "__main__":
    sk_url = sys.argv[1]
    with urllib.request.urlopen(sk_url) as response:
        print(response.headers.get('X-Request-Id'))
