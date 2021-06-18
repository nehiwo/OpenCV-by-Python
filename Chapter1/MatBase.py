import cv2
import numpy as np

if __name__ == '__main__':

    size = np.array([720, 1280, 3])

    redColor = np.array([127., 0., 255.])

    img = np.full(size, redColor, dtype=np.uint8)

    cv2.imshow('Red', img)
    cv2.waitKey(0)

    cv2.destroyAllwindow()