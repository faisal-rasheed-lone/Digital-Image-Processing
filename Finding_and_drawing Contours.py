import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("Samples/img_3.png")
imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

ret, thresh = cv.threshold(imgGray, 127, 255, 0)

contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

cv.drawContours(img, contours, -1, (0, 255, 100), 1)

cv. imshow("image", img)
cv.imshow("grayImage", imgGray)

cv.waitKey(0)
cv.destroyAllWindows()