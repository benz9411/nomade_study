# 적응 임계점
# cv2.adaptiveThreshold(image,max_value,adaptive_method,type,block_size,C)

import cv2


image = cv2.imread('images/sca.jpg',cv2.IMREAD_GRAYSCALE)

thres1 = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_MEAN_C
                                ,cv2.THRESH_BINARY,21,3)
thres2 = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                               cv2.THRESH_BINARY,21,3)

cv2.imshow('image',thres1)
cv2.waitKey(0)

cv2.imshow('image',thres2)
cv2.waitKey(0)

