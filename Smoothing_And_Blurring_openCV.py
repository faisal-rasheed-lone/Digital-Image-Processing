import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

kernel = np.ones((5, 5), np.float32)/25
img = cv.imread("Samples/img_2.png", cv.IMREAD_COLOR)
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

# Applying homogeneous filter
simple_filter = cv.filter2D(img, -1, kernel)
# blurring the image
blur = cv.blur(img, (5, 5))
# Gaussian Filter
gaussian_fil = cv.GaussianBlur(img, (5,5), 0)
# median filter
median_fil = cv.medianBlur(img, 5)
# Bilateral_filter
bilateral_fil = cv.bilateralFilter(img, 9, 75, 75)


images = [img, simple_filter, blur, gaussian_fil, median_fil, bilateral_fil]
labels = ["org image", "simple_filter", "blur", "gaussian_fil",
          "median_fil", "bilateral_fil"]
for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(labels[i])
    plt.xticks([]), plt.yticks([])

plt.show()
