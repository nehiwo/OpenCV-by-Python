import cv2
import numpy as np

if __name__ == '__main__':
    print(cv2.__version__)

    size = np.array([480, 640, 3])

    img = np.full(size, (255, 255, 255), dtype=np.uint8)

    color = np.array([91., 37., 26.])

    pt1 = np.array([[100, 20], [230, 40], [320, 100], [380, 150], [290, 200], [200, 330], [150, 300]], np.int32)
    pt2 = np.array([[50, 100], [100, 50], [250, 200], [100, 150]], np.int32)

    cv2.polylines(img=img, pts=[pt1, pt2], isClosed=True, color=color, thickness=3, lineType=cv2.LINE_AA)

    pts = np.array([[400, 100], [500, 350], [300, 350]], np.int32)

    cv2.fillConvexPoly(img=img, points=pts, color=color, lineType=cv2.LINE_AA)

    cv2.imshow('Final result', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()