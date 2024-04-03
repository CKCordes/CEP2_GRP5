from time import sleep
from Model import DevicesModel, ZigbeeDevice
from KitchenStoveTracker import KitchenStoveTracker
from paho.mqtt import publish, subscribe
import json

if __name__ == "__main__":

    stove_devices_model = DevicesModel()
    stove_devices_model.add_devices([ZigbeeDevice("test", "power plug", "kitchen")])

  
    stove_tracker = KitchenStoveTracker("Stove tracker", stove_devices_model)
    stove_tracker.start()

    while True:
        sleep(5)
        publish.single(topic = "zigbee2mqtt/test",
                       payload=json.dumps({"hello": "yes"}))

    stove_tracker.stop()
