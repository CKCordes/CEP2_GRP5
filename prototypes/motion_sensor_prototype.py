import paho.mqtt.client as mqtt
import json

def on_message(client, userdata, msg):
    #print(f"topic = {msg.topic}, payload = {msg.payload.decode()}")
    json_msg = json.loads(msg.payload.decode())
    occupancy = json_msg["occupancy"]
    print(f"Occupancy parsed: {occupancy}")
    
client = mqtt.Client()
client.on_message = on_message
client.connect("localhost", 1883)
client.subscribe("zigbee2mqtt/grp5 rigtig sensor")
client.loop_forever()