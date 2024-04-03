from dataclasses import dataclass
from typing import List, Optional, Union
from enum import Enum


@dataclass
class ZigbeeDevice:
    id_: str
    type_: str
    location: str
    
class DevicesModel:
    def __init__(self):
        # key is device_id(friendly_name thing), value is a ZigbeeDevice
        self.__devices: dict[str, ZigbeeDevice] = {}

    @property
    def actuators_list(self) -> List[ZigbeeDevice]:
        return list(filter(lambda s: s.type_ in {"led", "power plug"},
                           self.__devices.values()))

    @property
    def devices_list(self) -> List[ZigbeeDevice]:
        return list(self.__devices.values())

    @property
    def sensors_list(self) -> List[ZigbeeDevice]:
        return list(filter(lambda s: s.type_ in {"pir"},
                           self.__devices.values()))

    def add_devices(self, device: Union[ZigbeeDevice, List[ZigbeeDevice]]) -> None:

        list_devices = [device] if isinstance(device, ZigbeeDevice) else device

        for s in list_devices:
            self.__devices[s.id_] = s

    def find(self, device_id: str) -> Optional[ZigbeeDevice]:
        """ Retrieve a device from the database by its ID.

        Args:
            device_id (str): ID of the device to retrieve.

        Returns:
            Optional[Cep2ZigbeeDevice]: a device. If the device is not stored, then None is returned
        """

        devices = list(filter(lambda kv: kv[0] == device_id,
                              self.__devices.items()))

        return devices[0][1] if len(devices) >= 1 else None

    def all_devices_as_topics(self) -> list[str]:
        topics = []
        for id in self.__devices:
            topics.append("zigbee2mqtt/" + id)
        return topics