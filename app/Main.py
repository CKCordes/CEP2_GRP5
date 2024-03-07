from time import sleep
from Controller import Controller
from Model import Model, ZigbeeDevice


if __name__ == "__main__":
    # Create a data model and add a list of known Zigbee devices.
    devices_model = Model()
    devices_model.add([ZigbeeDevice("0x00158d00044c228a", "pir"),
                       ZigbeeDevice("0xccccccfffeeaa775", "led"),
                       ZigbeeDevice("0xddddddfffeeaa775", "power plug")])

    # Create a controller and give it the data model that was instantiated.
    controller = Controller(devices_model)
    controller.start()

    print("Waiting for events...")

    while True:
        sleep(1)

    controller.stop()
