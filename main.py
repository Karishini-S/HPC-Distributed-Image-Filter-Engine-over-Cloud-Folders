import os
from filters.filter import grayscale_filter, blur_filter, edge_filter, save_image
import cv2

def process_image(input_path, output_folder, filters):
    img = cv2.imread(input_path)
    if img is None:
        print(f"Error: Could not load image {input_path}")
        return

    base_name = os.path.splitext(os.path.basename(input_path))[0]
    for f in filters:
        processed = f(img)
        save_image(processed, output_folder, f"{base_name}_{f.__name__}.jpg")

if __name__ == "__main__":
    input_folder = "inputs"
    output_folder = "outputs"

    filters = [grayscale_filter, blur_filter, edge_filter]

    for file in os.listdir(input_folder):
        if file.lower().endswith((".jpg", ".png", ".jpeg")):
            img_path = os.path.join(input_folder, file)
            print(f"Processing {img_path} ...")
            process_image(img_path, output_folder, filters)

    print("Sequential processing finished!")