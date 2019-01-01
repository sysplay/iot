# API Ref: https://cloud.google.com/speech-to-text/docs/basics

# importing the requests library
import sys
import requests
import base64
import json

if len(sys.argv) != 2:
	print("Usage: %s <audio_file>" % (sys.argv[0]))
	exit(1)

# file given here
speech_file = sys.argv[1]

# your API key here
API_KEY = "gcp_api_key"

# defining the api-endpoint
URL = "https://speech.googleapis.com/v1/speech:recognize" + "?key=" + API_KEY

with open(speech_file, "rb") as speech:
	# Base64 encode the binary audio file for inclusion in the JSON request
	speech_content = base64.b64encode(speech.read())

# defining a params dict for the parameters to be sent to the API
DATA = {
	"audio": {
		"content": speech_content
	},
	"config": {
		"enableAutomaticPunctuation": "true",
		"encoding": "LINEAR16", # optional for wav & flac
		"sampleRateHertz": 48000, # works w/o it
		"languageCode": "en-IN",
		"enableWordTimeOffsets": "true", # word time offsets
		"model": "default"
	}
}

# sending post request and saving response as response object
r = requests.post(url = URL, data = json.dumps(DATA))

print(r)

# extracting data in json format
output = r.json()

print(output)
