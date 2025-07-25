# Lane-and-Pothole-Detection-using-Computer-Vision
A real-time road safety assistance system that detects lane markings and identifies potholes using OpenCV and YOLOv5. This project enhances driver awareness by overlaying detected lanes and potholes on live camera footage.

**Features**

✅ Lane Detection using:

Grayscale conversion & Gaussian Blur

Canny edge detection for lane boundaries

Region of Interest (ROI) masking

Hough Transform for line detection

✅ Pothole Detection using:

YOLOv5 model for real-time pothole identification

Bounding boxes & confidence scores over detected potholes

✅ Real-time Processing from a camera feed or video file
✅ Overlay visualization with lanes highlighted in green and potholes marked with bounding boxes
✅ Modular code structure for easy integration into ADAS (Advanced Driver Assistance Systems)

**🛠 Tech Stack**

Computer Vision: OpenCV
Deep Learning: YOLOv5 (Ultralytics)
Programming Language: Python
Model Framework: PyTorch

**📂 How It Works**

Lane Detection:
  Convert each video frame to grayscale
  Apply Gaussian blur and Canny edge detection
  Mask only the Region of Interest (ROI)
  Use Hough Transform to detect lane lines and overlay them
  
Pothole Detection:
  Feed frames to a YOLOv5 model
  Detect potholes and return annotated frames with bounding boxes
  
Combine results → output a frame with both lanes & potholes marked

