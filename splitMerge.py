from PIL import Image
import argparse
import os

def split_image(image_path, chunk_size, output_folder):
    with Image.open(image_path) as img:
        width, height = img.size
        for i in range(0, width, chunk_size):
            for j in range(0, height, chunk_size):
                box = (i, j, i+chunk_size, j+chunk_size)
                chunk = img.crop(box)
                chunk.save(os.path.join(output_folder, f"chunk_{i}_{j}.png"))

def merge_images(image_folder, output_path):
    images = []
    for file_name in sorted(os.listdir(image_folder)):
        if file_name.endswith('.png'):
            file_path = os.path.join(image_folder, file_name)
            images.append(Image.open(file_path))
    width, height = images[0].size
    rows = int(height/width)
    new_image = Image.new('RGB', (width*rows, height), (255, 255, 255))
    for i in range(rows):
        for j in range(int(width/height)):
            new_image.paste(images[i*rows+j], (j*width, i*height))
    new_image.save(output_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Split and Merge an Image')
    parser.add_argument('--image', type=str, required=True, help='path to the input image')
    parser.add_argument('--chunk_size', type=int, required=True, help='size of each chunk')
    parser.add_argument('--output_folder', type=str, required=True, help='path to the output folder')
    parser.add_argument('--merge', action='store_true', help='flag to merge the chunks back into the original image')
    parser.add_argument('--output_path', type=str, help='path to the output image')
    args = parser.parse_args()

    if not args.merge:
        split_image(args.image, args.chunk_size, args.output_folder)
    else:
        merge_images(args.output_folder, args.output_path)


