import cv2

def __main():
    img = cv2.imread('IMG1.jpg')
    img = getResize(img)

    img = getPeople(img)
    cv2.imshow('Final result', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def getPeople(img):
    gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)

    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(svmdetector=cv2.HOGDescriptor_getDefaultPeopleDetector())
    human, _ = hog.detectMultiScale(img=gray, winStride=(10, 10), padding=(15, 15), scale=None)
    for (x, y, w, h) in human:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 3)
    return img

def getResize(img):
    basedPixSize = 1280
    height, width, = img.shape[:2]
    largeSize = max(height, width)

    resizeRate = basedPixSize / largeSize

    img = cv2.resize(img, (int(width * resizeRate), int(height * resizeRate)))

    return img

if __name__ == "__main__":
    print(cv2.__version__)
    cascadeFile = '../venv/lib/python3.7/site-packages/cv2/data/haarcascade_print(cv2.getBuildInformation())fullbody.xml'
    cascade = cv2.CascadeClassifier(cascadeFile)
    __main()