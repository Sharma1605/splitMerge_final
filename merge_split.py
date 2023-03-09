# import os
# import argparse
# from PIL import Image

# # Define argparse arguments
# parser = argparse.ArgumentParser(description='Split and merge an image')
# parser.add_argument('input_image', type=str, help='path to input image')
# parser.add_argument('output_folder', type=str, help='path to output folder')
# parser.add_argument('--chunk-size', type=int, default=256, help='size of each image chunk')

# # Parse arguments
# args = parser.parse_args()

# # Load input image
# input_image = Image.open(args.input_image)

# # Create output folder if it doesn't exist
# if not os.path.exists(args.output_folder):
#     os.makedirs(args.output_folder)

# # Split input image into chunks
# width, height = input_image.size
# chunk_size = args.chunk_size
# for i in range(0, height, chunk_size):
#     for j in range(0, width, chunk_size):
#         box = (j, i, j+chunk_size, i+chunk_size)
#         chunk = input_image.crop(box)
#         chunk_filename = f'{args.output_folder}/{i}_{j}.png'
#         chunk.save(chunk_filename)

# # Merge image chunks into a single image
# output_image = Image.new('RGB', (width, height))
# for i in range(0, height, chunk_size):
#     for j in range(0, width, chunk_size):
#         chunk_filename = f'projectOC/powerlines-OC/output_folder/{i}_{j}.png'
#         if os.path.exists(chunk_filename):
#             chunk = Image.open(chunk_filename)
#             output_image.paste(chunk, (j, i))

# # Save output image
# output_image.save(f'{args.output_folder}/merged.png')
import argparse
import os
from PIL import Image

def split_image(image_path, chunk_size, output_folder):
    image = Image.open(image_path)
    width, height = image.size
    for i in range(0, width, chunk_size):
        for j in range(0, height, chunk_size):
            box = (i, j, i+chunk_size, j+chunk_size)
            chunk = image.crop(box)
            chunk_path = os.path.join(output_folder, f"{i}_{j}.png")
            chunk.save(chunk_path)

def merge_images(input_folder, output_path):
    chunks = []
    for filename in os.listdir(input_folder):
        chunk_path = os.path.join(input_folder, filename)
        chunk = Image.open(chunk_path)
        chunks.append((int(filename.split("_")[0]), int(filename.split("_")[1]), chunk))
    chunks.sort()
    width = max(x+w for x,y,w,h in chunks)
    height = max(y+h for x,y,w,h in chunks)
    image = Image.new("RGBA", (width, height))
    for x, y, chunk in chunks:
        image.paste(chunk, (x, y))
    image.save(output_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Split an image into small chunks and store them in a folder, and then merge them back into the same image using argparse and two different command lines.")
    subparsers = parser.add_subparsers(dest="command", required=True)
    
    split_parser = subparsers.add_parser("split", help="Split an image into small chunks and store them in a folder.")
    split_parser.add_argument("image_path", help="The path to the input image.")
    split_parser.add_argument("chunk_size", type=int, help="The size of each chunk.")
    split_parser.add_argument("output_folder", help="The path to the output folder.")
    
    merge_parser = subparsers.add_parser("merge", help="Merge small image chunks from a folder into a single image.")
    merge_parser.add_argument("input_folder", help="The path to the input folder.")
    merge_parser.add_argument("output_file", help="The path to the output image.")
    
    args = parser.parse_args()
    
    if args.command == "split":
        split_image(args.image_path, args.chunk_size, args.output_folder)
    elif args.command == "merge":
        merge_images(args.input_folder, args.output_file)

