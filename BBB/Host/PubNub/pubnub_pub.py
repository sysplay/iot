# API Ref: https://www.pubnub.com/docs/mqtt-pubnub-bridge/getting-started

# importing the mqtt library
import paho.mqtt.client as mqtt
import json

# API key here
PUB_KEY = "pubnub_pub_key"
SUB_KEY = "pubnub_sub_key"
SEC_KEY = "pubnub_sec_key"
CLIENT_ID = "pc-sysplay"

# defining the api-endpoint
URL = "mqtt.pndsn.com"

# defining a params dict for the parameters to be sent to the API
DATA = {
	"value": "on",
	"arg": "0",
	"cmd": "led",
	"device": "pc"
}

client = mqtt.Client(client_id = PUB_KEY + "/" + SUB_KEY + "/" + CLIENT_ID)
client.connect(URL, 1883, 60)
client.publish("msg", json.dumps(DATA))
