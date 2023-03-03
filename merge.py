from PIL import Image
merged_img = np.zeros_like(img)
i = 0
for x in range(0, img.shape[0], chunk_size):
    for y in range(0, img.shape[1], chunk_size):
        merged_img[x:x+chunk_size, y:y+chunk_size] = chunks[i]
        i += 1

# Save the merged image using OpenCV
img.save('merged_image.jpg', merged_img)
img.show()
