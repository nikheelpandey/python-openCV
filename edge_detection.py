import cv2
import numpy as np

cap = cv2.VideoCapture (0)

while True:
    _, frame = cap.read()

    laplacian = cv2.Laplacian(frame, cv2.CV_64F)
    sobelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=3)
    cv2.imshow('orignal', frame)
    cv2.imshow('laplacian', laplacian)
    cv2.imshow('sobelx', sobelx)
    cv2.imshow('sobely', sobely)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
cv2.destroyAllwindows()
cap.release()
