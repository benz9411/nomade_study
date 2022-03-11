import cv2

image=cv2.imread('images/cat.jpg')

cv2.imshow('Image', image[:,:,0])
cv2.waitKey(0)

image[:,:, 2]=0
cv2.imshow('image',image)
cv2.waitKey(0)