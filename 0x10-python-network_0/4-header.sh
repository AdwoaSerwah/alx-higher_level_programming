#!/bin/bash
# Sends a GET request to the URL with a header variable X-School-User-Id set to 98
curl -sH "X-School-User-Id: 98" "$1"
