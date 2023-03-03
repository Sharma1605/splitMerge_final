import cv2

img = cv2.imread('/content/drive/MyDrive/images_grid/Toimage.JPG')
chunk_size = 256
rows = img.shape[0] // chunk_size
cols = img.shape[1] // chunk_size
chunks = []

for r in range(rows):
    for c in range(cols):
        chunk = img[r*chunk_size:(r+1)*chunk_size, c*chunk_size:(c+1)*chunk_size]
        cv2.imwrite(f'chunks/chunk_{r}_{c}.jpg', chunk)
