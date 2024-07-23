import cv2
import numpy as np

cap = cv2.VideoCapture(0)


while(True):
    ret , frame = cap.read()

    cv2.imshow('Frame', frame)
    
    k = cv2.waitKey(25)  & 0xFF
    if k == 27:
        cap.release()
        cv2.destroyAllWindows()
        break



