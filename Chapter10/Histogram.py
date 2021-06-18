import cv2
import numpy as np

def __main():
    img = cv2.imread('IMG2.jpg')
    img = getHist(img)
    cv2.imshow('Final result', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def getResize(src):
    global shotSize
    basePixSize = 1280
    height, width = src.shape[:2]
    largeSize = max(height, width)
    resizeRate = basePixSize / largeSize
    shotSize = min(height, width) * resizeRate
    dst = cv2.resize(src, (int(width * resizeRate), int(height * resizeRate)))
    return dst

def getHist(img):
    img = getResize(img)
    channel = 3
    upper = 70
    size = np.array([upper * 3, 256, channel])
    blackColor = np.array([0, 0, 0])
    hist = np.full(size, blackColor, dtype=np.uint8)
    height, width, _ = hist.shape[:3]

    for j in range(channel):
        bgrHist = cv2.calcHist(images=[img], channels=[j], mask=None, histSize=[256], ranges=[0, 256])
        cv2.normalize(src=bgrHist, dst=bgrHist, alpha=0, beta=upper, norm_type=cv2.NORM_MINMAX)

        color = [0, 0, 0]
        color[j] = 255
        baseLine = j * upper + upper
        for i in range(0, 256):
            vertical = bgrHist[i]
            cv2.line(hist, (i, baseLine), (i, baseLine - vertical), color)

    y = 10
    x = 10
    img[y:y+height, x:x+width] = hist
    return img

if __name__ == "__main__":
    print(cv2.__version__)
    __main()