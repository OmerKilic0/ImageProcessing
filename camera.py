import cv2
import numpy as np

cap = cv2.VideoCapture(0)


while(True):
    ret , frame = cap.read()

    cv2.imshow('Frame', frame)

    saveKey = 0xFF

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    video = cv2.VideoWriter('output.mp4', fourcc, 30, (640, 640))

    if(saveKey == ord('q')):
        video.write(frame)

    k = cv2.waitKey(25)  & 0xFF
    if k == 27:
        cap.release()
        video.release()
        cv2.destroyAllWindows()
        break



