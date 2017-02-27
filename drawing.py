import numpy as np
import cv2

img = cv2.imread('watch.jpg', cv2.IMREAD_COLOR)

cv2.line(img, (0,0), (1500,1500), (0,0,0), 10)

cv2.rectangle(img, (10,15),(750,700), (255,0,0), 15)

cv2.circle(img, (100,100), 55, (255,125,100), -1)
pts = np.array([[100,15],[23,314],[504,65],[76,807],[98,109]], np.int32)
pts = pts.reshape(-1,1,2)
cv2.polylines(img, [pts], False, (100,70,50), 2)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'Opencv is great', (750,650), font, 1, (200,255,0), 2)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
 
