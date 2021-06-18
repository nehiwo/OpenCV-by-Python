import cv2
import numpy as np

if __name__ == '__main__':
    print(cv2.__version__)

    size = np.array([480, 640, 3])

    img = np.full(size, (255, 255, 255), dtype=np.uint8)

    color = np.array([91., 37., 26.])

    cv2.ellipse(img=img, center=(300, 100), axes=(100, 50), angle=0, startAngle=0, endAngle=300, color=color, thickness=-1, lineType=cv2.LINE_AA)
    cv2.ellipse(img=img, center=(300, 200), axes=(300, 100), angle=340, startAngle=0, endAngle=360, color=color, thickness=3, lineType=cv2.LINE_AA)

    cv2.imshow('Final result', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()