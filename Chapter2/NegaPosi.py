import cv2
import Separation as sp

if __name__ == '__main__':
    img = cv2.imread('DSC_0047.jpg')

    img = sp.getResize(img)
    org = img.copy()

    img = cv2.bitwise_not(img)

    cv2.imshow('Original', org)
    cv2.imshow('Final result', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()