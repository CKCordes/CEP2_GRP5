import json
from dataclasses import dataclass
from typing import Any
import requests

DATABASE_HTTP_HOST = "http://localhost:8000"
        
class WebClient:
    def __init__(self, host: str = DATABASE_HTTP_HOST) -> None:

        self.__host = host

    def send_event(self, encoded_heucod: str) -> int:
        try:
            # A new event is sent as an HTTP POST request.
            response = requests.post(self.__host, data=encoded_heucod)

            return response.status_code
        except requests.exceptions.ConnectionError:
            raise ConnectionError(f"Error connecting to {self.__host}")
