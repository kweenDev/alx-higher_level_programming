#!/bin/bash

# Send an OPTIONS request to the URL and display the Allow header containing accepted methods
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
