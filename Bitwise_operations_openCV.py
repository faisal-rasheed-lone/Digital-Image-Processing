import numpy as np
import cv2

# Creating an image of 512 * 512 with 3 channels
img1 = np.zeros((512,512,3), np.uint8)
# Adding rectangle to the image
img1 = cv2.rectangle(img1, (200,200), (400, 400), (255, 150, 255), -1)

# Creating a 2nd image of 512 * 512 with 3 channels
img2 = np.zeros((512,512,3), np.uint8)
# Adding Circle to the image
img2 = cv2.circle(img2, (200,200), 150, (100, 150, 255), -1)

# performing bitwise operators
# bitwise And
bitwise_AND = cv2.bitwise_and(img1, img2)

# bitwise OR
bitwise_OR = cv2.bitwise_or(img1, img2)

# bitwise Not
bitwise_NOT = cv2.bitwise_not(img1)

# bitwise XOR
bitwise_XOR = cv2.bitwise_xor(img1, img2)

# displaying the images
cv2.imshow("Original image 1", img1)
cv2.imshow("Original Image 2", img2)
cv2.imshow("Bitwise And ", bitwise_AND)
cv2.imshow("Bitwise OR ", bitwise_OR)
cv2.imshow("Bitwise NOT ", bitwise_NOT)
cv2.imshow("Bitwise XOR ", bitwise_XOR)

cv2.waitKey(0)
cv2.destroyAllWindows()
