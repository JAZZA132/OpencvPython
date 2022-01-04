import cv2
import numpy as np
import random

img = cv2.imread('dontsex.jpg')
# 顏色排列是B,G,R
# img  = np.empty((300,300,3),np.uint8)

# for row in range(300):
#     for col in range(img.shape[1]):
#         img[row][col] = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
newimg = img[:150,:200]


cv2.imshow('img',img)
cv2.imshow('newimg',newimg)
cv2.waitKey(0)
















# cap = cv2.VideoCapture(0)
# if not cap.isOpened():
#     print("Cannot open camera")
#     exit()

# while True:   
#     ret,frame = cap.read()
#     if ret:
#         frame = cv2.resize(frame, (0, 0), fx = 0.4, fy =0.4)
#         cv2.imshow('video',frame)
#     else:
#         break
#     if cv2.waitKey(10) == ord('q'):
#         break



# img = cv2.imread('dontsex.jpg')

# # 調整大小
# img = cv2.resize(img, (300,300))
# #秀出圖片
# cv2.imshow('img' ,img)
# # 讓圖片持續存在
# cv2.waitKey(0)