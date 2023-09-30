import numpy as np
import cv2

while True:
    frame = cv2.imread("Samples/img.png")
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_bound = np.array([110, 50, 50])
    upper_bound = np.array([130, 150, 255])

    m = cv2.inRange(frame, lower_bound, upper_bound)
    result = cv2.bitwise_and(frame, frame, mask = m)

    cv2.imshow("frame", frame)
    cv2.imshow("result", result)
    key = cv2.waitKey(1)
    if key ==27:
        break

cv2.release()
cv2.destroyAllWindows()