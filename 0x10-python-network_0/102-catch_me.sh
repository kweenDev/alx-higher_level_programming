#!/bin/bash

# Makes a request to 0.0.0.0:5000/catch_me to get the server to respond with "You got me!" in the body

# Use curl to make a POST request to 0.0.0.0:5000/catch_me with a custom header
curl -sL -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
