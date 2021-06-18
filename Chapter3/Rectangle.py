import cv2
import numpy as np

if __name__ == '__main__':
    print(cv2.__version__)

    size = np.array([480, 640, 3])

    img = np.full(size, (255, 255, 255), dtype=np.uint8)

    color = np.array([32., 7., 66.])

    cv2.rectangle(img=img, pt1=(100, 0), pt2=(200, 400), color=color, thickness=-1)
    cv2.rectangle(img=img, pt1=(300, 0), pt2=(500, 400), color=color, thickness=3)

    cv2.imshow('Final result', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()