from dataclasses import dataclass
from typing import List, Optional, Union
from enum import Enum

@dataclass
class ZigbeeDevice:
    id_: str
    type_: str
    location: str

class LEDstrip(ZigbeeDevice):
    pass

@dataclass
class Patient:
    patient_id: str

    
    
class DevicesModel:
    def __init__(self, devices: Union[ZigbeeDevice, List[ZigbeeDevice]] = []):
        # key is device_id(friendly_name thing), value is a ZigbeeDevice
        self.__devices: dict[str, ZigbeeDevice] = {}
        
        if devices != []:
            self.add_devices(devices)
        

    @property
    def actuators_list(self) -> List[ZigbeeDevice]:
        return list(filter(lambda s: s.type_ in {"led", "power_plug"},
                           self.__devices.values()))


    @property
    def devices_list(self) -> List[ZigbeeDevice]:
        return list(self.__devices.values())

    @property
    def sensors_list(self) -> List[ZigbeeDevice]:
        return list(filter(lambda s: s.type_ in {"pir"},
                           self.__devices.values()))

    def get_type(self, device_type: str) -> List[ZigbeeDevice]:
        return list(filter(lambda s: s.type_ is device_type,
                           self.__devices.values()))
        
    def add_devices(self, device: Union[ZigbeeDevice, List[ZigbeeDevice]]) -> None:

        list_devices = [device] if isinstance(device, ZigbeeDevice) else device

        for s in list_devices:
            self.__devices[s.id_] = s

    def find(self, device_id: str) -> Optional[ZigbeeDevice]:
        devices = list(filter(lambda kv: kv[0] == device_id,
                              self.__devices.items()))

        return devices[0][1] if len(devices) >= 1 else None

    def all_devices_as_topics(self) -> list[str]:
        topics = []
        for id in self.__devices:
            topics.append("zigbee2mqtt/" + id)
        return topics