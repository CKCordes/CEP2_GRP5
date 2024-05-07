import json
from dataclasses import dataclass
from typing import Any
import requests
from .Model import Patient, DevicesModel
from .Zigbee2mqttClient import Zigbee2mqttClient, Zigbee2mqttMessage, Zigbee2mqttMessageType
import time
from .resources.heucod import HeucodEvent
import uuid

DATABASE_HTTP_HOST = "http://localhost:8000/api/dbupdater"

class WebClient:
    def __init__(self, 
                 paitent: Patient,
                 devices: DevicesModel,
                 database_host: str = DATABASE_HTTP_HOST) -> None:
        self.name = "WebClient"
        self.__patient = paitent
        self.__devices = devices
        self.__host = database_host
        self.__z2m_client = Zigbee2mqttClient(on_message_clbk = self.__event_received,
                                              serving         = "WebClient")
    
    def start(self) -> None:
        
        self.__z2m_client.connect()
        z2m_health = self.__z2m_client.check_health()
        if z2m_health != "ok":
            self.log("Zigbee2MqttClient - health check BAD")
            ##self.__z2m_client.disconnect() # giver fejl som kommer helt inde i koden.
            return
            
        self.log(f"{self.name} : Zigbee2MqttClient is OK - Starting tracking!")
    
    def stop(self) -> None:
        self.__z2m_client.disconnect()
    
    def __event_received(self, message: Zigbee2mqttMessage):
        # If message is None (it wasn't parsed correcty in the Z2Mclient), then don't do anything
        if not message:
            return

        if message.type_ != Zigbee2mqttMessageType.DEVICE_EVENT:
            return
        
        topics_tokens = message.topic.split("/")
        if len(topics_tokens) <= 1:
            return

        # Retrieve the device ID from the topic.
        device_id = topics_tokens[1]
        
        heucod = HeucodEvent()
        
        # Figure out eventtype
        
        device = self.__devices.find(device_id)
        
        if device is None:
            self.log(f"Device{device_id} not found in webclient")
            return
        
        event_type_ = "BasicEvent"
        event_type_enum_ = 81325
        
        if device.type_ == "pir":
            event_type_ = "RoomMovementEvent"
            event_type_enum_ = 82099
            
        elif device.type_ == "power_plug":
            event_type_ = "CookingDeviceUsage"
            event_type_enum_ = 82136
        
        # == Event ==
        heucod.id_ = uuid.uuid4()
        heucod.event_type = event_type_
        heucod.event_type_enum = event_type_enum_
        heucod.description = message.data
        heucod.advanced = ""
        heucod.timestamp = time.time()
        heucod.start_time = -1
        heucod.end_time = -1
        heucod.length = -1
        heucod.sensor_blind_duration = -1
        heucod.value = -1
        heucod.unit = ""
        heucod.value2 = -1
        heucod.unit2 = ""
        heucod.value3 = -1
        heucod.unit3 = ""
        heucod.direct_event = False
        heucod.sending_delay = -1
        
        # == Patient ==
        heucod.patient_id = self.__patient.patient_id
        heucod.caregiver_id = 1
        heucod.monitor_id = 1
        heucod.location = ""
        heucod.street_adress = ""
        heucod.city = "Aarhus"
        heucod.postal_code = 8200
        heucod.site = ""
        heucod.room = "" 
        
        # == Sensor ==
        heucod.sensor_id = device_id
        heucod.sensor_type = device.type_
        heucod.sensor_location = device.location
        heucod.sensor_rtc_clock = True
        heucod.device_model = ""
        heucod.device_vendor = ""
        heucod.gateway_id = ""
        heucod.service_id = ""
        heucod.power = 100
        heucod.battery = 100
        heucod.rssi = 1.0
        heucod.measured_power = 1.0
        heucod.signal_to_noise_ratio = 0.5
        heucod.accuracy = 1
        heucod.link_quality = 255
            
            
        # == send the event
        encoded_heucod = heucod.to_json()
        try:
            response = self.send_event(encoded_heucod)
            self.log(f"Send event with response: {response}")
        except:
            self.log(f"Trouble posting event")
        

    def log(self, string: str):
        now = time.strftime('%X')
        print(f"[{now}] {self.name} : {string}"  )
        

    def send_event(self, encoded_heucod: str) -> int:
        try:
            # A new event is sent as an HTTP POST request.
            response = requests.post(self.__host, data=encoded_heucod)

            return response
        except requests.exceptions.ConnectionError:
            raise ConnectionError(f"Error connecting to {self.__host}")
