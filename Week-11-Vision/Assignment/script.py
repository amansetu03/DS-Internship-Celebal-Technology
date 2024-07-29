import cv2
import numpy as np
from matplotlib import pyplot as plt

# Function to calculate and plot histograms of color channels
def plot_histograms(image_path):
    # Read the image
    image = cv2.imread(image_path)
    
    # Check if image is loaded
    if image is None:
        print("Error: Unable to load image.")
        return
    
    # Convert image from BGR to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Split the image into its RGB channels
    r, g, b = cv2.split(image_rgb)
    
    # Calculate histograms
    hist_r = cv2.calcHist([r], [0], None, [256], [0, 256])
    hist_g = cv2.calcHist([g], [0], None, [256], [0, 256])
    hist_b = cv2.calcHist([b], [0], None, [256], [0, 256])
    
    # Plot histograms
    plt.figure(figsize=(12, 6))
    plt.subplot(131)
    plt.plot(hist_r, color='r')
    plt.title('Red Channel Histogram')
    plt.xlim([0, 256])
    
    plt.subplot(132)
    plt.plot(hist_g, color='g')
    plt.title('Green Channel Histogram')
    plt.xlim([0, 256])
    
    plt.subplot(133)
    plt.plot(hist_b, color='b')
    plt.title('Blue Channel Histogram')
    plt.xlim([0, 256])
    
    plt.tight_layout()
    plt.show()

# Path to the image
image_path = './Image/test.jpeg'

# Call the function to plot histograms
plot_histograms(image_path)
