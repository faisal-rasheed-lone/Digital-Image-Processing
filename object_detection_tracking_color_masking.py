import numpy as np
import cv2


# Dummy callback function for trackbar
def nothing(x):
    pass


# Create a named window for the trackbars
cv2.namedWindow("Tracking")
# Create trackbars for lower and upper HSV values
cv2.createTrackbar("LH", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LS", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LV", "Tracking", 0, 255, nothing)
cv2.createTrackbar("UH", "Tracking", 0, 255, nothing)
cv2.createTrackbar("US", "Tracking", 0, 255, nothing)
cv2.createTrackbar("UV", "Tracking", 0, 255, nothing)

while True:
    # Load a sample image
    frame = cv2.imread("Samples/img.png")

    # Convert the frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Get trackbar positions for lower and upper HSV values
    l_h = cv2.getTrackbarPos("LH", "Tracking")
    l_s = cv2.getTrackbarPos("LS", "Tracking")
    l_v = cv2.getTrackbarPos("LV", "Tracking")
    u_h = cv2.getTrackbarPos("UH", "Tracking")
    u_s = cv2.getTrackbarPos("US", "Tracking")
    u_v = cv2.getTrackbarPos("UV", "Tracking")

    # Create lower and upper bounds arrays for masking
    lower_bound = np.array([l_h, l_s, l_v])
    upper_bound = np.array([u_h, u_s, u_v])

    # Create a mask using the inRange function
    mask = cv2.inRange(hsv, lower_bound, upper_bound)

    # Apply the mask to the original frame
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Display the original frame, mask, and result
    cv2.imshow("Original Frame", frame)
    cv2.imshow("Mask", mask)
    cv2.imshow("Result", result)

    # Exit the loop if the 'Esc' key is pressed
    key = cv2.waitKey(1)
    if key == 27:
        break

# Release any resources and close all windows
cv2.destroyAllWindows()
