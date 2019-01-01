# importing the requests library
import requests
import json

# your API key here
API_KEY = "gcp_api_key"

# defining the api-endpoint
URL = "https://speech.googleapis.com/v1/speech:recognize" + "?key=" + API_KEY

# defining a params dict for the parameters to be sent to the API
DATA = {
	"audio": {
		"uri": "gs://cloud-samples-tests/speech/brooklyn.flac"
	},
	"config": {
		"encoding": "FLAC",
		"sampleRateHertz": 16000,
		"languageCode": "en-US",
		"enableWordTimeOffsets": "false"
	}
}

# sending post request and saving response as response object
r = requests.post(url = URL, data = json.dumps(DATA))

print(r)

# extracting data in json format
output = r.json()

print(output)
