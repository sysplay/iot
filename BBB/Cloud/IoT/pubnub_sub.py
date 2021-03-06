# API Ref: https://www.pubnub.com/docs/mqtt-pubnub-bridge/getting-started

# importing the mqtt library
import paho.mqtt.client as mqtt
import json
import sys
import time
from iop import *

# API key here
PUB_KEY = "pubnub_pub_key"
SUB_KEY = "pubnub_sub_key"
SEC_KEY = "pubnub_sec_key"
CLIENT_ID = "sbc-bbb"

# defining the api-endpoint
URL = "mqtt.pndsn.com"

def on_message(client, userdata, msg):
	print("message received =", str(msg.payload.decode("utf-8")))
	#print("message received =", str(msg.payload))
	print("message topic =", msg.topic)
	print("message qos =", msg.qos)
	print("message retain flag =", msg.retain)
	data = json.loads(msg.payload.decode("utf-8"))
	#print(data)

client = mqtt.Client(client_id = PUB_KEY + "/" + SUB_KEY + "/" + CLIENT_ID)
client.connect(URL, 1883, 60)
client.on_message = on_message
#client.loop_start()
client.subscribe("msg")
#time.sleep(4)
#client.loop_stop()
client.loop_forever()
