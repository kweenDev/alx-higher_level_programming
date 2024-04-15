#!/bin/bash
# Send a request to the URL and capture the response body size in bytes
curl -s "$1" | wc -c
