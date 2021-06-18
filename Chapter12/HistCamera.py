import cv2
import numpy as np
import CameraInCar as cic

def __main():
    cap = cv2.VideoCapture(0, cv2.CAP_V4L)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    if not cap.isOpened():
        print("Not Opened Video Camera")
        exit()

    while True:
        ret, img = cap.read()

        if not ret:
            print("Video Capture Err")
            break

        org = img.copy()
        img = cic.getResize(img)
        base = aveImg(img)
        rbRate = getCompHist(img, base)
        setMessage(org, rbRate)
        cv2.imshow('Histgram Camera', org)
        cv2.imshow('base Camera', base)
        if cv2.waitKey(10) > -1:
            break

    cap.release()
    cv2.destroyAllWindows()

def aveImg(img):
    global frame
    global buffer
    global baseImg

    baseImg = np.zeros_like(img, dtype='int32')
    buffer.append(img)
    frame += 1
    print(frame)
    if frame > 100:
        buffer.pop(0)
    i = 0
    for tempImg in buffer:
        baseImg += tempImg
        i += 1
    dst = np.uint8(baseImg // i)
    return dst

def getCompHist(TargetImg, baseImg):
    TargetImg = cv2.cvtColor(TargetImg, cv2.COLOR_BGR2GRAY)
    baseImg = cv2.cvtColor(baseImg, cv2.COLOR_BGR2GRAY)

    hist1 = cv2.calcHist(images=[TargetImg], channels=[0], mask=None, histSize=[256], ranges=[0, 256])
    hist2 = cv2.calcHist(images=[baseImg], channels=[0], mask=None, histSize=[256], ranges=[0, 256])

    histResult = cv2.compareHist(H1=hist1, H2=hist2, method=cv2.HISTCMP_CORREL)
    compRate = np.uint8(histResult * 100)
    return compRate

def setMessage(img, compRate):
    if compRate < 90 or compRate > 100:
        color = (0, 0, 255)
    else:
        color = (0, 0, 0)
    cv2.rectangle(img, (5, 5), (200, 50), color, -1)
    cv2.putText(img=img, text="R/B={0}".format(compRate), org=(18, 35),
                fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1,
                color=(255, 255, 255), lineType=cv2.LINE_AA)

if __name__ == "__main__":
    buffer = list()
    frame = 0
    __main()