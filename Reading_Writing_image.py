import cv2

# Read an image from file
image_path = 'Samples/newton.jpg'
img = cv2.imread(image_path)

# Check if the image was read successfully
if img is None:
    print("Error: Could not read the image.")
    exit()

# Convert the image to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Save the grayscale image to a new file
output_path = 'Samples/newton_output_gray.jpg'
cv2.imwrite(output_path, gray_img)

# Display the original and processed images (optional)
cv2.imshow('Original Image', img)
cv2.imshow('Grayscale Image', gray_img)

# Wait for a key press and then close all OpenCV windows
cv2.waitKey(0)
cv2.destroyAllWindows()
