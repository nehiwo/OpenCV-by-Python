import socketserver
import cv2
import pickle

HOST = '192.168.0.10'
POST = 2000
BUFFER_SIZE = 4096
ADDRE = (HOST, POST)
cap = None

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        ret, img = cap.read()
        if not ret:
            print("Video Capture Err")
            exit()
        bData = pickle.dumps(img)
        self.request.send(bData)

if __name__ == "__main__":
    cap = cv2.VideoCapture(0, cv2.CAP_V4L)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    if not cap.isOpened():
        print("Not Opened Video Camera")
        exit()

    with socketserver.TCPServer((ADDRE), MyTCPHandler) as server:
        server.serve_forever()