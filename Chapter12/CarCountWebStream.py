import cv2
import numpy as np
import bottle
import time

web = bottle.Bottle()

@web.route('/')
def main():
    return bottle.static_file('index.html', root='../Chapter11/')

@web.route('/video_recv')
def video_recv():
    bottle.response.content_type = 'multipart/x-mixed-replace;boundary=frame'
    return __main()

def __main():
    cap = cv2.VideoCapture('PXL_20201011_005931739.mp4')

    while True:
        ret, img = cap.read()
        if not ret:
            print("Video Capture Err")
            break

        img = rs.getResize(img)
        img = getArea(img)

        cv2.imshow('Finel result', img)
        if cv2.waitKey(10) > -1:
            break

    cap.release()

def getArea(img):
    w = 310
    h = 5

    x1 = 570
    y1 = 630
    x2 = x1 + w
    y2 = y1 + h

    x3 = 930
    y3 = 630
    x4 = x3 + w
    y4 = y3 + h

    area1 = img[y1:y2, x1:x2]
    area2 = img[y3:y4, x3:x4]
    area1 = getBackgroundSubMog(img, area1, 1)
    area2 = getBackgroundSubMog(img, area2, 2)

    img[y1:y2, x1:x2] = cv2.cvtColor(area1, cv2.COLOR_GRAY2BGR)
    img[y3:y4, x3:x4] = cv2.cvtColor(area2, cv2.COLOR_GRAY2BGR)

    return img

def getBackgroundSubMog(img, area, loadLine):
    global inside
    global outside
    global outsideZeroCount
    global insideZeroCount

    monitor = fgbg.apply(area)
    avePixelNum = np.average(monitor)

    print("Average = {0}".format(avePixelNum))

    if loadLine == 2:
        if avePixelNum < 5:
            outsideZeroCount += 1
        else:
            if outsideZeroCount > 5:
                outside += 1
                outsideZeroCount = 0
    if loadLine == 1:
        if avePixelNum < 5:
            insideZeroCount += 1
        else:
            if insideZeroCount > 5:
                inside += 1
                insideZeroCount = 0

    cv2.putText(img=img, text="{0}".format(outside), org=(1100,680),
                fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1.5, color=(255, 255, 255),
                lineType=cv2.LINE_AA)

    return monitor

if __name__ == "__main__":
    outside = 0
    inside = 0
    outsideZeroCount = 0
    insideZeroCount = 0

    fgbg = cv2.bgsegm.createBackgroundSubtractorMOG(history=120)
    web.run(host='192.168.0.10', post=8080)