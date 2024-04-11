from Operator import Operator
from typing import List
from time import time

# Tracker topics needed:
#   1. Room tracker
#   2. Stove tracker
# Assumptions for operating
#   1. The stove can only be turned on with the occupancy in the kitchen being true.
class KitchenGuardOperator(Operator):
    
    def initialize(self):
        self.log("Initializing KitchenGuardOperator")
        self.__room_tracker_name = self.__trackers[0]
        self.__stove_tracker_name = self.__trackers[1] 
        self.stove_active = False
        self.stove_time_turned_on = None
        self.last_time_in_kitchen = None
        self.alarming = False
        
        self.ALARM_TIME = 60 * 1
        self.TURN_OFF_TIME = 60 * 2

    
    def parse_message(self, tracker_name: str, message: str):
        if tracker_name == self.__stove_tracker_name:
            
            new_stove_state = message["StoveState"]
            
            if message["StoveState"] is None:
                self.log("Mistake in stove tracker data")
                return
            
            if self.stove_active == True and new_stove_state == "OFF":
                self.stove_active = False 
                self.alarming = False

            if self.stove_active == False and new_stove_state == "ON":
                self.stove_active = True
                self.stove_turned_on = time() 
                
            
        if tracker_name == self.__room_tracker_name:
            
            kitchen_occupancy = message["occupancy"]["kitchen"]
            if kitchen_occupancy is None:
                self.log(f"Mistake in room tracker data or parse message incorrectly")
                return
            
            if kitchen_occupancy is True:
                self.last_time_in_kitchen = time()
            
            pass
                
    def operate(self):
        
        if not self.stove_turned_on:
            return
        
        if (self.last_time_in_kitchen + self.ALARM_TIME) > time():
            self.alarming = True
            self.__alarm_resident()
        
        
        if self.alarming and (self.last_time_in_kitchen + self.TURN_OFF_TIME) > time():
            self.__turn_off_stove()
            
            
        
    def __alarm_resident(self):
        pass

    def __turn_off_stove(self):
        pass