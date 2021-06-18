import cv2
import numpy as np

def __main():
    global mask, img
    cv2.namedWindow("Repair")
    cv2.setMouseCallback("Repair", onMouse, None)

    while True:
        img = cv2.inpaint(img, mask, 3, cv2.INPAINT_TELEA)
        cv2.imshow("Repair", img)
        if cv2.waitKey(10) > -1:
            break

def onMouse(event, x, y, flags, param):
    global drawing

    if event == cv2.EVENT_MOUSEMOVE:
        print("x = ", x)
        print("y = ", y)

        if drawing:
            cv2.circle(mask, (x, y), 3, 255, -1)

    elif event == cv2.EVENT_LBUTTONDOWN:
        drawing = True

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False

if __name__ == "__main__":
    print(cv2.__version__)

    img = cv2.imread('../Chapter10/IMG1.jpg')
    h, w, c = img.shape
    mask = np.zeros((h, w, 1), dtype=np.uint8)
    drawing = False

    __main()