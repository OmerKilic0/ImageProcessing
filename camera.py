import cv2
import numpy as np

cap = cv2.VideoCapture(0)

if(cap.isOpened() == False):
    print("Cap is not opened")

while(cap.isopened()):
    ret , frame = cap.read()

    cv2.imshow('Frame', frame)
    
