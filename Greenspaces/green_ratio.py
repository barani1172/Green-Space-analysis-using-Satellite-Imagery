import cv2
import numpy as np
import os
import pandas as pd


def get_green_percentage(image_path):
    image = cv2.imread(image_path)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define range of green color in HSV
    lower_green = np.array([40, 40, 40])
    upper_green = np.array([70, 255, 255])

    # Threshold the HSV image to get only green colors
    mask = cv2.inRange(hsv, lower_green, upper_green)

    # Calculate percentage of green pixels in the image
    total_pixels = mask.shape[0] * mask.shape[1]
    green_pixels = cv2.countNonZero(mask)
    green_percentage = (green_pixels / total_pixels) * 100

    return green_percentage


input_folder = "D:/Datasets/Satellite images/"
output_folder = "D:/Datasets/Satellite/"
output_filename = "Chandigarh.csv"

columns = ["Image name", "Green percent"]
results = []

for filename in os.listdir(input_folder):
    if filename.startswith("chandigarh") and filename.endswith(".jpg"):
        # Get the image path
        image_path = os.path.join(input_folder, filename)
        image_name = filename[:len(filename)-4]

        green_percent = get_green_percentage(image_path)
        results.append([image_name, green_percent])

df = pd.DataFrame(results, columns=columns)

output_path = os.path.join(output_folder, output_filename)
df.to_csv(output_path, index=False)

print(f"Results saved to {output_path}")
