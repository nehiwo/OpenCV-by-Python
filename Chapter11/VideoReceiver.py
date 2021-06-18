import socket
import cv2
import pickle

if __name__ == "__main__":
    HOST = '192.168.0.10'
    POST = 2000
    BUFFER_SIZE = 4096
    ADDRE = (HOST, POST)

    for num in range(1000):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socketTCP:
            socketTCP.connect(ADDRE)
            fullData = b''
            data = b''
            while True:
                data = socketTCP.recv(BUFFER_SIZE)
                if len(data) <= 0:
                    break

                fullData += data
            print('Data = {}'.format(len(fullData)))
            img = pickle.loads(fullData)
            cv2.imshow('VideoStream', img)
            if cv2.waitKey(1) != -1:
                break

    cv2.destroyAllWindows()