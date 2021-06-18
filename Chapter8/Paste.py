import cv2
import Cutout as cut

def __main():
    img = cv2.imread('DSC_72.JPG')
    overLay = cut.__main()
    org = img.copy()

    height, width, _ = overLay.shape

    x = 50
    y = 30
    img[y: y + height, x: x + width ] = overLay
    cv2.imshow('Final result', img)
    cv2.imshow('Original', org)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    print(cv2.__version__)
    __main()