#!/bin/bash
# Script to make a request to 0.0.0.0:5000/catch_me and capture "You got me!" response

# Send a PUT request with custom header and body
curl -s -X PUT -L -d "user_id=98" 0.0.0.0:5000/catch_me
