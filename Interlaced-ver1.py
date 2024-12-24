import cv2
import numpy as np

# Function to apply interlaced effect
def interlace_frame(frame, frame_number):
    height, width, _ = frame.shape
    output = frame.copy()

    for y in range(0, height, 2):
        if frame_number % 2 == 0:
            output[y] = 0  # Black out even lines in even frames
        else:
            output[y+1] = 0  # Black out odd lines in odd frames

    return output

# Load the video
video_path = '/path/to/video.mp4'
cap = cv2.VideoCapture(video_path)

# Get video properties
fps = int(cap.get(cv2.CAP_PROP_FPS))
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Output video
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('interlaced_video.mp4', fourcc, fps, (width, height))

frame_number = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Apply the interlaced effect
    interlaced_frame = interlace_frame(frame, frame_number)
    out.write(interlaced_frame)
    
    frame_number += 1

cap.release()
out.release()
cv2.destroyAllWindows()

