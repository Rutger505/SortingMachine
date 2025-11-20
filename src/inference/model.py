from ultralytics import YOLO


class ColorDetection:
    def __init__(self, model_file: str):
        self.model = YOLO(model_file)

    def predict(self, image):
        # TODO make prediction a string of color
        result = self.model(image)
        print(result)
        return result
