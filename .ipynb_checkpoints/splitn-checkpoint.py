from PIL import Image
import os

# Open the image
img = Image.open('Timage.jpg')

# Set the chunk size (width and height)
chunk_size = 100

# Get the dimensions of the image
width, height = img.size

# Calculate the number of chunks in the x and y directions
x_chunks = width // chunk_size
y_chunks = height // chunk_size

# Create the output directory if it doesn't exist
if not os.path.exists('output'):
    os.makedirs('output')

# Loop through each chunk and save it as a separate file
for x in range(x_chunks):
    for y in range(y_chunks):
        # Calculate the coordinates of the chunk
        left = x * chunk_size
        upper = y * chunk_size
        right = (x + 1) * chunk_size
        lower = (y + 1) * chunk_size
        
        # Crop the image to the chunk
        chunk = img.crop((left, upper, right, lower))
        
        # Save the chunk as a separate file
        chunk_filename = f'output/chunk_{x}_{y}.jpg'
        chunk.save(chunk_filename)


