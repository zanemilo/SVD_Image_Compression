# Real-Time Image Compression with SVD

A lightweight real-time image compression tool using Singular Value Decomposition (SVD) with an interactive GUI built in Tkinter. This project demonstrates matrix factorization-based image compression, enabling users to visually adjust the compression level and observe results in real-time.
## Features

-Load and Display Images – Supports various image formats.<br> - Adjustable Compression Ratio – Modify compression level with a simple slider.<br> - Real-Time Updates – Observe compression effects dynamically.<br> - Preserves Image Quality – Leverages SVD to achieve high-quality compression while reducing file size.<br> - Lightweight & Easy to Use – Simple Python implementation with minimal dependencies.
## How It Works

The algorithm applies Singular Value Decomposition (SVD) to compress images by reducing the number of singular values used in reconstruction. The more singular values retained, the higher the quality and file size; fewer values lead to stronger compression and reduced size.
## Why Use SVD for Image Compression?

    Mathematically Robust – Decomposes the image into essential features.
    Flexible Compression – Users can control how much detail is preserved.
    Good for Low-Storage Applications – Reduces image size efficiently while maintaining structural integrity.

## Installation & Setup

    Clone the Repository:
```bash
git clone https://github.com/zanemilo/SVD_Image_Compression
cd SVD_Image_Compression
```
Install Dependencies:

pip install numpy opencv-python pillow

Run the Application:
```bash
    python main.py
```
## Usage

    Launch the application (python main.py).
    Load an image using the file selection dialog.
    Adjust the slider to modify the compression ratio.
    Observe the compressed image update in real-time.

## Use Cases

- Reducing image storage size without significant quality loss.<br> - Understanding matrix factorization techniques in computer vision.<br> - Exploring SVD for data compression in machine learning and signal processing.<br> - Building interactive visualization tools for educational purposes.<br>
##  Future Improvements

    Implement batch processing for multiple images.
    Add JPEG-style lossy compression comparisons.
    Explore GPU acceleration with CUDA for faster computation.
    Enable saving compressed images with an optimized format.

### Contributing

If you'd like to enhance this project, feel free to submit a pull request or suggest improvements via issues. Contributions are welcome! 
#### License

This project is licensed under the MIT License – free to use, modify, and distribute.
