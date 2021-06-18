import cv2
import Blend

def __main():
    img = cv2.imread('IMG_1.JPG')

    img = Blend.getResize(img)
    org = img.copy()
    height, width, channels = img.shape[:3]

    M = cv2.getRotationMatrix2D(center=(width * 9 / 12, height / 4), angle=110, scale=0.3)

    dst = cv2.warpAffine(src=img, M=M, dsize=(width, height))

    cv2.imshow('Original', org)
    cv2.imshow('Final result', dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    print(cv2.__version__)
    __main()