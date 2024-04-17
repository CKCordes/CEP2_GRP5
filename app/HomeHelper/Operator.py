from .Model import DevicesModel
from .TrackerMqttClient import TrackerClient
from .Zigbee2mqttClient import (Zigbee2mqttClient,
                                   Zigbee2mqttMessage, Zigbee2mqttMessageType)
from abc import ABC, abstractmethod
from threading import Event, Thread
from time import sleep
from typing import List
import json
import time

class Operator(ABC):
    def __init__(self, 
                 name: str = "NoNameOperator", 
                 actuators: DevicesModel = DevicesModel(), 
                 tracker_topics: List[str] = [] ):
        
        self.name = name
        self.actuator_devices = actuators 
        self.trackers = tracker_topics
        self.__tracker_client = TrackerClient(on_message_clbk = self.__message_received,
                                              topics          = self.trackers,
                                              serving         = self.name)
        
        # entirely for actuators
        self.z2m_client = Zigbee2mqttClient(on_message_clbk = None,
                                              topics          = [],
                                              serving         = self.name)
                                              
        self.__stop_operating_thread = Event()
        self.__operating_thread = Thread(target=self.__opearate_worker,
                                       daemon=True)
        
    def __message_received(self, trackername: str, message: str) -> None:
        
        if trackername in self.trackers:
            self.log(f"message received: [{trackername}] {message} ")
            json_message = json.loads(message)
            self.parse_message(trackername, json_message)
        else:
            self.log(f"event from unknown tracker : [{trackername}] {message} ")
            pass
        
    def log(self, string: str):
        now = time.strftime('%X')
        print(f"[{now}] {self.name} : {string}"  )
    
    def start(self) -> None:
        self.z2m_client.connect()
        
        z2m_health = self.z2m_client.check_health()
        if z2m_health != "ok":
            self.log("Zigbee2MqttClient - health check BAD")
            ##self.z2m_client.disconnect() # giver fejl som kommer helt inde i koden.
            return
            
        self.log(f"Zigbee2MqttClient is OK - Operationg ready")
        
        self.__tracker_client.connect()
        
        self.initialize()
        self.__operating_thread.start()
        
    
    def stop(self) -> None:
        self.z2m_client.disconnect()
        self.__stop_operating_thread.set()
    
    @abstractmethod
    def parse_message(self, tracker_name: str, message: str):
        pass
    
    @abstractmethod
    def initialize(self):
        pass
    
    @abstractmethod
    def operate(self):
        pass
    
    def __opearate_worker(self) -> None:
        while not self.__stop_operating_thread.is_set():
            sleep(5)
            self.operate()