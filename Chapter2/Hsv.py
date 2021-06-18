from Chapter2 import Gray
import cv2

def getHsv(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV_FULL)
    return img

if __name__ == '__main__':
    img = Gray.createImage()
    cv2.imshow('Original', img)

    img = getHsv(img)
    cv2.imshow('HSV', img)
    cv2.waitKey(0)

    cv2.destroyAllWindows()