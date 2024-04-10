from Model import DevicesModel
from TrackerMqttClient import TrackerClient
from Zigbee2mqttClient import (Zigbee2mqttClient,
                                   Zigbee2mqttMessage, Zigbee2mqttMessageType)
from abc import ABC, abstractmethod
from threading import Event, Thread
from time import sleep
from typing import List

class Operator(ABC):
    def __init__(self, 
                 name: str = "NoNameOperator", 
                 actuators: DevicesModel = DevicesModel(), 
                 tracker_topics: List[str] = [] ):
        
        self.name = name
        self.devices_model = actuators 
        self.__trackers = tracker_topics
        self.__tracker_client = TrackerClient(on_message_clbk = self.__message_received,
                                              topics          = tracker_topics,
                                              serving         = self.name)
        
        self.__z2m_client = Zigbee2mqttClient(on_message_clbk = None,
                                              topics          = [],
                                              serving         = self.name)
                                              
        
    def __message_received(self, trackername: str, message: str) -> None:
        if trackername in self.__trackers:
            self.log(f"message received: [{trackername}] {message} ")
            self.parse_message(trackername, message)
        else:
            self.log(f"event from unknown tracker : [{trackername}] {message} ")
            pass
        
    def log(self, string: str):
        print(f"{self.name} : {string}"  )
    
    def start(self) -> None:
        self.__z2m_client.connect()
        
        z2m_health = self.__z2m_client.check_health()
        if z2m_health != "ok":
            self.log("Zigbee2MqttClient - health check BAD")
            ##self.__z2m_client.disconnect() # giver fejl som kommer helt inde i koden.
            return
            
        self.log(f"Zigbee2MqttClient is OK - Operationg ready")
        
        self.__tracker_client.connect()
        
        self.initialize()
        
    
    def stop(self) -> None:
        self.__z2m_client.disconnect()
    
    @abstractmethod
    def parse_message(self, tracker_name: str, message: str):
        pass
    
    @abstractmethod
    def initialize(self):
        pass