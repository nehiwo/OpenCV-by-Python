import cv2
import Hog

def __main():
    img = cv2.imread('IMG1.jpg')

    img = Hog.getResize(img)

    x, y, w, h = cv2.selectROI('Final result', img=img, showCrosshair=True, fromCenter=True)

    dst = img[y:y+h, x:x+w]

    cv2.imshow('Final result', dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    print(cv2.__version__)
    __main()