import cv2
import numpy as np
import os

# Load an image
image_path = "Samples/HS.jpg"
image = cv2.imread(image_path)

# Create a directory to save the masks
if not os.path.exists("annotated_masks"):
    os.makedirs("annotated_masks")

# Create an empty mask
mask = np.zeros_like(image)

# Initialize variables for polygon drawing
drawing = False
points = []


# Mouse callback function for drawing polygons
def draw_polygon(event, x, y, flags, param):
    global drawing, points

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        points = [(x, y)]

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            points.append((x, y))

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.polylines(mask, [np.array(points)], isClosed=True, color=(255, 255, 255), thickness=2)
        points = []


# Create a window and set the mouse callback
cv2.namedWindow("Image")
cv2.setMouseCallback("Image", draw_polygon)

while True:
    combined = cv2.addWeighted(image, 0.7, mask, 0.3, 0)
    cv2.imshow("Image", combined)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
    elif key == ord("c"):
        mask = np.zeros_like(image)
    elif key == ord("s"):
        mask_path = os.path.join("annotated_masks", os.path.basename(image_path).replace(".", f"_mask."))
        cv2.imwrite(mask_path, mask)
        print(f"Saved mask as {mask_path}")

cv2.destroyAllWindows()
