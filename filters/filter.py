import cv2
import os

# Grayscale filter
def grayscale_filter(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Blur filter
def blur_filter(img, ksize=(5, 5)):
    return cv2.GaussianBlur(img, ksize, 0)

# Edge detection filter
def edge_filter(img):
    return cv2.Canny(img, 100, 200)

# Save image helper
def save_image(img, output_folder, filename):
    os.makedirs(output_folder, exist_ok=True)
    path = os.path.join(output_folder, filename)
    cv2.imwrite(os.path.join(output_folder, filename), img)
    print(f"Saved {path}")
