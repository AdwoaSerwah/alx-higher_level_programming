#!/usr/bin/python3
# This script fetches https://alx-intranet.hbtn.io/status
import urllib.request

the_url = "https://alx-intranet.hbtn.io/status"
with urllib.request.urlopen(the_url) as response:
    response_body = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(response_body)))
    print("\t- content: {}".format(response_body))
    print("\t- utf8 content: {}".format(response_body.decode('utf-8')))
