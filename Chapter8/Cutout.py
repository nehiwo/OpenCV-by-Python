import cv2
import Encode as resize

def __main():
    img = cv2.imread('DSC_71.JPG')
    img = resize.getResize(img)
    y = 600
    x = 700
    h = 800
    w = 1000
    dst = img[y:h, x:w]

    cv2.imshow('Original', img)
    cv2.imshow('Final result', dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return dst

if __name__ == "__main__":
    print(cv2.__version__)
    __main()