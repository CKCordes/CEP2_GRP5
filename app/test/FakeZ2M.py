import json

from time import sleep
from time import time 
from paho.mqtt import publish, subscribe

MQTT_BROKER_HOST = "localhost"
MQTT_BROKER_PORT = 1883 

if __name__ == "__main__":
    print("Fake Zigbee2Mosquitto bridge")
    
    while True:
        message = subscribe.simple(hostname=MQTT_BROKER_HOST,
                                   port=MQTT_BROKER_PORT,
                                   topics="zigbee2mqtt/bridge/request/health_check",
                                   keepalive=10000)
        if message:
            publish.single(payload=json.dumps({"status": "ok"}),
                         hostname=MQTT_BROKER_HOST,
                         port=MQTT_BROKER_PORT,
                         topic="zigbee2mqtt/bridge/response/health_check")
            
            print("Have send a response")



    

