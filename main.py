import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np
import cv2

def compress_image_svd(image, compression_ratio):
    """
    Compresses the input color image using Singular Value Decomposition (SVD)
    based on the given compression ratio.

    Args:
        image (numpy.ndarray): The input color image to be compressed.
        compression_ratio (float): The ratio for compression (0 to 1).

    Returns:
        numpy.ndarray: The compressed color image.
    """
    # Initialize an empty list to store the compressed color channels
    compressed_channels = []

    # Perform SVD and compression for each color channel (R, G, B)
    for i in range(3):
        channel = image[:, :, i]
        U, S, Vt = np.linalg.svd(channel, full_matrices=False)
        k = int(compression_ratio * len(S))
        compressed_channel = np.dot(U[:, :k], np.dot(np.diag(S[:k]), Vt[:k, :]))
        compressed_channels.append(compressed_channel)

    # Stack the compressed color channels back into a single image
    compressed_image = np.stack(compressed_channels, axis=2)
    return compressed_image

def update_image(compression_ratio):
    """
    Updates the displayed image based on the given compression ratio.

    Args:
        compression_ratio (int): The compression ratio from the slider (1 to 100).
    """
    if not image_loaded:
        return

    # Convert the compression ratio from percentage to a fraction
    compression_ratio = compression_ratio / 100.0
    # Compress the image
    compressed_image = compress_image_svd(original_image, compression_ratio)
    # Normalize the compressed image to the range [0, 255]
    compressed_image = (compressed_image - np.min(compressed_image)) / (np.max(compressed_image) - np.min(compressed_image)) * 255
    compressed_image = compressed_image.astype(np.uint8)
    # Convert the compressed image to a format suitable for Tkinter
    compressed_image_pil = Image.fromarray(compressed_image)
    compressed_image_tk = ImageTk.PhotoImage(compressed_image_pil)
    # Update the image label with the compressed image
    img_label.config(image=compressed_image_tk)
    img_label.image = compressed_image_tk

def load_image():
    """
    Opens a file dialog to load an image and updates the display.
    """
    global original_image, image_loaded
    # Open file dialog to select an image
    file_path = filedialog.askopenfilename()
    if file_path:
        # Read the image using OpenCV
        original_image = cv2.imread(file_path)
        original_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)  # Convert to RGB
        image_loaded = True
        # Update the displayed image with the initial compression ratio
        update_image(compression_slider.get())

# Initialize the main window
root = tk.Tk()
root.title("Real-Time Image Compression")

# Add a button to load an image
load_button = tk.Button(root, text="Load Image", command=load_image)
load_button.pack()

# Add a slider to control the compression ratio
compression_slider = tk.Scale(root, from_=1, to_=100, orient=tk.HORIZONTAL, command=lambda v: update_image(int(v)))
compression_slider.set(50)  # Set the initial value of the slider
compression_slider.pack()

# Add a label to display the image
img_label = tk.Label(root)
img_label.pack()

# Initialize global variables
original_image = None
image_loaded = False

# Start the GUI event loop
root.mainloop()
