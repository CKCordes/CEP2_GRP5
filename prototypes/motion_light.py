import paho.mqtt.client as mqtt
import json

light_id = "led_strip"

def on_message(client, userdata, msg):
    print(f"topic = {msg.topic}, payload = {msg.payload.decode()}")
    json_msg = json.loads(msg.payload.decode())
    occupancy = json_msg["occupancy"]
    print(f"Occupancy parsed: {occupancy}")
    print(userdata)
    
    new_state = "ON" if occupancy else "OFF"
    client.publish(topic=f"zigbee2mqtt/{light_id}/set",
                              payload=json.dumps({"state": f"TOGGLE"}))
    print("Light changed")
    
  
client_sensor = mqtt.Client()
client_sensor.on_message = on_message
client_sensor.connect("localhost", 1883)
client_sensor.subscribe("zigbee2mqtt/stor_sensor")
client_sensor.loop_forever()
