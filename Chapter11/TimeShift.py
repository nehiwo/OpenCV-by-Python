import cv2
import numpy as np

def __main():
    width = 1280.
    height = 720.
    cap = cv2.VideoCapture(0, cv2.CAP_V4L)

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

    if not cap.isOpened():
        print("Not Opened Video Camera")
        exit()

    while True:
        ret, img = cap.read()
        img = cv2.flip(src=img, flipCode=1)
        buf = videoBuf(img)
        cv2.imshow('Late', buf)
        cv2.imshow('Real', img)
        if cv2.waitKey(10) > -1:
            break

    cap.release()
    cv2.destroyAllWindows()
    return 0

def videoBuf(img):
    global frame
    global buffer

    buffer.append(img)
    frame += 1
    print(frame)
    if frame > 200:
        dst = buffer.pop(0)
    else:
        size = img.shape
        dst = np.zeros(size, dtype=np.uint8)

    return dst

if __name__ == "__main__":
    print(cv2.__version__)
    buffer = list()
    frame = 0
    __main()