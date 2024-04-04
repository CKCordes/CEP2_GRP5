from Tracker import Tracker
from Zigbee2mqttClient import Zigbee2mqttMessage
from enum import Enum
import json

class KitchenStoveTracker(Tracker):
    """
    Requires ONE power plug actuator of the stove 
    
    Tracking message format: {"StoveState" : "ON" | "OFF"}
    """    
    
    def initialize(self):
        self.log(f"Initializeing kicken tracker")
        
        self.__stove_power = "OFF"
        
    def parse_event(self, message: Zigbee2mqttMessage):
        
        self.__stove_power = message.data["state"]
        
    def tracking_message(self) -> str:
        return json.dumps({"StoveState": self.__stove_power})
        
        
        
        
        
        
        