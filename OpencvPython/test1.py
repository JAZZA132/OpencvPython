import cv2
import numpy as np
kernel = np.ones((3,3),np.uint8)
kernel1 = np.ones((10,10),np.uint8)


img = cv2.imread('dontsex.jpg')
img = cv2.resize(img,(0,0),fx=0.5,fy=0.5)

# 灰色
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# 模糊
blur = cv2.GaussianBlur(img, (15,15), 10)
# 邊緣
canny = cv2.Canny(img,200,250)
# 線條膨脹效果
dilate = cv2.dilate(canny,kernel,iterations = 1)
# 線條變細效果
erode  = cv2.erode(dilate,kernel1,iterations = 1)



# cv2.imshow('img',img)
# cv2.imshow('gray',gray)
# cv2.imshow('blur',blur)
cv2.imshow('canny',canny)
cv2.imshow('dilate',dilate)
cv2.imshow('erode',erode)

cv2.waitKey(0)