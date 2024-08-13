#!/usr/bin/python3
"""
This script takes in a letter, sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""
import requests
import sys

if __name__ == "__main__":
    sk_url = "http://0.0.0.0:5000/search_user"

    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""

    data = {'q': q}
    result = requests.post(sk_url, data=data)

    try:
        json_result = result.json()
        if json_result:
            print("[{}] {}".format(
                json_result.get('id'), json_result.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
