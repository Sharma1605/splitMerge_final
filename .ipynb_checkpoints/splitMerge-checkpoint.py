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

def merge_chunks(input_folder, output_path):
    images = []
    for filename in sorted(os.listdir(input_folder)):
        if filename.endswith('.png'):
            filepath = os.path.join(input_folder, filename)
            images.append(Image.open(filepath))
    widths, heights = zip(*(i.size for i in images))
    total_width = sum(widths)
    max_height = max(heights)
    new_image = Image.new('RGB', (total_width, max_height))
    x_offset = 0
    for img in images:
        new_image.paste(img, (x_offset, 0))
        x_offset += img.size[0]
    new_image.save(output_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Split and merge an image')
    parser.add_argument('input_path', type=str, help='Path to input image')
    parser.add_argument('--chunk_size', type=int, default=256, help='Size of image chunks (default: 256)')
    parser.add_argument('--output_folder', type=str, default='chunks', help='Folder to save image chunks (default: chunks)')
    parser.add_argument('--merge', action='store_true', help='Merge the image chunks')
    parser.add_argument('--output_path', type=str, default='output.png', help='Path to save the merged image (default: output.png)')
    args = parser.parse_args()

    if not args.merge:
        save_chunks(args.input_path, args.chunk_size, args.output_folder)
    else:
        merge_chunks(args.output_folder, args.output_path)

