import cv2
import numpy as np

if __name__ == '__main__':
    print(cv2.__version__)

    size = np.array([480, 640, 3])

    img = np.full(size, (255, 255, 255), dtype=np.uint8)

    color = np.array([91., 37., 26.])

    cv2.arrowedLine(img=img, pt1=(200, 200), pt2=(100, 200), color=color, thickness=1)
    cv2.arrowedLine(img=img, pt1=(400, 200), pt2=(100, 300), color=color, thickness=3)

    cv2.imshow('Final result', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()