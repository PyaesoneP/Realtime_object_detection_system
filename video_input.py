import cv2
import torch

# Video path (same as before)
video_path = './IED_SmartWasteBin (1).mp4'

# Load YOLOv5 model
model_path = './yolov5s.pt'  # Replace with your actual model path
model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_path)

# Open video capture
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()

ret, frame = cap.read()  # Read a single frame for testing

if not ret:
    print("Error: Could not read frame.")
    exit()

# Perform inference
results = model(frame)

# Print the results (bounding boxes, confidence, classes)
print(results.pandas().xyxy[0])  # Print results as pandas dataframe

# Display the frame (optional for now, just for visual confirmation)
cv2.imshow('Single Frame with Detection (check console for output)', frame)
cv2.waitKey(0)  # Wait until a key is pressed
cv2.destroyAllWindows()

cap.release()