from Tracker import Tracker
from Zigbee2mqttClient import Zigbee2mqttMessage
import json 

class RoomTracker(Tracker):
    """
        Tracking message format:    ZigbeeDevice("KitchenOccupancy" :  "TRUE" | "FALSE"),
                                    ZigbeeDevice("BedroomOccupancy" :  "TRUE" | "FALSE"),
                                    ZigbeeDevice("BathroomOccupancy" :  "TRUE" | "FALSE"),
                                    ZigbeeDevice("LivingRoomOccupancy" :  "TRUE" | "FALSE"),
                                    ZigbeeDevice("HallOccupancy" :  "TRUE" | "FALSE"),
    """
    def initialize(self):
        self.log(f"Initializing RoomTracker")

        self.__RoomsOccupancy = {}
        
        deviceslist = self.devices_model.devices_list()
        for device in deviceslist:
            self.__RoomsOccupancy[device.location] = False

    def parse_event(self, message: Zigbee2mqttMessage):
        device = self.devices_model.find(message.deviceID)
        
        self.__RoomsOccupancy[device.location] = message.data["occupancy"]

    def tracking_message(self) -> str:
        return json.dumps({"Occupancy": self.__RoomsOccupancy})