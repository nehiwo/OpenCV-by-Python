import cv2
import numpy as np

def __main():
    img = cv2.imread('IMG1.jpg')
    temple = cv2.imread('IMG2.jpg')
    h, w, _ = temple.shape

    result = cv2.matchTemplate(image=img, templ=temple, method=cv2.TM_CCOEFF)

    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
    x, y = maxLoc
    color = np.array([255., 0., 0.])
    cv2.rectangle(img=img, pt1=(x, y), pt2=(x + w, y + h), color=color, thickness=3)

    cv2.imshow('Final result', img)
    cv2.imshow('Template', temple)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return 0

if __name__ == "__main__":
    print(cv2.__version__)
    __main()