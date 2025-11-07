# TODO inference logic
import os

from src.inference.model import ColorDetection


def main():
    color_detector = ColorDetection(f"{os.getcwd()}/../../best.pt")

    print(color_detector.predict(f"{os.getcwd()}/../../test.jpg"))


if __name__ == '__main__':
    main()
