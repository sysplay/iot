import snowboydecoder
import sounddevice as sd
import requests
import base64
import json
import sys

fs = 48000
duration = 5 # seconds

#sd.default.device = 4
#sd.default.device = "The Sims 4 Headset"

def text_to_speech(text):
	# your API key here
	API_KEY = "AIzaSyBwU5q6m4XwrxGWsVT2EB9neUFlMaTHYQ8"

	# defining the api-endpoint
	URL = "https://texttospeech.googleapis.com/v1/text:synthesize" + "?key=" + API_KEY

	# defining a params dict for the parameters to be sent to the API
	DATA = {
	  'input':{
		'text': text
	  },
	  'voice':{
		'languageCode':'en-gb',
		'name':'en-US-Standard-D',
		'ssmlGender':'MALE'
	  },
	  'audioConfig':{
		'audioEncoding':'LINEAR16'
	  }
	}
	# sending post request and saving response as response object
	r = requests.post(url = URL, data = json.dumps(DATA))

	#print(r)

	# extracting data in json format
	output = r.json()

	#print(output)

	# Base64 decode into binary audio file
	return base64.b64decode(output['audioContent'])

def speech_to_text(recording):
	# your API key here
	API_KEY = "AIzaSyBwU5q6m4XwrxGWsVT2EB9neUFlMaTHYQ8"

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

	#print(r)

	# extracting data in json format
	output = r.json()

	#print(output)

	return output['results'][0]['alternatives'][0]['transcript']

def callback(indata, frames, time, status):
	#print(frames)
	#print(time)
	if status:
		print(status)
	#print("Playing back ...")
	print("Processing. Please wait ...")
	with sd.RawOutputStream(samplerate=16000, channels=1, dtype='int16') as sdros:
		sdros.write(text_to_speech("Processing. Please wait ..."))
		text = speech_to_text(indata)
		print("You said:", text)
		sdros.write(text_to_speech("You said " + text))
	print("Please say \"Smart Mirror\" to activate me.")

def detected_callback():
	print("Please speak. Recording ...")
	with sd.RawInputStream(samplerate=fs, blocksize=duration*fs, channels=1, dtype='int16', callback=callback):
		sd.sleep(int(duration * 1000))

print("Please say \"Smart Mirror\" to activate me.")
detector = snowboydecoder.HotwordDetector("smart_mirror.pmdl", sensitivity=0.5, audio_gain=1)
detector.start(detected_callback)