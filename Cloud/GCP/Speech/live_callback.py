import sounddevice as sd
import requests
import base64
import json
import sys

fs = 48000
duration = 5 # seconds

#sd.default.device = 4
#sd.default.device = "The Sims 4 Headset"

def speech_to_text(recording):
	print("Processing ...")

	# your API key here
	API_KEY = "gcp_api_key"

	# defining the api-endpoint
	URL = "https://speech.googleapis.com/v1/speech:recognize" + "?key=" + API_KEY

	# Base64 encode the binary audio recording for inclusion in the JSON request
	speech_content = base64.b64encode(recording)

	# defining a params dict for the parameters to be sent to the API
	DATA = {
		"audio": {
			"content": speech_content
		},
		"config": {
			"enableAutomaticPunctuation": "true",
			"encoding": "LINEAR16", # optional for wav & flac
			"sampleRateHertz": fs,
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

	#print(output['results'][0]['alternatives'][0]['transcript'])

def callback(indata, frames, time, status):
	#print(frames)
	#print(time)
	if status:
		print(status)
	print("Playing back ...")
	with sd.RawOutputStream(channels=1, dtype='int16') as sdros:
		sdros.write(indata)
	speech_to_text(indata)

print("Please speak. Recording ...")
with sd.RawInputStream(samplerate=fs, blocksize=duration*fs, channels=1, dtype='int16', callback=callback):
	sd.sleep(int(duration * 1000))
