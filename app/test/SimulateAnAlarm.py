from time import sleep

from paho.mqtt import publish, subscribe
import json

if __name__ == "__main__":
    
    z2m_power_plug_name ="test_stove_actuator"
    kitchen_sensor_name = "test_kitchen"

    publish.single(topic = "zigbee2mqtt/" + z2m_power_plug_name,
                       payload=json.dumps({"state": "ON"}))
    sleep(10)
    publish.single(topic = "zigbee2mqtt/" + kitchen_sensor_name,
                       payload=json.dumps({"occupancy": True}))
    sleep(5)
    publish.single(topic = "zigbee2mqtt/" + kitchen_sensor_name,
                       payload=json.dumps({"occupancy": False}))