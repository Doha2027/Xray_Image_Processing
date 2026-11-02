import cv2
import numpy as np
import torch

print("X-ray Image Processing")
print("OpenCV version:", cv2.__version__)
print("NumPy version:", np.__version__)

image = cv2.imread("xray.jpg", cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Error: Image not found!")

else:
    print("Image loaded successfully!")
    print("Image dimensions:", image.shape)

    print("Pixel value at (100, 100):", image[100, 100])
    print("Minimum pixel value:", image.min())
    print("Maximum pixel value:", image.max())
    print("Mean pixel intensity:", f"{image.mean():.2f}")

    brighter_image = cv2.add(image, 40)
    print("Mean intensity after brightness adjustment:", f"{brighter_image.mean():.2f}")

    image_tensor = torch.from_numpy(image.copy())
    
    print("Tensor shape:", image_tensor.shape)
    print("Tensor data type:", image_tensor.dtype)

    low_contrast = cv2.convertScaleAbs(image, alpha=0.5, beta=0)
    high_contrast = cv2.convertScaleAbs(image, alpha=1.5, beta=0)
    blurred_image = cv2.GaussianBlur(image, (5, 5), 0)

    display_scale = 0.2

    original_display = cv2.resize(image, None, fx=display_scale, fy=display_scale)
    low_display = cv2.resize(low_contrast, None, fx=display_scale, fy=display_scale)
    high_display = cv2.resize(high_contrast, None, fx=display_scale, fy=display_scale)
    brighter_display = cv2.resize(brighter_image, None, fx=display_scale, fy=display_scale)
    blurred_display = cv2.resize(blurred_image, None, fx=display_scale, fy=display_scale)

    cv2.imshow("Original X-ray", original_display)
    cv2.imshow("Low Contrast", low_display)
    cv2.imshow("High Contrast", high_display)
    cv2.imshow("Brighter X-ray", brighter_display)
    cv2.imshow("Gaussian Blur", blurred_display)

    cv2.waitKey(0)
    cv2.destroyAllWindows()