import os

from src.inference.model import ColorDetection
from src.inference.serial_interface import SerialInterface, MessageType


def main():
    color_detector = ColorDetection(f"{os.getcwd()}/best.pt")

    callbacks = {
        MessageType.REQUEST_COLOR: lambda: color_detector.predict(f"{os.getcwd()}/test.jpg"),
        MessageType.PING: lambda: "pong"
    }

    print(callbacks[MessageType.REQUEST_COLOR]())
    print(callbacks[MessageType.PING]())

    serial_interface = SerialInterface(
        port="/dev/ttyUSB0",  # Adjust port as needed
        baudrate=9600,
        timeout=1.0,
        callbacks=callbacks
    )

    serial_interface.listen()


if __name__ == '__main__':
    main()
