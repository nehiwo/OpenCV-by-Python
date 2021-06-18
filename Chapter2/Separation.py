import cv2

def getResize(src):

    basePixSize = 1280

    height = src.shape[0]
    width = src.shape[1]

    largeSize = max(height, width)

    resizeRate = basePixSize / largeSize

    dst = cv2.resize(src, (int(width * resizeRate), int(height * resizeRate)))

    return dst

if __name__ == '__main__':
    img = cv2.imread('DSC_0047.jpg')
    img = getResize(img)
    org = img.copy()

    bgr = cv2.split(m=img)

    cv2.imshow('Blue', bgr[0])
    cv2.imshow('Green', bgr[1])
    cv2.imshow('Red', bgr[2])
    cv2.imshow('Original', org)
    cv2.waitKey(0)
    cv2.destroyAllWindows()