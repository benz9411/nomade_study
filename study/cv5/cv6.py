# cv2.createTrackbar()
#vlaue: 초기 값 count max 값 , on_chamge: 값이 변경될 때 호출되는 callbak

import cv2
import numpy as np

def change_color(x):
  r = cv2.getTrackbarPos("R", "Image")
  g = cv2.getTrackbarPos("G", "Image")
  b = cv2.getTrackbarPos("B", "Image")
  image[:] = [b, g, r]
  cv2.imshow('Image', image)
  
image = np.zeros((600, 400, 3), np.uint8)
cv2.namedWindow("Image")

cv2.createTrackbar("R", "Image", 0, 255, change_color)
cv2.createTrackbar("G", "Image", 0, 255, change_color)
cv2.createTrackbar("B", "Image", 0, 255, change_color)

cv2.imshow('Image', image)
cv2.waitKey(0)

# Tracker 매우 신기함 