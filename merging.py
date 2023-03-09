import argparse
from PIL import Image
import os

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
    
    
    merge_parser = subparsers.add_parser("merge", help="Merge small image chunks from a folder into a single image.")
    merge_parser.add_argument("input_folder", help="The path to the input folder.")
    merge_parser.add_argument("output_path", help="The path to the output image.")
    
    args = parser.parse_args()
    
    if args.command == "split":
        split_image(args.image_path, args.chunk_size, args.output_folder)
    elif args.command == "merge":
        merge_images(args.input_folder, args.output_path)
