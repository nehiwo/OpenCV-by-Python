import cv2
import numpy as np

if __name__ == '__main__':
    print(cv2.__version__)

    size = np.array([480, 640, 3])

    img = np.zeros(size, dtype=np.uint8)

    color = np.array([91., 37., 26.])

    cv2.drawMarker(img=img, position=(50, 200), color=color)
    cv2.drawMarker(img=img, position=(100, 200), color=color, markerType=cv2.MARKER_STAR)
    cv2.drawMarker(img=img, position=(150, 200), color=color, markerType=cv2.MARKER_DIAMOND)
    cv2.drawMarker(img=img, position=(200, 200), color=color, markerType=cv2.MARKER_SQUARE, markerSize=20)
    cv2.drawMarker(img=img, position=(250, 200), color=color, markerType=cv2.MARKER_CROSS, markerSize=30)
    cv2.drawMarker(img=img, position=(300, 200), color=color, markerType=cv2.MARKER_TRIANGLE_DOWN, markerSize=40)
    cv2.drawMarker(img=img, position=(350, 200), color=color, markerType=cv2.MARKER_TRIANGLE_UP, markerSize=40, thickness=5)

    cv2.imshow('Final result', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()