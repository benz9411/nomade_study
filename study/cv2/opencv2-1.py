import cv2


image=cv2.imread('images/cat.jpg')


for i in range(0,100):
    for j in range(0,99):
        image[i,j]=[255,255,255]

image[0:100, 0:100] = [0,0,0]

cv2.imshow('Image',image)
cv2.waitKey(0)

