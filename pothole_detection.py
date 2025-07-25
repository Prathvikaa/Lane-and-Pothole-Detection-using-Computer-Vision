import cv2
from ultralytics import YOLO

# Load the YOLO model
model = YOLO('models/yolov5su.pt')

def detect_potholes(frame):
    # Perform detection
    results = model(frame)

    # Annotate the frame
    annotated_frame = results[0].plot()  # Annotated frame
    return annotated_frame
