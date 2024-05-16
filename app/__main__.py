from .HomeHelper.Model import DevicesModel, ZigbeeDevice, LEDstrip, Patient
from .HomeHelper.WebClient import WebClient
from .KitchenStoveTracker import KitchenStoveTracker
from .RoomTracker import RoomTracker
from .KitchenGuardOperator import KitchenGuardOperator
from paho.mqtt import publish, subscribe
from time import sleep
import json

if __name__ == "__main__":
    
    patient = Patient("Test_simulation_patient")
    
    # Room tracker
    room_motion_sensors = DevicesModel([ZigbeeDevice("lille_sensor", "pir", "kitchen"),
                                        ZigbeeDevice("stor_sensor", "pir", "livingroom"),])
    room_tracker = RoomTracker("Room_Tracker", room_motion_sensors)
    
    # Stove tracker
    stove_actuator = ZigbeeDevice("smart_plug", "power_plug", "kitchen")
    stove_power_model = DevicesModel(stove_actuator)
    stove_tracker = KitchenStoveTracker("Stove_Tracker", stove_power_model) 
    
    # Kitchen guard operator
    lights = LEDstrip("led_strip", "led", "livingroom")
    kitchenguard_devices = stove_power_model
    kitchenguard_devices.add_devices(lights)
    
    kitchen_guard_operator = KitchenGuardOperator("KitchenGuard", 
                                                   kitchenguard_devices, 
                                                   [room_tracker.name, stove_tracker.name])
    
    # Database client
    all_devices = DevicesModel([ZigbeeDevice("lille_sensor", "pir", "kitchen"),
                                ZigbeeDevice("stor_sensor", "pir", "livingroom"),
                                ZigbeeDevice("smart_plug", "power_plug", "kitchen"),
                                LEDstrip("led_strip", "led", "livingroom")])
    web_client = WebClient(patient, all_devices)
    web_client.start()
    
    
    # Start the program
    room_tracker.start()
    stove_tracker.start()
    kitchen_guard_operator.start()
    

    try:
        while True:
            sleep(5)
    except KeyboardInterrupt:
        pass
    room_tracker.stop()
    stove_tracker.stop()
    kitchen_guard_operator.stop()
    print("helleo")
