from WebClient import WebClient,WebDeviceEvent
from App.TrackerMqttClient import TrackerClient

from abc import ABC, abstractmethod
from Tracker import Tracker
from typing import Any, Callable, List, Optional, List

class Operator(ABC):
    def __init__(self, name: str = "NoNameOperator", trackers: List[str] = [], actuators: List[str] = []):
        self.name = name
        self.__trackers = trackers
        self.__actuators = actuators
        self.__tracker_client = TrackerClient()
        
    
        
    

    



