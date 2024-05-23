from __future__ import annotations
import json
from dataclasses import dataclass
from enum import Enum
from queue import Empty, Queue
from threading import Event, Thread
from time import sleep
from typing import Any, Callable, List, Optional
from paho.mqtt.client import Client as MqttClient, MQTTMessage, CallbackAPIVersion
from paho.mqtt import publish, subscribe

MQTT_BROKER_HOST = "localhost"
MQTT_BROKER_PORT = 1883 

class TrackerClient:
    STANDARD_TOPIC = "no_topic"

    def __init__(self,
                 on_message_clbk: Callable[[str, str], None],
                 host: str = MQTT_BROKER_HOST,
                 port: int = MQTT_BROKER_PORT,
                 topics: List[str] = [STANDARD_TOPIC],
                 serving: str = "NotServingAnyOne"):
        
        self.__client = MqttClient(CallbackAPIVersion.VERSION2)
        self.__client.on_connect = self.__on_connect
        self.__client.on_disconnect = self.__on_disconnect
        self.__client.on_message = self.__on_message
        self.__connected = False
        self.__events_queue = Queue()
        self.__mqtt_host = host
        self.__on_message_clbk = on_message_clbk
        self.__mqtt_port = port
        self.__stop_worker = Event()
        self.__subscriber_thread = Thread(target=self.__worker,
                                          daemon=True)
        self.__topics = topics
        self.serving = serving

    def connect(self) -> None:
        """ Connects to the MQTT broker specified in the initializer. This is a blocking function.
        """
        # In the client is already connected then stop here.
        if self.__connected:
            return

        # Connect to the host given in initializer.
        self.__client.connect(self.__mqtt_host,
                              self.__mqtt_port)
        self.__client.loop_start()
        # Subscribe to all topics given in the initializer.
        for t in self.__topics:
            self.__client.subscribe(t)
        # Start the subscriber thread.
        self.__subscriber_thread.start()


    def disconnect(self) -> None:
        """ Disconnects from the MQTT broker.
        """
        self.__stop_worker.set()
        self.__client.loop_stop()
        # Unsubscribe from all topics given in the initializer.
        for t in self.__topics:
            self.__client.unsubscribe(t)
        self.__client.disconnect()


    def __on_connect(self, client, userdata, flags, rc, properties) -> None:
        """ Callback invoked when a connection with the MQTT broker is established.
        """
        
        self.__connected = True
        print(f"{self.serving} : Tracker client connected")

    def __on_disconnect(self, client, userdata, rc, properties, extra) -> None:
        """ Callback invoked when the client disconnects from the MQTT broker occurs.
        """
        
        self.__connected = False
        print(f"{self.serving} : Tracker client disconnected")

    def __on_message(self, client, userdata, message: MQTTMessage) -> None:
        """ Callback invoked when a message has been received on a topic that the client subscribed.
        """

        # Push a message to the queue. This will later be processed by the worker.
        self.__events_queue.put(message)

    def __worker(self) -> None:
        """ This method pulls zigbee2mqtt messages from the queue of received messages, pushed when
        a message is received, i.e. by the __on_message() callback. This method will be stopped when
        the instance of zigbee2mqttClient disconnects, i.e. disconnect() is called and sets the
        __stop_worker event.
        """
        while not self.__stop_worker.is_set():
            try:
                # Pull a message from the queue.
                message: MQTTMessage = self.__events_queue.get(timeout=1)
            except Empty:
                # This exception is raised when the queue pull times out. Ignore it and retry a new pull.
                pass
            else:
                # If a message was successfully pulled from the queue, then process it and callback the function on the tracker.
                if message:
                    self.__on_message_clbk(message.topic, message.payload.decode())
