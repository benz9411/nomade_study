import cv2

#ROI 관심있는걸 쓴다

image=cv2.imread('images/cat.jpg')

roi = image[200:350, 50:200]

image[0:150, 0:150] = roi

cv2.imshow('Image', image)
cv2.waitkey(0)