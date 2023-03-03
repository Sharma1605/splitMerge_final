import cv2
import os
import numpy as np

chunk_size = 256
rows = 20
cols = 20

# Create an empty image to store the merged chunks
merged_image = np.zeros((rows * chunk_size, cols * chunk_size, 3), dtype=np.uint8)

# Loop over the rows and columns of the image, and insert each chunk into the merged image
for r in range(rows):
    for c in range(cols):
        chunk_path =f'chunks/chunk_{r}_{c}.jpg'
        chunk = cv2.imread(chunk_path)
        merged_image[r*chunk_size:(r+1)*chunk_size, c*chunk_size:(c+1)*chunk_size] = chunk

# Save the merged image
cv2.imwrite('merged_image.jpg', merged_image)
cv2.imshow(merged_image)
