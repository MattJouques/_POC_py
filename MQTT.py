# !/usr/bin/python

import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, rc):
    print("Connected with result code "+str(rc))
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    #client.subscribe("$SYS/#")
    client.subscribe("HiveNet")
    client.subscribe("testclient1/Status")
    client.subscribe("testclient1/Command")
    client.subscribe("testclient1/Location")
    client.subscribe("testclient1/Distance")
    client.subscribe("testclient2/Status")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    #print(msg.topic+" "+str(msg.payload))
    msgTopic = [x.strip() for x in msg.topic.split("/")]
    msgClientId = msgTopic[0]
    msgType = msgTopic[1]
    msgContent = str(msg.payload)
    if msgType == "HiveNet":
        print("Registration request from %s" % (msgClientId))
    elif msgType == "Status":
        print("Status request from %s: %s" % (msgClientId, msgContent))
    else:
        print("%s message from %s: %s" % (msgType, msgClientId, msgContent))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("10.1.0.10", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()