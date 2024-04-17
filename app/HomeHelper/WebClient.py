import json
from dataclasses import dataclass
from typing import Any
import requests

DATABASE_HTTP_HOST = "http://localhost:8000"
        
class WebClient:
    """ Represents a local web client that sends events to a remote web service.
    """

    def __init__(self, host: str = DATABASE_HTTP_HOST) -> None:
        """ Default initializer.

        Args:
            host (str): an URL with the address of the remote web service
        """
        self.__host = host

    def send_event(self, encoded_heucod: str) -> int:
        """ Sends a new event to the web service.

        Args:
            event (str): a string with the event to be sent.

        Raises:
            ConnectionError: if the connection to the web service fails

        Returns:
            int: the status code of the request
        """
        try:
            # A new event is sent as an HTTP POST request.
            response = requests.post(self.__host, data=encoded_heucod)

            return response.status_code
        except requests.exceptions.ConnectionError:
            raise ConnectionError(f"Error connecting to {self.__host}")
