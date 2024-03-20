from Model import DevicesModel
from WebClient import WebClient,WebDeviceEvent
from Zigbee2mqttClient import (Zigbee2mqttClient,
                                   Zigbee2mqttMessage, Zigbee2mqttMessageType)
from abc import ABC, abstractmethod
from Tracker import Tracker
from typing import Any, Callable, List, Optional, List

def Operator(ABC):
    def __init__(self, name: str = "NoName", trackers: List[str] = []):
        self.name = name

    



