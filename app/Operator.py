from Model import DevicesModel
from Zigbee2mqttClient import (Zigbee2mqttClient,
                                   Zigbee2mqttMessage, Zigbee2mqttMessageType)
from abc import ABC, abstractmethod
from threading import Event, Thread
from time import sleep
from typing import List

class Operator(ABC):
    def __init__(self, name: str = "NoNameOperator", actuators: DevicesModel = DevicesModel(), tracker_topics: List[str] = [] ):
        self.name = name
        self.__devices_model = actuators 
        self.__z2m_client = Zigbee2mqttClient(on_message_clbk = self.__event_received,
                                              topics          = self.__devices_model.all_devices_as_topics(),
                                              serving         = name)
        self.__stop_sending_thread = Event()
        
    
    
    

    



