import argparse
from PIL import Image
import os

def split_image(image_path, chunk_size):
    with Image.open(image_path) as img:
        width, height = img.size
        for i in range(0, width, chunk_size):
            for j in range(0, height, chunk_size):
                box = (i, j, i+chunk_size, j+chunk_size)
                yield img.crop(box)

def save_chunks(image_path, chunk_size, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    for i, chunk in enumerate(split_image(image_path, chunk_size)):
        chunk.save(os.path.join(output_folder, f"chunk_{i}.png"))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Split and merge an image')
    parser.add_argument('input_path', type=str, help='Path to input image')
    parser.add_argument('--chunk_size', type=int, default=256, help='Size of image chunks (default: 256)')
    parser.add_argument('--output_folder', type=str, default='chunks', help='Folder to save image chunks (default: chunks)')
