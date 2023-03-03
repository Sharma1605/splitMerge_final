from PIL import Image
import numpy as np
# Load the image
image = Image.open('Timage.jpg')
# Convert the image to a numpy array
image_array = np.array(image)

# Set the size of the chunks
chunk_size = 64
# Split the image into chunks
chunks = [image_array[x:x+chunk_size,y:y+chunk_size] for x in range(0, image_array.shape[0], chunk_size) for y in range(0, image_array.shape[1], chunk_size)]
# Merge the chunks into a single image
rows = []
for i in range(0, len(chunks), int(image_array.shape[1]/chunk_size)):
    row = np.concatenate(chunks[i:i+int(image_array.shape[1]/chunk_size)], axis=1)
    rows.append(row)

merged_image = np.concatenate(rows, axis=0)

# Save the merged image
merged_image = Image.fromarray(merged_image)
merged_image.save('merged_image.jpg')
