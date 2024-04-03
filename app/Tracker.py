from Model import DevicesModel
from WebClient import WebClient,WebDeviceEvent
from Zigbee2mqttClient import (Zigbee2mqttClient,
                                   Zigbee2mqttMessage, Zigbee2mqttMessageType)
from abc import ABC, abstractmethod

# The trakcer will recieve data from zigbee
# The devives it recieves are only appropriote for its behavior.

class Tracker(ABC):
    
    def __init__(self, name: str = "NoName", devices: DevicesModel = DevicesModel()):
        self.name = name
        self.__devices_model = devices
        self.__z2m_client = Zigbee2mqttClient(on_message_clbk = self.__event_received,
                                              topics          = self.__devices_model.all_devices_as_topics(),
                                              serving         = name)
        

    def __event_received(self, message: Zigbee2mqttMessage) -> None:

        # If message is None (it wasn't parsed correcty in the Z2Mclient), then don't do anything.
        
        if not message:
            return

        if message.type_ != Zigbee2mqttMessageType.DEVICE_EVENT:
            return
        
        topics_tokens = message.topic.split("/")
        if len(topics_tokens) <= 1:
            return

        # Retrieve the device ID from the topic.
        device_id = topics_tokens[1]

        # If the device ID is known, in the devices model, then we want to use its data, because it is relevant for the tracker.
        device = self.__devices_model.find(device_id)

        # If the message is not a device event, then don't do anything.

        if device:
            self.__log(f"event received on topic : [{message.topic}] {message.data} ' ")
  
            self.__parse_event(message)
        else:
            self.__log(f"event from unknown device : [{message.topic}] {message.data} ' ")
            pass
    
    def __log(self, *values: object):
        print(f"{self.name} | " + values)
            
    def start(self) -> None:
        self.__z2m_client.connect()
        
        z2m_health = self.__z2m_client.check_health()
        if z2m_health != "ok":
            self.__log("Zigbee2MqttClient mistake")
            ##self.__z2m_client.disconnect() # giver fejl som kommer helt inde i koden.
            return
            
        print(f"{self.name} : Zigbee2MqttClient is OK : Starting Tracking")
        self.initialize()
        
    
    def stop(self) -> None:
        self.__z2m_client.disconnect()
    
    @abstractmethod
    def __parse_event(self, message: Zigbee2mqttMessage):
        pass
    
    @abstractmethod
    def initialize(self):
        pass