from Tracker import Tracker
from Zigbee2mqttClient import Zigbee2mqttMessage
from enum import Enum

class KitchenStoveTracker(Tracker):
    
    
    def initialize(self):
        self.__log(f"{self.name} : Initializeing kicken tracker")
        
        self.__stove_power = "OFF"
        
    
    def __parse_event(self, message: Zigbee2mqttMessage):
        
        self.__stove_power = message.data["state"]
        
        
        
        
        
        
        
        
        