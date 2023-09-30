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

# Morphological operations
kernel = np.ones((2,2), np.uint8)
dilation = cv.dilate(adap1, kernel , iterations = 1)
erosion = cv.erode(adap1, kernel , iterations = 2)
opening = cv.morphologyEx(adap1, cv.MORPH_OPEN, kernel)
closing = cv.morphologyEx(adap1, cv.MORPH_CLOSE, kernel)
Morph_grad = cv.morphologyEx(adap1, cv.MORPH_GRADIENT, kernel)
Top_hat = cv.morphologyEx(adap1, cv.MORPH_TOPHAT, kernel)


titles = ['Original image', 'S_binary_thresh', 'binary inverse',
          'binary trunc', 'thresh to zero', 'thresh to zero inverse',
          'adaptive mean', 'adaptive gaussian', 'dilation', 'erosion',
          'opening', 'Closing', 'Morph_grad', 'Top_hat']

images = [image, S_binary_thresh, binary_thresh_inverse,
          binary_thresh_truncate, binary_thresh_zero, binary_thresh_zero_inverse,
          adap1, adap2, dilation, erosion, opening, closing, Morph_grad, Top_hat]


for i in range(14):
    plt.subplot(2, 7, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()

cv.waitKey(0)
cv.destroyAllWindows()