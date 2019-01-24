#/bin/bash

curl -H "Content-Type: application/json; charset=utf-8" \
	https://texttospeech.googleapis.com/v1/text:synthesize?key=gcp_api_key \
	-d @curl.json \
	| grep : | sed -e 's/^.*: "\(.*\)".*$/\1/g' | base64 -d - > curl.mp3
