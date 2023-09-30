import os
from PIL import Image


def process_images(input_folder, output_folder, target_size=(512, 512)):
    for root, dirs, files in os.walk(input_folder):
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp')):
                input_path = os.path.join(root, file)
                subfolder_name = os.path.basename(root)
                output_subfolder = os.path.join(output_folder, subfolder_name)

                if not os.path.exists(output_subfolder):
                    os.makedirs(output_subfolder)

                name, ext = os.path.splitext(file)
                output_filename = os.path.join(output_subfolder, f"{name}.jpg")  # Save as .jpg

                # Add a counter to the filename if it already exists
                counter = 1
                while os.path.exists(output_filename):
                    output_filename = os.path.join(output_subfolder, f"{name}_{counter}.jpg")
                    counter += 1

                try:
                    img = Image.open(input_path)
                    img = img.convert("RGB")
                    img = img.resize(target_size, Image.LANCZOS)
                    img.save(output_filename, "JPEG")
                except Exception as e:
                    print(f"Error processing '{input_path}': {e}")


if __name__ == "__main__":
    input_folder = "D:\Project Dataset"
    output_folder = "D:\Project Dataset1"

    process_images(input_folder, output_folder)
