from time import sleep

from paho.mqtt import publish, subscribe
import json

if __name__ == "__main__":
    
    client_test_sensor = "test_client_sensor"

    while True: 
        sleep(5)
        publish.single(topic = "zigbee2mqtt/" + client_test_sensor,
                       payload=json.dumps({"occupancy": True}))