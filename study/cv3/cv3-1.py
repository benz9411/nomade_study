#이미지 변경만 해도 많고 3d vision만 해도 다양한 내용 존재
# 가장 간단하고 쉬운거 공부 

# 문제 확대 한다고 하면 그 남은 픽셀들은 어케 채우나?
#추가 되는 픽셀을 어케 채울껀지 -> 보간법
#중간값 등등 ->resize 함수 사용

import cv2
from numpy import interp

image=cv2.imread('images/cat.jpg')
cv2.imshow('image',image)
cv2.waitKey(0)

expand = cv2.resize(image, None, fx=2.0, fy=2.0, interpolation=cv2.INTER_CUBIC )
cv2.imshow('Image',expand)
cv2.waitKey(0)


shrink = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC )
cv2.imshow('Image',shrink)
cv2.waitKey(0)
