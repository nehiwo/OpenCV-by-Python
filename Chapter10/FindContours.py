import cv2
import numpy as np
import Histogram as hi

def __main():
    img = cv2.imread('IMG2.jpg')
    img = hi.getResize(img)
    img = getFindContours(img)

    cv2.imshow('Final result', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def getFindContours(src):
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    ksize = (25, 25)
    gray = cv2.GaussianBlur(gray, ksize, 0, 0)
    ret, climg = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    cv2.imshow('Preimag', gray)

    contours, _ = cv2.findContours(image=climg, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_SIMPLE)
    result = cv2.drawContours(image=src, contours=contours, contourIdx=0, color=(0, 0, 255),
                              thickness=2, lineType=cv2.LINE_AA)

    cv2.imshow('Result', result)

    for i, cont in enumerate(contours):
        rect = cv2.minAreaRect(cont)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        dst = cv2.drawContours(src, [box], -1, (255, 255, 0), 2, cv2.LINE_AA)
        cv2.ellipse(dst, rect, (0, 255, 255), 2)

    return dst

if __name__ == "__main__":
    print(cv2.__version__)
    __main()