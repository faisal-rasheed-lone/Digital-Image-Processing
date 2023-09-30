import cv2
import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

image = cv.imread("Samples/img_1.png")


img = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
retval, S_binary_thresh = cv.threshold(image, 127.0, 255.0, cv.THRESH_BINARY)
retval, binary_thresh_inverse = cv.threshold(image, 127.0, 255.0, cv.THRESH_BINARY_INV)
retval, binary_thresh_truncate = cv.threshold(image, 127.0, 255.0, cv.THRESH_TRUNC)
retval, binary_thresh_zero = cv.threshold(image, 127.0, 255.0, cv.THRESH_TOZERO)
retval, binary_thresh_zero_inverse = cv.threshold(image, 127.0, 255.0, cv.THRESH_TOZERO_INV)


# Adaptive threshholding
adap1 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
adap2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)

titles = ['Original image', 'S_binary_thresh', 'binary inverse',
          'binary trunc', 'thresh to zero', 'thresh to zero inverse', 'adaptive mean', 'adaptive gaussian']

images = [image, S_binary_thresh, binary_thresh_inverse,
          binary_thresh_truncate, binary_thresh_zero, binary_thresh_zero_inverse,
          adap1, adap2]


for i in range(8):
    plt.subplot(2, 4, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()

cv.waitKey(0)
cv.destroyAllWindows()
