#!/usr/bin/python3
"""
This script takes in a URL and an email, sends a POST request to the URL
with the email as a parameter, and displays the response body
"""
import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":
    sk_url = sys.argv[1]
    email = sys.argv[2]
 
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    with urllib.request.urlopen(sk_url, data) as response:
        print(response.read().decode('utf-8'))
