import cv2
import sys
def __main():
    for i in range(0, 3):
        img = cv2.imread('DSC_7' + str(i + 1) + '.JPG')
        img = getResize(img)
        matImg = img.copy()

        result, jpegImg = cv2.imencode('.jpg', img=img, params=[int(cv2.IMWRITE_JPEG_QUALITY), 80])

        result, pngImg = cv2.imencode('.png', img=img, params=[int(cv2.IMWRITE_PNG_COMPRESSION), 8])

        result, tifImg = cv2.imencode('.tif', img=img, params=[int(cv2.IMWRITE_TIFF_COMPRESSION)])

        print("Mat size = {0}".format (sys.getsizeof(img)))

        print("Jpeg size = {0}".format(sys.getsizeof(jpegImg)))

        print("PNG size = {0}".format(sys.getsizeof(pngImg)))

        print("TIFF size = {0}".format(sys.getsizeof(tifImg)))

        jpegImg = cv2.imdecode(jpegImg, cv2.IMREAD_COLOR)

        pngImg = cv2.imdecode(pngImg, cv2.IMREAD_COLOR)

        tifImg = cv2.imdecode(tifImg, cv2.IMREAD_COLOR)

        cv2.imshow('Original', matImg)
        cv2.imshow('Jpeg', jpegImg)
        cv2.imshow('PNG', pngImg)
        cv2.imshow('Tiff', tifImg)

        cv2.waitKey(0)
        cv2.destroyAllWindows()

def getResize(src):

    basePixSize = 1280

    height = src.shape[0]
    width = src.shape[1]

    largeSize = max(height, width)

    resizeRate = basePixSize / largeSize

    dst = cv2.resize(src, (int(width * resizeRate), int(height * resizeRate)))

    return dst

if __name__ == "__main__":
    print(cv2.__version__)
    __main()