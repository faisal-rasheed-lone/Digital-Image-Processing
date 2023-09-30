import cv2

# Define the FourCC code for XVID codec
fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')

# Create a VideoCapture object
cap = cv2.VideoCapture(0)  # 0 indicates the default webcam

# Check if the VideoCapture object is successfully opened
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Get the frame width and height
frame_width = int(cap.get(3)) #3 indicates width
frame_height = int(cap.get(4)) #4 indicates height

# Create a VideoWriter object to save the video
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (frame_width, frame_height))

while True:
    # Capture a frame from the camera
    ret, frame = cap.read()

    if not ret:
        print("Error: Failed to capture frame.")
        break

    # Display the frame (optional)
    cv2.imshow('Frame', frame)

    # Write the frame to the VideoWriter
    out.write(frame)

    # Press 'q' to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture and VideoWriter objects
cap.release()
out.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
