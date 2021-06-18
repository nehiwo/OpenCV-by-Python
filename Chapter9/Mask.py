import cv2
import numpy as np
import Blend

def __main():
    img = cv2.imread('IMG_1.JPG')

    img = Blend.getResize(img)
    org = img.copy()
    mask = baseImage(img)

    maskImg = getMaskImg(img, mask)

    cv2.imshow('Original', org)
    cv2.imshow('Mask', mask)
    cv2.imshow('Final result', maskImg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def getMaskImg(img, mask):
    mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
    compImg = cv2.copyTo(src=img, mask=mask)
    return compImg

def baseImage(img):
    height, width = img.shape[:2]
    size = np.array([height, width, 3])
    img = np.zeros(size, dtype=np.uint8)
    centerX = int(width / 2)
    centerY = int(height / 2)
    w = int(centerX * 0.6)
    h = int(centerY * 0.6)
    color = np.array([255., 255., 255.])
    cv2.ellipse(img=img, center=(centerX, centerY),
                axes=(w, h), angle=0, startAngle=0, endAngle=360, color=color,
                thickness=-1, lineType=cv2.LINE_AA)
    return img

if __name__ == "__main__":
    print(cv2.__version__)
    __main()