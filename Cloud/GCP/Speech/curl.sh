#/bin/bash

curl -s -H "Content-Type: application/json" \
	https://speech.googleapis.com/v1/speech:recognize?key=gcp_api_key \
	-d @curl.json
