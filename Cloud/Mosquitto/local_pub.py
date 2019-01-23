# API Ref: https://www.pubnub.com/docs/mqtt-pubnub-bridge/getting-started

# importing the mqtt library
import paho.mqtt.client as mqtt
import json

# Client ID
CLIENT_ID = "pc-sysplay"

# defining the api-endpoint
URL = "localhost"

# defining a params dict for the parameters to be sent to the API
DATA = {
	"value": "on",
	"arg": "0",
	"cmd": "led",
	"device": "pc"
}

client = mqtt.Client(client_id = CLIENT_ID)
client.connect(URL, 1883, 60)
client.publish("msg", json.dumps(DATA))
