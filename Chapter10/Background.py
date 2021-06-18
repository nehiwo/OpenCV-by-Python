import cv2
import  Histogram as hi

def __main():
    cap = cv2.VideoCapture("MVI_1592.MP4")

    if not cap.isOpened():
        print("Not Opened Video Camera")
        exit()

    while True:
        ret, img = cap.read()
        img = hi.getResize(img)
        org = img
        if not ret:
            print("Video Capture Err")
            break

        subImg = getBackgroundSubMog(org, img)
        cv2.imshow('bugs', subImg)
        if cv2.waitKeyEx(10) > -1:
            break
    cv2.destroyAllWindows()

def getBackgroundSubMog(org, img):
    global fgbg
    subImg = fgbg.apply(img)
    contours, hierarchy = cv2.findContours(image=subImg, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)
    contours = list(filter(lambda x: cv2.contoursArea(x) > 100, contours))
    resultImg = cv2.drawContours(image=org, contours=contours, contourIdx=-1, color=(0, 0, 255), thickness=2)
    return resultImg

if __name__ == "__main__":
    print(cv2.__version__)
    __main()