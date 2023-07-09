from PIL import Image
import numpy as np

# Load the satellite image
img = Image.open("D:/Datasets/Satellite images/chennai21.jpg")

# Convert the image to RGB
img = img.convert("RGB")

# Extract the green channel of the image
green_channel = img.split()[1]

# Threshold the green channel
threshold = 100
binary_img = np.array(green_channel) > threshold

# Count the number of white pixels
num_green_pixels = np.sum(binary_img)

# Calculate the total number of pixels
total_pixels = img.width * img.height

# Calculate the green percentage
green_percent = (num_green_pixels / total_pixels) * 100

print("Green percentage:", green_percent)
