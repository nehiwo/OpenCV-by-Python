import cv2
import Blend
import numpy as np

def __main():
    img = cv2.imread('IMG_2.JPG')

    img = Blend.getResize(img)
    org = img.copy()
    height, width, channels = img.shape[:3]

    pts1 = np.float32([[388, 174], [943,170], [243, 717], [1068, 720]])

    color = (255, 0, 0)
    for i, pos in enumerate(pts1):
        cv2.circle(img=org, center=(pos[0], pos[1]), radius=5, color=color,
                   thickness=-1, lineType=cv2.LINE_AA)

    pts2 = np.float32([[100, 100], [720, 100], [100, 960], [720, 960]])

    M = cv2.getPerspectiveTransform(src=pts1, dst=pts2)

    dst = cv2.warpPerspective(src=img, M=M, dsize=(width, height))

    cv2.imshow('Original', org)
    cv2.imshow('Final result', dst)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    print(cv2.__version__)
    __main()