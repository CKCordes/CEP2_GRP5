from Operator import Operator
from typing import List


# Tracker topics needed:
#   1. Room tracker
#   2. Stove tracker
class KitchenGuardOperator(Operator):
    def initialize(self):
        self.log("Initializing KitchenGuardOperator")
        self.__room_tracker_name = self.__trackers[0]
        self.__stove_tracker_name = self.__trackers[1] 
        self.stove_active = False
        self.last_in_kitchen = None

    
    def parse_message(self, tracker_name: str, message: str):
        if tracker_name == self.__stove_tracker_name:
            self.stove_active = True if message["StoveState"] == "ON" else False 
            
        if tracker_name == self.__room_tracker_name:
            pass
        
        
        
