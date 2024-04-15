#!/bin/bash
# Send a JSON POST request with the file content as the body and display the body of the response
curl -sX POST -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
