#/bin/bash

curl -H "Content-Type: application/json; charset=utf-8" \
	https://texttospeech.googleapis.com/v1/text:synthesize?key=AIzaSyBwU5q6m4XwrxGWsVT2EB9neUFlMaTHYQ8 \
	-d @curl.json \
	| grep : | sed -e 's/^.*: "\(.*\)".*$/\1/g' | base64 -d - > curl.mp3
