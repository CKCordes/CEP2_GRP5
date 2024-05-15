from time import sleep

from paho.mqtt import publish, subscribe
import json

if __name__ == "__main__":
    
    z2m_power_plug_name ="power_plug"
    kitchen_sensor_name = "pir"
    sleep(2)
    publish.single(topic=f"zigbee2mqtt/led_strip/set",
                              payload=json.dumps({"state": "ON"}))
    sleep(2)
    publish.single(topic=f"zigbee2mqtt/led_strip/set",
                              payload=json.dumps({"state": "OFF"}))
    sleep(2)
    publish.single(topic = "zigbee2mqtt/" + kitchen_sensor_name,
                       payload=json.dumps({"occupancy": True}))
    sleep(10)
    publish.single(topic = "zigbee2mqtt/" + z2m_power_plug_name,
                       payload=json.dumps({"power": 10, "state": "ON"}))
    sleep(5)
    publish.single(topic = "zigbee2mqtt/" + kitchen_sensor_name,
                       payload=json.dumps({"occupancy": False}))