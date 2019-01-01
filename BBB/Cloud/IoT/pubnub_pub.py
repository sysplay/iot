# API Ref: https://www.pubnub.com/docs/mqtt-pubnub-bridge/getting-started

# importing the mqtt library
import paho.mqtt.client as mqtt
from iop import *
import json
import time

# API key here
PUB_KEY = "pubnub_pub_key"
SUB_KEY = "pubnub_sub_key"
SEC_KEY = "pubnub_sec_key"
CLIENT_ID = "sbc-bbb"

# defining the api-endpoint
URL = "mqtt.pndsn.com"

# defining a params dict for the parameters to be sent to the API
DATA = {
	"value": "unknown",
	"sensor": "unknown",
	"device": CLIENT_ID
}

client = mqtt.Client(client_id = PUB_KEY + "/" + SUB_KEY + "/" + CLIENT_ID)
client.connect(URL, 1883, 60)
while 1:
	time.sleep(1)
	av = analog_read(0)
	if av < 2047:
		continue
	DATA["sensor"] = "AIN0"
	DATA["value"] = av
	client.publish("msg", json.dumps(DATA))
