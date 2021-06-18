import cv2
def __main():
    img1 = cv2.imread('IMG_1.JPG')
    img2 = cv2.imread('IMG_2.JPG')

    img1 = getResize(img1)
    img2 = getResize(img2)

    imgMask = getMaskImg(img1, img2)

    cv2.imshow('Original1', img1)
    cv2.imshow('Original2', img2)
    cv2.imshow('Final result', imgMask)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def getMaskImg(img1, img2):
    compImg = cv2.addWeighted(src1=img1, alpha=0.5, src2=img2, beta=0.5, gamma=0)
    return compImg

def getResize(src):
    basePixSize = 1000
    height, width = cv2.imread('IMG_2.JPG').shape[:2]

    largeSize = max(height, width)

    resizeRate = basePixSize / largeSize

    dst = cv2.resize(src, (int(width * resizeRate), int(height * resizeRate)))

    return dst

if __name__ == "__main__":
    print(cv2.__version__)
    __main()