import numpy as np
import cv2
import time

def readEveryTenSecods():
    print("\n")
    print("Read frame for every 10 seconds...")
    time.sleep(10.0)

cap = cv2.VideoCapture('../test_data/test_data_2.mp4')
framerate = cap.get(cv2.CAP_PROP_FPS)
capture = 0
while(cap.isOpened()):
    ret, frame = cap.read()
    capture +=1

    if capture == (framerate * 2):
        capture = 0
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', gray)

    if cv2.waitKey(25) & 0xFF == ord('q') : 
        break

cap.release()
cv2.destroyAllWindows()