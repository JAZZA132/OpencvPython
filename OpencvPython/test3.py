import cv2
import numpy as np
img = cv2.imread('wang.jpg')
img = cv2.resize(img,(0,0),fx =0.5,fy =0.5)

hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

cv2.imshow('img',img)
cv2.waitKey(0)