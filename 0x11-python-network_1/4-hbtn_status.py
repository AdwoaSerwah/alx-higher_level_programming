#!/usr/bin/python3
"""
This script fetches https://alx-intranet.hbtn.io/status
"""
import requests

if __name__ == "__main__":
    sk_url = "https://alx-intranet.hbtn.io/status"

    response_body = requests.get(sk_url)
    print("Body response:")
    print("\t- type: {}".format(type(response_body.text)))
    print("\t- content: {}".format(response_body.text))
