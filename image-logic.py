import cv2
import numpy as np


img1 = cv2.imread('down1.jpg')
img2 = cv2.imread('down2.jpg')

img11 = img1[1:433, 1:640]
img22 = img2[1:433, 1:640]

weighted = cv2.addWeighted(img11, 0.5, img22, 0.5, 0)

cv2.imshow('weighted', weighted)
cv2.waitKey(0)
cv2.destroyAllwindows()
