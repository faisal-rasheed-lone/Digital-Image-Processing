import os
import cv2
from PIL import Image
import numpy as np

# Path to the input folder containing subfolders of different categories
input_folder = 'D:\Project Dataset'

# Path to the output folder where resized images will be saved
output_folder = 'D:\Project Dataset1'

# Target size for resizing
target_size = (512, 512)

# List of supported image formats
supported_input_formats = ['.jpg', '.jpeg', '.png', '.bmp', '.tif', '.tiff', '.webp', '.avif']

# Output format for saving resized images
output_image_format = 'jpg'

# List of category names (subfolder names)
category_names = os.listdir(input_folder)

# Loop through each category
for category_name in category_names:
    # Create the corresponding output folder
    category_output_folder = os.path.join(output_folder, category_name)
    os.makedirs(category_output_folder, exist_ok=True)

    # Get a list of image filenames in the current category
    image_filenames = os.listdir(os.path.join(input_folder, category_name))

    # Loop through each image in the category
    for image_filename in image_filenames:
        # Check if the input image format is supported
        image_name, image_ext = os.path.splitext(image_filename)
        if image_ext.lower() not in supported_input_formats:
            print(f"Unsupported format: {image_filename}")
            continue

        # Load the image using PIL
        image_path = os.path.join(input_folder, category_name, image_filename)
        with Image.open(image_path) as pil_image:
            pil_image = pil_image.convert("RGB")

            # Resize the image
            resized_image = pil_image.resize(target_size)

            # Convert PIL image to OpenCV format
            resized_cv_image = cv2.cvtColor(np.array(resized_image), cv2.COLOR_RGB2BGR)

        # Save the resized image to the output folder with the same name as original image
        output_image_filename = image_name + '.' + output_image_format
        output_image_path = os.path.join(category_output_folder, output_image_filename)
        cv2.imwrite(output_image_path, resized_cv_image)

        # Assign a label (category name) to the image
        with open(os.path.join(output_folder, 'labels.txt'), 'a') as f:
            f.write(f"{output_image_path} {category_name}\n")

print("Image resizing and labeling completed.")
