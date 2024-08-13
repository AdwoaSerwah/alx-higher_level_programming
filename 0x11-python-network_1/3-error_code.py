#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL and
displays the response body
"""
import urllib.request
import sys
import urllib.error

if __name__ == "__main__":
    sk_url = sys.argv[1]

    try:
        with urllib.request.urlopen(sk_url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.code))
