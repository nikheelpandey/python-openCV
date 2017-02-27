import cv2
import numpy as np

cap = cv2.VideoCapture ('hgraph.mp4')
fgbg = cv2.BackgroundSubtractorMOG2()

while (1):
	ret, frame = cap.read()
	fgmask = fgbg.apply(frame)

	cv2.imshow('orignal', frame)
	cv2.imshow('fg', fgmask)
	k = cv2.waitKey(30) & 0xff
	if k == 27:
		break
cap.release()
cv2.destroyAllWindows()