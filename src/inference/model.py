from ultralytics import YOLO


class ColorDetection:
    def __init__(self, model_file: str):
        self.model = YOLO(model_file)

    def predict(self, image):
        # TODO make prediction a string of color
        result = self.model(image)[0]
        most_probable_color = result.probs.top1
        most_probable_color_name = result.names[most_probable_color].lower()
        print(f"Result in model.py: {most_probable_color_name}")
        return result
