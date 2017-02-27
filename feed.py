import cv2
import numpy as np

cap = cv2.VideoCapture(0)

cv2.imshow('feed', cap)
cv2.waitKey(0)
cv2.destroyAllWindows()
