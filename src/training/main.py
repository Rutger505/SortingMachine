# The training of the model was originally executed in Google Colab. Hence the `userdata.get`

import os

from google.colab import userdata
from roboflow import Roboflow
from ultralytics import YOLO

# Download dataset from Roboflow
ROBOFLOW_API_KEY = userdata.get('ROBOFLOW_API_KEY')
roboflow = Roboflow(api_key=ROBOFLOW_API_KEY)

# Replace with your workspace and projects
project = roboflow.workspace("sortingmachine").project(
    "colordectection-rlg1a"
)

version = project.version(1)
dataset = version.download("folder")

# Train classification model
model = YOLO("yolov8n-cls.pt")

results = model.train(
    data=dataset.location,
    epochs=50,
    imgsz=224,
    patience=10
)

# Evaluate
metrics = model.val()

# Test on an image
test_image = "path_to_test_image.jpg"
predictions = model.predict(test_image)

os.getcwd()

# Export model to pth
model.export()
