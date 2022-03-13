#contours 외각이라는 뜻을 가지고 있다.
#이미지의 다양한 요소에서 외각을 찾는 것

import cv2
image = cv2.imread('images/sca.jpg')
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(image_gray, 127, 255, 0)

cv2.imshow('image',thresh)
cv2.waitKey(0)

contours, hierachy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print(contours)

image = cv2.drawContours(image, contours, -1, (0,255,0),4)

cv2.imshow('image',image)
cv2.waitKey(0)