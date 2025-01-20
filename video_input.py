import cv2

# Replace 'your_video_file.mp4' with the actual path to your video file
video_path = './IED_SmartWasteBin (1).mp4'

# Create a VideoCapture object
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("End of video.")
        break

    ret = cap.set(cv2.CAP_PROP_FRAME_WIDTH,320)
    ret = cap.set(cv2.CAP_PROP_FRAME_HEIGHT,240)
    # Display the frame
    cv2.imshow('Video', frame)

    # Exit on pressing the 'q' key
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Release the VideoCapture object and close all windows
cap.release()
cv2.destroyAllWindows()