#!/bin/bash
# Sends a JSON POST request to the URL with contents of a file as request body
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
