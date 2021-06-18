import cv2

def __main():
    imgs = [None, None, None, None, None]
    for i in range(0, 5):
        imgs[i] = cv2.imread('EdgeTest0' + str(i + 1) + '.jpeg')
        cv2.imshow('Original 0' + str(i + 1), imgs[i])
        imgs[i] = getResize(imgs[i])
        cv2.imshow('Resize 0' + str(i + 1), imgs[i])
        dst = cv2.Canny(image=imgs[i], threshold1=100, threshold2=200)
        cv2.imshow('Edge result 0' + str(i + 1), dst)
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

if __name__ == '__main__':
    print(cv2.__version__)
    __main()