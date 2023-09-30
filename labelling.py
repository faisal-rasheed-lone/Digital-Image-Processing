import os
from PIL import Image


def process_images(input_folder, output_folder, target_size=(512, 512)):
    for root, dirs, files in os.walk(input_folder):
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')):
                input_path = os.path.join(root, file)
                subfolder_name = os.path.basename(root)
                output_subfolder = os.path.join(output_folder, subfolder_name)

                if not os.path.exists(output_subfolder):
                    os.makedirs(output_subfolder)

                output_filename = os.path.join(output_subfolder, f"{subfolder_name}_{file}")

                try:
                    img = Image.open(input_path)
                    img = img.convert("RGB")
                    img = img.resize(target_size, Image.LANCZOS)
                    img.save(output_filename, "JPEG")
                except Exception as e:
                    print(f"Error processing '{input_path}': {e}")


if __name__ == "__main__":
    input_folder = "D:\Project Dataset1"
    output_folder = "D:\Project Dataset2"

    process_images(input_folder, output_folder)
