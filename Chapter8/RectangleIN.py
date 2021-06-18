import cv2
import numpy as np
import random

def __main():
    img = createBaseImage()
    org = img.copy()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    rect = cv2.boundingRect(array=gray)
    cv2.rectangle(org, rect, (0, 255, 255))

    cv2.imshow('Final result', org)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def __setNoise(img, color):
    global pts
    height, width, channels = img.shape[:3]
    for num in range(50):
        x = int(random.uniform((width / 2) - (width / 4), (width / 2) + (width / 4)))
        y = int(random.uniform((height / 2) - (height / 4), (height / 2) + (height / 4)))
        angle = (x, y, 5, 5)
        cv2.rectangle(img, angle, color, -1)

        pts = np.append(pts, np.array([[x, y]]), axis=0)

    return img

def createBaseImage():
    size = (480, 640, 3)

    color = (0., 0., 0.)

    img = np.full(size, color, dtype=np.uint8)

    color = (255., 255., 255.)
    img = __setNoise(img, color)

    return img

if __name__ == "__main__":
    print(cv2.__version__)
    pts = np.empty((0, 2), int)
    __main()