from ultralytics import YOLO


class ColorDetection:
    def __init__(self, model_file: str):
        self.model = YOLO(model_file)

    def predict(self, image):
        result = self.model(image)[0]
        color_index = result.probs.top1
        color_name = result.names[color_index].lower()
        return color_name
