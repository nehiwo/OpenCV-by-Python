import cv2
import numpy as np

if __name__ == '__main__':
    print(cv2.__version__)

    size = np.array([480, 640, 3])

    img = np.zeros(size, dtype=np.uint8)

    color = np.array([43., 91., 11.])

    cv2.putText(img=img, text='CQ Publishing', org=(200, 100),
                fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1.0,
                color=color, lineType=cv2.LINE_AA)
    cv2.putText(img=img, text='CQ Publishing', org=(200, 150),
                fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=1.0,
                color=color, lineType=cv2.LINE_AA)
    cv2.putText(img=img, text='CQ Publishing', org=(200, 200),
                fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=1.0,
                color=color, lineType=cv2.LINE_AA)
    cv2.putText(img=img, text='CQ Publishing', org=(200, 250),
                fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=1.0,
                color=color, lineType=cv2.LINE_AA)
    cv2.putText(img=img, text='CQ Publishing', org=(200, 300),
                fontFace=cv2.FONT_HERSHEY_TRIPLEX, fontScale=1.0,
                color=color, lineType=cv2.LINE_AA)


    cv2.imshow('Final result', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()