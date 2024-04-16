from .HomeHelper.Tracker import Tracker
from .HomeHelper.Zigbee2mqttClient import Zigbee2mqttMessage
import json 

class RoomTracker(Tracker):
    """
        Tracking message format:    {"occupancy" : {"kitchen": True | False,
                                                    "room1": True | False,
                                                    ... 
                                                    }
                                    }
    """
    def initialize(self):
        self.log("Initializing RoomTracker")

        self.__RoomsOccupancy = {}
        
        deviceslist = self.devices_model.devices_list
        for device in deviceslist:
            self.__RoomsOccupancy[device.location] = False

    def parse_event(self, message: Zigbee2mqttMessage):
        device = self.devices_model.find(message.deviceID)
        
        self.__RoomsOccupancy[device.location] = message.data["occupancy"]

    def tracking_message(self) -> str:
        return json.dumps({"occupancy": self.__RoomsOccupancy})