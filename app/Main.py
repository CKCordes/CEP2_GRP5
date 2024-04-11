from time import sleep
from Model import DevicesModel, ZigbeeDevice
from KitchenStoveTracker import KitchenStoveTracker
from RoomTracker import RoomTracker
from KitchenGuardOperator import KitchenGuardOperator
from paho.mqtt import publish, subscribe
import json

if __name__ == "__main__":
    # Room tracker
    room_motion_sensors = DevicesModel([ZigbeeDevice("test_kitchen", "pir", "kitchen"),
                                        ZigbeeDevice("test_room", "pir", "livingroom"),
                                        ZigbeeDevice("test_bath", "pir", "bathroom"),])
    room_tracker = RoomTracker("Room_Tracker", room_motion_sensors)
    
    # Stove tracker
    stove_actuator = ZigbeeDevice("test_Stove_Actuator", "power_plug", "kitchen")
    stove_power_model = DevicesModel(stove_actuator)
    stove_tracker = KitchenStoveTracker("Stove_Tracker", stove_power_model) 
    
    
    # Kitchen guard operator
    kitchen_guard_operator = KitchenGuardOperator("KitchenGuard", 
                                                   stove_power_model, 
                                                   [room_tracker.name, stove_tracker.name])
    
    # Start the program
    room_tracker.start()
    stove_tracker.start()
    kitchen_guard_operator.start()
    

    while True:
        sleep(5)

    room_tracker.stop()
    stove_tracker.stop()
    kitchen_guard_operator.stop()
