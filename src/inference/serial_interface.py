import json
from enum import Enum
from typing import Callable

import serial


class MessageType(Enum):
    PING = "color-detection-ping"
    REQUEST_COLOR = "color-detection-request-color"


class SerialInterface:
    def __init__(self, port: str, baudrate: int, timeout: float):
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.serial_connection = None
        self.callbacks: dict[MessageType, list[Callable]] = {}

    def add_callback(self, message_type: MessageType, callback: Callable):
        self.callbacks[message_type] = self.callbacks.get(message_type, []) + [callback]

    def listen(self):
        self.__open_connection__()

        while True:
            line = self.__get_line__()
            if not line:
                print("[WARN] No more data received")
                continue

            print(f"Received: {line}")

            parsed = json.loads(line)
            message_type = MessageType(parsed["type"])
            for callback in self.callbacks.get(message_type, []):
                callback()

    def __open_connection__(self):
        self.serial_connection = serial.Serial(port=self.port, baudrate=self.baudrate, timeout=self.timeout)

    def __get_line__(self) -> str:
        return self.serial_connection.readline().decode('utf-8')

    def __send_line__(self, line: str):
        self.serial_connection.write(line.encode('utf-8'))
