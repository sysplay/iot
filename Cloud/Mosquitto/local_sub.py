# API Ref: https://www.pubnub.com/docs/mqtt-pubnub-bridge/getting-started

# importing the mqtt library
import paho.mqtt.client as mqtt
import sys
import time

# Client ID
CLIENT_ID = "lt-sysplay"

# defining the api-endpoint
URL = "localhost"

def on_message(client, userdata, msg):
	print("message received ", str(msg.payload.decode("utf-8")))
	#print("message received ", str(msg.payload))
	print("message topic =", msg.topic)
	print("message qos =", msg.qos)
	print("message retain flag =", msg.retain)

client = mqtt.Client(client_id = CLIENT_ID)
client.connect(URL, 1883, 60)
client.on_message = on_message
#client.loop_start()
client.subscribe("msg")
#time.sleep(4)
#client.loop_stop()
client.loop_forever()
