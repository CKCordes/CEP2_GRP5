from ..HomeHelper.Model import DevicesModel, ZigbeeDevice, LEDstrip, Patient
from ..HomeHelper.WebClient import WebClient
from ..KitchenStoveTracker import KitchenStoveTracker
from ..RoomTracker import RoomTracker
from ..KitchenGuardOperator import KitchenGuardOperator
from paho.mqtt import publish, subscribe
from time import sleep
import json

if __name__ == "__main__":
    
    patient = Patient("test_patient")
    
    # Room tracker
    room_motion_sensors = DevicesModel([ZigbeeDevice("test_kitchen", "pir", "kitchen"),
                                        ZigbeeDevice("test_room", "pir", "livingroom"),
                                        ZigbeeDevice("test_bath", "pir", "bathroom"),])
    room_tracker = RoomTracker("Room_Tracker", room_motion_sensors)
    
    # Stove tracker
    stove_actuator = ZigbeeDevice("test_stove_actuator", "power_plug", "kitchen")
    stove_power_model = DevicesModel(stove_actuator)
    stove_tracker = KitchenStoveTracker("Stove_Tracker", stove_power_model) 
    
    # Kitchen guard operator
    lights = LEDstrip("test_lights", "led", "livingroom")
    kitchenguard_devices = stove_power_model
    kitchenguard_devices.add_devices(lights)
    
    kitchen_guard_operator = KitchenGuardOperator("KitchenGuard", 
                                                   kitchenguard_devices, 
                                                   [room_tracker.name, stove_tracker.name])
    
    # Database client
    
    web_client = WebClient(patient)
    web_client.start()
    
    
    # Start the program
    room_tracker.start()
    stove_tracker.start()
    kitchen_guard_operator.start()
    

    while True:
        sleep(5)

    room_tracker.stop()
    stove_tracker.stop()
    kitchen_guard_operator.stop()
