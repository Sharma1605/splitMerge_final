import numpy as np
from PIL import Image

# Load the image using OpenCV
img = Image.open('Timage.jpg')

# Define the size of each chunk
chunk_size = 128

# Split the image into small chunks
chunks = [img[x:x+chunk_size, y:y+chunk_size] for x in range(0, img.shape[0], chunk_size) for y in range(0, img.shape[1], chunk_size)]
