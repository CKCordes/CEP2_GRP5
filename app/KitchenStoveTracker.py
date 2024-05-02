from .HomeHelper.Tracker import Tracker
from .HomeHelper.Zigbee2mqttClient import Zigbee2mqttMessage

import json

class KitchenStoveTracker(Tracker):
    """
    Requires ONE power plug actuator of the stove 
    
    Tracking message format: {"StoveUse" : "ON" | "OFF"}
    """    
    
    def initialize(self):
        self.log(f"Initializeing kicken tracker")
        
        self.__stove_usage = "OFF"
        
    def parse_event(self, message: Zigbee2mqttMessage):
        power = 0
        try:
            power = message.data["power"]
        except:
            self.log("no power in message ")
            return
            
        if power < 4:
            self.__stove_usage = "OFF"
        else:
            self.__stove_usage = "ON"
        
        
    def tracking_message(self) -> str:
        return json.dumps({"StoveUse": self.__stove_usage})
        
        
        