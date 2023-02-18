import cv2
import numpy as np

def frame_to_array(image_path, scale: float):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    width = int(img.shape[1] * scale)
    height = int(img.shape[0] * scale)
    scaled_img = cv2.resize(img, (width, height))

    thresh = cv2.threshold(scaled_img, 127, 255, cv2.THRESH_BINARY)[1]
    arr = np.where(thresh > 0, 1, 0)

    return arr