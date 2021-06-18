import Gray
import cv2

def getBinary(src):
    ret, c_dst = cv2.threshold(src, thresh=128, maxval=255, type=cv2.THRESH_BINARY)
    cv2.imshow('Binary Color', c_dst)

    src = Gray.getGray(src)
    cv2.imshow('Gray', src)

    ret, dst = cv2.threshold(src, thresh=128, maxval=255, type=cv2.THRESH_BINARY)

    return dst

def getBinaryInv(src):
    ret, c_dst = cv2.threshold(src, thresh=128, maxval=255, type=cv2.THRESH_BINARY_INV)
    cv2.imshow('Binary Color', c_dst)

    src = Gray.getGray(src)
    cv2.imshow('Gray', src)

    ret, dst = cv2.threshold(src, thresh=128, maxval=255, type=cv2.THRESH_BINARY_INV)

    return dst

def getBinaryOtsu(src):
    src = Gray.getGray(src)
    cv2.imshow('Gray', src)

    ret, dst = cv2.threshold(src, thresh=0, maxval=255, type=cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    return dst

def getBinaryTriangle(src):
    src = Gray.getGray(src)
    cv2.imshow('Gray', src)

    ret, dst = cv2.threshold(src, thresh=0, maxval=255, type=cv2.THRESH_BINARY + cv2.THRESH_TRIANGLE)

    return dst

def getBinaryTozero(src):
    ret, c_dst = cv2.threshold(src, thresh=128, maxval=255, type=cv2.THRESH_TOZERO)
    cv2.imshow('Binary Color', c_dst)

    src = Gray.getGray(src)
    cv2.imshow('Gray', src)

    ret, dst = cv2.threshold(src, thresh=128, maxval=255, type=cv2.THRESH_TOZERO)

    return dst

def getBinaryTozeroInv(src):
    ret, c_dst = cv2.threshold(src, thresh=128, maxval=255, type=cv2.THRESH_TOZERO_INV)
    cv2.imshow('Binary Color', c_dst)

    src = Gray.getGray(src)
    cv2.imshow('Gray', src)

    ret, dst = cv2.threshold(src, thresh=128, maxval=255, type=cv2.THRESH_TOZERO_INV)

    return dst

def getBinaryTrank(src):
    ret, c_dst = cv2.threshold(src, thresh=128, maxval=255, type=cv2.THRESH_TRUNC)
    cv2.imshow('Binary Color', c_dst)

    src = Gray.getGray(src)
    cv2.imshow('Gray', src)

    ret, dst = cv2.threshold(src, thresh=128, maxval=255, type=cv2.THRESH_TRUNC)

    return dst

if __name__ == '__main__':
    img = Gray.createImage()
    cv2.imshow('Original', img)

    #img = getBinary(img)
    #img = getBinaryInv(img)
    #img = getBinaryOtsu(img)
    #img = getBinaryTriangle(img)
    #img = getBinaryTozero(img)
    #img = getBinaryTozeroInv(img)
    img = getBinaryTrank(img)
    cv2.imshow('Final result', img)
    cv2.waitKey(0)

    cv2.destroyAllWindows()