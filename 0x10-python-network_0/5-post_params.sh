#!/bin/bash
# Sends a POST request to the URL with email and subject variables
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
