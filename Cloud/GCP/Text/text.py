# API Ref: https://cloud.google.com/text-to-speech/docs/basics

# importing the requests library
import requests
import base64
import json
import sys

if len(sys.argv) != 2:
	print("Usage: %s <audio_file>" % (sys.argv[0]))
	exit(1)

# file given here
audio_file = sys.argv[1]

# your API key here
API_KEY = "gcp_api_key"

# defining the api-endpoint
URL = "https://texttospeech.googleapis.com/v1/text:synthesize" + "?key=" + API_KEY

# defining a params dict for the parameters to be sent to the API
DATA = {
  'input':{
    'text':'I\'ve added the event to your calendar.'
  },
  'voice':{
    'languageCode':'en-gb',
    'name':'en-GB-Standard-A',
    'ssmlGender':'FEMALE'
  },
  'audioConfig':{
    'audioEncoding':'MP3'
  }
}
# sending post request and saving response as response object
r = requests.post(url = URL, data = json.dumps(DATA))

print(r)

# extracting data in json format
output = r.json()

print(output)

with open(audio_file, "wb") as audio:
	# Base64 decode into binary audio file
	audio.write(base64.b64decode(output['audioContent']))
