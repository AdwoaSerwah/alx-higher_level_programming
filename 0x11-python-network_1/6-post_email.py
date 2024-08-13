#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL,
and displays the 'X-Request-Id' value found in response header
"""
import requests
import sys

if __name__ == "__main__":
    sk_url = sys.argv[1]
    email = {'email': sys.argv[2]}

    result = requests.post(sk_url, data=email)
    print(result.text)
