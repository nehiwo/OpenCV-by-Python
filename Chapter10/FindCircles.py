import cv2
import numpy as np
import Histogram as hi

def __main():
    img = cv2.imread('IMG2.jpg')
    img = hi.getResize(img)
    img = getCircles(img)

    cv2.imshow('Final result', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def getCircles(src):
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    ksize = (25, 25)
    gray = cv2.GaussianBlur(gray, ksize, 0, 0)
    ret, gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    cv2.imshow('Preimag', gray)

    circles = cv2.HoughCircles(image=gray, method=cv2.HOUGH_GRADIENT, dp=1, minDist=20,
                               param1=100, param2=20, minRadius=None, maxRadius=None)
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for circle in circles[0, :]:
            dst = cv2.circle(src, (circle[0], circle[1]), circle[2], (255, 0, 255), 2)
    return dst

if __name__ == "__main__":
    print(cv2.__version__)
    __main()