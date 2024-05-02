from .HomeHelper.Operator import Operator
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
        self.stove_active = False
        self.resident_in_kitchen = False
        self.last_time_in_kitchen = None
        self.alarming = False
    
        self.ALARM_TIME = 60 * 0.5
        self.TURN_OFF_TIME = 60 * 1

        self.__room_tracker_name = self.trackers[0]
        self.__stove_tracker_name = self.trackers[1] 
    
    def disable(self):
        self.alarm_resident("OFF")
        
    # message: JSON
    def parse_message(self, tracker_name: str, json_message: any):
        if tracker_name == self.__stove_tracker_name:
            
            new_stove_state = json_message["StoveUse"]
            
            if json_message["StoveUse"] is None:
                self.log("Mistake in stove tracker data")
                return
            
            if self.stove_active == True and new_stove_state == "OFF":
                self.stove_active = False 
                self.alarming = False

            if self.stove_active == False and new_stove_state == "ON":
                self.stove_active = True
                self.stove_turned_on = time() 
                
            
        if tracker_name == self.__room_tracker_name:
            kitchen_occupancy = json_message["occupancy"]["kitchen"]
                               
            if kitchen_occupancy is None:
                self.log(f"Mistake in room tracker data or parse message incorrectly")
                return
            
            if kitchen_occupancy is True:
                self.last_time_in_kitchen = time()
                self.resident_in_kitchen = True
            else:
                self.resident_in_kitchen = False
                
    def operate(self):
        
        if self.last_time_in_kitchen is None:
            return
        
        if self.alarming and self.resident_in_kitchen:
            self.log("Turning off alarm")
            self.alarming = False
            self.alarm_resident("OFF")
            self.turn_stove("ON")
        
        if not self.stove_active:
            return
        
        if self.stove_active and (time() - self.last_time_in_kitchen) > self.ALARM_TIME:
            if not self.alarming:
                self.log("Turning on alarm")
                self.alarm_resident("ON")
            self.alarming = True
            
        
        
        if self.alarming and (time() - self.last_time_in_kitchen) > self.TURN_OFF_TIME:
            self.log("Turning off stove")
            self.turn_stove("OFF")
            

            
                    
    def alarm_resident(self, state):
        stove_plug_device = self.actuator_devices.get_type("led")[0]
        
        self.z2m_client.change_state(stove_plug_device.id_, state)
        

    def turn_stove(self, state):
        
        stove_plug_device = self.actuator_devices.get_type("power_plug")[0]
        
        self.z2m_client.change_state(stove_plug_device.id_,state)
        
       