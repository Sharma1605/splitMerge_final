from PIL import Image
import os

def splitting(img_path,chunk_size):
    img = Image.open(img_path)

    # Get the dimensions of the image
    width, height = img.size

    # Calculate the number of chunks in the x and y directions
    x_chunks = width // chunk_size
    y_chunks = height // chunk_size

    # Create the output directory if it doesn't exist
    if not os.path.exists('projectOC/powerlines-OC/output'):
        os.makedirs('projectOC/powerlines-OC/output')

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
            chunk_filename = f'projectOC/powerlines-OC/output/chunk_{x}_{y}.jpg'
            chunk.save(chunk_filename)

splitting('Timage.jpg',100)

