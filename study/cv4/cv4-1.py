#image transformation

#cv2.add() :Saturation 연산을 수행합니다
#0보다 작으면 0,255보다 크면 255로 표현
#np.add().Modulo 연산을 수행합니다 256은 0, 257 1로 

import cv2


image_1 = cv2.imread('images/cat.jpg')
image_2 = cv2.imread('images/sky.jpg')

result = cv2.add(image_1, image_2)
cv2.imshow('Image',result)
cv2.waitKey(0)

result = image_1 + image_2
cv2.imshow('Image', result)
cv2.waitKey(0)