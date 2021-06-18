import cv2

def __main():
    cap = cv2.VideoCapture(0, cv2.CAP_V4L)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    if not cap.isOpened():
        print("Not opened Video Camera")
        exit()

    while True:
        ret, img = cap.read()
        if ret == False:
            print("Video Capture Err")
            break

        img = getResize(img)

        cv2.imshow("Final result", img)

        if cv2.waitKey(10) > -1:
            break

    cap.release()
    cv2.destroyAllWindows()

def getResize(src):
    basePixSize = 720

    height = src.shape[0]
    width = src.shape[1]

    largeSize = max(height, width)

    resizeRate = basePixSize / largeSize

    dst = cv2.resize(src, (int(width * resizeRate), int(height * resizeRate)), interpolation=None)

    return dst

if __name__ == "__main__":
    print(cv2.__version__)

    __main()