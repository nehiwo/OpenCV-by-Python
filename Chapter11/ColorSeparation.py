import cv2
import numpy as np
import copy

def __main():
    global K_NUMBERS;
    img = cv2.imread('../Chapter10/IMG2.jpg')
    img = getResize(img)

    colors = img.reshape(-1, 3)
    colors = colors.astype(np.float32)

    criteria = cv2.TERM_CRITERIA_MAX_ITER + cv2.TERM_CRITERIA_EPS, 10, 1.0

    _, labels, center = cv2.kmeans(data=colors, K=K_NUMBERS, bestLabels=None,
                                   criteria=criteria, attempts=10, flags=cv2.KMEANS_RANDOM_CENTERS,
                                   centers=None)

    _, colorWait = np.unique(labels, axis=0, return_counts=True)

    dst = center[labels.ravel()].reshape(img.shape)
    dst = dst.astype(np.uint8)
    BubbleSort(colorWait, center)

    cv2.imshow('ESP', dst)
    cv2.imshow('ORG', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def setColorBar(colorWait, center):
    size = (100, 400, 3)
    img = np.zeros(size, dtype=np.uint8)
    cv2.rectangle(img, (0, 0), (size[1], size[0]), (255, 255, 255), -1)
    totalPixels = 0
    next_x = 0
    for pixels in colorWait:
        totalPixels += pixels

    for num in range(K_NUMBERS):
        height = totalPixels / colorWait[num]
        x = next_x
        y = 0
        w = int(size[1] / height + 1)
        h = 100

        next_x = x + w
        angle = (x, y, w, h)
        color = (int(np.ceil(center[num][0])),
                 int(np.ceil(center[num][1])),
                 int(np.ceil(center[num][2])))
        cv2.rectangle(img, angle, color, -1)

    cv2.imshow("Dominant Color", img)

def getResize(src):
    basePixSize = 1280
    height, width = src.shape[:2]
    largeSize = max(height, width)
    resizeRate = basePixSize / largeSize
    dst = cv2.resize(src, (int(width * resizeRate), int(height * resizeRate)))
    return dst

def BubbleSort(colorWait, center):
    for i in range(len(colorWait)):
        for j in range(len(colorWait) - 1, i, -1):
            if colorWait[j] > colorWait[j - 1]:
                colorWait[j], colorWait[j - 1] = colorWait[j - 1], colorWait[j]
                center[j], center[j - 1] = copy.copy(center[j - 1]), copy.copy(center[j])
    setColorBar(colorWait, center)

if __name__ == "__main__":
    print(cv2.__version__)
    K_NUMBERS = 6
    __main()