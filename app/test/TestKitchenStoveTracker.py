from time import sleep
from Model import DevicesModel, ZigbeeDevice
from KitchenStoveTracker import KitchenStoveTracker
from paho.mqtt import publish, subscribe
import json

if __name__ == "__main__":
    
    z2m_power_plug_name ="test_stove_power"

    stove_devices_model = DevicesModel()
    stove_devices_model.add_devices([ZigbeeDevice(z2m_power_plug_name, "power plug", "kitchen")])

    stove_tracker = KitchenStoveTracker("test/StoveTracker", stove_devices_model)
    stove_tracker.start()

    while True:
        sleep(5)
        publish.single(topic = "zigbee2mqtt/" + z2m_power_plug_name,
                       payload=json.dumps({"state": "ON"}))

    stove_tracker.stop()
