import cv2
import numpy as np

frameCount = 0
thresRate = 150
speedList = np.array([])
aveSpeed = 0

def setSpeedMovie(img):
    global frameCount
    global aveSpeed

    height, width = img.shape[:2]
    y = int(height * 0.8)
    x = int(width * 0.5)
    h = y + 5
    w = x + int(width * 0.3)

    monitor = img[y:h, x:w]
    cv2.imshow("Monitor", monitor)
    monitor = cv2.cvtColor(monitor, cv2.COLOR_BGR2GRAY)

    _, monitor = cv2.threshold(monitor, thresRate, 255, cv2.THRESH_BINARY)

    avePixelNum = np.average(monitor)

    if avePixelNum > 10:
        frameCount += 1
    else:
        print(frameCount)
        if frameCount > 0:
            aveSpeed = getSpeed(frameCount)
        frameCount = 0

    cv2.imshow('Monitor', monitor)
    img = getResize(img)
    color = (255, 255, 255)
    cv2.putText(img, "Speed {0}Km/h".format(aveSpeed), (10, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, color, 1, cv2.LINE_AA)
    return img

def getSpeed(num):
    global speedList
    whiteLine = 8
    oneFrameSec = 1 / 30
    whiteLinePassingSec = num * oneFrameSec
    carSpeed = whiteLine / 1000 / whiteLinePassingSec * 60 * 60

    if carSpeed < 150:
        speedList = np.append(speedList, carSpeed)

    if speedList.size > 10:
        speedList = np.delete(speedList, carSpeed)

    print('Speed = {0} Count = {1}'.format(np.average(speedList), speedList.size))

    return int(np.average(speedList))

def getResize(img):
    basePixSize = 1280
    height, width = img.shape[:2]
    largeSize = max(height, width)
    resizeRate = basePixSize / largeSize
    img = cv2.resize(img, (int(width * resizeRate), int(height * resizeRate)))
    return img

if __name__ == "__main__":
    cap = cv2.VideoCapture("MVI_1186_Trim.mp4")

    if not cap.isOpened():
        print("Not Opened Video Camera")
        exit()

    while True:
        ret, img = cap.read()
        if not ret:
            print("Video Capture Err")
            break

        img = setSpeedMovie(img)

        cv2.imshow("Speed", img)
        if cv2.waitKey(10) > -1:
            break

    cv2.destroyAllWindows()