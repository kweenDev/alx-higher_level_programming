#!/bin/bash

# Send a request to the URL and extract the status code from the response
curl -s -o /dev/null -w "%{http_code}" "$1"
