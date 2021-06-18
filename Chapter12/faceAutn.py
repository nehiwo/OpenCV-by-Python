import cv2
import os
import numpy as np
import FacePhoto as fp

def __main():
    global infoFlag
    global faces
    global labels
    global authCount
    message = ""

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.train(faces, np.array(labels))

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

        dst = fp.setReultArea(img)

        camFace = getCameraFace(dst)
        if len(camFace) is not 0:
            infoFlag = True
            camFace = resizeAuthImg(camFace, faces[0])
            camFace = cv2.cvtColor(camFace, cv2.COLOR_BGR2GRAY)
            lableNum, cofidence = recognizer.predict(camFace)

            if cofidence > 50:
                authCount = 0
            else:
                message = 'Lable={0} level={1}'.format(lableNum, int(cofidence))
                infoFlag = False
            print()

def resizeAuthImg(src, baseImg):
    height, width = baseImg.shape[:2]
    dst = cv2.resize(src, (width, height), interpolation=None)
    return dst

def getCameraFace(img):
    global cascade
    global authCount
    face = []
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    bodyRect = cascade.detectMultiScale(image=gray, scaleFactor=1.05, minNeighbors=10,
                                        flag=None, minSize=(100, 100))
    for x, y, w, h in bodyRect:
        authCount += 1
        if authCount == 10:
            face = img[y:y + h, x:x + w]
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 3)
    return face

def loadFace():
    faceImages = list()
    fileCount = 0
    baseImg = []
    path = ('1', '2', '3')

    for i, folder in enumerate(path):
        for fileName in os.listdir(folder):
            print(fileName)
            face = cv2.imread(folder + '/' + fileName)

            if fileCount == 0:
                baseImg = face
            face = resizeAuthImg(face, baseImg)
            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
            faceImages.append(face)
            labels.append(int(folder))
            fileCount += 1
    return faceImages

def setInfo(img, msg):
    cv2.rectangle(img, (50, 50), (600, 120), (0, 0, 0), -1)
    cv2.putText(img=img, text="{0}".format(msg), org=(100, 100), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                fontScale=1.5, color=(255, 255, 255), lineType=cv2.LINE_AA)

if __name__ =="__main__":
    cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    authCount = 0
    infoFlag = False
    labels = []
    faces = loadFace()
    __main()
