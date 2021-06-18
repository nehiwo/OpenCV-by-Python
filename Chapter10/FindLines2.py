import cv2
import numpy as np
import Histogram as hi

def __main():
    img = cv2.imread('IMG2.jpg')
    img = hi.getResize(img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, bw = cv2.threshold(src=gray, thresh=0, maxval=255, type=cv2.THRESH_OTSU)
    bw = cv2.Canny(bw, 10, 200, apertureSize=3)

    lines = cv2.HoughLinesP(image=bw, rho=1, theta=np.pi/180, threshold=100,
                            maxLineGap=10, minLineLength=100)

    if lines is not None:
        for x1, y1, x2, y2 in lines[:, 0]:
            cv2.line(img, (x1, y1), (x2, y2), (0, 255, 255), 2)

    cv2.imshow('Edges', bw)
    cv2.imshow('Final result', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    print(cv2.__version__)
    __main()