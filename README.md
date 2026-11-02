## X-ray Image Processing and Analysis

## Project Overview

This project explores basic image processing and analysis using a grayscale X-ray image. It uses Python, OpenCV, NumPy, and PyTorch to load an image, examine its pixel values, apply simple image transformations, and convert the image array into a PyTorch tensor.

The project is intended as a practical introduction to working with medical images through programming.

## Objectives

- Load and display a grayscale X-ray image.
- Examine image dimensions and pixel intensity values.
- Calculate basic image statistics.
- Adjust image brightness and contrast.
- Apply Gaussian blur.
- Convert the image from a NumPy array into a PyTorch tensor.

## Tools and Libraries

- Python
- OpenCV
- NumPy
- PyTorch

## Methods

### 1. Image Loading

The X-ray image is loaded in grayscale using OpenCV.

The image is loaded using a relative path, allowing the project to locate the image file within the project folder without relying on a device-specific file path.

### 2. Basic Image Analysis

The program examines the image dimensions and retrieves pixel intensity information, including the minimum, maximum, and mean intensity values.

### 3. Brightness Adjustment

OpenCV is used to increase image brightness by adding a constant value to the pixel intensities.

### 4. Contrast Adjustment

Two contrast versions are created using different scaling factors:

- Low contrast: 0.5
- High contrast: 1.5

### 5. Gaussian Blur

A Gaussian blur filter with a 5 × 5 kernel is applied to the original image.

### 6. PyTorch Tensor Conversion

The grayscale image, initially represented as a NumPy array, is converted into a PyTorch tensor. Its shape and data type are then inspected.

No deep learning model is trained in this project.

### 7. Image Display

The program displays five versions of the image:

- Original X-ray
- Low contrast
- High contrast
- Brighter X-ray
- Gaussian blur

The displayed images are resized for convenient viewing. The original image data is used for the processing operations.

## Results

The program successfully loaded and processed the X-ray