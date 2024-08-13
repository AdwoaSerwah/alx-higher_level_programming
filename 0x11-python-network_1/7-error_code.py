#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL,
and displays the response body
"""
import requests
import sys

if __name__ == "__main__":
    sk_url = sys.argv[1]
    result = requests.get(sk_url)

    if result.status_code >= 400:
        print('Error code: {}'.format(result.status_code))
    else:
        print(result.text)
