import cv2

def __main():
    img = cv2.imread('IMG2.jpg')
    img = getResize(img)

    img = getHuman(img)
    cv2.imshow('Final result', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def getHuman(img):
    global cascade

    gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)

    bodyRect = cascade.detectMultiScale(image=gray, scaleFactor=1.01, minNeighbors=5)
    for x, y, w, h in bodyRect:
        cv2.rectangle(img=img, pt1=(x, y), pt2=(x + w, y + h), color=(0, 255, 255), thickness=3)
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