from PIL import Image
import os
import sys

def split_image(image_path, chunk_size):
    """Splits an image into small chunks and stores them in a folder"""

    # Open the image and get its size
    with Image.open(image_path) as image:
        width, height = image.size

        # Determine the number of chunks to split the image into
        x_chunks = width // chunk_size
        y_chunks = height // chunk_size

        # Create the output folder if it does not exist
        output_folder = os.path.splitext(image_path)[0]
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Split the image into chunks and save them to the output folder
        for i in range(x_chunks):
            for j in range(y_chunks):
                left = i * chunk_size
                top = j * chunk_size
                right = left + chunk_size
                bottom = top + chunk_size
                chunk = image.crop((left, top, right, bottom))
                chunk_path = os.path.join(output_folder, f"chunk_{i}_{j}.png")
                chunk.save(chunk_path)

if __name__ == "__main__":
    # Get the image path and chunk size from the command line arguments
    image_path = sys.argv[1]
    chunk_size = int(sys.argv[2])

    # Split the image into small chunks and store them in a folder
    split_image(image_path, chunk_size)

